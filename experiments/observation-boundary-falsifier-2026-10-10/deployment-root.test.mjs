import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync, existsSync } from "node:fs";

const load = (path) => JSON.parse(readFileSync(new URL(path, import.meta.url), "utf8").replace(/^\/\/[^\n]*\n/gm, ""));
const root = load("../../wrangler.jsonc");
const nested = load("./cloudflare-probe/wrangler.jsonc");
const prefix = "experiments/observation-boundary-falsifier-2026-10-10/cloudflare-probe/";

test("repository root configuration matches existing Cloudflare Worker settings", () => {
  assert.equal(root.name, "swm-medium-observation-probe");
  assert.equal(root.name, nested.name);
  assert.equal(root.main, prefix + nested.main);
  assert.equal(root.compatibility_date, nested.compatibility_date);
  assert.deepEqual(root.cache, nested.cache);
  assert.deepEqual(root.vars, nested.vars);
  assert.ok(existsSync(new URL("../../" + root.main, import.meta.url)));
});

test("source scope is pinned and does not contain private bindings", () => {
  assert.match(root.vars.PINNED_SOURCE_COMMIT, /^[a-f0-9]{40}$/);
  assert.equal(root.vars.PINNED_SOURCE_COMMIT, "cff9839c1ac33189c23d93a399f17b44e8f219a0");
  for (const blocked of ["durable_objects","d1_databases","r2_buckets","queues","ai","routes","triggers"]) {
    assert.equal(Object.hasOwn(root,blocked),false,blocked);
  }
});
