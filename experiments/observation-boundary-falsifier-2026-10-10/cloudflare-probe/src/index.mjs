/**
 * Cloudflare Workers Caching (2026) experiment. Read-only, public and replaceable.
 * GET /project and /project.json show source-navigation only, never project truth.
 * Pinned ?ref=<40-hex-commit> permits exact comparison of both representations.
 * Standard HTTP cache headers + cache.enabled in Wrangler own caching, not Cache API.
 */
const REPO = "Jozzpoly/Shared-Work-Medium-Lab";
const DOC_PATH = "docs/RESEARCH_STATE.md";
const API = "https://api.github.com/repos/" + REPO;
const SCHEMA = "swm.source-navigation-observation.v0";
const COMMIT_RE = /^[a-f0-9]{40}$/;
function sourceError(message,status=503) {
  const e=new Error(message);e.status=status;return e;
}
function apiHeaders(env) {
  const h=new Headers({
    "Accept":"application/vnd.github+json",
    "User-Agent":"swm-medium-observation-probe",
    "X-GitHub-Api-Version":"2026-03-10"
  });
  if (env.GITHUB_TOKEN) h.set("Authorization","Bearer "+env.GITHUB_TOKEN);
  return h;
}
async function readJson(requestFn,url,env) {
  const response=await requestFn(url,{headers:apiHeaders(env)});
  if (!response.ok) throw sourceError("GitHub unavailable: HTTP "+response.status);
  try{return await response.json();}
  catch{throw sourceError("GitHub returned invalid JSON");}
}
function decodeBase64(value) {
  try {
    const bytes=Uint8Array.from(atob(value.replace(/\s/g,"")),c=>c.charCodeAt(0));
    return new TextDecoder("utf-8",{fatal:true}).decode(bytes);
  } catch { throw sourceError("invalid source encoding"); }
}
function headings(markdown) {
  let fence=null;
  return markdown.split(/\r?\n/).flatMap((line,index)=>{
    const m=line.match(/^\s*(\x60{3,}|~{3,})/);
    if(m){
      const t=m[1][0];
      if(!fence)fence={type:t,length:m[1].length};
      else if(fence.type===t&&m[1].length>=fence.length)fence=null;
      return [];
    }
    if(fence)return [];
    const h=line.match(/^(#{2,3})\s+(.+?)\s*#*\s*$/);
    return h?[{level:h[1].length,title:h[2],line:index+1}]:[];
  });
}
async function digest(s) {
  const bytes=await crypto.subtle.digest("SHA-256",new TextEncoder().encode(s));
  return Array.from(new Uint8Array(bytes),b=>b.toString(16).padStart(2,"0")).join("");
}
export async function sampleObservation(env,{requestFn=fetch,now=()=>new Date().toISOString(),ref=null}={}) {
  if(ref!==null&&!COMMIT_RE.test(ref))throw sourceError("invalid pinned commit",400);
  const commit=ref??(await readJson(requestFn,API+"/commits/main",env))?.sha;
  if(!COMMIT_RE.test(commit||""))throw sourceError("cannot verify source commit");
  const file=await readJson(requestFn,API+"/contents/"+DOC_PATH+"?ref="+commit,env);
  if(file?.encoding!=="base64"||typeof file.content!=="string"||!COMMIT_RE.test(file.sha||"")) {
    throw sourceError("cannot verify pinned document");
  }
  if(file.content.length>800000)throw sourceError("source exceeds sample size");
  const text=decodeBase64(file.content);
  const hash=await digest(text);
  const observedAt=now();
  if(Number.isNaN(Date.parse(observedAt)))throw sourceError("invalid clock",500);
  return {
    schema:SCHEMA,kind:"navigation-only",
    observation_id:"sha256:"+hash,
    observed_at:observedAt,
    claims_about_current_product:[],
    source:{
      url:"https://github.com/"+REPO+"/blob/"+commit+"/"+DOC_PATH,
      repository:REPO,commit_sha:commit,blob_sha:file.sha,
      content_sha256:hash,git_ref_pinned:true,
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
  return "<!doctype html><html lang=\"pl\"><head><meta charset=\"utf-8\"><title>Medium — źródła</title></head><body><main>"+
    "<h1>Medium — nawigacja po źródłach</h1>"+
    "<p>Indeks dokumentu; nie interpretuje aktualnego stanu, znaczenia zmian ani Owner PASS.</p>"+
    "<p>Próbka: <time>"+esc(o.observed_at)+"</time>, commit <code>"+esc(o.source.commit_sha)+"</code>.</p>"+
    "<p>Obserwacja: <code>"+esc(o.observation_id)+"</code>.</p>"+
    "<nav aria-label=\"Sekcje\"><ol>"+links+"</ol></nav>"+
    "<p><a href=\""+esc(o.source.url)+"\">Otwórz przypięte źródło</a></p></main></body></html>";
}
export function createHandler({requestFn=fetch,now=()=>new Date().toISOString()}={}){
  return async(request,env={})=>{
    const url=new URL(request.url);
    if(request.method!=="GET")return new Response("Method not allowed",{status:405,headers:{Allow:"GET"}});
    if(url.pathname==="/health")return Response.json({
      status:"runtime-only",source_health:"not checked",scope:"experimental"
    },{headers:{"Cache-Control":"no-store"}});
    if(url.pathname!=="/"&&url.pathname!=="/project"&&url.pathname!=="/project.json"){
      return new Response("Not found",{status:404});
    }
    const asJson=url.pathname==="/project.json";
    const ref=url.searchParams.get("ref");
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
