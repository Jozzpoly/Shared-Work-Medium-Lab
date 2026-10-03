from __future__ import annotations

import json
import re
from collections import Counter
from importlib.metadata import version
from pathlib import Path

import gymnasium as gym
import numpy as np
from PIL import Image

import browsergym.core  # registers browsergym/openended
from browsergym.utils.obs import flatten_axtree_to_str, flatten_dom_to_str


ROOT = Path(__file__).resolve().parent
ARTIFACTS = ROOT / "artifacts"
ARTIFACTS.mkdir(exist_ok=True)

VIEWPORT = {"width": 1280, "height": 900}
PIXEL_MISMATCH_RATIO_LIMIT = 0.0005


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def observe(name: str, path: Path) -> dict:
    env = gym.make(
        "browsergym/openended",
        task_kwargs={"start_url": path.resolve().as_uri()},
        headless=True,
        viewport=VIEWPORT,
        timeout=2000,
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
        Image.fromarray(screenshot).save(ARTIFACTS / f"{name}.png")

        axtree = obs["axtree_object"]
        axtree_text = flatten_axtree_to_str(
            axtree,
            remove_redundant_static_text=True,
        )
        (ARTIFACTS / f"{name}_axtree.txt").write_text(axtree_text, encoding="utf-8")

        dom_text = flatten_dom_to_str(obs["dom_object"])
        (ARTIFACTS / f"{name}_dom.txt").write_text(dom_text, encoding="utf-8")

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


p0 = observe("p0", ROOT / "p0.html")
p1 = observe("p1", ROOT / "p1.html")

same_text = p0["visible_text"] == p1["visible_text"]
same_links = p0["links"] == p1["links"]

if p0["screenshot"].shape != p1["screenshot"].shape:
    pixel_mismatch_ratio = 1.0
    mean_abs_pixel_delta = 255.0
else:
    delta = np.abs(
        p0["screenshot"].astype(np.int16) - p1["screenshot"].astype(np.int16)
    )
    mismatched_pixels = np.any(delta != 0, axis=2)
    pixel_mismatch_ratio = float(mismatched_pixels.mean())
    mean_abs_pixel_delta = float(delta.mean())

    # Amplified diff image for human inspection.
    amplified = np.clip(delta * 8, 0, 255).astype(np.uint8)
    Image.fromarray(amplified).save(ARTIFACTS / "pixel_diff_x8.png")

p0_heading = p0["roles"].get("heading", 0)
p1_heading = p1["roles"].get("heading", 0)
p0_list = p0["roles"].get("list", 0)
p1_list = p1["roles"].get("list", 0)
p0_listitem = p0["roles"].get("listitem", 0)
p1_listitem = p1["roles"].get("listitem", 0)

semantic_divergence = (
    p1_heading >= 4
    and p1_heading > p0_heading
    and p1_list >= 1
    and p1_list > p0_list
    and p1_listitem >= 3
    and p1_listitem > p0_listitem
)

report = {
    "spike": "mp1a-browsergym-apparatus-v0",
    "browsergym_core_version": version("browsergym-core"),
    "viewport": VIEWPORT,
    "parity": {
        "normalized_visible_text_equal": same_text,
        "raw_link_label_and_target_equal": same_links,
        "pixel_mismatch_ratio": pixel_mismatch_ratio,
        "pixel_mismatch_ratio_limit": PIXEL_MISMATCH_RATIO_LIMIT,
        "mean_absolute_pixel_delta": mean_abs_pixel_delta,
    },
    "semantic_divergence": {
        "pass": semantic_divergence,
        "p0_heading_roles": p0_heading,
        "p1_heading_roles": p1_heading,
        "p0_list_roles": p0_list,
        "p1_list_roles": p1_list,
        "p0_listitem_roles": p0_listitem,
        "p1_listitem_roles": p1_listitem,
    },
    "observation_size": {
        "p0_axtree_chars": p0["axtree_chars"],
        "p1_axtree_chars": p1["axtree_chars"],
        "p0_dom_chars": p0["dom_chars"],
        "p1_dom_chars": p1["dom_chars"],
    },
    "roles": {
        "p0": p0["roles"],
        "p1": p1["roles"],
    },
    "links": p0["links"],
}

(ARTIFACTS / "report.json").write_text(
    json.dumps(report, indent=2, ensure_ascii=False),
    encoding="utf-8",
)

print(json.dumps(report, indent=2, ensure_ascii=False))

failures = []
if not same_text:
    failures.append("visible text parity failed")
if not same_links:
    failures.append("link parity failed")
if pixel_mismatch_ratio > PIXEL_MISMATCH_RATIO_LIMIT:
    failures.append(
        f"pixel parity failed: {pixel_mismatch_ratio:.6f} > "
        f"{PIXEL_MISMATCH_RATIO_LIMIT:.6f}"
    )
if not semantic_divergence:
    failures.append("intended AXTree semantic divergence was not established")

if failures:
    raise SystemExit("APPARATUS FAIL: " + "; ".join(failures))

print("APPARATUS PASS: visual/factual parity preserved while AXTree semantics diverged.")
