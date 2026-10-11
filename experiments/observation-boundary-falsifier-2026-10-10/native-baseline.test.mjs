import assert from "node:assert/strict";
import test from "node:test";
import {createObservation,renderHtml,renderJson} from "./native-baseline.mjs";

const observedAt="2026-10-10T01:45:00Z";
const fence=String.fromCharCode(96).repeat(3);
const document=["# State","## Current project state","Owner-observed FAIL.",fence+"markdown","## Not a real heading",fence,"### Native source",""].join("\n");

test("native baseline never invents current/product verdicts",()=>{
  const x=createObservation(document,{observedAt});
  assert.equal(x.kind,"navigation-only");
  assert.deepEqual(x.claims_about_current_product,[]);
  assert.equal(x.source.version_verified,false);
  assert.equal(x.source.version,null);
});
test("links track original heading lines, ignoring code fences",()=>{
  const x=createObservation(document,{observedAt});
  assert.deepEqual(x.headings.map(h=>[h.level,h.line,h.title]),[
    [2,2,"Current project state"],[3,7,"Native source"]
  ]);
  assert.match(renderHtml(x),/#L7/);
});
test("both representations share the same single sampled observation",()=>{
  const x=createObservation(document,{observedAt});
  const decoded=JSON.parse(renderJson(x));
  assert.equal(decoded.observation_id,x.observation_id);
  assert.ok(renderHtml(x).includes(x.observation_id));
  assert.equal(createObservation(document,{observedAt}).observation_id,x.observation_id);
  assert.notEqual(createObservation(document+"changed",{observedAt}).observation_id,x.observation_id);
});
test("source headings are escaped and cross-origin sources rejected",()=>{
  const x=createObservation("## <img src=x onerror=alert(1)>",{observedAt});
  const html=renderHtml(x);
  assert.ok(!html.includes("<img"));
  assert.ok(html.includes("&lt;img"));
  assert.throws(()=>createObservation(document,{observedAt,sourceUrl:"https://evil.invalid/"}));
});

test("fenced-code near-closers cannot create fake headings or hide later ones", () => {
  const tick = String.fromCharCode(96);
  const lines = [
    "## Before",
    tick.repeat(3) + "js",
    "literal command",
    tick.repeat(3) + "not-a-closing-fence",
    "## FALSE inside code",
    tick.repeat(3),
    "## After",
    "~~~markdown",
    "## Inside tilde",
    tick.repeat(3),
    "## STILL INSIDE tilde",
    "~~~~ ",
    "## After tilde",
    tick.repeat(4),
    tick.repeat(3),
    "## STILL INSIDE length-4",
    tick.repeat(4) + " ",
    "## Last"
  ];
  const result = createObservation(lines.join("\n"), { observedAt });
  assert.deepEqual(result.headings.map(h => [h.line, h.title]), [
    [1, "Before"], [7, "After"], [13, "After tilde"], [18, "Last"]
  ]);
});
