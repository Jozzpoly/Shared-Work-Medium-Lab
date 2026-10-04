from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WORLD = ROOT / "world.json"
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

def esc(x):
    return html.escape(str(x))

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

def main():
    world = json.loads(WORLD.read_text(encoding="utf-8"))
    OUT.mkdir(parents=True, exist_ok=True)

    place_by_id = {p["id"]: p for p in world["places"]}
    episode_by_id = {e["id"]: e for e in world["episodes"]}
    artifact_by_id = {a["id"]: a for a in world["artifacts"]}

    # Fail closed on structural assumptions used by this specimen.
    for artifact in world["artifacts"]:
        if artifact["origin_episode"] not in episode_by_id:
            raise SystemExit(f"Unknown origin episode: {artifact['origin_episode']}")
        for placement in artifact["placements"]:
            if placement["place"] not in place_by_id:
                raise SystemExit(f"Unknown placement place: {placement['place']}")

    # ROOT: intentionally quiet. No episode/artifact names, counts, turn IDs, or source refs.
    cards = []
    for p in world["places"]:
        cards.append(f"""<article class="card">
<h2>{esc(p["title"])}</h2>
<p>{esc(p["description"])}</p>
<p class="muted">{esc(p["current_question"])}</p>
<p><a href="{place_filename(p["id"])}">Enter this place</a></p>
</article>""")

    root = f"""
<header>
<h1>{esc(world["campaign"]["title"])}</h1>
<p>{esc(world["campaign"]["question"])}</p>
<p class="muted">You do not need to inspect everything that exists here.</p>
</header>
<section class="grid" aria-label="Places">
{''.join(cards)}
</section>
<footer>This surface is intentionally incomplete. Something may happen elsewhere and never appear here. That is not automatically a failure.</footer>
"""
    (OUT / "index.html").write_text(page(world["campaign"]["title"], root), encoding="utf-8")

    # PLACE pages: expose only locally relevant doors, not deep trace contents.
    for p in world["places"]:
        local_eps = [e for e in world["episodes"] if p["id"] in e["places"]]
        local_artifacts = [
            (a, pl)
            for a in world["artifacts"]
            for pl in a["placements"]
            if pl["place"] == p["id"]
        ]

        doors = []
        for e in local_eps:
            doors.append(f"""<article class="card">
<h2>Preserved episode</h2>
<p>{esc(e["title"])}</p>
<p><a href="{episode_filename(e["id"])}">Open episode</a></p>
</article>""")
        for a, placement in local_artifacts:
            doors.append(f"""<article class="card">
<h2>Local artifact</h2>
<p>{esc(a["title"])}</p>
<p class="muted">{esc(placement["local_note"])}</p>
<p><a href="{artifact_filename(a["id"])}">Open artifact</a></p>
</article>""")

        body = f"""
{home_link()}
<header>
<h1>{esc(p["title"])}</h1>
<p>{esc(p["description"])}</p>
<p class="muted">{esc(p["current_question"])}</p>
</header>
<section class="grid" aria-label="Local doors">
{''.join(doors) if doors else '<p class="muted">Nothing is surfaced here right now.</p>'}
</section>
<footer>Local relevance is not a global priority score.</footer>
"""
        (OUT / place_filename(p["id"])).write_text(page(p["title"], body), encoding="utf-8")

    # EPISODE pages: deep trace only after explicit entry.
    for e in world["episodes"]:
        refs = "".join(
            f'<li><a href="{esc(r["href"])}">{esc(r["label"])}</a> <small>({esc(r["kind"])})</small></li>'
            for r in e["source_refs"]
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
        (OUT / episode_filename(e["id"])).write_text(page(e["title"], body), encoding="utf-8")

    # ARTIFACT pages: author claim + multiple local interpretations.
    for a in world["artifacts"]:
        placements = "".join(
            f"""<div class="note">
<strong>{esc(place_by_id[pl["place"]]["title"])}</strong>
<p>{esc(pl["local_note"])}</p>
</div>"""
            for pl in a["placements"]
        )
        refs = "".join(
            f'<li><a href="{esc(r["href"])}">{esc(r["label"])}</a></li>'
            for r in a["source_refs"]
        )

        body = f"""
{home_link()}
<header><h1>{esc(a["title"])}</h1><p>{esc(a["description"])}</p></header>
<div class="note"><strong>Author's claim</strong><p>{esc(a["author_claim"])}</p></div>
<h2>Local meanings</h2>
{placements}
<h2>Sources</h2>
<ul>{refs}</ul>
<footer>No global score decides which local interpretation is the “correct importance”.</footer>
"""
        (OUT / artifact_filename(a["id"])).write_text(page(a["title"], body), encoding="utf-8")

    print(f"Generated {len(list(OUT.glob('*.html')))} pages.")

if __name__ == "__main__":
    main()
