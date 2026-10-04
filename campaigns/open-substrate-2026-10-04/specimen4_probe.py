from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIXTURES = HERE / "fixtures"
RENDERER = HERE / "open_render.py"
REPORT = HERE / "specimen4-current.json"

OBJECT_ID = "minimal-shared-identity-004"
UNKNOWN_MARKER = "unclassified"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    failures = []

    fixture = FIXTURES / "specimen-004"
    fixture_object = fixture / "object.json"
    obj = read_json(fixture_object)

    if obj.get("id") != OBJECT_ID:
        failures.append("specimen #4 identity changed")

    for forbidden in ["kind", "views", "body", "provenance"]:
        if forbidden in obj:
            failures.append(
                f"specimen #4 unexpectedly gained convenience field {forbidden!r}"
            )

    with tempfile.TemporaryDirectory(prefix="open-substrate-specimen4-") as td:
        out = Path(td) / "site"
        command = ["python", str(RENDERER)]
        for number in (1, 2, 3, 4):
            command += [
                "--package",
                str(FIXTURES / f"specimen-00{number}"),
            ]
        command += ["--out", str(out)]

        result = subprocess.run(
            command,
            cwd=HERE,
            capture_output=True,
            text=True,
            timeout=30,
        )

        observation = {
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }

        if result.returncode == 0:
            manifest = read_json(out / "manifest.json")
            objects = manifest.get("objects", [])
            target = next(
                (item for item in objects if item.get("id") == OBJECT_ID),
                None,
            )
            observation["generated_object_count"] = len(objects)
            observation["target_manifest"] = target

            if target is None:
                failures.append("specimen #4 is absent from generated object index")
            else:
                if target.get("kind") is not None:
                    failures.append("missing kind was synthesized into a non-null kind")

                owner_page = out / target["owner_page"]
                technical_page = out / target["technical_page"]
                raw_object = out / target["raw_object"]

                if not owner_page.is_file():
                    failures.append("specimen #4 Owner fallback page is missing")
                else:
                    owner_text = owner_page.read_text(encoding="utf-8")
                    if '<html lang="pl">' not in owner_text:
                        failures.append("specimen #4 Owner fallback is not Polish-first")
                    if f"<h1>{OBJECT_ID}</h1>" not in owner_text:
                        failures.append("stable id is not used as fallback Owner title")
                    if "Brak zadeklarowanych źródeł." not in owner_text:
                        failures.append("absence of provenance is not stated honestly")
                    if "Deklarowany rodzaj: <code>brak</code>" not in owner_text:
                        failures.append("missing kind is not represented as absent")
                    if "browser/field-knot" in owner_text:
                        failures.append("specimen #1 kind leaked into specimen #4 view")

                if not technical_page.is_file():
                    failures.append("specimen #4 technical/raw page is missing")
                else:
                    technical_text = technical_page.read_text(encoding="utf-8")
                    if UNKNOWN_MARKER not in technical_text:
                        failures.append("unknown nested metadata disappeared")
                    if "<strong>declared kind:</strong> <code>null</code>" not in technical_text:
                        failures.append("technical view does not preserve null kind")

                if not raw_object.is_file():
                    failures.append("specimen #4 raw object.json is missing")
                elif raw_object.read_bytes() != fixture_object.read_bytes():
                    failures.append("specimen #4 raw object.json changed")

            specimen1 = next(
                (
                    item
                    for item in objects
                    if item.get("id") == "browser-field-knot-001"
                ),
                None,
            )
            if specimen1 is None:
                failures.append("specimen #1 disappeared when specimen #4 was added")

            observation["record_count"] = len(manifest.get("records", []))

        else:
            failures.append("current generic adapter rejected specimen #4")

    renderer_text = RENDERER.read_text(encoding="utf-8")
    for literal in [OBJECT_ID, UNKNOWN_MARKER]:
        if literal in renderer_text:
            failures.append(
                f"renderer contains specimen-004-specific literal {literal!r}"
            )

    report = {
        "campaign": "open-substrate-2026-10-04",
        "specimen": "specimen-004",
        "mode": "second-shared-object-current-adapter",
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
        raise SystemExit("SPECIMEN 004 GENERIC FALLBACK FAIL: " + "; ".join(failures))


if __name__ == "__main__":
    main()
