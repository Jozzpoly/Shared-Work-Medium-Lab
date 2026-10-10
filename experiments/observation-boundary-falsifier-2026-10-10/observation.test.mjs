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
import { createHash } from "node:crypto";
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

function sourceReceipt(markdown, sourceRef, observedAt) {
  return {
    source_ref: sourceRef,
    observed_at: observedAt,
    content_sha256: createHash("sha256").update(markdown, "utf8").digest("hex")
  };
}

test("negative control: v0 misses the current frontier in today's canonical layout", () => {
  assert.match(stateText, /^## Frontier topology refresh\b/m);
  assert.equal(legacyDeclaredState(stateText).frontier, "unknown");
});

test("negative control: v0 headline status omits explicit Owner product FAIL", () => {
  assert.match(stateText, /Owner-observed FAIL\s*\/\s*not accepted/);
  assert.doesNotMatch(legacyDeclaredState(stateText).status, /Owner-observed FAIL/i);
});

test("a source receipt must change when source bytes change", () => {
  const first = sourceReceipt(stateText, "commit-A", "2026-10-10T00:00:00Z");
  const changed = sourceReceipt(stateText + "\n", "commit-B", "2026-10-10T00:00:01Z");
  assert.notEqual(first.content_sha256, changed.content_sha256);
});

test("HTML and JSON must be projections of ONE sampled receipt, not independent reads", () => {
  const once = sourceReceipt(stateText, "one-pinned-source", "2026-10-10T00:00:00Z");
  const htmlProjection = { representation: "html", source: once };
  const jsonProjection = { representation: "json", source: once };
  assert.deepEqual(htmlProjection.source, jsonProjection.source);
  assert.equal(htmlProjection.source.content_sha256, jsonProjection.source.content_sha256);
});

test("source content SHA-256 is NOT a Git commit or Git blob SHA", () => {
  const receipt = sourceReceipt(stateText, "unverified", "2026-10-10T00:00:00Z");
  assert.equal(receipt.content_sha256.length, 64);
  assert.equal(receipt.source_ref, "unverified");
});
