/**
 * Bounded live Cloudflare qualification: one immutable source, seven HTTP GETs.
 * Explicitly separates provenance/mechanics from actual cache HIT and product use.
 * Requires HTTPS Worker URL when used as CLI; no background polling.
 */
import {createHash} from "node:crypto";
import {readFileSync} from "node:fs";
import {fileURLToPath} from "node:url";

const config=JSON.parse(readFileSync(new URL("./wrangler.jsonc",import.meta.url),"utf8"));
export const PIN=config.vars.PINNED_SOURCE_COMMIT;
const githubRaw="https://raw.githubusercontent.com/Jozzpoly/Shared-Work-Medium-Lab/"+PIN+"/docs/RESEARCH_STATE.md";
function sha(x){return createHash("sha256").update(x,"utf8").digest("hex");}
function target(u){
  const url=new URL(u);
  if(url.protocol!=="https:"||url.username||url.password||url.search||url.hash||url.pathname!=="/"||
     !/^swm-medium-observation-probe\.[a-z0-9-]+\.workers\.dev$/.test(url.hostname)){
    throw Error("Only the exact experimental *.workers.dev origin is accepted");
  }
  return url.origin;
}
async function grab(fetchFn,url){
  const r=await fetchFn(url,{method:"GET"});
  const s=await r.text();
  return {status:r.status,body:s,cf_cache_status:r.headers.get("cf-cache-status"),
    id:r.headers.get("x-swm-observation-id"),cache_control:r.headers.get("cache-control")};
}
export async function qualify(origin,{fetchFn=fetch}={}){
  const base=target(origin);
  const first=await grab(fetchFn,base+"/project.json?ref="+PIN);
  const second=await grab(fetchFn,base+"/project.json?ref="+PIN);
  const html=await grab(fetchFn,base+"/project?ref="+PIN);
  const health=await grab(fetchFn,base+"/health");
  const badNonce=await grab(fetchFn,base+"/project.json?nonce=unapproved");
  const badRef=await grab(fetchFn,base+"/project.json?ref="+"b".repeat(40));
  const raw=await grab(fetchFn,githubRaw);
  let doc;
  try{doc=JSON.parse(second.body);}catch{doc=null;}
  const digest=sha(raw.body);
  const failures=[];
  if(raw.status!==200)failures.push("immutable GitHub source not retrievable");
  if(first.status!==200||second.status!==200||html.status!==200)failures.push("read-only projections unavailable");
  if(doc?.source?.commit_sha!==PIN)failures.push("source version mismatch");
  if(doc?.source?.content_sha256!==digest)failures.push("source bytes mismatch");
  if(doc?.observation_id!=="sha256:"+digest||first.id!==doc?.observation_id||html.id!==doc?.observation_id)
    failures.push("representation identity mismatch");
  if(!html.body.includes(doc?.observation_id||"UNAVAILABLE"))failures.push("HTML receipt missing");
  if(doc?.claims_about_current_product?.length!==0)failures.push("unapproved interpretation supplied");
  if(health.status!==200)failures.push("health endpoint failed");
  else if(JSON.parse(health.body).source_health!=="not checked")failures.push("health falsely certifies GitHub");
  if(badNonce.status!==400||badRef.status!==400)failures.push("unbounded query surface");
  const statuses=[first.cf_cache_status,second.cf_cache_status,html.cf_cache_status];
  return {
    test:"swm-cloudflare-live-qualification-v0",source_ref:PIN,
    mechanics:failures.length?"FAIL":"PASS",
    failures,
    cache:statuses.includes("HIT")?"HIT_OBSERVED":"HIT_NOT_OBSERVED",
    cache_headers:statuses,
    source_response_status:raw.status,
    source_digest:raw.status===200?digest:null,
    observations:{headings:doc?.headings?.length??null,observed_at:doc?.observed_at??null},
    boundaries:"no independent agent-lift, Owner-UX or continuous freshness qualification"
  };
}
if(process.argv[1]&&fileURLToPath(import.meta.url)===process.argv[1]){
  const url=process.argv[2];
  if(!url){process.stderr.write("Pass the actual experimental Worker HTTPS origin\n");process.exitCode=2;}
  else {
    try{const result=await qualify(url);process.stdout.write(JSON.stringify(result,null,2)+"\n");
      if(result.mechanics!=="PASS")process.exitCode=1;
    }catch(e){process.stderr.write(String(e.message||e)+"\n");process.exitCode=2;}
  }
}
