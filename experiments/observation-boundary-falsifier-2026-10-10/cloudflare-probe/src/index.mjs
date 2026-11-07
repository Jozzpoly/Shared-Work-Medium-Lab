/**
 * Cloudflare Workers Caching (2026) experiment. Read-only, public and replaceable.
 * GET /project and /project.json show source-navigation only, never project truth.
 * Pinned ?ref=<approved commit> only. Unknown query keys are rejected before source I/O.
 * Standard HTTP cache headers + cache.enabled in Wrangler own caching, not Cache API.
 */
const REPO = "Jozzpoly/Shared-Work-Medium-Lab";
const DOC_PATH = "docs/RESEARCH_STATE.md";
const SCHEMA = "swm.source-navigation-observation.v0";
const COMMIT_RE = /^[a-f0-9]{40}$/;
function sourceError(message,status=503) {
  const e=new Error(message);e.status=status;return e;
}
function headings(markdown) {
  let fence = null;
  return markdown.split(/\r?\n/).flatMap((line, index) => {
    if (fence) {
      // CommonMark: a closer may have at most 3 leading spaces, must
      // use the opening marker, be at least as long, and end with whitespace.
      const close = line.match(/^ {0,3}(`{3,}|~{3,})[ \t]*$/);
      if (close && close[1][0] === fence.type && close[1].length >= fence.length) {
        fence = null;
      }
      return [];
    }
    const open = line.match(/^ {0,3}(`{3,}|~{3,})(.*)$/);
    if (open && !(open[1][0] === "`" && open[2].includes("`"))) {
      fence = { type: open[1][0], length: open[1].length };
      return [];
    }
    const h = line.match(/^(#{2,3})\s+(.+?)\s*#*\s*$/);
    return h ? [{ level: h[1].length, title: h[2], line: index + 1 }] : [];
  });
}
async function digest(s) {
  const bytes=await crypto.subtle.digest("SHA-256",new TextEncoder().encode(s));
  return Array.from(new Uint8Array(bytes),b=>b.toString(16).padStart(2,"0")).join("");
}
export async function sampleObservation(env,{requestFn=fetch,now=()=>new Date().toISOString(),ref=null}={}) {
  if(ref!==null&&!COMMIT_RE.test(ref))throw sourceError("invalid pinned commit",400);
  let commit, text, blobSha, hash, channel;
  if(ref!==null){
    // Immutable source path with an independently prequalified digest.
    // No unauthenticated GitHub REST quota is consumed by this specimen route.
    if(ref!==env.PINNED_SOURCE_COMMIT ||
       !/^[a-f0-9]{64}$/.test(env.PINNED_SOURCE_SHA256||"") ||
       !COMMIT_RE.test(env.PINNED_SOURCE_BLOB_SHA||"")){
      throw sourceError("unqualified pinned source",400);
    }
    commit=ref;
    const rawUrl="https://raw.githubusercontent.com/"+REPO+"/"+commit+"/"+DOC_PATH;
    const response=await requestFn(rawUrl,{headers:{"User-Agent":"swm-medium-observation-probe"}});
    if(!response.ok)throw sourceError("pinned raw source unavailable: HTTP "+response.status);
    text=await response.text();
    if(text.length>500000)throw sourceError("pinned raw source too large");
    hash=await digest(text);
    if(hash!==env.PINNED_SOURCE_SHA256)throw sourceError("pinned raw content digest mismatch");
    blobSha=env.PINNED_SOURCE_BLOB_SHA;
    channel="github-raw-verified-content-digest";
  }else{
    // Moving ref: current contents can be observed without inventing a commit SHA.
    // The raw branch URL can be stale at its CDN and is NOT an immutable revision.
    commit=null;
    const url="https://raw.githubusercontent.com/"+REPO+"/main/"+DOC_PATH;
    const response=await requestFn(url,{headers:{"User-Agent":"swm-medium-observation-probe"}});
    if(!response.ok)throw sourceError("moving raw source unavailable: HTTP "+response.status);
    text=await response.text();
    if(text.length>500000)throw sourceError("moving raw source exceeds sample size");
    hash=await digest(text);
    blobSha=null;
    channel="github-raw-moving-main";
  }
  const observedAt=now();
  if(Number.isNaN(Date.parse(observedAt)))throw sourceError("invalid clock",500);
  return {
    schema:SCHEMA,kind:"navigation-only",
    observation_id:"sha256:"+hash,
    observed_at:observedAt,
    claims_about_current_product:[],
    source:{
      url:"https://github.com/"+REPO+"/blob/"+(commit??"main")+"/"+DOC_PATH,
      repository:REPO,commit_sha:commit,blob_sha:blobSha,
      content_sha256:hash,git_ref_pinned:commit!==null,source_version_verified:commit!==null,source_channel:channel,
      line_anchors_stable:commit!==null,
      observed_as_readable_at:observedAt
    },
    headings:headings(text)
  };
}
function esc(s) {
  return String(s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
}
export function renderObservationHtml(o){
  const links=o.headings.map(h=>"<li><a href=\""+esc(o.source.url)+"#L"+h.line+"\">"+esc(h.title)+"</a></li>").join("\n");
  const versionNote=o.source.git_ref_pinned
    ? "<p>Przypięta rewizja Git; odnośniki do linii odnoszą się do tej konkretnej wersji.</p>"
    : "<p>Niezweryfikowana rewizja Git: obserwacja zmiennej gałęzi main. Odnośniki do linii mogą się przesunąć po kolejnej zmianie źródła.</p>";
  const displayedRevision=o.source.git_ref_pinned ? "commit <code>"+esc(o.source.commit_sha)+"</code>" : "main (dokładny commit nieznany)";
  const sourceLabel=o.source.git_ref_pinned ? "Otwórz przypięte źródło" : "Otwórz ruchome źródło main";
  return "<!doctype html><html lang=\"pl\"><head><meta charset=\"utf-8\"><title>Medium — źródła</title></head><body><main>"+
    "<h1>Medium — nawigacja po źródłach</h1>"+
    "<p>Indeks dokumentu; nie interpretuje aktualnego stanu, znaczenia zmian ani Owner PASS.</p>"+
    "<p>Próbka: <time>"+esc(o.observed_at)+"</time>, "+displayedRevision+".</p>"+versionNote+
    "<p>Obserwacja: <code>"+esc(o.observation_id)+"</code>.</p>"+
    "<nav aria-label=\"Sekcje\"><ol>"+links+"</ol></nav>"+
    "<p><a href=\""+esc(o.source.url)+"\">"+sourceLabel+"</a></p></main></body></html>";
}
export function createHandler({requestFn=fetch,now=()=>new Date().toISOString()}={}){
  return async(request,env={})=>{
    const url=new URL(request.url);
    if(request.method!=="GET")return new Response("Method not allowed",{status:405,headers:{Allow:"GET"}});
    const params=[...url.searchParams.entries()];
    if(params.length>1 || (params.length===1 && params[0][0]!=="ref")){
      return new Response("Unsupported query",{status:400,headers:{"Cache-Control":"no-store"}});
    }
    if(url.pathname==="/health" && params.length){
      return new Response("Health does not accept query parameters",{status:400,headers:{"Cache-Control":"no-store"}});
    }
    if(url.pathname==="/health")return Response.json({
      status:"runtime-only",source_health:"not checked",scope:"experimental"
    },{headers:{"Cache-Control":"no-store"}});
    if(url.pathname!=="/"&&url.pathname!=="/project"&&url.pathname!=="/project.json"){
      return new Response("Not found",{status:404});
    }
    const asJson=url.pathname==="/project.json";
    const ref=url.searchParams.get("ref");
    // A public unbounded ?ref accepts infinitely many cache keys and can drain the upstream budget.
    // Only one explicitly configured commit is allowed for this controlled A/B specimen.
    if(ref!==null && (!COMMIT_RE.test(ref) || !COMMIT_RE.test(env.PINNED_SOURCE_COMMIT||"") || ref!==env.PINNED_SOURCE_COMMIT)){
      return new Response("Pinned source revision is not approved",{status:400,headers:{"Cache-Control":"no-store"}});
    }
    try{
      const o=await sampleObservation(env,{requestFn,now,ref});
      const ttl=ref?3600:300; // pinned commit immutable; main sample may be stale
      const headers={
        "Cache-Control":"public, max-age="+ttl,
        "X-SWM-Observation-Id":o.observation_id,
        "X-SWM-Source-Commit":o.source.commit_sha,
        "X-SWM-Cache-Policy":"workers-caching-http",
        "X-Content-Type-Options":"nosniff"
      };
      // Do not claim HTML and JSON were sampled atomically on separate requests.
      // With ?ref=<sha>, both resolve the same immutable Git commit.
      if(asJson)return Response.json(o,{headers});
      headers["Content-Type"]="text/html; charset=utf-8";
      headers["Content-Security-Policy"]="default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; frame-ancestors 'none'";
      return new Response(renderObservationHtml(o),{headers});
    }catch(e){
      const status=e.status===400?400:503;
      if(asJson)return Response.json({status:"source-unknown",detail:e.message||"unavailable"},{
        status,headers:{"Cache-Control":"no-store"}
      });
      return new Response("<!doctype html><html lang=\"pl\"><meta charset=\"utf-8\"><h1>Brak zweryfikowanej obserwacji</h1></html>",{
        status,headers:{"Cache-Control":"no-store","Content-Type":"text/html; charset=utf-8"}
      });
    }
  };
}
export default {fetch(request,env){return createHandler()(request,env);}};
