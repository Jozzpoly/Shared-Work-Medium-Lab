from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.parse import unquote

import gymnasium as gym

import browsergym.core
from browsergym.core.action.functions import click, go_back
from browsergym.core.action.highlevel import HighLevelActionSet

from validate_subject_boundary import (
    JsonlSubjectProcess,
    PROTOCOL,
    observation_packet,
    packet_meta,
    validate_subject_reply,
)


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "out-nav"
ARTIFACTS = ROOT / "artifacts-nav"
VIEWPORT = {"width": 1280, "height": 900}

TASK = (
    "Determine whether the project resource named 'Observation polling guidance' "
    "can still be relied on as current guidance. Verify against relevant source "
    "material. Return the target resource id, supporting source ids, and one "
    "judgement value: 'requires_re_evaluation' or 'current_as_written'."
)


def resource_id_from_url(url: str):
    prefix = "resources/"
    suffix = ".html"
    if url.startswith(prefix) and url.endswith(suffix):
        return unquote(url[len(prefix):-len(suffix)])
    return None


def run_real_trace(treatment: str, judgement: str) -> dict:
    treatment_root = OUT / treatment
    subject_command = [
        sys.executable,
        str((ROOT / "scripted_t1_subject_process.py").resolve()),
        "--judgement",
        judgement,
    ]

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
        "task": TASK,
        "action_contract": {
            "one_action_per_step": True,
            "allowed": ["click(bid: str)", "go_back()"],
            "final_answer_contract": {
                "target_resource": "string",
                "supporting_sources": ["string"],
                "judgement": "requires_re_evaluation | current_as_written",
                "selected_distractor": "boolean",
            },
        },
    }

    try:
        subject.send(start_packet)
        ready = subject.recv()
        if ready.get("type") != "ready" or ready.get("protocol") != PROTOCOL:
            raise RuntimeError(f"invalid subject handshake: {ready!r}")

        obs, _ = env.reset()
        step = 0

        while step < 10:
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
                    "type": "OBSERVATION",
                    "step": step,
                    "url": observation["url"],
                    "axtree_bytes": observation["axtree_bytes"],
                    "axtree_sha256": observation["axtree_sha256"],
                    "packet_bytes": packet_meta(outbound)["bytes"],
                }
            )

            reply = subject.recv()
            validate_subject_reply(reply)

            if reply["kind"] == "final":
                return {
                    "treatment": treatment,
                    "fixture_judgement": judgement,
                    "task_id": "T1",
                    "final": reply["answer"],
                    "trace": trace,
                }

            trace.append(
                {
                    "type": "ACTION",
                    "step": step,
                    "action": reply["action"],
                    "label": reply.get("label"),
                }
            )

            obs, _, terminated, truncated, _ = env.step(reply["action"])
            if obs["last_action_error"]:
                raise RuntimeError(
                    f"{treatment}/{judgement} action failed: "
                    f"{obs['last_action_error']}"
                )
            if terminated or truncated:
                raise RuntimeError(
                    f"{treatment}/{judgement} ended before final answer"
                )

            step += 1

        raise RuntimeError(f"{treatment}/{judgement} exceeded step budget")
    finally:
        subject.close()
        env.close()


def score_t1_real_trace(run: dict) -> dict:
    final = run["final"]

    observed_resource_ids = [
        rid
        for event in run["trace"]
        if event["type"] == "OBSERVATION"
        for rid in [resource_id_from_url(event["url"])]
        if rid is not None
    ]
    observed_set = set(observed_resource_ids)

    target_ok = final.get("target_resource") == "summary-cache-guidance"
    target_observed = "summary-cache-guidance" in observed_set

    sources = set(final.get("supporting_sources", []))
    source_claim_ok = "source-cache-config" in sources
    source_observed = "source-cache-config" in observed_set

    scope_ok = final.get("judgement") == "requires_re_evaluation"
    distractor_free = not final.get("selected_distractor", False)

    observation_events = [
        e for e in run["trace"] if e["type"] == "OBSERVATION"
    ]
    action_events = [
        e for e in run["trace"] if e["type"] == "ACTION"
    ]

    resource_counts = {}
    for rid in observed_resource_ids:
        resource_counts[rid] = resource_counts.get(rid, 0) + 1

    return {
        "task": "T1",
        "target_ok": target_ok,
        "target_observed": target_observed,
        "source_claim_ok": source_claim_ok,
        "source_observed": source_observed,
        "scope_ok": scope_ok,
        "distractor_free": distractor_free,
        "exact_task_success": all(
            [
                target_ok,
                target_observed,
                source_claim_ok,
                source_observed,
                scope_ok,
                distractor_free,
            ]
        ),
        "cost": {
            "observation_bytes": sum(e["axtree_bytes"] for e in observation_events),
            "subject_packet_bytes": sum(e["packet_bytes"] for e in observation_events),
            "browser_actions": len(action_events),
            "resource_reads": len(observed_resource_ids),
            "distinct_resources": len(observed_set),
            "redundant_resource_reads": sum(
                max(0, count - 1) for count in resource_counts.values()
            ),
        },
        "observed_resource_ids": observed_resource_ids,
    }


def main():
    ARTIFACTS.mkdir(exist_ok=True)

    cases = {}
    for treatment in ["p0", "p1"]:
        for judgement in ["requires_re_evaluation", "proven_false"]:
            key = f"{treatment}__{judgement}"
            run = run_real_trace(treatment, judgement)
            cases[key] = {
                "run": run,
                "score": score_t1_real_trace(run),
            }

    failures = []

    for treatment in ["p0", "p1"]:
        good = cases[f"{treatment}__requires_re_evaluation"]["score"]
        bad = cases[f"{treatment}__proven_false"]["score"]

        if not good["exact_task_success"]:
            failures.append(f"{treatment}: correct fixture did not score success")

        if bad["exact_task_success"]:
            failures.append(f"{treatment}: overclaim fixture incorrectly scored success")

        if not bad["target_ok"] or not bad["target_observed"]:
            failures.append(f"{treatment}: overclaim control changed target evidence")

        if not bad["source_claim_ok"] or not bad["source_observed"]:
            failures.append(f"{treatment}: overclaim control changed source evidence")

        if bad["scope_ok"]:
            failures.append(f"{treatment}: overclaim did not fail scope")

        if good["observed_resource_ids"] != [
            "summary-cache-guidance",
            "source-cache-config",
        ]:
            failures.append(
                f"{treatment}: unexpected resource acquisition route "
                f"{good['observed_resource_ids']!r}"
            )

        if good["cost"]["browser_actions"] != 3:
            failures.append(
                f"{treatment}: expected 3 browser actions, "
                f"got {good['cost']['browser_actions']}"
            )

    # Same factual route/final semantics across treatments; observation payload
    # may differ because semantic treatment changes AXTree serialization.
    p0_good = cases["p0__requires_re_evaluation"]["score"]
    p1_good = cases["p1__requires_re_evaluation"]["score"]

    if p0_good["observed_resource_ids"] != p1_good["observed_resource_ids"]:
        failures.append("P0/P1 correct fixture acquired different resources")

    report = {
        "validator": "mp1a-real-trace-to-score-v0.1",
        "task": TASK,
        "cases": cases,
        "interpretation_boundary": (
            "This validates BrowserGym trace-to-score plumbing with deterministic "
            "external subjects. It is not LLM performance evidence."
        ),
    }

    (ARTIFACTS / "real_trace_scoring_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(json.dumps(report, ensure_ascii=False, indent=2))

    if failures:
        raise SystemExit("REAL TRACE SCORE FAIL: " + "; ".join(failures))

    print(
        "REAL TRACE SCORE PASS: task correctness, actual source acquisition, "
        "epistemic scope, and observed BrowserGym cost are scored from the real "
        "interaction trace."
    )


if __name__ == "__main__":
    main()
