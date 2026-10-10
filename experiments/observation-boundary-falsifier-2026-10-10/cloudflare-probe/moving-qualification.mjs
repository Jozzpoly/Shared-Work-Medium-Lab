/**
 * Real-network check of a moving GitHub main observation.
 * Checks honesty about source identity separately from raw/CDN freshness.
 * Does not claim atomic cross-origin observation or agent/product benefit.
 */
import {createHash} from "node:crypto";
import {fileURLToPath} from "node:url";

const EXPECTED_ORIGIN="https://swm-medium-observation-probe.jozzpoly.workers.dev";
const GITHUB="https://raw.githubusercontent.com/Jozzpoly/Shared-Work-Medium-Lab/main/docs/RESEARCH_STATE.md";
const SOURCE_URL="https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/main/docs/RESEARCH_STATE.md";
const sha=t=>createHash("sha256").update(t,"utf8").digest("hex");

export async function inspectMovingSource(origin,{fetchFn=fetch}={}) {
  if(new URL(origin).origin!==EXPECTED_ORIGIN||new URL(origin).pathname!=="/"||new URL(origin).search||new URL(origin).hash) {
    throw Error("Refusing unapproved worker origin");
  }
  const [worker,raw]=await Promise.all([
    fetchFn(EXPECTED_ORIGIN+"/project.json",{method:"GET"}),
    fetchFn(GITHUB,{method:"GET"})
  ]);
  let observation=null;
  try{observation=JSON.parse(await worker.text());}catch{}
  const rawBody=await raw.text();
  const errors=[];
  if(worker.status!==200)errors.push("moving Worker route unavailable");
  if(observation?.schema!=="swm.source-navigation-observation.v0")errors.push("unexpected source schema");
  if(observation?.source?.source_channel!=="github-raw-moving-main")errors.push("wrong observation channel");
  if(observation?.source?.commit_sha!==null||observation?.source?.blob_sha!==null||
     observation?.source?.git_ref_pinned!==false||observation?.source?.source_version_verified!==false) {
    errors.push("moving ref falsely promoted to pinned Git revision");
  }
  if(observation?.source?.url!==SOURCE_URL)errors.push("moving source URL misleading");
  if(typeof observation?.source?.content_sha256!=="string"||
     observation?.observation_id!=="sha256:"+observation.source.content_sha256)errors.push("content receipt mismatch");
  if(!Array.isArray(observation?.headings)||
     !observation.headings.some(h=>h.title.startsWith("Owner-observed product boundary"))||
     !observation.headings.some(h=>h.title.startsWith("Frontier topology refresh"))) {
    errors.push("critical source navigation landmarks missing");
  }
  const independentDigest=raw.status===200?sha(rawBody):null;
  const sameBytes=independentDigest!==null && observation?.source?.content_sha256===independentDigest;
  return {
    test:"swm-moving-main-live-qualification-v0",
    epistemics:errors.length?"FAIL":"PASS",
    errors,
    worker_status:worker.status,
    direct_source_status:raw.status,
    source_agreement:independentDigest===null?"UNKNOWN_SOURCE_UNAVAILABLE":sameBytes?"SAME_BYTES":"DIVERGED_OR_RACE_OR_CACHE",
    independent_digest:independentDigest,
    worker_digest:observation?.source?.content_sha256??null,
    observed_at:observation?.observed_at??null,
    caveat:"moving source and edge cache are not atomic; byte mismatch does not by itself establish incorrect data"
  };
}
if(process.argv[1] && fileURLToPath(import.meta.url)===process.argv[1]){
  try{
    const result=await inspectMovingSource(process.argv[2]||"");
    process.stdout.write(JSON.stringify(result,null,2)+"\n");
    if(result.epistemics!=="PASS")process.exitCode=1;
  }catch(e){process.stderr.write(String(e.message||e)+"\n");process.exitCode=2;}
}
