from __future__ import annotations

import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "site"
WORLD = ROOT / "world.json"


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for key, value in attrs:
                if key == "href" and value:
                    self.hrefs.append(value)


def main():
    world = json.loads(WORLD.read_text(encoding="utf-8"))
    failures = []

    # Campaign law: no one global relevance/priority score.
    forbidden = {"priority", "importance", "global_rank", "relevance_score", "unread_count", "notification_count", "requires_attention", "urgent"}
    def walk(obj, path="$"):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in forbidden:
                    failures.append(f"forbidden global ranking field at {path}.{k}")
                walk(v, f"{path}.{k}")
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                walk(item, f"{path}[{i}]")
    walk(world)

    # The Codex window must survive as one artifact with different local interpretations.
    artifact = next((a for a in world["artifacts"] if a["id"] == "codex-exchange-window"), None)
    if not artifact:
        failures.append("missing codex-exchange-window artifact")
    else:
        places = {p["place"] for p in artifact["placements"]}
        if not {"combat", "swm"}.issubset(places):
            failures.append("exchange window is not represented in both Combat and SWM niches")
        notes = {p["place"]: p["local_note"] for p in artifact["placements"]}
        if notes.get("combat") == notes.get("swm"):
            failures.append("local interpretations were flattened into one shared note")

    # Continuity anchors are allowed to be more specific than one conversation address.
    for episode in world["episodes"]:
        anchor = episode.get("continuity_anchor")
        if anchor and anchor["predecessor_turn"] == anchor["confirmed_entry_turn"]:
            failures.append(f"{episode['id']} continuity anchor collapsed predecessor and entry")

    html_files = sorted(SITE.glob("*.html"))
    expected_pages = 1 + len(world["places"]) + len(world["episodes"]) + len(world["artifacts"])
    if len(html_files) != expected_pages:
        failures.append(f"expected {expected_pages} generated pages, got {len(html_files)}")

    known_pages = {p.name for p in html_files}
    for page in html_files:
        parser = Links()
        parser.feed(page.read_text(encoding="utf-8"))
        for href in parser.hrefs:
            parsed = urlparse(href)
            if parsed.scheme or href.startswith("../") or href.startswith("../../"):
                continue
            target = parsed.path or page.name
            if target and target not in known_pages:
                failures.append(f"{page.name}: unresolved internal link {href}")

    # Quiet root: deep trace exists, but must not be injected into the root surface.
    root_text = (SITE / "index.html").read_text(encoding="utf-8")
    deep_markers = []
    for episode in world["episodes"]:
        deep_markers.extend([
            episode["title"],
            episode.get("continuity_anchor", {}).get("predecessor_turn"),
            episode.get("continuity_anchor", {}).get("confirmed_entry_turn"),
        ])
    for artifact in world["artifacts"]:
        deep_markers.append(artifact["title"])
        deep_markers.append(artifact["author_claim"])
    for marker in [m for m in deep_markers if m]:
        if marker in root_text:
            failures.append(f"deep trace leaked into root surface: {marker}")

    rendered = "\n".join(p.read_text(encoding="utf-8").lower() for p in html_files)
    forbidden_ui = ["mark as read", "you must read", "requires your attention"]
    for phrase in forbidden_ui:
        if phrase in rendered:
            failures.append(f"attention-demand UI leaked into specimen: {phrase}")

    report = {
        "campaign": world["campaign"]["id"],
        "pages": [p.name for p in html_files],
        "artifact_local_placements": {
            p["place"]: p["local_note"] for p in artifact["placements"]
        } if artifact else {},
        "episode_count": len(world["episodes"]),
        "place_count": len(world["places"]),
        "laws_under_test": world["laws_under_test"],
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

    print("QUIET PRESENCE SPECIMEN PASS")


if __name__ == "__main__":
    main()
