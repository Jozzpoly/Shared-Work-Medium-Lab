from __future__ import annotations

import argparse
import hashlib
import json
import random
from pathlib import Path
from urllib.parse import quote


PROTOCOL_VERSION = "mp1a-navigable-pilot-v0.2"
PUBLIC_PILOT_SEED = "mp1a-public-navigable-pilot-2026-10-03-001"

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
.shell { width: 1040px; margin: 26px auto; }
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
.body { margin: 10px 0; }
.meta { font-size: 12px; color: #4b5563; margin-top: 7px; }
.relations { font-size: 12px; color: #4b5563; margin-top: 8px; }
.footer { font-size: 12px; color: #4b5563; }
.collection-list { display: grid; gap: 8px; }
.row {
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 10px;
  background: #fff;
}
.row-title { font-weight: 700; }
</style>
"""


def seed_int(seed: str) -> int:
    return int.from_bytes(hashlib.sha256(seed.encode("utf-8")).digest()[:8], "big")


def resource(resource_id, kind, title, index_summary, body, revision, authority, relations=None):
    return {
        "resource_id": resource_id,
        "kind": kind,
        "title": title,
        "index_summary": index_summary,
        "body": body,
        "revision": revision,
        "authority": authority,
        "relations": relations or [],
    }


def build_world(seed: str) -> tuple[dict, dict]:
    rng = random.Random(seed_int(seed))

    resources = [
        resource(
            "decision-import-rule","decision","Import acceptance rule",
            "Defines the current mechanical acceptance boundary for imports.",
            "An import is mechanically accepted when the parser emits a normalized record containing all required fields.",
            "D2","decision record",
        ),
        resource(
            "test-parser-fixture","machine test","Parser fixture run",
            "Records the latest reference-fixture parser result.",
            "The parser produced a valid normalized record for the reference fixture and all required fields were present.",
            "T8","machine test",[("tests","decision-import-rule")],
        ),
        resource(
            "owner-import-observation","Owner observation","Imported object remains unusable",
            "Records an Owner-visible observation after the parser test.",
            "The Owner observed that the imported object still could not be used in the visible product flow after the parser test passed.",
            "O3","Owner observation",[("observes","decision-import-rule")],
        ),
        resource(
            "summary-import-status","derived summary","Import path status",
            "Current derived summary of the import path.",
            "The import path is operational because the parser fixture passed normalization.",
            "S4","derived summary",[("based on","test-parser-fixture")],
        ),
        resource(
            "source-cache-config","source document","Observation cache policy",
            "Canonical source for observation sampling behavior.",
            "Revision C9 changed the source sampling interval from sixty seconds to ten minutes and added explicit stale-state reporting.",
            "C9","source document",
        ),
        resource(
            "summary-cache-guidance","derived summary","Observation polling guidance",
            "Derived operational guidance for observers.",
            "Project observers should sample the source every sixty seconds to remain current.",
            "S2","derived summary",[("based on","source-cache-config")],
        ),
        resource(
            "issue-relay-alpha","issue","Relay Alpha intermittently loses updates",
            "Issue report for the Alpha relay path.",
            "The Alpha path misses a subset of updates shortly after a configuration refresh.",
            "I11","issue",
        ),
        resource(
            "issue-relay-bravo","issue","Bravo worker repeats stale output",
            "Issue report for the Bravo worker.",
            "The Bravo worker sometimes repeats the prior output after its environment is refreshed.",
            "I14","issue",
        ),
        resource(
            "issue-relay-charlie","issue","Charlie probe starts without live state",
            "Issue report for the Charlie probe.",
            "The Charlie probe occasionally starts with an empty state immediately after the same configuration refresh.",
            "I19","issue",
        ),
        resource(
            "source-relay-refresh","change record","Relay refresh change",
            "Change record for the shared relay refresh path.",
            "A recent refresh-path change now clears the shared relay snapshot before replacement state is confirmed.",
            "R6","change record",
        ),
        resource(
            "summary-api-capability","derived summary","Remote project API capabilities",
            "Derived description of current remote API capabilities.",
            "The project API supports both reading and remote mutation of project records.",
            "S7","derived summary",[("summarizes","source-api-contract")],
        ),
        resource(
            "source-api-contract","source document","Project API contract",
            "Canonical contract for the current public project API.",
            "The current public project API is read-only. Mutation endpoints are intentionally unavailable in this environment.",
            "A5","source document",
        ),
    ]

    release_specs = [
        ("cedar","pass","pass","pass"),
        ("elm","pass","pass","pass"),
        ("fir","pass","fail","pass"),
        ("grove","pass","pass","pass"),
        ("harbor","pass","pass","fail"),
        ("juniper","pass","pass","pass"),
        ("kelp","pass","pass","pass"),
        ("larch","pass","pass","pass"),
    ]
    for name, smoke, contract, owner in release_specs:
        resources.append(
            resource(
                f"release-{name}","release record",f"{name.title()} release candidate",
                "Release candidate verification record.",
                f"Smoke check: {smoke}. Contract check: {contract}. Owner-visible check: {owner}.",
                f"RC-{rng.randint(10,99)}","release record",
                [("uses rule","decision-release-condition")],
            )
        )

    resources.append(
        resource(
            "decision-release-condition","decision","Release acceptance condition",
            "Defines the acceptance rule used by release candidates.",
            "A release candidate is accepted only when smoke, contract, and Owner-visible checks all pass.",
            "D6","decision record",
        )
    )

    noise = [
        ("note-renderer-colors","research note","Renderer color note","Visual research note.","A future renderer experiment may compare two neutral background palettes.","N4"),
        ("issue-doc-typo","issue","Documentation typo","Low-impact documentation issue.","One internal note contains a misspelled component name with no runtime effect.","I22"),
        ("note-archive-layout","research note","Archive layout idea","Possible archive presentation idea.","A possible archive view could group historical experiments by month.","N8"),
        ("change-footer-copy","change record","Footer copy edit","Presentation-only copy change.","The project footer wording was shortened without changing any behavior.","R9"),
    ]
    for rid, kind, title, summary, body, rev in noise:
        resources.append(resource(rid,kind,title,summary,body,rev,kind))

    rng.shuffle(resources)

    collections = [
        {
            "collection_id":"release-records",
            "title":"Release records",
            "description":"Current release-candidate records.",
            "members":[f"release-{name}" for name,*_ in release_specs],
        },
        {
            "collection_id":"relay-issues",
            "title":"Relay issues",
            "description":"Open issue reports concerning relay behavior.",
            "members":["issue-relay-alpha","issue-relay-bravo","issue-relay-charlie"],
        },
        {
            "collection_id":"derived-summaries",
            "title":"Derived summaries",
            "description":"Current derived project summaries.",
            "members":["summary-import-status","summary-cache-guidance","summary-api-capability"],
        },
    ]

    world = {
        "protocol_version":PROTOCOL_VERSION,
        "seed":seed,
        "seed_commitment":hashlib.sha256(seed.encode("utf-8")).hexdigest(),
        "project":"Atlas Lab",
        "status":"Pilot world generated from one canonical source.",
        "resources":resources,
        "collections":collections,
    }
    evaluator = {
        "pilot_only":True,
        "motifs":{
            "scope_conflict":{
                "resources":["test-parser-fixture","owner-import-observation","summary-import-status"],
                "expected_boundary":"machine PASS is narrower than Owner-visible product outcome",
            },
            "stale_dependency":{
                "resources":["source-cache-config","summary-cache-guidance"],
                "expected_boundary":"summary references superseded sampling guidance",
            },
            "distributed_common_cause":{
                "resources":["issue-relay-alpha","issue-relay-bravo","issue-relay-charlie","source-relay-refresh"],
                "expected_boundary":"refresh-path change is a plausible shared cause",
            },
            "batchable_collection":{
                "resources":[f"release-{name}" for name,*_ in release_specs],
                "collection":"release-records",
                "rule":"decision-release-condition",
                "expected_exceptions":["release-fir","release-harbor"],
            },
            "authority_conflict":{
                "resources":["summary-api-capability","source-api-contract"],
                "authoritative":"source-api-contract",
            },
        },
    }
    return world,evaluator


def stable_json(data):
    return json.dumps(data,ensure_ascii=False,sort_keys=True,indent=2)+"\n"


def rel_resource_path(resource_id):
    return f"resources/{quote(resource_id)}.html"


def page(title, body):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
{CSS}
</head>
<body>{body}</body>
</html>"""


def nav_p0(prefix=""):
    return f"""<div class="nav">
<a href="{prefix}index.html">Home</a>
<a href="{prefix}collections/release-records.html">Release records</a>
<a href="{prefix}collections/relay-issues.html">Relay issues</a>
<a href="{prefix}collections/derived-summaries.html">Derived summaries</a>
</div>"""


def nav_p1(prefix=""):
    return f"""<nav class="nav" aria-label="Project navigation">
<a href="{prefix}index.html">Home</a>
<a href="{prefix}collections/release-records.html">Release records</a>
<a href="{prefix}collections/relay-issues.html">Relay issues</a>
<a href="{prefix}collections/derived-summaries.html">Derived summaries</a>
</nav>"""


def render_index(world, semantic):
    cards=[]
    for r in world["resources"]:
        href=rel_resource_path(r["resource_id"])
        if semantic:
            cards.append(f"""<li><article class="card">
<h3 class="card-title"><a href="{href}">{r['title']}</a></h3>
<div class="kind">{r['kind']}</div>
<p>{r['index_summary']}</p>
<div class="meta">Revision {r['revision']} · source: {r['authority']}</div>
</article></li>""")
        else:
            cards.append(f"""<div class="card">
<div class="card-title"><a href="{href}">{r['title']}</a></div>
<div class="kind">{r['kind']}</div>
<div>{r['index_summary']}</div>
<div class="meta">Revision {r['revision']} · source: {r['authority']}</div>
</div>""")
    items="\n".join(cards)
    if semantic:
        body=f"""<main class="shell">
<div class="topbar"><h1 class="title">Atlas Lab — project world</h1>{nav_p1()}</div>
<section class="panel" aria-labelledby="state-h"><h2 id="state-h" class="section-title">Current world state</h2><p class="lead">{world['status']}</p><div class="footer">World commitment: {world['seed_commitment'][:16]}</div></section>
<section class="panel" aria-labelledby="resources-h"><h2 id="resources-h" class="section-title">Resource index</h2><p class="lead">Open a resource to inspect its full evidence.</p><ul class="resource-grid">{items}</ul></section>
</main>"""
    else:
        body=f"""<div class="shell">
<div class="topbar"><div class="title">Atlas Lab — project world</div>{nav_p0()}</div>
<div class="panel"><div class="section-title">Current world state</div><div class="lead">{world['status']}</div><div class="footer">World commitment: {world['seed_commitment'][:16]}</div></div>
<div class="panel"><div class="section-title">Resource index</div><div class="lead">Open a resource to inspect its full evidence.</div><div class="resource-grid">{items}</div></div>
</div>"""
    return page("Atlas Lab — project world",body)


def render_resource(world, r, semantic):
    relation_bits=[]
    for kind,target in r["relations"]:
        relation_bits.append(f'{kind} → <a href="{quote(target)}.html">{target}</a>')
    rel="Relations: "+("; ".join(relation_bits) if relation_bits else "none")
    if semantic:
        body=f"""<main class="shell">
<div class="topbar"><h1 class="title">{r['title']}</h1>{nav_p1("../")}</div>
<article class="panel" aria-labelledby="resource-h">
<h2 id="resource-h" class="section-title">Resource evidence</h2>
<div class="kind">{r['kind']}</div>
<p class="body">{r['body']}</p>
<div class="meta">Revision {r['revision']} · source: {r['authority']}</div>
<p class="relations">{rel}</p>
</article>
</main>"""
    else:
        body=f"""<div class="shell">
<div class="topbar"><div class="title">{r['title']}</div>{nav_p0("../")}</div>
<div class="panel">
<div class="section-title">Resource evidence</div>
<div class="kind">{r['kind']}</div>
<div class="body">{r['body']}</div>
<div class="meta">Revision {r['revision']} · source: {r['authority']}</div>
<div class="relations">{rel}</div>
</div>
</div>"""
    return page(f"{r['title']} — Atlas Lab",body)


def render_collection(world, collection, semantic):
    lookup={r["resource_id"]:r for r in world["resources"]}
    rows=[]
    for rid in collection["members"]:
        r=lookup[rid]
        href=f"../resources/{quote(rid)}.html"
        if semantic:
            rows.append(f"""<li class="row"><div class="row-title"><a href="{href}">{r['title']}</a></div><div class="meta">{r['kind']} · Revision {r['revision']}</div></li>""")
        else:
            rows.append(f"""<div class="row"><div class="row-title"><a href="{href}">{r['title']}</a></div><div class="meta">{r['kind']} · Revision {r['revision']}</div></div>""")
    items="\n".join(rows)
    if semantic:
        body=f"""<main class="shell">
<div class="topbar"><h1 class="title">{collection['title']}</h1>{nav_p1("../")}</div>
<section class="panel" aria-labelledby="collection-h">
<h2 id="collection-h" class="section-title">Collection members</h2>
<p class="lead">{collection['description']}</p>
<ul class="collection-list">{items}</ul>
</section>
</main>"""
    else:
        body=f"""<div class="shell">
<div class="topbar"><div class="title">{collection['title']}</div>{nav_p0("../")}</div>
<div class="panel">
<div class="section-title">Collection members</div>
<div class="lead">{collection['description']}</div>
<div class="collection-list">{items}</div>
</div>
</div>"""
    return page(f"{collection['title']} — Atlas Lab",body)


def compile_treatment(world, root: Path, semantic: bool):
    root.mkdir(parents=True,exist_ok=True)
    (root/"resources").mkdir(exist_ok=True)
    (root/"collections").mkdir(exist_ok=True)
    (root/"index.html").write_text(render_index(world,semantic),encoding="utf-8")
    for r in world["resources"]:
        (root/"resources"/f"{r['resource_id']}.html").write_text(render_resource(world,r,semantic),encoding="utf-8")
    for c in world["collections"]:
        (root/"collections"/f"{c['collection_id']}.html").write_text(render_collection(world,c,semantic),encoding="utf-8")


def hash_tree(root: Path):
    out={}
    for p in sorted(x for x in root.rglob("*") if x.is_file()):
        out[str(p.relative_to(root))]=hashlib.sha256(p.read_bytes()).hexdigest()
    return out


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--seed",default=PUBLIC_PILOT_SEED)
    args=parser.parse_args()

    world,evaluator=build_world(args.seed)
    args.out.mkdir(parents=True,exist_ok=True)
    (args.out/"world.json").write_text(stable_json(world),encoding="utf-8")
    (args.out/"evaluator.json").write_text(stable_json(evaluator),encoding="utf-8")
    compile_treatment(world,args.out/"p0",False)
    compile_treatment(world,args.out/"p1",True)

    manifest={
        "protocol_version":PROTOCOL_VERSION,
        "seed_commitment":world["seed_commitment"],
        "resource_count":len(world["resources"]),
        "collection_count":len(world["collections"]),
        "p0_files":hash_tree(args.out/"p0"),
        "p1_files":hash_tree(args.out/"p1"),
        "world_sha256":hashlib.sha256((args.out/"world.json").read_bytes()).hexdigest(),
        "evaluator_sha256":hashlib.sha256((args.out/"evaluator.json").read_bytes()).hexdigest(),
    }
    (args.out/"manifest.json").write_text(stable_json(manifest),encoding="utf-8")
    print(stable_json(manifest),end="")


if __name__=="__main__":
    main()
