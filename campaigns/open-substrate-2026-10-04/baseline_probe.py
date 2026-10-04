from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
QUIET = REPO / "campaigns" / "quiet-presence-2026-10-04"
REPORT = HERE / "baseline.json"

MARKER = "OPEN_SUBSTRATE_UNKNOWN_FIELD_MARKER_PL"


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


def render_text(root: Path) -> str:
    site = root / "site"
    if not site.exists():
        return ""
    return "\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted(site.rglob("*.html"))
    )


def main():
    observations = {}

    with tempfile.TemporaryDirectory(prefix="open-substrate-baseline-") as td:
        temp = Path(td)

        # 0. Known Quiet Presence should remain a valid baseline.
        known = fresh_copy(temp, "known")
        known_render = run_python(known, "render.py")
        known_verify = run_python(known, "verify.py") if known_render["returncode"] == 0 else None
        observations["known_quiet_presence"] = {
            "render": known_render,
            "verify": known_verify,
            "passes": (
                known_render["returncode"] == 0
                and known_verify is not None
                and known_verify["returncode"] == 0
            ),
        }

        # 1. Put a completely new standalone object family beside the known families.
        #    Does discovery notice it without any platform change?
        standalone = fresh_copy(temp, "unknown-standalone")
        organisms = standalone / "organisms"
        organisms.mkdir(exist_ok=True)
        (organisms / "baseline-organism.json").write_text(
            json.dumps(
                {
                    "id": "baseline-organism",
                    "kind": "experimental/strange-organism",
                    "title": "Dziwny organizm bazowy",
                    "unknown_payload": {"shape": "spiral", "answer": 17},
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        standalone_render = run_python(standalone, "render.py")
        standalone_output = render_text(standalone)
        observations["unknown_standalone_family"] = {
            "render_returncode": standalone_render["returncode"],
            "title_appears_in_generated_view": "Dziwny organizm bazowy" in standalone_output,
            "observation": (
                "discovered"
                if "Dziwny organizm bazowy" in standalone_output
                else "silently_not_discovered"
            ),
        }

        # 2. Create a local door with semantics the current core does not know.
        unknown_door = fresh_copy(temp, "unknown-door")
        door_path = unknown_door / "places" / "swm" / "doors" / "baseline-unknown.json"
        door_path.write_text(
            json.dumps(
                {
                    "target_kind": "organism",
                    "target_id": "baseline-organism",
                    "local_note": "Eksperymentalny lokalny ślad do nieznanej formy.",
                    "relation_kind": "learned-from",
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        unknown_door_render = run_python(unknown_door, "render.py")
        observations["unknown_local_relation_target"] = {
            "render": unknown_door_render,
            "accepted": unknown_door_render["returncode"] == 0,
            "mentions_unsupported_target_kind": (
                "unsupported target_kind" in (
                    unknown_door_render["stdout"] + unknown_door_render["stderr"]
                )
            ),
        }

        # 3. Create a participant-owned perspective to an unknown target family.
        unknown_perspective = fresh_copy(temp, "unknown-perspective")
        perspective_path = (
            unknown_perspective
            / "participants"
            / "codex"
            / "perspectives"
            / "baseline-unknown.json"
        )
        perspective_path.write_text(
            json.dumps(
                {
                    "target_kind": "organism",
                    "target_id": "baseline-organism",
                    "kind": "experimental perspective",
                    "text": "This is intentionally a perspective on a target family the core does not know.",
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        unknown_perspective_render = run_python(unknown_perspective, "render.py")
        observations["unknown_participant_target"] = {
            "render": unknown_perspective_render,
            "accepted": unknown_perspective_render["returncode"] == 0,
            "mentions_unsupported_target_kind": (
                "unsupported target_kind" in (
                    unknown_perspective_render["stdout"]
                    + unknown_perspective_render["stderr"]
                )
            ),
        }

        # 4. Add future metadata to a known object. Does the derived human view retain/surface it?
        extra_field = fresh_copy(temp, "unknown-field")
        artifact_path = extra_field / "artifacts" / "codex-exchange-window.json"
        artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
        artifact["future_extension"] = {
            "owner_summary_pl": MARKER,
            "agent_hint_en": "Unknown extension field preserved in source.",
        }
        artifact_path.write_text(
            json.dumps(artifact, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        extra_render = run_python(extra_field, "render.py")
        extra_output = render_text(extra_field)
        observations["unknown_field_on_known_object"] = {
            "render_returncode": extra_render["returncode"],
            "source_field_survives": MARKER in artifact_path.read_text(encoding="utf-8"),
            "field_visible_in_generated_view": MARKER in extra_output,
        }

        # 5. Characterize the current default audience language rather than judging it.
        language = fresh_copy(temp, "language")
        language_render = run_python(language, "render.py")
        index = (
            (language / "site" / "index.html").read_text(encoding="utf-8")
            if (language / "site" / "index.html").exists()
            else ""
        )
        observations["current_owner_surface_language"] = {
            "render_returncode": language_render["returncode"],
            "html_lang_en": '<html lang="en">' in index,
            "contains_english_entry_label": "Enter this place" in index,
            "contains_polish_entry_label": "Wejdź" in index,
        }

    report = {
        "campaign": "open-substrate-2026-10-04",
        "phase": "baseline-characterization",
        "source_specimen": "campaigns/quiet-presence-2026-10-04",
        "observations": observations,
    }
    REPORT.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, indent=2, ensure_ascii=False))

    if not observations["known_quiet_presence"]["passes"]:
        raise SystemExit("Baseline invalid: known Quiet Presence no longer passes its own renderer/verifier.")


if __name__ == "__main__":
    main()
