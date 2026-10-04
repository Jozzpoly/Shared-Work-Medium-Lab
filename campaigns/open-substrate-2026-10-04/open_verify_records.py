from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE = HERE / "site"
SPECIMEN1 = HERE / "fixtures" / "specimen-001"
SPECIMEN2 = HERE / "fixtures" / "specimen-002"
REPORT = HERE / "record-verification.json"

TARGET_ID = "browser-field-knot-001"
TRACE_ID = "reflex-local-trace-001"
TRACE_KIND = "reflex/borrowed-lens"
RELATION_KIND = "borrowed-as-debugging-lens"
OWNER_TITLE = "Lokalny ślad Reflexu"
OWNER_NOTE_MARKER = "To znaczenie należy do Reflexu"
BANNED_RENDERER_LITERALS = {
    TRACE_ID,
    TRACE_KIND,
    RELATION_KIND,
    "reflex",
}


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    failures = []

    manifest_path = SITE / "manifest.json"
    if not manifest_path.is_file():
        failures.append("Open Substrate manifest is missing")
        manifest = {"objects": [], "records": []}
    else:
        manifest = read_json(manifest_path)

    objects = manifest.get("objects", [])
    records = manifest.get("records", [])

    target = next((item for item in objects if item.get("id") == TARGET_ID), None)
    if target is None:
        failures.append("target shared identity is missing from generated object index")

    trace_raw = None
    trace_manifest = None
    for item in records:
        raw_href = item.get("raw_href")
        if not raw_href:
            continue
        raw_path = SITE / raw_href
        if not raw_path.is_file():
            continue
        try:
            data = read_json(raw_path)
        except json.JSONDecodeError:
            continue
        if data.get("trace_id") == TRACE_ID:
            trace_raw = raw_path
            trace_manifest = item
            break

    if trace_raw is None or trace_manifest is None:
        failures.append("relation-only Reflex trace is not preserved in generated raw records")
    else:
        original_trace = SPECIMEN2 / "trace.json"
        if trace_raw.read_bytes() != original_trace.read_bytes():
            failures.append("relation-only trace bytes changed during derivation")

        if trace_manifest.get("source_package_role") != "records":
            failures.append("relation-only trace was promoted to an object package")

        refs = trace_manifest.get("references", [])
        targets = {ref.get("object_id") for ref in refs}
        if TARGET_ID not in targets:
            failures.append("record manifest lost stable target identity reference")

        trace_data = read_json(trace_raw)
        if trace_data.get("owner_scope") != {
            "scope_kind": "place",
            "scope_id": "reflex",
        }:
            failures.append("Reflex local ownership changed")
        if trace_data.get("relation", {}).get("kind") != RELATION_KIND:
            failures.append("unknown relation semantics were flattened or changed")
        if trace_data.get("relation", {}).get("to", {}).get("object_id") != TARGET_ID:
            failures.append("trace no longer points to the target shared identity")

    if target is not None:
        owner_page = SITE / target["owner_page"]
        if not owner_page.is_file():
            failures.append("target Owner page is missing")
        else:
            text = owner_page.read_text(encoding="utf-8")
            if OWNER_TITLE not in text:
                failures.append("Reflex-owned trace title is not visible beside target")
            if OWNER_NOTE_MARKER not in text:
                failures.append("Reflex local meaning is not visible beside target")
            if RELATION_KIND not in text:
                failures.append("unknown relation semantics are not inspectable")
            if trace_manifest and trace_manifest.get("raw_href") not in text:
                failures.append("Owner view has no path to exact Reflex raw trace")

        raw_object = SITE / target["raw_object"]
        original_object = SPECIMEN1 / "object.json"
        if not raw_object.is_file() or raw_object.read_bytes() != original_object.read_bytes():
            failures.append("target shared object bytes changed while adding external trace")

    # The target fixture itself must remain physically untouched.
    if (SPECIMEN1 / "local" / "reflex").exists():
        failures.append("Reflex trace leaked into specimen #1 source package")

    renderer = (HERE / "open_render.py").read_text(encoding="utf-8")
    for literal in BANNED_RENDERER_LITERALS:
        if literal in renderer:
            failures.append(
                f"open_render.py contains specimen-002-specific literal {literal!r}"
            )

    report = {
        "campaign": "open-substrate-2026-10-04",
        "phase": "phase-2-independent-record-packages",
        "target_identity": TARGET_ID,
        "trace_identity": TRACE_ID,
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
        raise SystemExit("OPEN SUBSTRATE RECORD PACKAGE FAIL: " + "; ".join(failures))


if __name__ == "__main__":
    main()
