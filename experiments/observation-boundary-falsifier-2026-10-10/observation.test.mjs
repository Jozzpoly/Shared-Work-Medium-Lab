/**
 * Bounded negative-control test for the historical Cloudflare observation gateway.
 *
 * Legacy source: experiment/semantic-medium-v0
 *   experiments/semantic-medium-v0/cloudflare-observation-gateway/src/index.js
 * Source observed: docs/RESEARCH_STATE.md in the current checkout.
 *
 * This is NOT a Cloudflare runtime, source freshness, or product acceptance test.
 * It reproduces a known source-layout / semantic-projection blind spot.
 */
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";

const stateText = readFileSync(
  new URL("../../docs/RESEARCH_STATE.md", import.meta.url),
  "utf8"
);

function stripLightMarkdown(value) {
  return (value || "")
    .replace(/\*\*/g, "")
    .replace(/`/g, "")
    .replace(/^>\s?/gm, "")
    .trim();
}

// Kept behaviorally identical to the 2026-10-03 v0 gateway's parser.
// A reproduced failure here is evidence about THAT parser, not all parsers.
function legacyDeclaredState(markdown) {
  const status = stripLightMarkdown(
    markdown.match(/\*\*Status:\*\*\s*(.+)/i)?.[1]
  ) || "unknown";

  const frontierSection = markdown.split(/\n## Current frontier\s*\n/i)[1] || "";
  const frontierBlock = frontierSection.split(/\n#{2,6}\s+/)[0] || "";
  const frontier = frontierBlock
    .split(/\n+/)
    .map(line => line.replace(/^>\s?/, "").trim())
    .filter(line => line && !line.startsWith("#"))
    .slice(0, 5)
    .join(" ");

  return { status, frontier: stripLightMarkdown(frontier) || "unknown" };
}

test("negative control: v0 misses the current frontier in today's canonical layout", () => {
  assert.match(stateText, /^## Frontier topology refresh\b/m);
  assert.equal(legacyDeclaredState(stateText).frontier, "unknown");
});

test("negative control: v0 headline status omits explicit Owner product FAIL", () => {
  assert.match(stateText, /Owner-observed FAIL\s*\/\s*not accepted/);
  assert.doesNotMatch(legacyDeclaredState(stateText).status, /Owner-observed FAIL/i);
});

test("negative control: v0 loses source-native PR entry links along with the frontier", () => {
  assert.match(stateText, /\[PR #5 — Quiet Presence ecological campaign\]\(https:\/\/github\.com\//);
  assert.equal(legacyDeclaredState(stateText).frontier, "unknown");
});

test("negative control: a later historical heading can be misread as today's frontier", () => {
  const misleading = stateText + "\n## Current frontier\nRetired history is the current plan.\n";
  assert.equal(
    legacyDeclaredState(misleading).frontier,
    "Retired history is the current plan."
  );
});
