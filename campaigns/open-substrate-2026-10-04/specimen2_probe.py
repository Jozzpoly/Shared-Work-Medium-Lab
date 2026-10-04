from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPECIMEN1 = HERE / "fixtures" / "specimen-001"
SPECIMEN2 = HERE / "fixtures" / "specimen-002"
RENDERER = HERE / "open_render.py"
REPORT = HERE / "specimen2-current.json"

TARGET_ID = "browser-field-knot-001"
TRACE_ID = "reflex-local-trace-001"
RELATION_KIND = "borrowed-as-debugging-lens"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def tree_hash(root: Path):
    digest = hashlib.sha256()
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        relative = path.relative_to(root).as_posix().encode("utf-8")
        digest.update(len(relative).to_bytes(8, "big"))
        digest.update(relative)
        data = path.read_bytes()
        digest.update(len(data).to_bytes(8, "big"))
        digest.update(data)
    return digest.hexdigest()


def run_renderer(out: Path):
    return subprocess.run(
        [
            "python",
            str(RENDERER),
            "--package",
            str(SPECIMEN1),
            "--package",
            str(SPECIMEN2),
            "--out",
            str(out),
        ],
        cwd=HERE,
        capture_output=True,
        text=True,
        timeout=30,
    )


def validate_fixture():
    failures = []

    if (SPECIMEN2 / "object.json").exists():
        failures.append("specimen #2 must not contain object.json")

    trace_path = SPECIMEN2 / "trace.json"
    if not trace_path.is_file():
        failures.append("specimen #2 trace.json is missing")
        return failures

    trace = read_json(trace_path)

    if trace.get("trace_id") != TRACE_ID:
        failures.append("trace identity changed")
    if trace.get("owner_scope") != {
        "scope_kind": "place",
        "scope_id": "reflex",
    }:
        failures.append("trace is no longer locally owned by Reflex")
    if trace.get("relation", {}).get("to", {}).get("object_id") != TARGET_ID:
        failures.append("trace no longer points to specimen #1 identity")
    if trace.get("relation", {}).get("kind") != RELATION_KIND:
        failures.append("unknown relation semantics changed")
    if trace.get("views", {}).get("owner", {}).get("language") != "pl":
        failures.append("Owner trace view is not Polish")
    if trace.get("views", {}).get("agent", {}).get("language") != "en":
        failures.append("agent trace view is not English")
    if trace.get("execution") != "none":
        failures.append("specimen #2 must remain passive")

    return failures


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=["current"],
        default="current",
        help="Current adapter closure mode. Add future modes only after evidence.",
    )
    args = parser.parse_args()

    failures = validate_fixture()

    before_target = tree_hash(SPECIMEN1)

    with tempfile.TemporaryDirectory(prefix="open-substrate-specimen2-") as td:
        out = Path(td) / "site"
        result = run_renderer(out)

        after_target = tree_hash(SPECIMEN1)
        combined = result.stdout + result.stderr

        observation = {
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "rejected": result.returncode != 0,
            "missing_object_json_failure": "package has no object.json" in combined,
            "specimen1_tree_before": before_target,
            "specimen1_tree_after": after_target,
            "specimen1_unchanged": before_target == after_target,
            "partial_output_exists": out.exists(),
            "partial_output_files": (
                sorted(
                    p.relative_to(out).as_posix()
                    for p in out.rglob("*")
                    if p.is_file()
                )
                if out.exists()
                else []
            ),
        }

    if args.mode == "current":
        if not observation["rejected"]:
            failures.append(
                "current adapter unexpectedly accepted relation-only package; "
                "re-audit before changing substrate"
            )
        if not observation["missing_object_json_failure"]:
            failures.append(
                "current failure is not the frozen one-object-per-package closure"
            )
        if not observation["specimen1_unchanged"]:
            failures.append("attempt mutated specimen #1 fixture bytes")

    report = {
        "campaign": "open-substrate-2026-10-04",
        "specimen": "specimen-002",
        "mode": args.mode,
        "target_identity": TARGET_ID,
        "trace_identity": TRACE_ID,
        "observation": observation,
        "result": "PASS" if not failures else "FAIL",
        "failures": failures,
    }

    REPORT.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, indent=2, ensure_ascii=False))

    if failures:
        raise SystemExit("SPECIMEN 002 CURRENT-CLOSURE FAIL: " + "; ".join(failures))


if __name__ == "__main__":
    main()
