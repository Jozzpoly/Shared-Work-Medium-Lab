from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
QUIET = REPO / "campaigns" / "quiet-presence-2026-10-04"
FIXTURE = HERE / "fixtures" / "specimen-001"
REPORT = HERE / "specimen1-current.json"

OBJECT_ID = "browser-field-knot-001"
UNKNOWN_KIND = "browser/field-knot"
EXPECTED_SOURCE_SHA256 = "4399ceb14d97d6c1c38da33c643a860b4781277d64763636cf35f846ebeefd07"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_python(root: Path, script: str):
    result = subprocess.run(
        ["python", script],
        cwd=root,
        capture_output=True,
        text=True,
        timeout=30,
    )
    return {
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }


def fresh_copy(tmp_root: Path, name: str) -> Path:
    target = tmp_root / name
    shutil.copytree(QUIET, target)
    site = target / "site"
    if site.exists():
        shutil.rmtree(site)
    return target


def rendered_text(root: Path) -> str:
    site = root / "site"
    if not site.exists():
        return ""
    return "\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted(site.rglob("*"))
        if path.is_file() and path.suffix in {".html", ".json", ".md", ".txt"}
    )


def validate_fixture():
    obj = read_json(FIXTURE / "object.json")
    relation = read_json(FIXTURE / "local" / "swm" / "relation.json")
    perspective = read_json(
        FIXTURE / "participants" / "browser" / "perspective.json"
    )
    body = (FIXTURE / "body" / "note.md").read_text(encoding="utf-8")
    source = FIXTURE / "source" / "original-observation.en.md"

    failures = []

    if obj.get("id") != OBJECT_ID:
        failures.append("fixture object id changed")
    if obj.get("kind") != UNKNOWN_KIND:
        failures.append("fixture unknown kind changed")
    if obj.get("views", {}).get("owner", {}).get("language") != "pl":
        failures.append("Owner fixture view is not Polish")
    if obj.get("views", {}).get("agent", {}).get("language") != "en":
        failures.append("agent fixture view is not English")
    if obj.get("body", {}).get("execution") != "none":
        failures.append("specimen #1 must remain passive")
    if "<script" in body.lower():
        failures.append("specimen #1 body unexpectedly contains script")
    if sha256(source) != EXPECTED_SOURCE_SHA256:
        failures.append("original source bytes changed")
    if obj.get("provenance", [{}])[0].get("sha256") != EXPECTED_SOURCE_SHA256:
        failures.append("declared source hash does not match frozen expectation")
    if relation.get("to", {}).get("object_id") != OBJECT_ID:
        failures.append("local relation no longer targets specimen identity")
    if relation.get("relation_kind") != "useful-as-negative-space":
        failures.append("unknown relation semantics changed")
    if perspective.get("about", {}).get("object_id") != OBJECT_ID:
        failures.append("participant perspective no longer targets specimen identity")
    if "unfamiliar_payload" not in obj:
        failures.append("adversarial unknown metadata disappeared")

    return {
        "passes": not failures,
        "failures": failures,
        "object": obj,
        "relation": relation,
        "perspective": perspective,
        "source_sha256": sha256(source),
    }


def observe_current_substrate():
    observations = {}

    with tempfile.TemporaryDirectory(prefix="open-substrate-specimen1-") as td:
        temp = Path(td)

        # A. Merely preserve the foreign package beside today's known families.
        # Current core is expected to ignore it rather than generically expose it.
        standalone = fresh_copy(temp, "standalone")
        foreign = standalone / "foreign" / "specimen-001"
        shutil.copytree(FIXTURE, foreign)
        result = run_python(standalone, "render.py")
        text = rendered_text(standalone)
        owner_title = "Węzeł terenowy Browsera"
        body_marker = "pasywne body"
        observations["foreign_package"] = {
            "render": result,
            "owner_title_visible": owner_title in text,
            "body_visible": body_marker in text.lower(),
            "observation": (
                "generically_visible"
                if owner_title in text
                else "silently_not_discovered"
            ),
        }

        # B. A place tries to point at the foreign thing through today's door shape.
        local = fresh_copy(temp, "local-relation")
        door_path = local / "places" / "swm" / "doors" / "specimen-001.json"
        door_path.write_text(
            json.dumps(
                {
                    "target_kind": UNKNOWN_KIND,
                    "target_id": OBJECT_ID,
                    "local_note": (
                        "W SWM ten obcy węzeł jest lokalnym falsyfikatorem "
                        "zamkniętej ontologii."
                    ),
                    "relation_kind": "useful-as-negative-space",
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        result = run_python(local, "render.py")
        observations["place_points_to_unknown_kind"] = {
            "render": result,
            "accepted": result["returncode"] == 0,
            "unsupported_kind_failure": (
                "unsupported target_kind" in (result["stdout"] + result["stderr"])
            ),
        }

        # C. A participant tries to hold a perspective on the same unknown identity.
        participant = fresh_copy(temp, "participant-perspective")
        participant_dir = participant / "participants" / "browser"
        (participant_dir / "perspectives").mkdir(parents=True, exist_ok=True)
        (participant_dir / "participant.json").write_text(
            json.dumps(
                {
                    "id": "browser",
                    "title": "Browser",
                    "description": "Campaign participant.",
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        (participant_dir / "perspectives" / "specimen-001.json").write_text(
            json.dumps(
                {
                    "target_kind": UNKNOWN_KIND,
                    "target_id": OBJECT_ID,
                    "kind": "working interpretation",
                    "text": (
                        "This perspective is intentionally about a target kind "
                        "the current core does not know."
                    ),
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        result = run_python(participant, "render.py")
        observations["participant_points_to_unknown_kind"] = {
            "render": result,
            "accepted": result["returncode"] == 0,
            "unsupported_kind_failure": (
                "unsupported target_kind" in (result["stdout"] + result["stderr"])
            ),
        }

    return observations


def assert_current_closure(observations):
    failures = []

    foreign = observations["foreign_package"]
    if foreign["render"]["returncode"] != 0:
        failures.append("foreign package unexpectedly breaks ordinary render")
    if foreign["owner_title_visible"]:
        failures.append(
            "current substrate unexpectedly exposes specimen #1 generically; "
            "baseline assumptions need re-audit"
        )

    local = observations["place_points_to_unknown_kind"]
    if local["accepted"] or not local["unsupported_kind_failure"]:
        failures.append(
            "current local-target closure changed; baseline assumptions need re-audit"
        )

    participant = observations["participant_points_to_unknown_kind"]
    if participant["accepted"] or not participant["unsupported_kind_failure"]:
        failures.append(
            "current participant-target closure changed; baseline assumptions need re-audit"
        )

    return failures


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=["current"],
        default="current",
        help=(
            "Phase 0/early Phase 1 mode. A future strict-open mode should be "
            "added only after the substrate mechanism is chosen, so this harness "
            "does not pre-design the implementation."
        ),
    )
    args = parser.parse_args()

    fixture = validate_fixture()
    observations = observe_current_substrate()

    failures = []
    if not fixture["passes"]:
        failures.extend(fixture["failures"])
    if args.mode == "current":
        failures.extend(assert_current_closure(observations))

    report = {
        "campaign": "open-substrate-2026-10-04",
        "specimen": "specimen-001",
        "mode": args.mode,
        "fixture_integrity": {
            "passes": fixture["passes"],
            "failures": fixture["failures"],
            "source_sha256": fixture["source_sha256"],
        },
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
        raise SystemExit("SPECIMEN 001 HARNESS FAIL: " + "; ".join(failures))


if __name__ == "__main__":
    main()
