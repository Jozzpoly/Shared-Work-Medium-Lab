from __future__ import annotations

import argparse
import hashlib
import json
import random
from pathlib import Path


PROTOCOL_VERSION = "mp1a-pilot-world-v0.1"
PUBLIC_PILOT_SEED = "mp1a-public-pilot-2026-10-03-001"

CSS = """
<style>
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  font-family: Arial, Helvetica, sans-serif;
  background: #f3f4f6;
  color: #111827;
  font-size: 15px;
  line-height: 1.4;
}
h1, h2, h3, p, ul, li, main, nav, section, article {
  margin: 0;
  padding: 0;
  font: inherit;
  color: inherit;
}
ul { list-style: none; }
.shell { width: 1080px; margin: 26px auto; }
.topbar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }
.title { font-size: 26px; font-weight: 700; line-height: 1.15; }
.nav { display: flex; gap: 14px; }
a { color: #1d4ed8; text-decoration: underline; }
.panel {
  background: #ffffff;
  border: 1px solid #d1d5db;
  border-radius: 10px;
  padding: 16px;
  margin-bottom: 14px;
}
.section-title { font-size: 18px; font-weight: 700; margin-bottom: 8px; }
.lead { margin-bottom: 12px; color: #374151; }
.resource-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
.resource-grid > * { min-width: 0; display: block; }
.card {
  height: 100%;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 11px;
  background: #fff;
}
.card-title { font-weight: 700; margin-bottom: 5px; }
.kind {
  display: inline-block;
  border: 1px solid #9ca3af;
  border-radius: 999px;
  padding: 1px 7px;
  font-size: 11px;
  color: #374151;
  margin-bottom: 6px;
}
.body { min-height: 61px; }
.meta { font-size: 12px; color: #4b5563; margin-top: 7px; }
.relations { font-size: 12px; color: #4b5563; margin-top: 6px; }
.footer { font-size: 12px; color: #4b5563; }
</style>
"""


def seed_int(seed: str) -> int:
    return int.from_bytes(hashlib.sha256(seed.encode("utf-8")).digest()[:8], "big")


def resource(resource_id, kind, title, body, revision, authority, relations=None):
    return {
        "resource_id": resource_id,
        "kind": kind,
        "title": title,
        "body": body,
        "revision": revision,
        "authority": authority,
        "relations": relations or [],
    }


def build_world(seed: str) -> tuple[dict, dict]:
    rng = random.Random(seed_int(seed))

    resources = [
        resource(
            "decision-import-rule",
            "decision",
            "Import acceptance rule",
            "An import is mechanically accepted when the parser emits a normalized record containing all required fields.",
            "D2",
            "decision record",
        ),
        resource(
            "test-parser-fixture",
            "machine test",
            "Parser fixture run",
            "The parser produced a valid normalized record for the reference fixture and all required fields were present.",
            "T8",
            "machine test",
            [("tests", "decision-import-rule")],
        ),
        resource(
            "owner-import-observation",
            "Owner observation",
            "Imported object remains unusable",
            "The Owner observed that the imported object still could not be used in the visible product flow after the parser test passed.",
            "O3",
            "Owner observation",
            [("observes", "decision-import-rule")],
        ),
        resource(
            "summary-import-status",
            "derived summary",
            "Import path status",
            "The import path is operational because the parser fixture passed normalization.",
            "S4",
            "derived summary",
            [("based on", "test-parser-fixture")],
        ),
        resource(
            "source-cache-config",
            "source document",
            "Observation cache policy",
            "Revision C9 changed the source sampling interval from sixty seconds to ten minutes and added explicit stale-state reporting.",
            "C9",
            "source document",
        ),
        resource(
            "summary-cache-guidance",
            "derived summary",
            "Observation polling guidance",
            "Project observers should sample the source every sixty seconds to remain current.",
            "S2",
            "derived summary",
            [("based on", "source-cache-config")],
        ),
        resource(
            "issue-relay-alpha",
            "issue",
            "Relay Alpha intermittently loses updates",
            "The Alpha path misses a subset of updates shortly after a configuration refresh.",
            "I11",
            "issue",
        ),
        resource(
            "issue-relay-bravo",
            "issue",
            "Bravo worker repeats stale output",
            "The Bravo worker sometimes repeats the prior output after its environment is refreshed.",
            "I14",
            "issue",
        ),
        resource(
            "issue-relay-charlie",
            "issue",
            "Charlie probe starts without live state",
            "The Charlie probe occasionally starts with an empty state immediately after the same configuration refresh.",
            "I19",
            "issue",
        ),
        resource(
            "source-relay-refresh",
            "change record",
            "Relay refresh change",
            "A recent refresh-path change now clears the shared relay snapshot before replacement state is confirmed.",
            "R6",
            "change record",
        ),
        resource(
            "summary-api-capability",
            "derived summary",
            "Remote project API capabilities",
            "The project API supports both reading and remote mutation of project records.",
            "S7",
            "derived summary",
            [("summarizes", "source-api-contract")],
        ),
        resource(
            "source-api-contract",
            "source document",
            "Project API contract",
            "The current public project API is read-only. Mutation endpoints are intentionally unavailable in this environment.",
            "A5",
            "source document",
        ),
    ]

    release_specs = [
        ("cedar", "pass", "pass", "pass"),
        ("elm", "pass", "pass", "pass"),
        ("fir", "pass", "fail", "pass"),
        ("grove", "pass", "pass", "pass"),
        ("harbor", "pass", "pass", "fail"),
        ("juniper", "pass", "pass", "pass"),
        ("kelp", "pass", "pass", "pass"),
        ("larch", "pass", "pass", "pass"),
    ]
    for name, smoke, contract, owner in release_specs:
        resources.append(
            resource(
                f"release-{name}",
                "release record",
                f"{name.title()} release candidate",
                f"Smoke check: {smoke}. Contract check: {contract}. Owner-visible check: {owner}.",
                f"RC-{rng.randint(10, 99)}",
                "release record",
                [("uses rule", "decision-release-condition")],
            )
        )

    resources.append(
        resource(
            "decision-release-condition",
            "decision",
            "Release acceptance condition",
            "A release candidate is accepted only when smoke, contract, and Owner-visible checks all pass.",
            "D6",
            "decision record",
        )
    )

    noise_templates = [
        ("note-renderer-colors", "research note", "Renderer color note", "A future renderer experiment may compare two neutral background palettes.", "N4"),
        ("issue-doc-typo", "issue", "Documentation typo", "One internal note contains a misspelled component name with no runtime effect.", "I22"),
        ("note-archive-layout", "research note", "Archive layout idea", "A possible archive view could group historical experiments by month.", "N8"),
        ("change-footer-copy", "change record", "Footer copy edit", "The project footer wording was shortened without changing any behavior.", "R9"),
    ]
    for rid, kind, title, body, rev in noise_templates:
        resources.append(resource(rid, kind, title, body, rev, kind))

    rng.shuffle(resources)

    world = {
        "protocol_version": PROTOCOL_VERSION,
        "seed": seed,
        "seed_commitment": hashlib.sha256(seed.encode("utf-8")).hexdigest(),
        "project": "Atlas Lab",
        "status": "Pilot world generated from one canonical source.",
        "resources": resources,
    }

    evaluator = {
        "pilot_only": True,
        "motifs": {
            "scope_conflict": {
                "resources": ["test-parser-fixture", "owner-import-observation", "summary-import-status"],
                "expected_boundary": "machine PASS is narrower than Owner-visible product outcome",
            },
            "stale_dependency": {
                "resources": ["source-cache-config", "summary-cache-guidance"],
                "expected_boundary": "summary references superseded sampling guidance",
            },
            "distributed_common_cause": {
                "resources": ["issue-relay-alpha", "issue-relay-bravo", "issue-relay-charlie", "source-relay-refresh"],
                "expected_boundary": "refresh-path change is a plausible shared cause",
            },
            "batchable_collection": {
                "resources": [f"release-{name}" for name, *_ in release_specs],
                "rule": "decision-release-condition",
                "expected_exceptions": ["release-fir", "release-harbor"],
            },
            "authority_conflict": {
                "resources": ["summary-api-capability", "source-api-contract"],
                "authoritative": "source-api-contract",
            },
        },
    }
    return world, evaluator


def relation_text(relations):
    if not relations:
        return "Relations: none"
    return "Relations: " + "; ".join(f"{kind} → {target}" for kind, target in relations)


def render_resource_p0(item):
    relation_links = []
    for kind, target in item["relations"]:
        relation_links.append(f'{kind} → <a href="#{target}">{target}</a>')
    rel = "Relations: " + ("; ".join(relation_links) if relation_links else "none")
    return f"""<div class="card" id="{item['resource_id']}">
      <div class="card-title"><a href="#{item['resource_id']}">{item['title']}</a></div>
      <div class="kind">{item['kind']}</div>
      <div class="body">{item['body']}</div>
      <div class="meta">Revision {item['revision']} · source: {item['authority']}</div>
      <div class="relations">{rel}</div>
    </div>"""


def render_resource_p1(item):
    relation_links = []
    for kind, target in item["relations"]:
        relation_links.append(f'{kind} → <a href="#{target}">{target}</a>')
    rel = "Relations: " + ("; ".join(relation_links) if relation_links else "none")
    return f"""<li>
      <article class="card" id="{item['resource_id']}">
        <h3 class="card-title"><a href="#{item['resource_id']}">{item['title']}</a></h3>
        <div class="kind">{item['kind']}</div>
        <p class="body">{item['body']}</p>
        <div class="meta">Revision {item['revision']} · source: {item['authority']}</div>
        <p class="relations">{rel}</p>
      </article>
    </li>"""


def render(world: dict, semantic: bool) -> str:
    if semantic:
        items = "\n".join(render_resource_p1(item) for item in world["resources"])
        body = f"""<main class="shell">
  <div class="topbar">
    <h1 class="title">Atlas Lab — project world</h1>
    <nav class="nav" aria-label="Project sections">
      <a href="#state">State</a>
      <a href="#resources">Resources</a>
      <a href="#about">About</a>
    </nav>
  </div>

  <section id="state" class="panel" aria-labelledby="state-heading">
    <h2 id="state-heading" class="section-title">Current world state</h2>
    <p class="lead">{world['status']}</p>
    <div class="footer">World commitment: {world['seed_commitment'][:16]}</div>
  </section>

  <section id="resources" class="panel" aria-labelledby="resources-heading">
    <h2 id="resources-heading" class="section-title">Project resources</h2>
    <ul class="resource-grid">{items}</ul>
  </section>

  <section id="about" class="panel" aria-labelledby="about-heading">
    <h2 id="about-heading" class="section-title">About this pilot</h2>
    <p>This public pilot validates treatment generation and parity. It is not a measured agent benchmark.</p>
  </section>
</main>"""
    else:
        items = "\n".join(render_resource_p0(item) for item in world["resources"])
        body = f"""<div class="shell">
  <div class="topbar">
    <div class="title">Atlas Lab — project world</div>
    <div class="nav">
      <a href="#state">State</a>
      <a href="#resources">Resources</a>
      <a href="#about">About</a>
    </div>
  </div>

  <div id="state" class="panel">
    <div class="section-title">Current world state</div>
    <div class="lead">{world['status']}</div>
    <div class="footer">World commitment: {world['seed_commitment'][:16]}</div>
  </div>

  <div id="resources" class="panel">
    <div class="section-title">Project resources</div>
    <div class="resource-grid">{items}</div>
  </div>

  <div id="about" class="panel">
    <div class="section-title">About this pilot</div>
    <div>This public pilot validates treatment generation and parity. It is not a measured agent benchmark.</div>
  </div>
</div>"""

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Atlas Lab — project world</title>
  {CSS}
</head>
<body>{body}</body>
</html>"""


def stable_json(data) -> str:
    return json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--seed", default=PUBLIC_PILOT_SEED)
    args = parser.parse_args()

    world, evaluator = build_world(args.seed)
    args.out.mkdir(parents=True, exist_ok=True)

    p0 = render(world, semantic=False)
    p1 = render(world, semantic=True)

    files = {
        "world.json": stable_json(world),
        "evaluator.json": stable_json(evaluator),
        "p0.html": p0,
        "p1.html": p1,
    }
    for name, content in files.items():
        (args.out / name).write_text(content, encoding="utf-8")

    manifest = {
        "protocol_version": PROTOCOL_VERSION,
        "seed_commitment": world["seed_commitment"],
        "resource_count": len(world["resources"]),
        "files": {
            name: hashlib.sha256(content.encode("utf-8")).hexdigest()
            for name, content in files.items()
        },
    }
    (args.out / "manifest.json").write_text(stable_json(manifest), encoding="utf-8")
    print(stable_json(manifest), end="")


if __name__ == "__main__":
    main()
