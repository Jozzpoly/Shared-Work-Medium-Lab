from __future__ import annotations

import hashlib
import json
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPECIMEN1 = HERE / "fixtures" / "specimen-001"
SPECIMEN2 = HERE / "fixtures" / "specimen-002"
SPECIMEN3 = HERE / "fixtures" / "specimen-003"
RENDERER = HERE / "open_render.py"
REPORT = HERE / "specimen3-current.json"

REAL_TARGET = "browser-field-knot-001"
FOREIGN_PAYLOAD_ID = "external-debug-object-77"


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


def main():
    failures = []

    trace = read_json(SPECIMEN3 / "trace.json")
    if trace.get("relation", {}).get("to", {}).get("object_id") != REAL_TARGET:
        failures.append("real Medium target changed")
    if (
        trace.get("foreign_payload", {})
        .get("snapshot", {})
        .get("object_id")
        != FOREIGN_PAYLOAD_ID
    ):
        failures.append("foreign payload control value changed")
    if trace.get("execution") != "none":
        failures.append("specimen #3 must remain passive")

    before1 = tree_hash(SPECIMEN1)
    before2 = tree_hash(SPECIMEN2)

    with tempfile.TemporaryDirectory(prefix="open-substrate-specimen3-") as td:
        out = Path(td) / "site"
        result = subprocess.run(
            [
                "python",
                str(RENDERER),
                "--package",
                str(SPECIMEN1),
                "--package",
                str(SPECIMEN2),
                "--package",
                str(SPECIMEN3),
                "--out",
                str(out),
            ],
            cwd=HERE,
            capture_output=True,
            text=True,
            timeout=30,
        )

    after1 = tree_hash(SPECIMEN1)
    after2 = tree_hash(SPECIMEN2)
    combined = result.stdout + result.stderr

    observation = {
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "rejected": result.returncode != 0,
        "foreign_payload_misclassified_as_reference": (
            f"unresolved object identity '{FOREIGN_PAYLOAD_ID}'" in combined
        ),
        "specimen1_unchanged": before1 == after1,
        "specimen2_unchanged": before2 == after2,
        "specimen1_tree_before": before1,
        "specimen1_tree_after": after1,
        "specimen2_tree_before": before2,
        "specimen2_tree_after": after2,
    }

    if not observation["rejected"]:
        failures.append(
            "current recursive reference scanner unexpectedly accepted specimen #3; "
            "re-audit before choosing a reference boundary"
        )
    if not observation["foreign_payload_misclassified_as_reference"]:
        failures.append(
            "expected semantic false-positive was not reproduced"
        )
    if not observation["specimen1_unchanged"]:
        failures.append("specimen #1 changed during false-positive probe")
    if not observation["specimen2_unchanged"]:
        failures.append("specimen #2 changed during false-positive probe")

    report = {
        "campaign": "open-substrate-2026-10-04",
        "specimen": "specimen-003",
        "mode": "current-recursive-reference-inference",
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
        raise SystemExit("SPECIMEN 003 FALSE-POSITIVE PROBE FAIL: " + "; ".join(failures))


if __name__ == "__main__":
    main()
