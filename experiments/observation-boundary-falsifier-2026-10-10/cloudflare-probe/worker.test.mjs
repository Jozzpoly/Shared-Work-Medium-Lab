import test from "node:test";
import assert from "node:assert/strict";
import {createHandler, sampleObservation, renderObservationHtml} from "./src/index.mjs";

const COMMIT="a".repeat(40), BLOB="b".repeat(40);
const text=["# Medium","## Owner-observed product boundary","Owner-observed FAIL / not accepted.","## Frontier topology refresh","### Current PR","## <img src=x>",""].join("\n");
const source={sha:BLOB,encoding:"base64",content:Buffer.from(text,"utf8").toString("base64")};
const clock=()=>"2026-10-10T01:00:00Z";
const req=path=>new Request("https://example.workers.dev"+path);
function fakeOrigin({status=200,commit=COMMIT}={}){
  const calls=[];
  const requestFn=async(url,init)=>{
    calls.push({url,headers:init.headers});
    if(status!==200)return new Response("source failure",{status});
    return Response.json(url.endsWith("/commits/main")?{sha:commit}:source);
  };
  return {calls,requestFn};
}

test("HTML + JSON from identical pinned commit match in identity and source",async()=>{
  const origin=fakeOrigin();
  const handler=createHandler({requestFn:origin.requestFn,now:clock});
  const html=await handler(req("/project?ref="+COMMIT),{});
  const json=await handler(req("/project.json?ref="+COMMIT),{});
  const data=await json.json();
  assert.equal(html.status,200);
  assert.equal(json.status,200);
  assert.equal(html.headers.get("X-SWM-Observation-Id"),data.observation_id);
  assert.match(await html.text(),new RegExp(data.observation_id));
  assert.equal(data.source.commit_sha,COMMIT);
  assert.equal(data.source.git_ref_pinned,true);
  assert.equal(data.source.blob_sha,BLOB);
  assert.equal(origin.calls.length,2);
  assert.ok(origin.calls.every(c=>c.url.endsWith("?ref="+COMMIT)));
});

test("latest views do not claim atomicity; HTTP cache policy is observable",async()=>{
  const origin=fakeOrigin();
  const handler=createHandler({requestFn:origin.requestFn,now:clock});
  const response=await handler(req("/project.json"),{});
  assert.equal(response.headers.get("Cache-Control"),"public, max-age=300");
  assert.equal(response.headers.get("X-SWM-Cache-Policy"),"workers-caching-http");
  assert.equal(response.headers.get("X-SWM-Cache"),null);
  assert.equal(origin.calls.length,2);
  const pinned=await handler(req("/project.json?ref="+COMMIT),{});
  assert.equal(pinned.headers.get("Cache-Control"),"public, max-age=3600");
});

test("source metadata is navigation, never inferred Owner product acceptance",async()=>{
  const origin=fakeOrigin();
  const data=await sampleObservation({}, {requestFn:origin.requestFn,now:clock});
  assert.equal(data.kind,"navigation-only");
  assert.deepEqual(data.claims_about_current_product,[]);
  assert.ok(data.headings.some(x=>x.title==="Owner-observed product boundary"));
  assert.match(renderObservationHtml(data),/&lt;img src=x&gt;/);
  assert.ok(!renderObservationHtml(data).includes("<img src=x>"));
});

test("source errors preserve UNKNOWN without cache poisoning",async()=>{
  const origin=fakeOrigin({status:403});
  const handler=createHandler({requestFn:origin.requestFn,now:clock});
  const response=await handler(req("/project.json"),{});
  const data=await response.json();
  assert.equal(response.status,503);
  assert.equal(data.status,"source-unknown");
  assert.equal(response.headers.get("Cache-Control"),"no-store");
});

test("malformed ref rejected before GitHub call",async()=>{
  const origin=fakeOrigin();
  const handler=createHandler({requestFn:origin.requestFn,now:clock});
  const response=await handler(req("/project.json?ref=latest"),{});
  assert.equal(response.status,400);
  assert.equal(origin.calls.length,0);
});

test("health indicates runtime, not source freshness",async()=>{
  const origin=fakeOrigin();
  const handler=createHandler({requestFn:origin.requestFn,now:clock});
  const response=await handler(req("/health"),{});
  assert.equal((await response.json()).source_health,"not checked");
  assert.equal(origin.calls.length,0);
});

test("optional token never enters response",async()=>{
  const origin=fakeOrigin();const secret="test-secret";
  const data=await sampleObservation({GITHUB_TOKEN:secret},{requestFn:origin.requestFn,now:clock});
  assert.equal(origin.calls[0].headers.get("Authorization"),"Bearer "+secret);
  assert.ok(!JSON.stringify(data).includes(secret));
});

test("GitHub cannot silently provide an invalid commit id",async()=>{
  const origin=fakeOrigin({commit:"invalid"});
  await assert.rejects(sampleObservation({}, {requestFn:origin.requestFn,now:clock}),/cannot verify source commit/);
});
