from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "site"

CSS = """
:root { color-scheme: dark; }
* { box-sizing: border-box; }
body {
  margin: 0;
  background: #111214;
  color: #e8e8e8;
  font: 16px/1.55 system-ui, sans-serif;
}
a { color: #b7d7ff; }
.wrap { max-width: 920px; margin: 0 auto; padding: 34px 22px 72px; }
header { margin-bottom: 28px; }
h1 { margin: 0 0 8px; font-size: 34px; }
h2 { margin: 28px 0 10px; }
h3 { margin: 0 0 7px; }
.muted { color: #a6abb3; }
.grid { display: grid; gap: 14px; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); }
.card {
  border: 1px solid #30343a;
  border-radius: 12px;
  background: #181a1e;
  padding: 16px;
}
.note {
  border: 1px solid #343a43;
  border-radius: 9px;
  padding: 12px;
  background: #15171a;
  margin-top: 12px;
}
.trace { border-left: 3px solid #48515d; padding-left: 14px; margin-top: 14px; }
.tag {
  display: inline-block;
  border: 1px solid #3d454f;
  border-radius: 999px;
  padding: 2px 8px;
  margin: 2px 4px 2px 0;
  font-size: 12px;
  color: #c7cbd1;
}
nav { margin: 0 0 24px; }
small, code { color: #a6abb3; }
footer { margin-top: 42px; color: #8f949c; font-size: 13px; }
"""

def esc(value):
    return html.escape(str(value))

def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def page(title, body):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<style>{CSS}</style>
</head>
<body><main class="wrap">{body}</main></body>
</html>"""

def home_link():
    return '<nav><a href="index.html">← Places</a></nav>'

def place_filename(place_id):
    return f"place-{place_id}.html"

def episode_filename(episode_id):
    return f"episode-{episode_id}.html"

def artifact_filename(artifact_id):
    return f"artifact-{artifact_id}.html"

def normalize_source_href(ref):
    href = ref.get("href", "")
    if href.startswith("../../docs/"):
        filename = href.split("/")[-1]
        return (
            "https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/main/docs/"
            + filename
        )
    return href

def load_campaign():
    campaign = read_json(ROOT / "campaign.json")

    places = {}
    doors_by_place = {}
    for place_file in sorted((ROOT / "places").glob("*/place.json")):
        place = read_json(place_file)
        place_id = place["id"]
        places[place_id] = place

        doors = []
        door_dir = place_file.parent / "doors"
        if door_dir.exists():
            for door_file in sorted(door_dir.glob("*.json")):
                door = read_json(door_file)
                door["_source_path"] = str(door_file.relative_to(ROOT))
                doors.append(door)
        doors_by_place[place_id] = doors

    episodes = {
        data["id"]: data
        for data in (
            read_json(path)
            for path in sorted((ROOT / "episodes").glob("*.json"))
        )
    }
    artifacts = {
        data["id"]: data
        for data in (
            read_json(path)
            for path in sorted((ROOT / "artifacts").glob("*.json"))
        )
    }

    sources = {
        data["id"]: data
        for data in (
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
    (
        campaign,
        places,
        doors_by_place,
        episodes,
        artifacts,
        sources,
        participants,
        perspectives_by_participant,
    ) = load_campaign()
    OUT.mkdir(parents=True, exist_ok=True)

    # Validate only what the renderer needs to guarantee.
    for artifact in artifacts.values():
        if artifact["origin_episode"] not in episodes:
            raise SystemExit(
                f"Artifact {artifact['id']} references unknown origin episode "
                f"{artifact['origin_episode']}"
            )

    for place_id, doors in doors_by_place.items():
        for door in doors:
            kind = door["target_kind"]
            target = door["target_id"]
            if kind == "episode" and target not in episodes:
                raise SystemExit(
                    f"{door['_source_path']} references unknown episode {target}"
                )
            if kind == "artifact" and target not in artifacts:
                raise SystemExit(
                    f"{door['_source_path']} references unknown artifact {target}"
                )
            if kind == "source" and target not in sources:
                raise SystemExit(
                    f"{door['_source_path']} references unknown source {target}"
                )
            if kind not in {"episode", "artifact", "source"}:
                raise SystemExit(
                    f"{door['_source_path']} has unsupported target_kind {kind}"
                )

    # Participant-owned perspectives must resolve without mutating shared artifact identity.
    for participant_id, perspectives in perspectives_by_participant.items():
        for perspective in perspectives:
            kind = perspective["target_kind"]
            target = perspective["target_id"]
            if kind == "artifact" and target not in artifacts:
                raise SystemExit(
                    f"{perspective['_source_path']} references unknown artifact {target}"
                )
            if kind == "episode" and target not in episodes:
                raise SystemExit(
                    f"{perspective['_source_path']} references unknown episode {target}"
                )
            if kind not in {"artifact", "episode"}:
                raise SystemExit(
                    f"{perspective['_source_path']} has unsupported target_kind {kind}"
                )

    # Root is intentionally quiet: only places and their current questions.
    cards = []
    for place_id in sorted(places):
        p = places[place_id]
        cards.append(f"""<article class="card">
<h2>{esc(p["title"])}</h2>
<p>{esc(p["description"])}</p>
<p class="muted">{esc(p["current_question"])}</p>
<p><a href="{place_filename(place_id)}">Enter this place</a></p>
</article>""")

    root = f"""
<header>
<h1>{esc(campaign["title"])}</h1>
<p>{esc(campaign["question"])}</p>
<p class="muted">You do not need to inspect everything that exists here.</p>
</header>
<section class="grid" aria-label="Places">
{''.join(cards)}
</section>
<footer>This surface is intentionally incomplete. Something may happen elsewhere and never appear here. That is not automatically a failure.</footer>
"""
    (OUT / "index.html").write_text(
        page(campaign["title"], root),
        encoding="utf-8",
    )

    # Each place owns only its local doors. No central placement list is required.
    for place_id in sorted(places):
        p = places[place_id]
        rendered_doors = []

        for door in doors_by_place[place_id]:
            target_id = door["target_id"]
            if door["target_kind"] == "episode":
                target = episodes[target_id]
                href = episode_filename(target_id)
                kind_label = "Preserved episode"
                action_label = "Open episode"
            elif door["target_kind"] == "artifact":
                target = artifacts[target_id]
                href = artifact_filename(target_id)
                kind_label = "Local artifact"
                action_label = "Open artifact"
            else:
                target = sources[target_id]
                href = target["href"]
                kind_label = "Source"
                action_label = "Open source"

            rendered_doors.append(f"""<article class="card">
<h2>{esc(kind_label)}</h2>
<p>{esc(target["title"])}</p>
<p class="muted">{esc(door["local_note"])}</p>
<p><a href="{esc(href)}">{esc(action_label)}</a></p>
</article>""")

        place_body = f"""
{home_link()}
<header>
<h1>{esc(p["title"])}</h1>
<p>{esc(p["description"])}</p>
<p class="muted">{esc(p["current_question"])}</p>
</header>
<section class="grid" aria-label="Local doors">
{''.join(rendered_doors) if rendered_doors else '<p class="muted">Nothing is surfaced here right now.</p>'}
</section>
<footer>Local relevance is not a global priority score.</footer>
"""
        (OUT / place_filename(place_id)).write_text(
            page(p["title"], place_body),
            encoding="utf-8",
        )

    # Episode deep trace appears only after an explicit door is entered.
    for episode_id in sorted(episodes):
        e = episodes[episode_id]
        refs = "".join(
            f'<li><a href="{esc(normalize_source_href(ref))}">{esc(ref["label"])}</a> '
            f'<small>({esc(ref["kind"])})</small></li>'
            for ref in e["source_refs"]
        )

        anchor = e.get("continuity_anchor")
        anchor_html = ""
        if anchor:
            anchor_html = f"""<div class="trace">
<strong>Continuity anchor</strong>
<p class="muted">{esc(anchor["note"])}</p>
<code>predecessor {esc(anchor["predecessor_turn"])}</code><br>
<code>entry {esc(anchor["confirmed_entry_turn"])}</code>
</div>"""

        body = f"""
{home_link()}
<header><h1>{esc(e["title"])}</h1><p>{esc(e["summary"])}</p></header>
<p>{''.join(f'<span class="tag">{esc(x)}</span>' for x in e["participants"])}</p>
{anchor_html}
<h2>Sources</h2>
<ul>{refs}</ul>
<footer>This is a preserved episode, not proof that every interpretation attached to it is causal truth.</footer>
"""
        (OUT / episode_filename(episode_id)).write_text(
            page(e["title"], body),
            encoding="utf-8",
        )

    # Artifact identity is shared, but local meanings are discovered from place-owned doors.
    for artifact_id in sorted(artifacts):
        a = artifacts[artifact_id]
        local_meanings = []

        for place_id in sorted(places):
            for door in doors_by_place[place_id]:
                if (
                    door["target_kind"] == "artifact"
                    and door["target_id"] == artifact_id
                ):
                    local_meanings.append(
                        f"""<div class="note">
<strong>{esc(places[place_id]["title"])}</strong>
<p>{esc(door["local_note"])}</p>
</div>"""
                    )

        refs = "".join(
            f'<li><a href="{esc(normalize_source_href(ref))}">{esc(ref["label"])}</a></li>'
            for ref in a["source_refs"]
        )

        participant_views = []
        for participant_id in sorted(participants):
            for perspective in perspectives_by_participant.get(participant_id, []):
                if (
                    perspective["target_kind"] == "artifact"
                    and perspective["target_id"] == artifact_id
                ):
                    participant_views.append(
                        f"""<div class="note">
<strong>{esc(participants[participant_id]["title"])}</strong>
<p>{esc(perspective["text"])}</p>
<small>{esc(perspective.get("kind", "participant perspective"))}</small>
</div>"""
                    )

        availability = a.get("body_availability")
        availability_html = ""
        if availability:
            availability_html = f"""<div class="note">
<strong>Artifact body availability</strong>
<p>{esc(availability.get("status", "unknown"))}</p>
<small>{esc(availability.get("note", ""))}</small>
</div>"""

        body = f"""
{home_link()}
<header><h1>{esc(a["title"])}</h1><p>{esc(a["description"])}</p></header>
{availability_html}
<h2>Participant perspectives</h2>
{''.join(participant_views) if participant_views else '<p class="muted">No participant perspective is attached.</p>'}
<h2>Local meanings</h2>
{''.join(local_meanings) if local_meanings else '<p class="muted">No place currently surfaces this artifact.</p>'}
<h2>Sources</h2>
<ul>{refs}</ul>
<footer>No participant interpretation or local placement is treated as the artifact's global meaning.</footer>
"""
        (OUT / artifact_filename(artifact_id)).write_text(
            page(a["title"], body),
            encoding="utf-8",
        )

    print(f"Generated {len(list(OUT.glob('*.html')))} pages.")

if __name__ == "__main__":
    main()
