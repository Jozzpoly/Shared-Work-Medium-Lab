from __future__ import annotations

import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
SITE = HERE / "site"
FIXTURE = HERE / "fixtures" / "specimen-001"
REPORT = HERE / "open-verification.json"

EXPECTED_ID = "browser-field-knot-001"
EXPECTED_KIND = "browser/field-knot"
EXPECTED_RELATION_KIND = "useful-as-negative-space"
EXPECTED_SOURCE_SHA = "4399ceb14d97d6c1c38da33c643a860b4781277d64763636cf35f846ebeefd07"
OWNER_TITLE = "Węzeł terenowy Browsera"
OWNER_SUMMARY_MARKER = "Pasywna, celowo obca forma"
LOCAL_NOTE_MARKER = "dzisiejszy substrate myli brak znanego typu"
PERSPECTIVE_MARKER = "I created this fixture to pressure the difference"
UNKNOWN_METADATA_MARKER = "asymmetric-knot"

BANNED_IMPLEMENTATION_LITERALS = {
    EXPECTED_ID,
    EXPECTED_KIND,
    EXPECTED_RELATION_KIND,
}


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        for key, value in attrs:
            if key == "href" and value:
                self.hrefs.append(value)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_internal_links(page: Path, failures):
    parser = Links()
    parser.feed(page.read_text(encoding="utf-8"))
    for href in parser.hrefs:
        parsed = urlparse(href)
        if parsed.scheme or parsed.netloc:
            continue
        target = (page.parent / parsed.path).resolve() if parsed.path else page.resolve()
        if not target.is_relative_to(SITE.resolve()) or not target.is_file():
            failures.append(f"{page.relative_to(SITE)}: unresolved link {href}")


def main():
    failures = []

    manifest_path = SITE / "manifest.json"
    if not manifest_path.is_file():
        failures.append("generated manifest is missing")
        manifest = {"objects": []}
    else:
        manifest = read_json(manifest_path)

    objects = manifest.get("objects", [])
    if len(objects) != 1:
        failures.append(f"expected one explicit foreign object, got {len(objects)}")
        obj_entry = None
    else:
        obj_entry = objects[0]

    if obj_entry:
        if obj_entry.get("id") != EXPECTED_ID:
            failures.append("generated identity does not match specimen identity")
        if obj_entry.get("kind") != EXPECTED_KIND:
            failures.append("declared unknown kind was not preserved")

        owner_page = SITE / obj_entry["owner_page"]
        tech_page = SITE / obj_entry["technical_page"]
        raw_object = SITE / obj_entry["raw_object"]

        if not owner_page.is_file():
            failures.append("Owner generic page is missing")
        else:
            text = owner_page.read_text(encoding="utf-8")
            if '<html lang="pl">' not in text:
                failures.append("Owner page is not Polish-first")
            for marker, name in [
                (OWNER_TITLE, "Owner title"),
                (OWNER_SUMMARY_MARKER, "Owner summary"),
                (LOCAL_NOTE_MARKER, "local relation note"),
                (PERSPECTIVE_MARKER, "participant perspective"),
            ]:
                if marker not in text:
                    failures.append(f"{name} is not visible in Owner generic view")
            if obj_entry["technical_page"] not in text:
                failures.append("Owner page has no voluntary path to technical view")

        if not tech_page.is_file():
            failures.append("technical agent/raw page is missing")
        else:
            text = tech_page.read_text(encoding="utf-8")
            if '<html lang="en">' not in text:
                failures.append("technical view is not marked English")
            if UNKNOWN_METADATA_MARKER not in text:
                failures.append("unknown nested metadata disappeared from technical view")

        fixture_object = FIXTURE / "object.json"
        if not raw_object.is_file():
            failures.append("exact raw object.json is missing")
        elif raw_object.read_bytes() != fixture_object.read_bytes():
            failures.append("raw object.json was not preserved byte-for-byte")

        body_rel = obj_entry.get("body", {}).get("relative")
        body_src = FIXTURE / "body" / "note.md"
        if not body_rel:
            failures.append("passive body was not exposed")
        else:
            body_dst = SITE / body_rel
            if not body_dst.is_file() or body_dst.read_bytes() != body_src.read_bytes():
                failures.append("passive body was not preserved byte-for-byte")

        provenance = obj_entry.get("provenance", [])
        if len(provenance) != 1:
            failures.append("expected exact source provenance entry")
        else:
            source_entry = provenance[0]
            source_href = source_entry.get("href")
            if source_entry.get("verified") is not True:
                failures.append("declared source SHA was not verified")
            if not source_href:
                failures.append("source was not exposed")
            else:
                source_dst = SITE / source_href
                if not source_dst.is_file():
                    failures.append("source file is missing")
                elif sha256(source_dst) != EXPECTED_SOURCE_SHA:
                    failures.append("source bytes changed in generated view")

        raw_root = raw_object.parent
        relation_candidates = list(raw_root.rglob("relation.json"))
        perspective_candidates = list(raw_root.rglob("perspective.json"))
        if len(relation_candidates) != 1:
            failures.append("exact local relation record was not preserved")
        else:
            relation = read_json(relation_candidates[0])
            if relation.get("to", {}).get("object_id") != EXPECTED_ID:
                failures.append("local relation no longer targets stable identity")
        if len(perspective_candidates) != 1:
            failures.append("exact participant perspective record was not preserved")
        else:
            perspective = read_json(perspective_candidates[0])
            if perspective.get("about", {}).get("object_id") != EXPECTED_ID:
                failures.append("participant perspective no longer targets stable identity")

    for page in sorted(SITE.rglob("*.html")):
        check_internal_links(page, failures)
        if "<script" in page.read_text(encoding="utf-8").lower():
            failures.append(f"{page.relative_to(SITE)} unexpectedly contains script")

    implementation = (HERE / "open_render.py").read_text(encoding="utf-8")
    for literal in BANNED_IMPLEMENTATION_LITERALS:
        if literal in implementation:
            failures.append(
                f"open_render.py contains specimen-specific implementation literal {literal!r}"
            )

    report = {
        "campaign": "open-substrate-2026-10-04",
        "phase": "phase-1-generic-passive-adapter",
        "manifest_objects": objects,
        "result": "PASS" if not failures else "FAIL",
        "failures": failures,
    }
    REPORT.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, indent=2, ensure_ascii=False))

    if failures:
        raise SystemExit("OPEN SUBSTRATE PHASE 1 FAIL: " + "; ".join(failures))


if __name__ == "__main__":
    main()
