from __future__ import annotations

import json
import re
from collections import Counter
from importlib.metadata import version
from pathlib import Path

import gymnasium as gym
import numpy as np
from PIL import Image

import browsergym.core
from browsergym.utils.obs import flatten_axtree_to_str, flatten_dom_to_str


ROOT = Path(__file__).resolve().parent
VIEWPORT = {"width": 1280, "height": 1400}
PIXEL_MISMATCH_RATIO_LIMIT = 0.0005


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def observe(page_path: Path):
    env = gym.make(
        "browsergym/openended",
        task_kwargs={"start_url": page_path.resolve().as_uri()},
        headless=True,
        viewport=VIEWPORT,
        timeout=2500,
        action_mapping=None,
    )
    try:
        obs, _ = env.reset()
        page = env.unwrapped.page
        axtree = obs["axtree_object"]
        roles = Counter(
            node.get("role", {}).get("value", "unknown")
            for node in axtree.get("nodes", [])
        )
        return {
            "visible_text": normalize_text(page.locator("body").inner_text()),
            "links": page.locator("a").evaluate_all(
                """els => els.map(a => ({
                    text: a.innerText.replace(/\\s+/g, ' ').trim(),
                    href: a.getAttribute('href')
                }))"""
            ),
            "screenshot": obs["screenshot"],
            "roles": dict(sorted(roles.items())),
            "axtree_text": flatten_axtree_to_str(
                axtree, remove_redundant_static_text=True
            ),
            "dom_text": flatten_dom_to_str(obs["dom_object"]),
        }
    finally:
        env.close()


def main():
    out = ROOT / "out-nav"
    artifacts = ROOT / "artifacts-nav"
    artifacts.mkdir(exist_ok=True)

    world = json.loads((out / "world.json").read_text(encoding="utf-8"))
    evaluator = json.loads((out / "evaluator.json").read_text(encoding="utf-8"))

    p0_root = out / "p0"
    p1_root = out / "p1"
    p0_files = sorted(str(p.relative_to(p0_root)) for p in p0_root.rglob("*.html"))
    p1_files = sorted(str(p.relative_to(p1_root)) for p in p1_root.rglob("*.html"))

    failures = []
    if p0_files != p1_files:
        failures.append("P0/P1 HTML file topology differs")

    # World integrity.
    ids = [r["resource_id"] for r in world["resources"]]
    known_ids = set(ids)
    if len(ids) != len(known_ids):
        failures.append("resource ids are not unique")

    unresolved = [
        [r["resource_id"], kind, target]
        for r in world["resources"]
        for kind, target in r["relations"]
        if target not in known_ids
    ]
    if unresolved:
        failures.append(f"unresolved resource relations: {unresolved}")

    collection_unknowns = [
        [c["collection_id"], member]
        for c in world["collections"]
        for member in c["members"]
        if member not in known_ids
    ]
    if collection_unknowns:
        failures.append(f"collection contains unknown resources: {collection_unknowns}")

    # Acquisition boundary: index may summarize resources but must not expose full bodies.
    index_text = normalize_text((p0_root / "index.html").read_text(encoding="utf-8"))
    leaked_bodies = [
        r["resource_id"] for r in world["resources"]
        if normalize_text(r["body"]) in index_text
    ]
    if leaked_bodies:
        failures.append(f"full evidence leaked into index: {leaked_bodies}")

    # Batch opportunity must remain latent: collection lists members, not their checks/results.
    release_page_text = normalize_text(
        (p0_root / "collections" / "release-records.html").read_text(encoding="utf-8")
    )
    forbidden_release_evidence = [
        "Smoke check:",
        "Contract check:",
        "Owner-visible check:",
    ]
    leaked_release = [
        marker for marker in forbidden_release_evidence if marker in release_page_text
    ]
    if leaked_release:
        failures.append(f"release collection leaks detail evidence: {leaked_release}")

    # Evaluator labels must not appear in treatment HTML.
    treatment_blob = "\n".join(
        p.read_text(encoding="utf-8")
        for root in [p0_root, p1_root]
        for p in root.rglob("*.html")
    )
    leaked_motifs = [
        label for label in evaluator["motifs"].keys()
        if label in treatment_blob
    ]
    if leaked_motifs:
        failures.append(f"evaluator motif labels leaked: {leaked_motifs}")

    page_reports = {}
    total_mismatch_pixels = 0
    total_pixels = 0
    semantically_richer_pages = 0

    for rel in p0_files:
        p0 = observe(p0_root / rel)
        p1 = observe(p1_root / rel)

        same_text = p0["visible_text"] == p1["visible_text"]
        same_links = p0["links"] == p1["links"]

        if p0["screenshot"].shape != p1["screenshot"].shape:
            mismatch_ratio = 1.0
            mean_delta = 255.0
        else:
            delta = np.abs(
                p0["screenshot"].astype(np.int16)
                - p1["screenshot"].astype(np.int16)
            )
            mismatched = np.any(delta != 0, axis=2)
            mismatch_ratio = float(mismatched.mean())
            mean_delta = float(delta.mean())
            total_mismatch_pixels += int(mismatched.sum())
            total_pixels += int(mismatched.size)

        p0_semantic_roles = sum(
            p0["roles"].get(role, 0)
            for role in ["heading", "article", "list", "listitem", "main", "navigation", "region"]
        )
        p1_semantic_roles = sum(
            p1["roles"].get(role, 0)
            for role in ["heading", "article", "list", "listitem", "main", "navigation", "region"]
        )
        richer = p1_semantic_roles > p0_semantic_roles
        if richer:
            semantically_richer_pages += 1

        page_reports[rel] = {
            "visible_text_equal": same_text,
            "links_equal": same_links,
            "pixel_mismatch_ratio": mismatch_ratio,
            "mean_absolute_pixel_delta": mean_delta,
            "p0_semantic_role_count": p0_semantic_roles,
            "p1_semantic_role_count": p1_semantic_roles,
            "semantic_richer": richer,
            "p0_axtree_chars": len(p0["axtree_text"]),
            "p1_axtree_chars": len(p1["axtree_text"]),
        }

        safe = rel.replace("/", "__")
        (artifacts / f"{safe}.p0.axtree.txt").write_text(
            p0["axtree_text"], encoding="utf-8"
        )
        (artifacts / f"{safe}.p1.axtree.txt").write_text(
            p1["axtree_text"], encoding="utf-8"
        )

        if rel in {"index.html", "collections/release-records.html"}:
            Image.fromarray(p0["screenshot"]).save(artifacts / f"{safe}.p0.png")
            Image.fromarray(p1["screenshot"]).save(artifacts / f"{safe}.p1.png")
            delta = np.abs(
                p0["screenshot"].astype(np.int16)
                - p1["screenshot"].astype(np.int16)
            )
            Image.fromarray(np.clip(delta * 8, 0, 255).astype(np.uint8)).save(
                artifacts / f"{safe}.diff_x8.png"
            )

        if not same_text:
            failures.append(f"{rel}: visible text parity failed")
        if not same_links:
            failures.append(f"{rel}: link parity failed")
        if mismatch_ratio > PIXEL_MISMATCH_RATIO_LIMIT:
            failures.append(
                f"{rel}: pixel mismatch {mismatch_ratio:.6f} exceeds "
                f"{PIXEL_MISMATCH_RATIO_LIMIT:.6f}"
            )
        if not richer:
            failures.append(f"{rel}: intended semantic enrichment absent")

    overall_pixel_mismatch = (
        total_mismatch_pixels / total_pixels if total_pixels else 0.0
    )

    expected_page_count = 1 + len(world["resources"]) + len(world["collections"])
    if len(p0_files) != expected_page_count:
        failures.append(
            f"unexpected treatment page count: {len(p0_files)} != {expected_page_count}"
        )

    report = {
        "spike": "mp1a-navigable-generated-pilot-v0.2",
        "browsergym_core_version": version("browsergym-core"),
        "page_count_per_treatment": len(p0_files),
        "expected_page_count_per_treatment": expected_page_count,
        "resource_count": len(world["resources"]),
        "collection_count": len(world["collections"]),
        "acquisition_boundary": {
            "full_resource_bodies_leaked_to_index": leaked_bodies,
            "release_collection_detail_markers_leaked": leaked_release,
        },
        "world_integrity": {
            "unique_resource_ids": len(ids) == len(known_ids),
            "unresolved_relations": unresolved,
            "unknown_collection_members": collection_unknowns,
            "evaluator_labels_leaked": leaked_motifs,
        },
        "parity": {
            "all_corresponding_visible_text_equal": all(
                r["visible_text_equal"] for r in page_reports.values()
            ),
            "all_corresponding_links_equal": all(
                r["links_equal"] for r in page_reports.values()
            ),
            "overall_pixel_mismatch_ratio": overall_pixel_mismatch,
            "per_page_limit": PIXEL_MISMATCH_RATIO_LIMIT,
        },
        "semantic_divergence": {
            "semantically_richer_pages": semantically_richer_pages,
            "total_pages": len(page_reports),
        },
        "pages": page_reports,
    }

    (artifacts / "navigable_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))

    if failures:
        raise SystemExit("NAVIGABLE PILOT FAIL: " + "; ".join(failures))

    print(
        "NAVIGABLE PILOT PASS: information acquisition now requires navigation, "
        "while every P0/P1 page remains visually/textually equivalent and "
        "semantically distinct."
    )


if __name__ == "__main__":
    main()
