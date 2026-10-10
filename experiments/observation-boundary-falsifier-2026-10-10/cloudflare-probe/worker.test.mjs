import test from "node:test";
import assert from "node:assert/strict";
import {createHandler, sampleObservation, renderObservationHtml} from "./src/index.mjs";

const COMMIT = "a".repeat(40);
const BLOB = "b".repeat(40);
const text = ["# Medium", "## Owner-observed product boundary", "Owner-observed FAIL / not accepted.", "## Frontier topology refresh", "### Current PR", "## <img src=x>", ""].join("\n");
const source = {
  sha: BLOB,
  encoding: "base64",
  content: Buffer.from(text, "utf8").toString("base64")
};
const record = {sha: COMMIT};
function fakeOrigin({responseStatus=200}={}) {
  const calls = [];
  const requestFn = async (url, init) => {
    calls.push({url, headers:init.headers});
    return responseStatus===200
      ? Response.json(url.endsWith("/commits/main") ? record : source)
      : new Response("source failure", {status:responseStatus});
  };
  return {calls,requestFn};
}
function fakeCache() {
  const entries=new Map();
  return {
    async match(key) {const x=entries.get(key.url);return x?.clone();},
    async put(key,response) {entries.set(key.url,response.clone());}
  };
}
const clock=()=>"2026-10-10T01:00:00Z";
const req=path=>new Request("https://example.workers.dev"+path);

test("two representations reuse exactly one cached sample (same colo)", async ()=>{
  const origin=fakeOrigin();
  const handler=createHandler({requestFn:origin.requestFn,cache:fakeCache(),now:clock});
  const html=await handler(req("/project"),{});
  const json=await handler(req("/project.json"),{});
  const obj=await json.json();
  assert.equal(html.status,200);
  assert.equal(json.status,200);
  assert.equal(html.headers.get("X-SWM-Cache"),"MISS");
  assert.equal(json.headers.get("X-SWM-Cache"),"HIT");
  assert.equal(origin.calls.length,2);
  assert.equal(origin.calls[1].url.endsWith("ref="+COMMIT),true);
  assert.equal(html.headers.get("X-SWM-Observation-Id"),obj.observation_id);
  assert.match(await html.text(),new RegExp(obj.observation_id));
  assert.equal(obj.source.commit_sha,COMMIT);
  assert.equal(obj.source.blob_sha,BLOB);
  assert.equal(obj.source.version_verified,true);
});

test("source content is navigation, never inferred product acceptance",async()=>{
  const origin=fakeOrigin();
  const obj=await sampleObservation({}, {requestFn:origin.requestFn,now:clock});
  assert.equal(obj.kind,"navigation-only");
  assert.deepEqual(obj.claims_about_current_product,[]);
  assert.ok(obj.headings.some(h=>h.title==="Owner-observed product boundary"));
  assert.match(renderObservationHtml(obj),/&lt;img src=x&gt;/);
  assert.ok(!renderObservationHtml(obj).includes("<img src=x>"));
});

test("source API failure becomes explicit UNKNOWN, never a cached PASS",async()=>{
  const origin=fakeOrigin({responseStatus:403});
  const handler=createHandler({requestFn:origin.requestFn,cache:fakeCache(),now:clock});
  const answer=await handler(req("/project.json"),{});
  const obj=await answer.json();
  assert.equal(answer.status,503);
  assert.equal(obj.status,"source-unknown");
  assert.equal(obj.previous_observation_not_revalidated,true);
  assert.equal(origin.calls.length,1);
});

test("runtime health is NOT source health",async()=>{
  const origin=fakeOrigin();
  const handler=createHandler({requestFn:origin.requestFn,cache:fakeCache(),now:clock});
  const res=await handler(req("/health"),{});
  assert.equal((await res.json()).source_health,"not checked");
  assert.equal(origin.calls.length,0);
});

test("optional GitHub token never enters outward observation",async()=>{
  const origin=fakeOrigin();
  const secret="sensitive-test-value";
  const obj=await sampleObservation({GITHUB_TOKEN:secret},{requestFn:origin.requestFn,now:clock});
  assert.equal(origin.calls[0].headers.get("Authorization"),"Bearer "+secret);
  assert.ok(!JSON.stringify(obj).includes(secret));
});

test("malformed source commit is rejected", async()=>{
  const origin={requestFn:async()=>Response.json({sha:"invalid"})};
  await assert.rejects(sampleObservation({}, {requestFn:origin.requestFn,now:clock}),/unverified source commit/);
});
