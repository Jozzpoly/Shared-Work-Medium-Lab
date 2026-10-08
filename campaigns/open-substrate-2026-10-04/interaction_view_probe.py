from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIXTURES = HERE / "fixtures"
RENDERER = HERE / "open_render.py"
REPORT = HERE / "interaction-view-verification.json"

RICH_ID = "browser-field-knot-001"
MINIMAL_ID = "minimal-shared-identity-004"
ENGLISH_PERSPECTIVE = "I created this fixture to pressure the difference"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    failures = []

    with tempfile.TemporaryDirectory(prefix="open-substrate-interaction-view-") as td:
        out = Path(td) / "site"
        command = ["python", str(RENDERER)]
        for number in (1, 2, 3, 4):
            command += ["--package", str(FIXTURES / f"specimen-00{number}")]
        command += ["--out", str(out)]

        result = subprocess.run(
            command,
            cwd=HERE,
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode != 0:
            failures.append("interaction preview render failed")
            manifest = {"objects": []}
        else:
            manifest = read_json(out / "manifest.json")

        objects = {item["id"]: item for item in manifest.get("objects", [])}

        root = (out / "index.html").read_text(encoding="utf-8") if (out / "index.html").is_file() else ""
        if "Rodzaj deklarowany:" in root:
            failures.append("root still exposes declared kind before Owner needs it")

        rich = objects.get(RICH_ID)
        if rich is None:
            failures.append("rich object missing from interaction preview")
        else:
            owner_path = out / rich["owner_page"]
            tech_path = out / rich["technical_page"]
            owner = owner_path.read_text(encoding="utf-8") if owner_path.is_file() else ""
            tech = tech_path.read_text(encoding="utf-8") if tech_path.is_file() else ""

            if "Deklarowany rodzaj:" in owner:
                failures.append("rich Owner view still exposes declared kind")

            notice = 'Oryginalna treść uczestnika jest w języku <code>en</code>.'
            if notice not in owner:
                failures.append("English participant perspective has no Polish Owner wrapper")

            original_at = owner.find(ENGLISH_PERSPECTIVE)
            details_at = owner.find("<details>", owner.find("Perspektywa uczestnika: browser"))
            details_end = owner.find("</details>", details_at)
            if original_at < 0:
                failures.append("exact English participant perspective disappeared")
            elif not (details_at >= 0 and details_at < original_at < details_end):
                failures.append("exact English perspective is not behind voluntary disclosure")

            for semantic in [
                "working-interpretation",
                "borrowed-as-debugging-lens",
                "contrasts-with",
            ]:
                semantic_at = owner.find(semantic)
                if semantic_at < 0:
                    failures.append(f"technical semantic marker {semantic!r} disappeared")
                    continue
                enclosing_details = owner.rfind("<details>", 0, semantic_at)
                enclosing_end = owner.find("</details>", enclosing_details)
                if not (enclosing_details >= 0 and semantic_at < enclosing_end):
                    failures.append(
                        f"technical semantic marker {semantic!r} is still exposed outside disclosure"
                    )

            # Slugs identify exact record+reference bytes, so changing the
            # refs contract must change the slug. Test two distinct displayed
            # independent records, not historical digest literals.
            independent_records = [
                item
                for item in manifest.get("records", [])
                if item.get("source_package_role") == "records"
                and item.get("relative") == "trace.json"
                and any(
                    ref.get("object_id") == RICH_ID
                    for ref in item.get("references", [])
                )
            ]
            expected_technical_labels = [
                f'{item["source_package_slug"]} / {item["relative"]}'
                for item in independent_records
            ]
            if len(independent_records) != 2:
                failures.append(
                    "rich technical view did not retain both independent trace records"
                )
            elif len(set(expected_technical_labels)) != 2:
                failures.append(
                    "independent record packages aliased one technical display identity"
                )
            for label in expected_technical_labels:
                if label not in tech:
                    failures.append(
                        f"technical view does not disambiguate independent record label {label!r}"
                    )

        minimal = objects.get(MINIMAL_ID)
        if minimal is None:
            failures.append("minimal object missing from interaction preview")
        else:
            owner_path = out / minimal["owner_page"]
            owner = owner_path.read_text(encoding="utf-8") if owner_path.is_file() else ""

            if "Ta rzecz deklaruje obecnie tylko tożsamość." not in owner:
                failures.append("minimal Owner view lacks compact sparse-state explanation")
            for empty_section in [
                "<h2>Treść</h2>",
                "<h2>Źródła</h2>",
                "<h2>Powiązane lokalne i uczestnikowe zapisy</h2>",
            ]:
                if empty_section in owner:
                    failures.append(
                        f"minimal Owner view still renders empty schema section {empty_section!r}"
                    )

        report = {
            "campaign": "open-substrate-2026-10-04",
            "phase": "interaction-view-progressive-disclosure",
            "render_returncode": result.returncode,
            "objects": list(objects),
            "result": "PASS" if not failures else "FAIL",
            "failures": failures,
        }

    REPORT.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, indent=2, ensure_ascii=False))

    if failures:
        raise SystemExit("INTERACTION VIEW FAIL: " + "; ".join(failures))


if __name__ == "__main__":
    main()
