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
.wrap { max-width: 980px; margin: 0 auto; padding: 32px 22px 64px; }
header { margin-bottom: 28px; }
h1 { margin: 0 0 8px; font-size: 34px; }
h2 { margin-top: 28px; }
h3 { margin: 0 0 8px; }
.muted { color: #a8abb2; }
.grid { display: grid; gap: 14px; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); }
.card {
  border: 1px solid #30343a;
  border-radius: 12px;
  background: #181a1e;
  padding: 16px;
}
.trace {
  border-left: 3px solid #4a5563;
  padding-left: 14px;
}
small, .small { color: #a8abb2; }
nav { display: flex; flex-wrap: wrap; gap: 12px; margin: 14px 0 24px; }
.tag {
  display: inline-block;
  border: 1px solid #3e454f;
  border-radius: 999px;
  padding: 2px 8px;
  margin: 2px 4px 2px 0;
  font-size: 12px;
  color: #c7cbd1;
}
.note {
  background: #15171a;
  border: 1px solid #2c3138;
  border-radius: 9px;
  padding: 12px;
  margin-top: 10px;
}
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

def nav():
    return '<nav><a href="index.html">Places</a><a href="episodes.html">Episodes</a><a href="artifacts.html">Artifacts</a></nav>'

def local_href(ref):
    return esc(ref["href"])

def main():
    world = json.loads(WORLD.read_text(encoding="utf-8"))
    OUT.mkdir(parents=True, exist_ok=True)

    place_ids = {p["id"] for p in world["places"]}
    episode_ids = {e["id"] for e in world["episodes"]}

    # Fail closed on the properties this specimen claims.
    if any("priority" in a or "importance" in a for a in world.get("artifacts", [])):
        raise SystemExit("Global importance/priority fields are not allowed in this specimen.")

    for artifact in world["artifacts"]:
        if artifact["origin_episode"] not in episode_ids:
            raise SystemExit(f"Unknown origin episode: {artifact['origin_episode']}")
        for placement in artifact["placements"]:
            if placement["place"] not in place_ids:
                raise SystemExit(f"Unknown placement place: {placement['place']}")

    for episode in world["episodes"]:
        if not episode.get("source_refs"):
            raise SystemExit(f"Episode {episode['id']} has no source refs.")
        for place in episode["places"]:
            if place not in place_ids:
                raise SystemExit(f"Episode {episode['id']} references unknown place {place}")
        anchor = episode.get("continuity_anchor")
        if anchor and (not anchor.get("predecessor_turn") or not anchor.get("confirmed_entry_turn")):
            raise SystemExit(f"Incomplete continuity anchor in {episode['id']}")

    places_html = []
    for p in world["places"]:
        related_eps = [e for e in world["episodes"] if p["id"] in e["places"]]
        placements = [
            (a, pl)
            for a in world["artifacts"]
            for pl in a["placements"]
            if pl["place"] == p["id"]
        ]
        bits = [f'<article class="card"><h3>{esc(p["title"])}</h3><p>{esc(p["description"])}</p><p class="small">Current question: {esc(p["current_question"])}</p>']
        if related_eps:
            bits.append("<p><strong>Recoverable episodes</strong></p>")
            bits.append("<ul>" + "".join(f'<li><a href="episodes.html#{esc(e["id"])}">{esc(e["title"])}</a></li>' for e in related_eps) + "</ul>")
        if placements:
            bits.append("<p><strong>Locally relevant artifacts</strong></p>")
            for artifact, placement in placements:
                bits.append(f'<div class="note"><a href="artifacts.html#{esc(artifact["id"])}">{esc(artifact["title"])}</a><br><small>{esc(placement["local_note"])}</small></div>')
        bits.append("</article>")
        places_html.append("".join(bits))

    home = f"""
<header><h1>{esc(world["campaign"]["title"])}</h1>
<p>{esc(world["campaign"]["question"])}</p>
<p class="muted">Nothing here is an inbox. You may enter a place, follow an episode, or ignore it.</p></header>
{nav()}
<section class="grid">{''.join(places_html)}</section>
<h2>Laws under test</h2>
<p>{''.join(f'<span class="tag">{esc(x)}</span>' for x in world["laws_under_test"])}</p>
"""
    (OUT / "index.html").write_text(page(world["campaign"]["title"], home), encoding="utf-8")

    eps = [f"<header><h1>Episodes</h1><p class='muted'>Preserved events, not notifications.</p></header>{nav()}"]
    for e in world["episodes"]:
        refs = "".join(f'<li><a href="{local_href(r)}">{esc(r["label"])}</a> <small>({esc(r["kind"])})</small></li>' for r in e["source_refs"])
        anchor = e.get("continuity_anchor")
        anchor_html = ""
        if anchor:
            anchor_html = f"""<div class="note"><strong>Continuity anchor</strong><br>
<small>{esc(anchor["note"])}</small><br>
<code>predecessor {esc(anchor["predecessor_turn"])}</code><br>
<code>entry {esc(anchor["confirmed_entry_turn"])}</code></div>"""
        eps.append(f"""<article class="card" id="{esc(e["id"])}">
<h2>{esc(e["title"])}</h2>
<p>{esc(e["summary"])}</p>
<p>{''.join(f'<span class="tag">{esc(x)}</span>' for x in e["participants"])}</p>
<div class="trace"><strong>Sources</strong><ul>{refs}</ul></div>
{anchor_html}
</article>""")
    (OUT / "episodes.html").write_text(page("Episodes — Quiet Presence", "".join(eps)), encoding="utf-8")

    arts = [f"<header><h1>Artifacts</h1><p class='muted'>Local inventions may travel without becoming platform features.</p></header>{nav()}"]
    for a in world["artifacts"]:
        placements = "".join(
            f'<div class="note"><strong>{esc(next(p["title"] for p in world["places"] if p["id"] == pl["place"]))}</strong><br><small>{esc(pl["local_note"])}</small></div>'
            for pl in a["placements"]
        )
        refs = "".join(f'<li><a href="{local_href(r)}">{esc(r["label"])}</a></li>' for r in a["source_refs"])
        arts.append(f"""<article class="card" id="{esc(a["id"])}">
<h2>{esc(a["title"])}</h2>
<p>{esc(a["description"])}</p>
<div class="note"><strong>Author's claim</strong><br>{esc(a["author_claim"])}</div>
<h3>Local placements</h3>{placements}
<h3>Sources</h3><ul>{refs}</ul>
</article>""")
    (OUT / "artifacts.html").write_text(page("Artifacts — Quiet Presence", "".join(arts)), encoding="utf-8")

    print(f"Generated {len(list(OUT.glob('*.html')))} pages.")

if __name__ == "__main__":
    main()
