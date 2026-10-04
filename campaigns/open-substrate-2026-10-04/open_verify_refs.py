from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE = HERE / "site"
SPECIMEN3 = HERE / "fixtures" / "specimen-003"
REPORT = HERE / "reference-verification.json"

TARGET_ID = "browser-field-knot-001"
TRACE_ID = "combat-foreign-payload-note-001"
FOREIGN_ID = "external-debug-object-77"
OWNER_TITLE = "Notatka Combatu z obcym payloadem"
OWNER_NOTE_MARKER = "nie powinno wymyślać semantyki"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    failures = []

    manifest_path = SITE / "manifest.json"
    if not manifest_path.is_file():
        failures.append("generated manifest is missing")
        manifest = {"objects": [], "records": []}
    else:
        manifest = read_json(manifest_path)

    target = next(
        (item for item in manifest.get("objects", []) if item.get("id") == TARGET_ID),
        None,
    )
    if target is None:
        failures.append("target shared identity is missing")

    trace_manifest = None
    trace_raw = None
    for item in manifest.get("records", []):
        raw_href = item.get("raw_href")
        if not raw_href:
            continue
        raw_path = SITE / raw_href
        if not raw_path.is_file():
            continue
        data = read_json(raw_path)
        if data.get("trace_id") == TRACE_ID:
            trace_manifest = item
            trace_raw = raw_path
            break

    if trace_manifest is None or trace_raw is None:
        failures.append("Specimen #3 raw trace is missing")
    else:
        if trace_raw.read_bytes() != (SPECIMEN3 / "trace.json").read_bytes():
            failures.append("Specimen #3 raw trace bytes changed")

        refs = trace_manifest.get("references", [])
        target_ids = [ref.get("object_id") for ref in refs]
        if target_ids != [TARGET_ID]:
            failures.append(
                f"explicit reference set is not exactly the intended target: {target_ids!r}"
            )
        if FOREIGN_ID in target_ids:
            failures.append("foreign payload id leaked into Medium references")

        raw_text = trace_raw.read_text(encoding="utf-8")
        if FOREIGN_ID not in raw_text:
            failures.append("foreign payload control data disappeared from raw trace")

        refs_href = trace_manifest.get("refs_href")
        if not refs_href:
            failures.append("record manifest does not expose its reference sidecar")
        else:
            generated_refs = SITE / refs_href
            original_refs = SPECIMEN3 / "medium.refs.json"
            if not generated_refs.is_file():
                failures.append("generated reference sidecar is missing")
            elif generated_refs.read_bytes() != original_refs.read_bytes():
                failures.append("reference sidecar was not preserved byte-for-byte")

    if target is not None:
        owner_page = SITE / target["owner_page"]
        if not owner_page.is_file():
            failures.append("target Owner page is missing")
        else:
            text = owner_page.read_text(encoding="utf-8")
            if OWNER_TITLE not in text:
                failures.append("Specimen #3 Owner title is not visible beside target")
            if OWNER_NOTE_MARKER not in text:
                failures.append("Specimen #3 local meaning is not visible beside target")
            if trace_manifest and trace_manifest.get("raw_href") not in text:
                failures.append("Owner view has no path to Specimen #3 exact raw record")

    renderer = (HERE / "open_render.py").read_text(encoding="utf-8")
    for forbidden in [
        "find_object_references",
        TRACE_ID,
        FOREIGN_ID,
        "foreign_payload",
        "contrasts-with",
    ]:
        if forbidden in renderer:
            failures.append(
                f"renderer contains fixture-specific/inference literal {forbidden!r}"
            )

    report = {
        "campaign": "open-substrate-2026-10-04",
        "phase": "phase-3-explicit-reference-boundary",
        "target_identity": TARGET_ID,
        "trace_identity": TRACE_ID,
        "foreign_payload_id_preserved": (
            trace_raw is not None
            and FOREIGN_ID in trace_raw.read_text(encoding="utf-8")
        ),
        "record_manifest": trace_manifest,
        "result": "PASS" if not failures else "FAIL",
        "failures": failures,
    }
    REPORT.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, indent=2, ensure_ascii=False))

    if failures:
        raise SystemExit("OPEN SUBSTRATE REFERENCE BOUNDARY FAIL: " + "; ".join(failures))


if __name__ == "__main__":
    main()
