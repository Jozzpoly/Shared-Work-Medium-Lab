from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load_evaluator():
    return json.loads((ROOT / "out" / "evaluator.json").read_text(encoding="utf-8"))


def resource_reads(trace):
    return [e for e in trace if e["type"] in {"OPEN_RESOURCE", "VERIFY_SOURCE"}]


def score_cost(run):
    reads = resource_reads(run["trace"])
    ids = [e["resource_id"] for e in reads]
    counts = Counter(ids)
    return {
        "total_observation_bytes": sum(int(e.get("bytes", 0)) for e in run["trace"]),
        "resource_reads": len(reads),
        "distinct_resources": len(set(ids)),
        "redundant_repeat_reads": sum(max(0, count - 1) for count in counts.values()),
        "environment_actions": len(run["trace"]),
    }


def score_t1(run, evaluator):
    motif = evaluator["motifs"]["stale_dependency"]
    expected_summary = "summary-cache-guidance"
    expected_dependency = "source-cache-config"

    final = run["final"]
    target_ok = final.get("target_resource") == expected_summary
    dependency_ok = expected_dependency in final.get("supporting_sources", [])
    scope_ok = final.get("judgement") == "requires_re_evaluation"
    distractor_free = not final.get("selected_distractor", False)

    return {
        "task": "T1",
        "target_ok": target_ok,
        "dependency_ok": dependency_ok,
        "scope_ok": scope_ok,
        "distractor_free": distractor_free,
        "exact_task_success": all([target_ok, dependency_ok, scope_ok, distractor_free]),
        "cost": score_cost(run),
    }


def score_t2(run, evaluator):
    motif = evaluator["motifs"]["distributed_common_cause"]
    expected_cause = "source-relay-refresh"
    supporting = {
        "issue-relay-alpha",
        "issue-relay-bravo",
        "issue-relay-charlie",
    }

    final = run["final"]
    cause_ok = final.get("cause_resource") == expected_cause
    cited = set(final.get("supporting_sources", []))
    support_count = len(cited & supporting)
    enough_support = support_count >= 3
    inference_scoped = final.get("claim_scope") == "plausible_common_cause"
    distractor_free = not final.get("selected_distractor", False)

    return {
        "task": "T2",
        "cause_ok": cause_ok,
        "support_count": support_count,
        "enough_support": enough_support,
        "inference_scoped": inference_scoped,
        "distractor_free": distractor_free,
        "exact_task_success": all([cause_ok, enough_support, inference_scoped, distractor_free]),
        "cost": score_cost(run),
    }


def score_t3(run, evaluator):
    motif = evaluator["motifs"]["batchable_collection"]
    expected = set(motif["expected_exceptions"])
    final_exceptions = set(run["final"].get("exceptions", []))
    correctness = final_exceptions == expected

    types = [event["type"] for event in run["trace"]]
    collection_members = set(motif["resources"])
    covered = {
        event.get("resource_id")
        for event in run["trace"]
        if event.get("resource_id") in collection_members
    }

    has_structure_recognition = "LIST_COLLECTION" in types
    has_generic_strategy = any(
        t in types for t in ["DERIVE_INDEX", "BATCH_TRANSFORM", "QUERY_STRUCTURE"]
    )
    reorganized_search = (
        "BATCH_TRANSFORM" in types
        or (
            "DERIVE_INDEX" in types
            and len(resource_reads(run)) < len(collection_members)
        )
    )
    coverage_ok = (
        len(covered) == len(collection_members)
        or bool(run["final"].get("collection_coverage_confirmed"))
    )
    no_task_specific_tool = not any(
        event.get("task_specific_tool", False)
        for event in run["trace"]
    )

    systematic = all(
        [
            has_structure_recognition,
            has_generic_strategy,
            reorganized_search,
            coverage_ok,
            no_task_specific_tool,
        ]
    )

    return {
        "task": "T3",
        "correct_exceptions": correctness,
        "structure_recognition": has_structure_recognition,
        "generic_strategy": has_generic_strategy,
        "reorganized_search": reorganized_search,
        "coverage_ok": coverage_ok,
        "no_task_specific_tool": no_task_specific_tool,
        "systematic_workflow": 1 if systematic else 0,
        "cost": score_cost(run),
    }


def score(run, evaluator):
    task = run["task_id"]
    if task == "T1":
        return score_t1(run, evaluator)
    if task == "T2":
        return score_t2(run, evaluator)
    if task == "T3":
        return score_t3(run, evaluator)
    raise ValueError(f"Unsupported task: {task}")


def main():
    evaluator = load_evaluator()
    cases_dir = ROOT / "synthetic_runs"
    results = {}

    for path in sorted(cases_dir.glob("*.json")):
        run = json.loads(path.read_text(encoding="utf-8"))
        results[path.stem] = score(run, evaluator)

    out = ROOT / "artifacts"
    out.mkdir(exist_ok=True)
    (out / "synthetic_scoring_results.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(results, ensure_ascii=False, indent=2))

    expected = {
        "t1_good": {"exact_task_success": True},
        "t1_overclaim": {"exact_task_success": False, "scope_ok": False},
        "t2_good": {"exact_task_success": True},
        "t3_serial_correct": {"correct_exceptions": True, "systematic_workflow": 0},
        "t3_systematic_correct": {"correct_exceptions": True, "systematic_workflow": 1},
    }

    failures = []
    for case, checks in expected.items():
        actual = results.get(case)
        if actual is None:
            failures.append(f"missing case: {case}")
            continue
        for key, value in checks.items():
            if actual.get(key) != value:
                failures.append(
                    f"{case}.{key}: expected {value!r}, got {actual.get(key)!r}"
                )

    # Explicitly verify that generativity and correctness are separate axes.
    if (
        results["t3_serial_correct"]["correct_exceptions"]
        != results["t3_systematic_correct"]["correct_exceptions"]
    ):
        failures.append("T3 fixtures do not hold correctness constant")

    serial_bytes = results["t3_serial_correct"]["cost"]["total_observation_bytes"]
    systematic_bytes = results["t3_systematic_correct"]["cost"]["total_observation_bytes"]
    if systematic_bytes >= serial_bytes:
        failures.append(
            "synthetic systematic trace must demonstrate lower acquisition cost than serial trace"
        )

    if failures:
        raise SystemExit("SCORING SEAM FAIL: " + "; ".join(failures))

    print("SCORING SEAM PASS: evaluator separates correctness, epistemic scope, acquisition cost, and systematic-workflow behavior.")


if __name__ == "__main__":
    main()
