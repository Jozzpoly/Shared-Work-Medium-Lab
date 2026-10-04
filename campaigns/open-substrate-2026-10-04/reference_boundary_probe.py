from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPECIMEN1 = HERE / "fixtures" / "specimen-001"
SPECIMEN2 = HERE / "fixtures" / "specimen-002"
SPECIMEN3 = HERE / "fixtures" / "specimen-003"
RENDERER = HERE / "open_render.py"
REPORT = HERE / "reference-boundary-negative.json"


def run(specimen3: Path, out: Path):
    return subprocess.run(
        [
            "python",
            str(RENDERER),
            "--package",
            str(SPECIMEN1),
            "--package",
            str(SPECIMEN2),
            "--package",
            str(specimen3),
            "--out",
            str(out),
        ],
        cwd=HERE,
        capture_output=True,
        text=True,
        timeout=30,
    )


def clone_specimen(root: Path, name: str):
    target = root / name
    shutil.copytree(SPECIMEN3, target)
    return target


def mutate_refs(specimen: Path, links):
    path = specimen / "medium.refs.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["links"] = links
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def observe_case(temp: Path, name: str, links, marker: str):
    specimen = clone_specimen(temp, name)
    mutate_refs(specimen, links)
    result = run(specimen, temp / f"site-{name}")
    combined = result.stdout + result.stderr
    return {
        "returncode": result.returncode,
        "rejected": result.returncode != 0,
        "expected_marker": marker,
        "marker_present": marker in combined,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }


def main():
    failures = []

    with tempfile.TemporaryDirectory(prefix="open-substrate-reference-negative-") as td:
        temp = Path(td)

        unresolved = observe_case(
            temp,
            "unresolved-target",
            [{"record": "trace.json", "object_id": "missing-medium-identity"}],
            "medium.refs.json points to unresolved object identity",
        )

        escaping = observe_case(
            temp,
            "escaping-record",
            [{"record": "../outside.json", "object_id": "browser-field-knot-001"}],
            "reference record path escapes package boundary",
        )

        missing_record = observe_case(
            temp,
            "missing-record",
            [{"record": "missing.json", "object_id": "browser-field-knot-001"}],
            "medium.refs.json points to missing record",
        )

    observations = {
        "unresolved_target": unresolved,
        "escaping_record_path": escaping,
        "missing_record": missing_record,
    }

    for name, observation in observations.items():
        if not observation["rejected"]:
            failures.append(f"{name}: invalid explicit reference was accepted")
        if not observation["marker_present"]:
            failures.append(
                f"{name}: rejection did not come from the intended boundary"
            )

    report = {
        "campaign": "open-substrate-2026-10-04",
        "phase": "phase-3-explicit-reference-negative-pressure",
        "observations": observations,
        "result": "PASS" if not failures else "FAIL",
        "failures": failures,
    }
    REPORT.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, indent=2, ensure_ascii=False))

    if failures:
        raise SystemExit("REFERENCE BOUNDARY NEGATIVE PROBE FAIL: " + "; ".join(failures))


if __name__ == "__main__":
    main()
