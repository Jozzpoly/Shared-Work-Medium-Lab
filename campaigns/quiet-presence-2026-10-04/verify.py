from __future__ import annotations

import json
import hashlib
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "site"

FORBIDDEN_GLOBAL_FIELDS = {
    "priority",
    "importance",
    "global_rank",
    "relevance_score",
    "unread_count",
    "notification_count",
    "requires_attention",
    "urgent",
}


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for key, value in attrs:
                if key == "href" and value:
                    self.hrefs.append(value)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def walk_forbidden(obj, failures, path="$"):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in FORBIDDEN_GLOBAL_FIELDS:
                failures.append(f"forbidden global attention/ranking field at {path}.{key}")
            walk_forbidden(value, failures, f"{path}.{key}")
    elif isinstance(obj, list):
        for index, item in enumerate(obj):
            walk_forbidden(item, failures, f"{path}[{index}]")


def load_objects():
    campaign = read_json(ROOT / "campaign.json")

    places = {}
    doors_by_place = {}
    for place_file in sorted((ROOT / "places").glob("*/place.json")):
        place = read_json(place_file)
        places[place["id"]] = place
        doors = []
        door_dir = place_file.parent / "doors"
        if door_dir.exists():
            for door_file in sorted(door_dir.glob("*.json")):
                door = read_json(door_file)
                door["_source_path"] = str(door_file.relative_to(ROOT))
                doors.append(door)
        doors_by_place[place["id"]] = doors

    episodes = {
        item["id"]: item
        for item in (
            read_json(path)
            for path in sorted((ROOT / "episodes").glob("*.json"))
        )
    }
    artifacts = {
        item["id"]: item
        for item in (
            read_json(path)
            for path in sorted((ROOT / "artifacts").glob("*.json"))
        )
    }

    sources = {
        item["id"]: item
        for item in (
            read_json(path)
            for path in sorted((ROOT / "sources").glob("*.json"))
        )
    } if (ROOT / "sources").exists() else {}

    participants = {}
    perspectives_by_participant = {}
    participants_root = ROOT / "participants"
    if participants_root.exists():
        for participant_file in sorted(participants_root.glob("*/participant.json")):
            participant = read_json(participant_file)
            participant_id = participant["id"]
            participants[participant_id] = participant
            perspectives = []
            perspective_dir = participant_file.parent / "perspectives"
            if perspective_dir.exists():
                for perspective_file in sorted(perspective_dir.glob("*.json")):
                    perspective = read_json(perspective_file)
                    perspective["_source_path"] = str(perspective_file.relative_to(ROOT))
                    perspectives.append(perspective)
            perspectives_by_participant[participant_id] = perspectives

    return (
        campaign,
        places,
        doors_by_place,
        episodes,
        artifacts,
        sources,
        participants,
        perspectives_by_participant,
    )


def main():
    failures = []
    (
        campaign,
        places,
        doors_by_place,
        episodes,
        artifacts,
        sources,
        participants,
        perspectives_by_participant,
    ) = load_objects()

    # The campaign must not smuggle global ranking/attention fields into any local object.
    walk_forbidden(campaign, failures, "$.campaign")
    for place_id, place in places.items():
        walk_forbidden(place, failures, f"$.places.{place_id}")
    for episode_id, episode in episodes.items():
        walk_forbidden(episode, failures, f"$.episodes.{episode_id}")
    for artifact_id, artifact in artifacts.items():
        walk_forbidden(artifact, failures, f"$.artifacts.{artifact_id}")
        if "placements" in artifact:
            failures.append(
                f"artifact {artifact_id} contains central placements; "
                "local meanings must live in place-owned door files"
            )
        if "author_claim" in artifact:
            failures.append(
                f"artifact {artifact_id} contains participant interpretation; "
                "participant claims must live in participant-owned perspectives"
            )
        if not artifact.get("body_href") and not artifact.get("body_availability"):
            failures.append(
                f"artifact {artifact_id} exposes neither a body nor an explicit availability status"
            )

    for source_id, source in sources.items():
        walk_forbidden(source, failures, f"$.sources.{source_id}")
        if not source.get("href"):
            failures.append(f"source {source_id} has no href")
        revision = source.get("revision")
        if revision and revision not in source.get("href", ""):
            failures.append(
                f"source {source_id} declares revision {revision} "
                "but href is not revision-bound"
            )

    for participant_id, participant in participants.items():
        walk_forbidden(participant, failures, f"$.participants.{participant_id}")
        for index, perspective in enumerate(
            perspectives_by_participant.get(participant_id, [])
        ):
            walk_forbidden(
                perspective,
                failures,
                f"$.participants.{participant_id}.perspectives[{index}]",
            )
    for place_id, doors in doors_by_place.items():
        for index, door in enumerate(doors):
            walk_forbidden(door, failures, f"$.places.{place_id}.doors[{index}]")

    # Every local door resolves without editing the target artifact/episode itself.
    for place_id, doors in doors_by_place.items():
        for door in doors:
            kind = door.get("target_kind")
            target_id = door.get("target_id")
            source = door["_source_path"]

            if kind == "artifact" and target_id not in artifacts:
                failures.append(f"{source}: unknown artifact {target_id}")
            elif kind == "episode" and target_id not in episodes:
                failures.append(f"{source}: unknown episode {target_id}")
            elif kind == "source" and target_id not in sources:
                failures.append(f"{source}: unknown source {target_id}")
            elif kind not in {"artifact", "episode", "source"}:
                failures.append(f"{source}: unsupported target_kind {kind}")

            if not door.get("local_note"):
                failures.append(f"{source}: missing local_note")

    # Participant-owned perspectives resolve without becoming artifact identity.
    for participant_id, perspectives in perspectives_by_participant.items():
        for perspective in perspectives:
            kind = perspective.get("target_kind")
            target_id = perspective.get("target_id")
            source = perspective["_source_path"]
            if kind == "artifact" and target_id not in artifacts:
                failures.append(f"{source}: unknown artifact {target_id}")
            elif kind == "episode" and target_id not in episodes:
                failures.append(f"{source}: unknown episode {target_id}")
            elif kind not in {"artifact", "episode"}:
                failures.append(f"{source}: unsupported target_kind {kind}")
            if not perspective.get("text"):
                failures.append(f"{source}: missing perspective text")

    # Concrete campaign claim: one shared artifact has two independent local meanings.
    exchange_id = "codex-exchange-window"
    refs = {}
    for place_id, doors in doors_by_place.items():
        for door in doors:
            if door.get("target_kind") == "artifact" and door.get("target_id") == exchange_id:
                refs[place_id] = door["local_note"]

    if not {"combat", "swm"}.issubset(refs):
        failures.append(
            "codex-exchange-window is not independently referenced by both Combat and SWM"
        )
    elif refs["combat"] == refs["swm"]:
        failures.append(
            "Combat and SWM local interpretations were flattened into one note"
        )

    # Continuity anchors remain more specific than one generic address.
    for episode_id, episode in episodes.items():
        anchor = episode.get("continuity_anchor")
        if anchor:
            if not anchor.get("predecessor_turn") or not anchor.get("confirmed_entry_turn"):
                failures.append(f"{episode_id}: incomplete continuity anchor")
            elif anchor["predecessor_turn"] == anchor["confirmed_entry_turn"]:
                failures.append(
                    f"{episode_id}: predecessor and entry collapsed into one identity"
                )

    # Rendered topology.
    html_files = sorted(SITE.glob("*.html"))
    expected_pages = 1 + len(places) + len(episodes) + len(artifacts)
    if len(html_files) != expected_pages:
        failures.append(
            f"expected {expected_pages} generated pages, got {len(html_files)}"
        )

    for page in sorted(SITE.rglob("*.html")):
        parser = Links()
        parser.feed(page.read_text(encoding="utf-8"))
        for href in parser.hrefs:
            parsed = urlparse(href)
            if parsed.scheme or parsed.netloc:
                continue
            target = (page.parent / parsed.path).resolve() if parsed.path else page.resolve()
            if not target.is_relative_to(SITE.resolve()) or not target.is_file():
                failures.append(f"{page.relative_to(SITE)}: unresolved internal link {href}")

    # Root must remain informationally quiet.
    root_text = (SITE / "index.html").read_text(encoding="utf-8")
    forbidden_root_markers = []

    for episode in episodes.values():
        forbidden_root_markers.append(episode["title"])
        anchor = episode.get("continuity_anchor", {})
        forbidden_root_markers.extend([
            anchor.get("predecessor_turn"),
            anchor.get("confirmed_entry_turn"),
        ])

    for artifact in artifacts.values():
        forbidden_root_markers.append(artifact["title"])

    for perspectives in perspectives_by_participant.values():
        for perspective in perspectives:
            forbidden_root_markers.append(perspective.get("text"))

    for marker in [x for x in forbidden_root_markers if x]:
        if marker in root_text:
            failures.append(f"deep trace leaked into root surface: {marker}")

    # Root links only to places, never directly to artifacts/episodes.
    root_parser = Links()
    root_parser.feed(root_text)
    root_internal = [
        urlparse(href).path
        for href in root_parser.hrefs
        if not urlparse(href).scheme
    ]
    expected_place_links = {f"place-{place_id}.html" for place_id in places}
    if set(root_internal) != expected_place_links:
        failures.append(
            f"root links are not place-only: {sorted(set(root_internal))}"
        )

    # No language that explicitly demands attention.
    rendered = "\n".join(
        p.read_text(encoding="utf-8").lower()
        for p in html_files
    )
    for phrase in ["mark as read", "you must read", "requires your attention"]:
        if phrase in rendered:
            failures.append(f"attention-demand language leaked into specimen: {phrase}")

    # Public field snapshot must preserve core canonical truths.
    field_root = ROOT / "field-surface.html"
    field_feniks = ROOT / "field-place-feniks.html"
    field_artifact = ROOT / "field-artifact-codex-exchange-window.html"

    if not field_root.exists():
        failures.append("public field root is missing")
    else:
        field_root_text = field_root.read_text(encoding="utf-8")
        if campaign["question"] not in field_root_text:
            failures.append("public field root does not match current campaign question")
        for marker in [x for x in forbidden_root_markers if x]:
            if marker in field_root_text:
                failures.append(
                    f"deep trace leaked into public field root: {marker}"
                )

    for place_id, doors in doors_by_place.items():
        field_place = ROOT / f"field-place-{place_id}.html"
        source_doors = [
            door for door in doors if door.get("target_kind") == "source"
        ]
        if source_doors and not field_place.exists():
            failures.append(
                f"public field page for {place_id} is missing despite source doors"
            )
            continue
        if field_place.exists():
            field_text = field_place.read_text(encoding="utf-8")
            for door in source_doors:
                source_id = door["target_id"]
                source_href = sources[source_id]["href"]
                # The field HTML is browsed through HTMLPreview, which rewrites
                # fragment-bearing hrefs into preview-local navigation. This
                # previously made a valid GitHub donor URL lead back to Combat.
                # Check this transport-specific failure, not research semantics.
                if urlparse(source_href).fragment:
                    failures.append(
                        f"public {place_id} source door {source_id} uses a fragment "
                        "that HTMLPreview rewrites"
                    )
                if source_href not in field_text:
                    failures.append(
                        f"public {place_id} field page does not expose source door {source_id}"
                    )

    exchange = artifacts.get("codex-exchange-window")
    if exchange and exchange.get("body_availability"):
        status = exchange["body_availability"].get("status")
        if not field_artifact.exists():
            failures.append("public exchange-window field page is missing")
        elif status and status not in field_artifact.read_text(encoding="utf-8"):
            failures.append(
                "public exchange-window page hides canonical body availability status"
            )
    if exchange and exchange.get("body_href"):
        field_links = Links()
        field_links.feed(field_artifact.read_text(encoding="utf-8"))
        if exchange["body_href"] not in field_links.hrefs:
            failures.append("public exchange-window page does not open its recovered body")

        body_dir = (ROOT / exchange["body_href"]).parent
        recovery = read_json(body_dir / "recovery.json")
        for filename, expected_hash in recovery["originalFilesSha256"].items():
            preserved = body_dir / filename
            if not preserved.is_file() or hashlib.sha256(preserved.read_bytes()).hexdigest() != expected_hash:
                failures.append(f"original window source changed after recovery: {filename}")

        original_messages = {}
        for filename in ("COMBAT_EXCHANGE_1.json", "COMBAT_EXCHANGE_2.json", "GUIDE_EXCHANGE.json"):
            record = read_json(body_dir / filename)
            for turn in record.get("returnedTurns", record.get("turns", [])):
                for item in turn["items"]:
                    if item["type"] not in {"userMessage", "agentMessage"}:
                        continue
                    text = item.get("text")
                    if text is None:
                        text = "\n".join(c["text"] for c in item.get("content", []) if c.get("type") == "text")
                    original_messages[item["id"]] = (turn["id"], text)
        recovered_messages = read_json(body_dir / "messages.json")
        recovered_ids = [message["messageId"] for message in recovered_messages]
        if len(recovered_ids) != len(set(recovered_ids)) or set(recovered_ids) != set(original_messages):
            failures.append("full window trace omits or duplicates original messages")
        for message in recovered_messages:
            if original_messages.get(message["messageId"]) != (message["turnId"], message["text"]):
                failures.append(f"window message is not exact: {message['messageId']}")

    report = {
        "campaign": campaign["id"],
        "places": sorted(places),
        "episodes": sorted(episodes),
        "artifacts": sorted(artifacts),
        "sources": sorted(sources),
        "participants": sorted(participants),
        "participant_perspective_count": sum(
            len(items) for items in perspectives_by_participant.values()
        ),
        "pages": [p.name for p in html_files],
        "exchange_window_local_meanings": refs,
        "central_artifact_placements_present": any(
            "placements" in artifact for artifact in artifacts.values()
        ),
        "artifact_participant_claims_present": any(
            "author_claim" in artifact for artifact in artifacts.values()
        ),
        "root_internal_links": root_internal,
        "result": "PASS" if not failures else "FAIL",
        "failures": failures,
    }

    (ROOT / "verification.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, indent=2, ensure_ascii=False))

    if failures:
        raise SystemExit("QUIET PRESENCE SPECIMEN FAIL: " + "; ".join(failures))

    print(
        "QUIET PRESENCE SPECIMEN PASS: shared artifact identity, "
        "place-owned local meaning, quiet root, and deep trace remain distinct."
    )


if __name__ == "__main__":
    main()
