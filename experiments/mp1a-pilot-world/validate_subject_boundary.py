from __future__ import annotations

import argparse
import hashlib
import json
import os
import shlex
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote

import gymnasium as gym

import browsergym.core
from browsergym.core.action.functions import click, go_back
from browsergym.core.action.highlevel import HighLevelActionSet
from browsergym.utils.obs import flatten_axtree_to_str


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "out-nav"
ARTIFACTS = ROOT / "artifacts-nav"
PROTOCOL = "mp1a-subject-jsonl-v0.1"
VIEWPORT = {"width": 1280, "height": 900}

FORBIDDEN_OUTBOUND_KEYS = {
    "evaluator",
    "motifs",
    "expected_exceptions",
    "seed",
    "seed_commitment",
    "ground_truth",
    "score",
}


def canonical_line(obj: dict) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def packet_meta(obj: dict) -> dict:
    line = canonical_line(obj)
    raw = line.encode("utf-8")
    return {
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "top_level_keys": sorted(obj.keys()),
    }


def assert_no_forbidden_keys(value, path="$"):
    if isinstance(value, dict):
        for key, child in value.items():
            if key in FORBIDDEN_OUTBOUND_KEYS:
                raise RuntimeError(f"forbidden subject-boundary key at {path}.{key}")
            assert_no_forbidden_keys(child, f"{path}.{key}")
    elif isinstance(value, list):
        for i, child in enumerate(value):
            assert_no_forbidden_keys(child, f"{path}[{i}]")


def relative_world_url(url: str, treatment_root: Path) -> str:
    decoded = unquote(url)
    marker = treatment_root.resolve().as_uri()
    if decoded.startswith(marker):
        tail = decoded[len(marker):].lstrip("/")
        return tail or "index.html"
    return decoded


def observation_packet(obs, treatment_root: Path) -> dict:
    tree = flatten_axtree_to_str(
        obs["axtree_object"],
        remove_redundant_static_text=True,
    )
    raw = tree.encode("utf-8")
    return {
        "url": relative_world_url(obs["url"], treatment_root),
        "axtree": tree,
        "axtree_bytes": len(raw),
        "axtree_sha256": hashlib.sha256(raw).hexdigest(),
        "last_action_error": obs["last_action_error"],
    }


class JsonlSubjectProcess:
    def __init__(self, command: list[str]):
        self.command = command
        self.tempdir = tempfile.TemporaryDirectory(prefix="mp1a-subject-")
        # Boundary smoke gets a deliberately sparse environment. Real provider
        # adapters must explicitly opt into any credential environment later.
        env = {
            "PATH": os.environ.get("PATH", ""),
            "PYTHONUNBUFFERED": "1",
        }
        self.proc = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            cwd=self.tempdir.name,
            env=env,
        )

    def send(self, obj: dict):
        assert_no_forbidden_keys(obj)
        line = canonical_line(obj)
        assert self.proc.stdin is not None
        self.proc.stdin.write(line + "\n")
        self.proc.stdin.flush()

    def recv(self) -> dict:
        assert self.proc.stdout is not None
        line = self.proc.stdout.readline()
        if not line:
            stderr = ""
            if self.proc.stderr is not None:
                stderr = self.proc.stderr.read()
            raise RuntimeError(
                f"subject process ended without response; stderr={stderr!r}"
            )
        return json.loads(line)

    def close(self):
        if self.proc.poll() is None:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=3)
            except subprocess.TimeoutExpired:
                self.proc.kill()
                self.proc.wait(timeout=3)
        self.tempdir.cleanup()


def validate_subject_reply(reply: dict):
    kind = reply.get("kind")
    if kind == "action":
        if set(reply.keys()) - {"kind", "action", "label"}:
            raise RuntimeError(f"unexpected action reply keys: {sorted(reply.keys())}")
        if not isinstance(reply.get("action"), str):
            raise RuntimeError("action reply missing action string")
        return
    if kind == "final":
        if set(reply.keys()) - {"kind", "answer"}:
            raise RuntimeError(f"unexpected final reply keys: {sorted(reply.keys())}")
        if not isinstance(reply.get("answer"), dict):
            raise RuntimeError("final reply missing answer object")
        return
    raise RuntimeError(f"invalid subject reply kind: {kind!r}")


def run_treatment(treatment: str, subject_command: list[str]) -> dict:
    treatment_root = OUT / treatment

    action_set = HighLevelActionSet(
        subsets=["custom"],
        custom_actions=[click, go_back],
        multiaction=False,
        strict=True,
    )

    env = gym.make(
        "browsergym/openended",
        task_kwargs={"start_url": (treatment_root / "index.html").resolve().as_uri()},
        headless=True,
        viewport=VIEWPORT,
        timeout=2500,
        action_mapping=action_set.to_python_code,
    )

    subject = JsonlSubjectProcess(subject_command)
    trace = []

    start_packet = {
        "type": "start",
        "protocol": PROTOCOL,
        "task": (
            "PLUMBING VALIDATION ONLY. Navigate to Release records, inspect "
            "Fir release candidate, return to the collection, inspect Harbor "
            "release candidate, then finish."
        ),
        "action_contract": {
            "one_action_per_step": True,
            "allowed": [
                "click(bid: str)",
                "go_back()",
            ],
            "reply_shapes": {
                "action": {"kind": "action", "action": "<one allowed action>"},
                "final": {"kind": "final", "answer": "<JSON object>"},
            },
        },
    }

    try:
        subject.send(start_packet)
        trace.append(
            {
                "type": "OUTBOUND_START",
                "meta": packet_meta(start_packet),
            }
        )

        ready = subject.recv()
        if ready.get("type") != "ready" or ready.get("protocol") != PROTOCOL:
            raise RuntimeError(f"invalid subject handshake: {ready!r}")

        subject_pid = ready.get("pid")

        obs, _ = env.reset()
        step = 0

        while step < 12:
            observation = observation_packet(obs, treatment_root)
            outbound = {
                "type": "observation",
                "protocol": PROTOCOL,
                "step": step,
                "observation": observation,
            }
            subject.send(outbound)

            trace.append(
                {
                    "type": "OUTBOUND_OBSERVATION",
                    "step": step,
                    "url": observation["url"],
                    "axtree_bytes": observation["axtree_bytes"],
                    "axtree_sha256": observation["axtree_sha256"],
                    "packet_meta": packet_meta(outbound),
                }
            )

            reply = subject.recv()
            validate_subject_reply(reply)

            trace.append(
                {
                    "type": "INBOUND_SUBJECT_REPLY",
                    "step": step,
                    "reply": reply,
                }
            )

            if reply["kind"] == "final":
                return {
                    "treatment": treatment,
                    "subject_pid": subject_pid,
                    "final": reply["answer"],
                    "trace": trace,
                    "browser_actions": sum(
                        1
                        for e in trace
                        if e["type"] == "INBOUND_SUBJECT_REPLY"
                        and e["reply"]["kind"] == "action"
                    ),
                    "subject_observation_bytes": sum(
                        e["axtree_bytes"]
                        for e in trace
                        if e["type"] == "OUTBOUND_OBSERVATION"
                    ),
                    "subject_packet_bytes": sum(
                        e["packet_meta"]["bytes"]
                        for e in trace
                        if e["type"] in {"OUTBOUND_START", "OUTBOUND_OBSERVATION"}
                    ),
                }

            obs, _, terminated, truncated, _ = env.step(reply["action"])

            if obs["last_action_error"]:
                raise RuntimeError(
                    f"{treatment} action failed at step {step}: "
                    f"{obs['last_action_error']}"
                )
            if terminated or truncated:
                raise RuntimeError(
                    f"{treatment} environment ended before subject final"
                )

            step += 1

        raise RuntimeError(f"{treatment} exceeded step budget")
    finally:
        subject.close()
        env.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--subject-command",
        default="",
        help=(
            "External JSONL subject command. Empty uses the deterministic "
            "boundary-smoke subject shipped with this experiment."
        ),
    )
    args = parser.parse_args()

    if args.subject_command:
        command = shlex.split(args.subject_command)
    else:
        command = [
            sys.executable,
            str((ROOT / "scripted_subject_process.py").resolve()),
        ]

    ARTIFACTS.mkdir(exist_ok=True)

    runs = {
        treatment: run_treatment(treatment, command)
        for treatment in ["p0", "p1"]
    }

    expected_urls = [
        "index.html",
        "collections/release-records.html",
        "resources/release-fir.html",
        "collections/release-records.html",
        "resources/release-harbor.html",
    ]

    failures = []

    if runs["p0"]["subject_pid"] == runs["p1"]["subject_pid"]:
        failures.append("P0/P1 did not receive fresh subject processes")

    for treatment, run in runs.items():
        urls = [
            e["url"]
            for e in run["trace"]
            if e["type"] == "OUTBOUND_OBSERVATION"
        ]
        if urls != expected_urls:
            failures.append(f"{treatment}: unexpected route {urls!r}")
        if run["browser_actions"] != 4:
            failures.append(
                f"{treatment}: expected 4 actions, got {run['browser_actions']}"
            )
        if not run["final"].get("route_complete"):
            failures.append(f"{treatment}: missing route_complete final")

        # Exact outbound payload audit: never send hidden apparatus vocabulary.
        for event in run["trace"]:
            if event["type"] not in {"OUTBOUND_START", "OUTBOUND_OBSERVATION"}:
                continue
            keys = event["meta"]["top_level_keys"] if event["type"] == "OUTBOUND_START" else event["packet_meta"]["top_level_keys"]
            if "evaluator" in keys:
                failures.append(f"{treatment}: evaluator key crossed subject boundary")

    report = {
        "validator": "mp1a-external-subject-boundary-v0.1",
        "protocol": PROTOCOL,
        "subject_command": command,
        "action_boundary": {
            "strict": True,
            "multiaction": False,
            "allowed_actions": ["click(bid)", "go_back()"],
        },
        "runs": runs,
        "note": (
            "This is a process/protocol isolation smoke with a deterministic "
            "scripted subject. It is not model evidence."
        ),
    }

    (ARTIFACTS / "subject_boundary_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))

    if failures:
        raise SystemExit("SUBJECT BOUNDARY FAIL: " + "; ".join(failures))

    print(
        "SUBJECT BOUNDARY PASS: fresh external subject processes received only "
        "task/action-contract/observation packets and controlled BrowserGym "
        "through the restricted action set."
    )


if __name__ == "__main__":
    main()
