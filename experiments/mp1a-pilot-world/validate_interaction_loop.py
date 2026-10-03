from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote

import gymnasium as gym

import browsergym.core
from browsergym.core.action.highlevel import HighLevelActionSet
from browsergym.utils.obs import flatten_axtree_to_str


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "out-nav"
ARTIFACTS = ROOT / "artifacts-nav"
VIEWPORT = {"width": 1280, "height": 900}


def link_bid(axtree_text: str, label: str) -> str:
    # BrowserGym flattened AXTree prints clickable links as:
    # [<bid>] link '<accessible name>'
    pattern = re.compile(
        r"\[([^\]]+)\]\s+link\s+" + re.escape(repr(label))
    )
    match = pattern.search(axtree_text)
    if not match:
        raise RuntimeError(f"link not found in observation: {label!r}")
    return match.group(1)


def relative_world_url(url: str, treatment_root: Path) -> str:
    decoded = unquote(url)
    marker = treatment_root.resolve().as_uri()
    if decoded.startswith(marker):
        tail = decoded[len(marker):].lstrip("/")
        return tail or "index.html"
    # Preserve unexpected navigation visibly instead of hiding it.
    return decoded


def observation_packet(obs, treatment_root: Path) -> dict:
    axtree = flatten_axtree_to_str(
        obs["axtree_object"],
        remove_redundant_static_text=True,
    )
    payload = axtree.encode("utf-8")
    return {
        "url": relative_world_url(obs["url"], treatment_root),
        "axtree": axtree,
        "observation_bytes": len(payload),
        "axtree_sha256": hashlib.sha256(payload).hexdigest(),
        "last_action_error": obs["last_action_error"],
    }


class ScriptedNavigationSubject:
    """Deterministic plumbing subject. Not an intelligence benchmark subject."""

    def __init__(self):
        self.phase = 0

    def next(self, observation: dict) -> dict:
        tree = observation["axtree"]

        if self.phase == 0:
            self.phase += 1
            label = "Release records"
            return {
                "kind": "browser_action",
                "label": label,
                "action": f"click({link_bid(tree, label)!r})",
            }

        if self.phase == 1:
            self.phase += 1
            label = "Fir release candidate"
            return {
                "kind": "browser_action",
                "label": label,
                "action": f"click({link_bid(tree, label)!r})",
            }

        if self.phase == 2:
            self.phase += 1
            return {
                "kind": "browser_action",
                "label": "go back to release collection",
                "action": "go_back()",
            }

        if self.phase == 3:
            self.phase += 1
            label = "Harbor release candidate"
            return {
                "kind": "browser_action",
                "label": label,
                "action": f"click({link_bid(tree, label)!r})",
            }

        if self.phase == 4:
            self.phase += 1
            return {
                "kind": "final",
                "result": {
                    "route_complete": True,
                    "purpose": "interaction-loop plumbing only",
                },
            }

        raise RuntimeError("scripted subject called after completion")


def run_treatment(treatment: str) -> dict:
    root = OUT / treatment
    action_set = HighLevelActionSet()

    env = gym.make(
        "browsergym/openended",
        task_kwargs={"start_url": (root / "index.html").resolve().as_uri()},
        headless=True,
        viewport=VIEWPORT,
        timeout=2500,
        action_mapping=action_set.to_python_code,
    )

    subject = ScriptedNavigationSubject()
    trace = []

    try:
        obs, _ = env.reset()
        step = 0

        while step < 12:
            packet = observation_packet(obs, root)
            trace.append(
                {
                    "type": "OBSERVATION",
                    "step": step,
                    "url": packet["url"],
                    "observation_bytes": packet["observation_bytes"],
                    "axtree_sha256": packet["axtree_sha256"],
                    "last_action_error": packet["last_action_error"],
                }
            )

            decision = subject.next(packet)
            trace.append(
                {
                    "type": "SUBJECT_DECISION",
                    "step": step,
                    **{k: v for k, v in decision.items() if k != "result"},
                }
            )

            if decision["kind"] == "final":
                return {
                    "treatment": treatment,
                    "final": decision["result"],
                    "trace": trace,
                    "observation_bytes_total": sum(
                        e["observation_bytes"]
                        for e in trace
                        if e["type"] == "OBSERVATION"
                    ),
                    "browser_actions": sum(
                        1
                        for e in trace
                        if e["type"] == "SUBJECT_DECISION"
                        and e["kind"] == "browser_action"
                    ),
                }

            obs, _, terminated, truncated, _ = env.step(decision["action"])

            if obs["last_action_error"]:
                raise RuntimeError(
                    f"{treatment} action failed at step {step}: "
                    f"{obs['last_action_error']}"
                )
            if terminated or truncated:
                raise RuntimeError(
                    f"{treatment} environment ended before scripted route completed"
                )

            step += 1

        raise RuntimeError(f"{treatment} exceeded scripted step budget")
    finally:
        env.close()


def main():
    ARTIFACTS.mkdir(exist_ok=True)

    runs = {
        treatment: run_treatment(treatment)
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
    for treatment, run in runs.items():
        observed_urls = [
            e["url"]
            for e in run["trace"]
            if e["type"] == "OBSERVATION"
        ]
        errors = [
            e["last_action_error"]
            for e in run["trace"]
            if e["type"] == "OBSERVATION" and e["last_action_error"]
        ]

        if observed_urls != expected_urls:
            failures.append(
                f"{treatment}: route mismatch: {observed_urls!r}"
            )
        if errors:
            failures.append(f"{treatment}: action errors present: {errors!r}")
        if run["browser_actions"] != 4:
            failures.append(
                f"{treatment}: expected 4 browser actions, got "
                f"{run['browser_actions']}"
            )
        if not run["final"].get("route_complete"):
            failures.append(f"{treatment}: final envelope missing route_complete")

    # Same scripted policy should traverse the same logical world topology.
    p0_urls = [
        e["url"] for e in runs["p0"]["trace"] if e["type"] == "OBSERVATION"
    ]
    p1_urls = [
        e["url"] for e in runs["p1"]["trace"] if e["type"] == "OBSERVATION"
    ]
    if p0_urls != p1_urls:
        failures.append("P0/P1 logical navigation routes diverged")

    # The observation payloads should *not* be identical: this is the intended
    # semantic treatment variable. Do not interpret magnitude as capability.
    p0_bytes = runs["p0"]["observation_bytes_total"]
    p1_bytes = runs["p1"]["observation_bytes_total"]
    if p0_bytes == p1_bytes:
        failures.append(
            "P0/P1 observation payload totals unexpectedly identical"
        )

    report = {
        "validator": "mp1a-scripted-interaction-loop-v0.1",
        "body": {
            "observation_mode": "BrowserGym flattened AXTree only",
            "action_mode": "BrowserGym HighLevelActionSet click/go_back",
            "viewport": VIEWPORT,
        },
        "expected_route": expected_urls,
        "runs": runs,
        "note": (
            "Scripted subject validates plumbing only. Observation-byte "
            "differences are treatment mechanics, not model-performance evidence."
        ),
    }

    (ARTIFACTS / "interaction_loop_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(json.dumps(report, ensure_ascii=False, indent=2))

    if failures:
        raise SystemExit("INTERACTION LOOP FAIL: " + "; ".join(failures))

    print(
        "INTERACTION LOOP PASS: identical scripted policy traversed both "
        "treatments through BrowserGym with complete per-step observation/action trace."
    )


if __name__ == "__main__":
    main()
