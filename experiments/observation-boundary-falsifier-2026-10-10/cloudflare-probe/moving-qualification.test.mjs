import test from "node:test";
import assert from "node:assert/strict";
import {createHash} from "node:crypto";
import {inspectMovingSource} from "./moving-qualification.mjs";
const origin="https://swm-medium-observation-probe.jozzpoly.workers.dev/";
const raw="## Owner-observed product boundary\n## Frontier topology refresh\n";
const hash=createHash("sha256").update(raw).digest("hex");
const sample={
 schema:"swm.source-navigation-observation.v0",
 observation_id:"sha256:"+hash,
 observed_at:"2026-10-10T03:00:00Z",
 source:{source_channel:"github-raw-moving-main",commit_sha:null,blob_sha:null,git_ref_pinned:false,source_version_verified:false,
  url:"https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/main/docs/RESEARCH_STATE.md",content_sha256:hash},
 headings:[{title:"Owner-observed product boundary",line:1},{title:"Frontier topology refresh",line:2}]
};
function fake({mismatch=false,misleading=false}={}){
 const o=misleading?{...sample,source:{...sample.source,commit_sha:"a".repeat(40)}}:sample;
 return async url=>url.includes("raw.githubusercontent.com")
   ?new Response(mismatch?raw+"changed":raw)
   :Response.json(o);
}
test("moving route keeps honest provenance and matches the sampled source",async()=>{
 const x=await inspectMovingSource(origin,{fetchFn:fake()});
 assert.equal(x.epistemics,"PASS");
 assert.equal(x.source_agreement,"SAME_BYTES");
 assert.deepEqual(x.errors,[]);
});
test("different edge observations are reported as possible drift, not false certainty",async()=>{
 const x=await inspectMovingSource(origin,{fetchFn:fake({mismatch:true})});
 assert.equal(x.epistemics,"PASS");
 assert.equal(x.source_agreement,"DIVERGED_OR_RACE_OR_CACHE");
});
test("a moving source must not manufacture a commit identity",async()=>{
 const x=await inspectMovingSource(origin,{fetchFn:fake({misleading:true})});
 assert.equal(x.epistemics,"FAIL");
 assert.ok(x.errors.some(e=>e.includes("falsely promoted")));
});
test("arbitrary targets cannot be supplied to network qualifier",async()=>{
 let calls=0;
 await assert.rejects(inspectMovingSource("https://example.invalid/",{fetchFn:async()=>{calls++;throw Error("bad")}}),/Refusing unapproved/);
 assert.equal(calls,0);
});
