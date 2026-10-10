/**
 * Differential A/B parity test on the actual checked-out Medium source.
 * Simulates only transport, not Cloudflare cache, live GitHub, user or agent.
 */
import test from "node:test";
import assert from "node:assert/strict";
import {readFileSync} from "node:fs";
import {createObservation as nativeObservation} from "./native-baseline.mjs";
import {sampleObservation as workerObservation} from "./cloudflare-probe/src/index.mjs";

const markdown=readFileSync(new URL("../../docs/RESEARCH_STATE.md",import.meta.url),"utf8");
const now=()=>"2026-10-10T02:00:00Z";
const commit="a".repeat(40),blob="b".repeat(40);
const requests=[];
const fakeGithub=async url=>{
  requests.push(url);
  const contents={
    sha:blob,encoding:"base64",
    content:Buffer.from(markdown,"utf8").toString("base64")
  };
  if(url.includes("raw.githubusercontent.com"))return new Response(markdown);
  return Response.json(url.endsWith("/commits/main")?{sha:commit}:contents);
};

test("real Medium source: A and B agree on content digest and every heading",async()=>{
  requests.length=0;
  const a=nativeObservation(markdown,{observedAt:now()});
  const b=await workerObservation({}, {requestFn:fakeGithub,now});
  assert.equal(a.observation_id,b.observation_id);
  assert.equal(a.source.content_sha256,b.source.content_sha256);
  assert.deepEqual(a.headings,b.headings);
  assert.ok(a.headings.length>=40);
  assert.equal(requests.length,1);
  assert.match(requests[0],/raw\.githubusercontent\.com\/Jozzpoly\/Shared-Work-Medium-Lab\/main\//);
  assert.equal(b.source.git_ref_pinned,false);
});

test("real Medium source: neither A nor B invents accepted product status",async()=>{
  const a=nativeObservation(markdown,{observedAt:now()});
  const b=await workerObservation({}, {requestFn:fakeGithub,now});
  assert.match(markdown,/Owner-observed FAIL\s*\/\s*not accepted/);
  assert.deepEqual(a.claims_about_current_product,[]);
  assert.deepEqual(b.claims_about_current_product,[]);
  assert.equal(a.kind,"navigation-only");
  assert.equal(b.kind,"navigation-only");
});
