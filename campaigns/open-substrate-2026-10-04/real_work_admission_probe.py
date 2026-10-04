from __future__ import annotations

import hashlib
import json
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIXTURES = HERE / "fixtures"
REAL_WORK = HERE / "real-work" / "reflex-debug-truth-2026-10-04"
RENDERER = HERE / "open_render.py"
REPORT = HERE / "real-work-admission-01.json"

OBJECT_ID = "reflex-debug-truth-audit-2026-10-04"
EXPECTED_BODY_SHA256 = "6e1045a93fcc612719c9a88fb49a82f18023d1812414f927b10f83e7770dec7e"
EXPECTED_CAPTURE_SHA256 = "2c9d9a9dde54e2b5408aba4c48b2f1a1f0453422db6f93c377a17cd93de3d772"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    failures = []

    object_meta = read_json(REAL_WORK / "object.json")
    body_path = REAL_WORK / "body" / "excerpt.md"
    capture_path = REAL_WORK / "source" / "capture.json"
    capture = read_json(capture_path)

    if object_meta.get("id") != OBJECT_ID:
        failures.append("real-work object identity changed")

    if "kind" in object_meta:
        failures.append("real-work object unexpectedly declares a core kind")

    if sha256(body_path) != EXPECTED_BODY_SHA256:
        failures.append("captured body bytes changed")

    if sha256(capture_path) != EXPECTED_CAPTURE_SHA256:
        failures.append("capture metadata bytes changed")

    if capture.get("body_sha256") != EXPECTED_BODY_SHA256:
        failures.append("capture metadata no longer binds to captured body")

    if capture.get("private_source_locator") != "not persisted in the public Medium repository":
        failures.append("private-source boundary is missing or changed")

    package_text = "\n".join(
        p.read_text(encoding="utf-8")
        for p in REAL_WORK.rglob("*")
        if p.is_file()
    )
    if "chatgpt.com/" in package_text:
        failures.append("private ChatGPT locator leaked into public real-work package")

    with tempfile.TemporaryDirectory(prefix="open-substrate-real-work-") as td:
        out = Path(td) / "site"
        command = ["python", str(RENDERER)]
        for number in (1, 2, 3, 4):
            command += ["--package", str(FIXTURES / f"specimen-00{number}")]
        command += ["--package", str(REAL_WORK), "--out", str(out)]

        result = subprocess.run(
            command,
            cwd=HERE,
            capture_output=True,
            text=True,
            timeout=30,
        )

        if result.returncode != 0:
            failures.append("existing generic renderer rejected real-work package")
            manifest = {"objects": []}
        else:
            manifest = read_json(out / "manifest.json")

        objects = {item["id"]: item for item in manifest.get("objects", [])}
        admitted = objects.get(OBJECT_ID)

        accidental_records = [
            item for item in manifest.get("records", [])
            if item.get("source_package_slug", "").startswith(
                "reflex-debug-truth-audit-2026-10-04-"
            )
        ]
        if accidental_records:
            failures.append(
                "explicit body/provenance files leaked into generic record inventory: "
                + repr([item.get("relative") for item in accidental_records])
            )

        if admitted is None:
            failures.append("real-work object missing from generated manifest")
        else:
            if admitted.get("kind") is not None:
                failures.append("renderer synthesized a kind for real-work object")

            owner_path = out / admitted["owner_page"]
            technical_path = out / admitted["technical_page"]

            owner = owner_path.read_text(encoding="utf-8") if owner_path.is_file() else ""
            technical = technical_path.read_text(encoding="utf-8") if technical_path.is_file() else ""

            for required in [
                "Reflex — granice prawdy debugowania",
                "DEBUG TRUTH audit również dał już bardzo jasny wynik",
                "czyją prawdę pokazuję?",
                "WORLD TRUTH",
                "BODY / SENSOR TRUTH",
                "ACTOR INTERNAL TRUTH",
                "OWNER / NARRATIVE VIEW",
                "Nie redukujemy fenomenu. Rozdzielamy warstwy prawdy.",
            ]:
                if required not in owner:
                    failures.append(f"Owner view lost real-work text {required!r}")

            if "Deklarowany rodzaj:" in owner:
                failures.append("Owner view exposes absent technical kind")

            if "declared kind:</strong> <code>null</code>" not in technical:
                failures.append("technical view does not preserve absent kind as null")

            raw_object = out / admitted["raw_object"]
            if read_json(raw_object) != object_meta:
                failures.append("raw object metadata changed during rendering")

            body = admitted.get("body", {})
            body_relative = body.get("relative")
            if not body_relative:
                failures.append("rendered manifest lost real-work body")
            else:
                copied_body = out / body_relative
                if not copied_body.is_file():
                    failures.append("rendered real-work body file missing")
                elif sha256(copied_body) != EXPECTED_BODY_SHA256:
                    failures.append("rendered real-work body is not byte-preserved")

            provenance = admitted.get("provenance", [])
            if len(provenance) != 2:
                failures.append("real-work provenance count changed")
            for item in provenance:
                if item.get("verified") is not True:
                    failures.append(
                        f"real-work provenance failed integrity verification: {item.get('label')!r}"
                    )

        rendered_text = "\n".join(
            p.read_text(encoding="utf-8", errors="ignore")
            for p in out.rglob("*")
            if p.is_file()
        )
        if "chatgpt.com/" in rendered_text:
            failures.append("private ChatGPT locator leaked into rendered public surface")

        for forbidden in [
            "Feniks uważa",
            "Combat uważa",
            "borrowed-as-debugging-lens",
            "contrasts-with",
        ]:
            admitted_text = ""
            if admitted is not None:
                owner_path = out / admitted["owner_page"]
                technical_path = out / admitted["technical_page"]
                if owner_path.is_file():
                    admitted_text += owner_path.read_text(encoding="utf-8")
                if technical_path.is_file():
                    admitted_text += technical_path.read_text(encoding="utf-8")
            if forbidden in admitted_text:
                failures.append(
                    f"real-work admission manufactured foreign-project meaning {forbidden!r}"
                )

        report = {
            "campaign": "open-substrate-2026-10-04",
            "phase": "real-work-admission-01",
            "object_id": OBJECT_ID,
            "bespoke_renderer_branch_added": False,
            "generic_adapter_changed_due_real_work_pressure": True,
            "generic_adapter_change": (
                "explicit declared body/provenance roles outrank generic JSON-record discovery"
            ),
            "source_class": "browser-observed real project conversation excerpt",
            "private_locator_persisted": False,
            "generic_records_from_real_work_package": [
                item.get("relative") for item in accidental_records
            ],
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
        raise SystemExit("REAL-WORK ADMISSION FAIL: " + "; ".join(failures))


if __name__ == "__main__":
    main()
