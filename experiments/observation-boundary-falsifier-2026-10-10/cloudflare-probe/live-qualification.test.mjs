import test from "node:test";
import assert from "node:assert/strict";
import {createHash} from "node:crypto";
import {qualify,PIN} from "./live-qualification.mjs";
const origin="https://swm-medium-observation-probe.jozzpoly.workers.dev";
const source="## Medium real source\nOwner-observed FAIL / not accepted.\n";
const digest=createHash("sha256").update(source).digest("hex");
const observation={
  observation_id:"sha256:"+digest,
  observed_at:"2026-10-10T02:00:00Z",
  source:{commit_sha:PIN,content_sha256:digest},
  claims_about_current_product:[],headings:[{title:"Medium real source",line:1}]
};
function fake({badDigest=false,noHit=false,badQuery=false}={}){
  const calls=[];
  return {
    calls,
    async fetchFn(url){
      calls.push(url);
      const headers=new Headers();
      let body,status=200;
      if(url.includes("raw.githubusercontent.com"))body=source;
      else if(url.endsWith("/health"))body=JSON.stringify({source_health:"not checked"});
      else if(url.includes("nonce=")||url.includes("ref="+"b".repeat(40))) {
        status=badQuery?200:400;body="Unsupported query";
      } else if(url.includes("/project.json")){
        body=JSON.stringify(badDigest?{...observation,source:{...observation.source,content_sha256:"invalid"}}:observation);
        headers.set("X-SWM-Observation-Id",observation.observation_id);
        headers.set("CF-Cache-Status",noHit?"MISS":calls.filter(x=>x.includes("/project.json?")).length===1?"MISS":"HIT");
      }else if(url.includes("/project?")){
        body="<html>Observation "+observation.observation_id+"</html>";
        headers.set("X-SWM-Observation-Id",observation.observation_id);
        headers.set("CF-Cache-Status","MISS");
      }else throw Error("Unexpected URL "+url);
      return new Response(body,{status,headers});
    }
  };
}
test("live qualification validates immutable source and observes a real cache HIT header",async()=>{
  const f=fake();
  const r=await qualify(origin,{fetchFn:f.fetchFn});
  assert.equal(r.mechanics,"PASS");
  assert.equal(r.cache,"HIT_OBSERVED");
  assert.equal(r.observations.headings,1);
  assert.equal(f.calls.length,7);
});
test("mechanical PASS never promotes missing cache evidence into HIT",async()=>{
  const f=fake({noHit:true});
  const r=await qualify(origin,{fetchFn:f.fetchFn});
  assert.equal(r.mechanics,"PASS");
  assert.equal(r.cache,"HIT_NOT_OBSERVED");
});
test("source mismatch and unbounded query are reported as genuine failures",async()=>{
  const f=fake({badDigest:true,badQuery:true});
  const r=await qualify(origin,{fetchFn:f.fetchFn});
  assert.equal(r.mechanics,"FAIL");
  assert.ok(r.failures.some(x=>x.includes("bytes mismatch")));
  assert.ok(r.failures.some(x=>x.includes("unbounded query")));
});
test("only the intended public Worker origin is callable",async()=>{
  let calls=0;
  await assert.rejects(qualify("https://attacker.example/",{fetchFn:async()=>{calls++;throw Error();}}),/Only the exact experimental/);
  assert.equal(calls,0);
});
