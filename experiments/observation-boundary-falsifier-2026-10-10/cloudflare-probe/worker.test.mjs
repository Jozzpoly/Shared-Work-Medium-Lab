import {createHash} from "node:crypto";
import test from "node:test";
import assert from "node:assert/strict";
import {createHandler, sampleObservation, renderObservationHtml} from "./src/index.mjs";

const COMMIT="a".repeat(40), BLOB="b".repeat(40);
const text=["# Medium","## Owner-observed product boundary","Owner-observed FAIL / not accepted.","## Frontier topology refresh","### Current PR","## <img src=x>",""].join("\n");
const source={sha:BLOB,encoding:"base64",content:Buffer.from(text,"utf8").toString("base64")};
const DIGEST=createHash("sha256").update(text,"utf8").digest("hex");
const pinnedEnv={PINNED_SOURCE_COMMIT:COMMIT,PINNED_SOURCE_SHA256:DIGEST,PINNED_SOURCE_BLOB_SHA:BLOB};
const clock=()=>"2026-10-10T01:00:00Z";
const req=path=>new Request("https://example.workers.dev"+path);
function fakeOrigin({status=200,commit=COMMIT}={}){
  const calls=[];
  const requestFn=async(url,init)=>{
    calls.push({url,headers:init.headers});
    if(status!==200)return new Response("source failure",{status});
    if(url.includes("raw.githubusercontent.com"))return new Response(text,{status:200});
    return Response.json(url.endsWith("/commits/main")?{sha:commit}:source);
  };
  return {calls,requestFn};
}

test("HTML + JSON from identical pinned commit match in identity and source",async()=>{
  const origin=fakeOrigin();
  const handler=createHandler({requestFn:origin.requestFn,now:clock});
  const html=await handler(req("/project?ref="+COMMIT),pinnedEnv);
  const json=await handler(req("/project.json?ref="+COMMIT),pinnedEnv);
  const data=await json.json();
  assert.equal(html.status,200);
  assert.equal(json.status,200);
  assert.equal(html.headers.get("X-SWM-Observation-Id"),data.observation_id);
  assert.match(await html.text(),new RegExp(data.observation_id));
  assert.equal(data.source.commit_sha,COMMIT);
  assert.equal(data.source.git_ref_pinned,true);
  assert.equal(data.source.blob_sha,BLOB);
  assert.equal(origin.calls.length,2);
  assert.ok(origin.calls.every(c=>c.url.includes("raw.githubusercontent.com/"+ "Jozzpoly/Shared-Work-Medium-Lab/"+COMMIT)));
  assert.equal(data.source.source_channel,"github-raw-verified-content-digest");
});

test("latest views do not claim atomicity; HTTP cache policy is observable",async()=>{
  const origin=fakeOrigin();
  const handler=createHandler({requestFn:origin.requestFn,now:clock});
  const response=await handler(req("/project.json"),{});
  assert.equal(response.headers.get("Cache-Control"),"public, max-age=300");
  assert.equal(response.headers.get("X-SWM-Cache-Policy"),"workers-caching-http");
  assert.equal(response.headers.get("X-SWM-Cache"),null);
  assert.equal(origin.calls.length,1);
  assert.match(origin.calls[0].url,/raw\.githubusercontent\.com\/Jozzpoly\/Shared-Work-Medium-Lab\/main\//);
  const pinned=await handler(req("/project.json?ref="+COMMIT),pinnedEnv);
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
  assert.match(origin.calls[0].url,/raw\.githubusercontent\.com\/Jozzpoly\/Shared-Work-Medium-Lab\/main\//);
  assert.equal(origin.calls[0].headers.Authorization,undefined);
  assert.ok(!JSON.stringify(data).includes(secret));
});

test("moving main content does not manufacture an immutable source revision",async()=>{
  const origin=fakeOrigin({commit:"invalid"});
  const data=await sampleObservation({}, {requestFn:origin.requestFn,now:clock});
  assert.equal(data.source.commit_sha,null);
  assert.equal(data.source.blob_sha,null);
  assert.equal(data.source.git_ref_pinned,false);
  assert.equal(data.source.source_version_verified,false);
  assert.equal(data.source.source_channel,"github-raw-moving-main");
  assert.equal(data.source.url,"https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/main/docs/RESEARCH_STATE.md");
  assert.equal(origin.calls.length,1);
});

test("adversarial query variants cannot cause GitHub source calls",async()=>{
  const origin=fakeOrigin();
  const handler=createHandler({requestFn:origin.requestFn,now:clock});
  const probes=[
    "/project.json?nonce=attacker",
    "/project.json?ref="+COMMIT+"&nonce=attacker",
    "/project?ref="+COMMIT+"&ref="+COMMIT,
    "/project.json?ref="+"b".repeat(40),
    "/project.json?ref="+COMMIT
  ];
  for(const path of probes){
    const r=await handler(req(path),{PINNED_SOURCE_COMMIT:"c".repeat(40)});
    assert.equal(r.status,400,path);
    assert.equal(r.headers.get("Cache-Control"),"no-store");
  }
  assert.equal(origin.calls.length,0);
});

test("valid pinned URL only works with explicitly configured approved ref",async()=>{
  const origin=fakeOrigin();
  const handler=createHandler({requestFn:origin.requestFn,now:clock});
  assert.equal((await handler(req("/project.json?ref="+COMMIT),{})).status,400);
  assert.equal(origin.calls.length,0);
  const allowed=await handler(req("/project.json?ref="+COMMIT),pinnedEnv);
  assert.equal(allowed.status,200);
  assert.equal(origin.calls.length,1);
});

test("health endpoint rejects arbitrary query keys before source I/O",async()=>{
  const origin=fakeOrigin();
  const handler=createHandler({requestFn:origin.requestFn,now:clock});
  const r=await handler(req("/health?nonce=1"),{});
  assert.equal(r.status,400);
  assert.equal(origin.calls.length,0);
});

test("approved pinned route succeeds via raw content even if REST API is limited",async()=>{
  let restCalls=0,rawCalls=0;
  const requestFn=async url=>{
    if(url.includes("raw.githubusercontent.com")){rawCalls++;return new Response(text);}
    restCalls++;return new Response("GitHub rate-limited",{status:403});
  };
  const h=createHandler({requestFn,now:clock});
  const result=await h(req("/project?ref="+COMMIT),pinnedEnv);
  assert.equal(result.status,200);
  assert.equal(rawCalls,1);
  assert.equal(restCalls,0);
});
test("pinned source digest corruption is rejected, not silently accepted",async()=>{
  const origin=fakeOrigin();
  const h=createHandler({requestFn:origin.requestFn,now:clock});
  const bad={...pinnedEnv,PINNED_SOURCE_SHA256:"f".repeat(64)};
  const result=await h(req("/project.json?ref="+COMMIT),bad);
  const body=await result.json();
  assert.equal(result.status,503);
  assert.equal(body.status,"source-unknown");
  assert.match(body.detail,/digest mismatch/);
});

test("moving main can change without providing a dishonest fixed commit",async()=>{
  let reads=0;
  const requestFn=async()=>new Response(text+"\nchange "+(++reads));
  const first=await sampleObservation({}, {requestFn,now:clock});
  const second=await sampleObservation({}, {requestFn,now:clock});
  assert.notEqual(first.observation_id,second.observation_id);
  assert.equal(first.source.commit_sha,null);
  assert.equal(second.source.git_ref_pinned,false);
});

test("moving link projections expose revision and line-anchor uncertainty",async()=>{
  const origin=fakeOrigin();
  const current=await sampleObservation({}, {requestFn:origin.requestFn,now:clock});
  const html=renderObservationHtml(current);
  assert.equal(current.source.line_anchors_stable,false);
  assert.match(html,/Niezweryfikowana rewizja Git/);
  assert.match(html,/Odnośniki do linii mogą się przesunąć/);
  assert.ok(!html.includes("<code>null</code>"));
  assert.match(html,/Otwórz ruchome źródło main/);
  const pinned=await sampleObservation(pinnedEnv,{requestFn:origin.requestFn,now:clock,ref:COMMIT});
  assert.equal(pinned.source.line_anchors_stable,true);
  assert.match(renderObservationHtml(pinned),/Przypięta rewizja Git/);
});

test("Worker parser excludes false fence headings and preserves later sections", async () => {
  const tick = String.fromCharCode(96);
  const sample = [
    "## Before",
    tick.repeat(3) + "js",
    tick.repeat(3) + "not-a-closer",
    "## FALSE inside",
    tick.repeat(3),
    "## After",
    "~~~~",
    tick.repeat(3),
    "## FALSE tilde",
    "~~~~",
    "## Last"
  ].join("\n");
  const o = await sampleObservation({}, {
    requestFn: async () => new Response(sample, { status: 200 }),
    now: clock
  });
  assert.deepEqual(o.headings.map(h => [h.line, h.title]), [
    [1, "Before"], [6, "After"], [11, "Last"]
  ]);
});
