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


def observe(name: str, page_path: Path, artifacts: Path) -> dict:
    env = gym.make(
        "browsergym/openended",
        task_kwargs={"start_url": page_path.resolve().as_uri()},
        headless=True,
        viewport=VIEWPORT,
        timeout=2500,
        action_mapping=None,
    )
    try:
        obs, info = env.reset()
        page = env.unwrapped.page

        visible_text = normalize_text(page.locator("body").inner_text())
        links = page.locator("a").evaluate_all(
            """els => els.map(a => ({
                text: a.innerText.replace(/\\s+/g, ' ').trim(),
                href: a.getAttribute('href')
            }))"""
        )

        screenshot = obs["screenshot"]
        Image.fromarray(screenshot).save(artifacts / f"{name}.png")

        axtree = obs["axtree_object"]
        axtree_text = flatten_axtree_to_str(axtree, remove_redundant_static_text=True)
        (artifacts / f"{name}_axtree.txt").write_text(axtree_text, encoding="utf-8")

        dom_text = flatten_dom_to_str(obs["dom_object"])
        (artifacts / f"{name}_dom.txt").write_text(dom_text, encoding="utf-8")

        roles = Counter(
            node.get("role", {}).get("value", "unknown")
            for node in axtree.get("nodes", [])
        )

        return {
            "visible_text": visible_text,
            "links": links,
            "screenshot": screenshot,
            "roles": dict(sorted(roles.items())),
            "axtree_chars": len(axtree_text),
            "dom_chars": len(dom_text),
        }
    finally:
        env.close()


def main():
    out = ROOT / "out"
    artifacts = ROOT / "artifacts"
    artifacts.mkdir(exist_ok=True)

    world = json.loads((out / "world.json").read_text(encoding="utf-8"))
    evaluator = json.loads((out / "evaluator.json").read_text(encoding="utf-8"))
    manifest = json.loads((out / "manifest.json").read_text(encoding="utf-8"))
    p0_html = (out / "p0.html").read_text(encoding="utf-8")
    p1_html = (out / "p1.html").read_text(encoding="utf-8")

    ids = [r["resource_id"] for r in world["resources"]]
    unique_ids = len(ids) == len(set(ids))
    known = set(ids)
    unresolved_relations = [
        [r["resource_id"], kind, target]
        for r in world["resources"]
        for kind, target in r["relations"]
        if target not in known
    ]

    motif_labels = set(evaluator["motifs"].keys())
    leaked_labels = sorted(
        label for label in motif_labels
        if label in p0_html or label in p1_html
    )

    p0 = observe("p0", out / "p0.html", artifacts)
    p1 = observe("p1", out / "p1.html", artifacts)

    same_text = p0["visible_text"] == p1["visible_text"]
    same_links = p0["links"] == p1["links"]

    delta = np.abs(
        p0["screenshot"].astype(np.int16) - p1["screenshot"].astype(np.int16)
    )
    mismatched_pixels = np.any(delta != 0, axis=2)
    pixel_mismatch_ratio = float(mismatched_pixels.mean())
    mean_abs_pixel_delta = float(delta.mean())
    Image.fromarray(np.clip(delta * 8, 0, 255).astype(np.uint8)).save(
        artifacts / "pixel_diff_x8.png"
    )

    p0_roles = p0["roles"]
    p1_roles = p1["roles"]

    semantic_divergence = (
        p1_roles.get("heading", 0) >= 4
        and p1_roles.get("heading", 0) > p0_roles.get("heading", 0)
        and p1_roles.get("list", 0) >= 1
        and p1_roles.get("list", 0) > p0_roles.get("list", 0)
        and p1_roles.get("listitem", 0) >= len(world["resources"])
        and p1_roles.get("listitem", 0) > p0_roles.get("listitem", 0)
        and p1_roles.get("article", 0) >= len(world["resources"])
    )

    report = {
        "spike": "mp1a-generated-pilot-world-v0",
        "browsergym_core_version": version("browsergym-core"),
        "manifest": manifest,
        "world_integrity": {
            "unique_resource_ids": unique_ids,
            "unresolved_relations": unresolved_relations,
            "motif_labels_leaked_to_treatment": leaked_labels,
        },
        "parity": {
            "normalized_visible_text_equal": same_text,
            "raw_link_label_and_target_equal": same_links,
            "pixel_mismatch_ratio": pixel_mismatch_ratio,
            "pixel_mismatch_ratio_limit": PIXEL_MISMATCH_RATIO_LIMIT,
            "mean_absolute_pixel_delta": mean_abs_pixel_delta,
        },
        "semantic_divergence": {
            "pass": semantic_divergence,
            "p0_roles": p0_roles,
            "p1_roles": p1_roles,
        },
        "observation_size": {
            "p0_axtree_chars": p0["axtree_chars"],
            "p1_axtree_chars": p1["axtree_chars"],
            "p0_dom_chars": p0["dom_chars"],
            "p1_dom_chars": p1["dom_chars"],
        },
        "link_count": len(p0["links"]),
    }

    (artifacts / "report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(json.dumps(report, ensure_ascii=False, indent=2))

    failures = []
    if not unique_ids:
        failures.append("resource ids are not unique")
    if unresolved_relations:
        failures.append(f"unresolved relations: {unresolved_relations}")
    if leaked_labels:
        failures.append(f"evaluator motif labels leaked: {leaked_labels}")
    if not same_text:
        failures.append("visible text parity failed")
    if not same_links:
        failures.append("link label/target parity failed")
    if pixel_mismatch_ratio > PIXEL_MISMATCH_RATIO_LIMIT:
        failures.append(
            f"pixel parity failed: {pixel_mismatch_ratio:.6f} > "
            f"{PIXEL_MISMATCH_RATIO_LIMIT:.6f}"
        )
    if not semantic_divergence:
        failures.append("intended AXTree semantic divergence was not established")

    if failures:
        raise SystemExit("PILOT APPARATUS FAIL: " + "; ".join(failures))

    print("PILOT APPARATUS PASS: deterministic canonical world compiles to visually identical but semantically distinct treatments.")


if __name__ == "__main__":
    main()
