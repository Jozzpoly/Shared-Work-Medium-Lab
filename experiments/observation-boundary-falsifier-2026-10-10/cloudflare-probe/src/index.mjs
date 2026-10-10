/**
 * Experimental public read-only source-observation Worker.
 * One sampled GitHub commit => one cacheable observation => HTML and JSON views.
 * Does not infer current project intent, accepted status, agent liveness or Owner PASS.
 * Cache API is colo-local: NOT a globally coherent source of truth.
 */
const REPO = "Jozzpoly/Shared-Work-Medium-Lab";
const DOC_PATH = "docs/RESEARCH_STATE.md";
const API = "https://api.github.com/repos/" + REPO;
const SCHEMA = "swm.source-navigation-observation.v0";
const CACHE_SECONDS = 600;

function safeError(message, status = 503) {
  const error = new Error(message);
  error.status = status;
  return error;
}
function sourceHeaders(env) {
  const h = new Headers({
    "Accept": "application/vnd.github+json",
    "User-Agent": "swm-observation-comparison-probe",
    "X-GitHub-Api-Version": "2026-03-10"
  });
  if (env.GITHUB_TOKEN) h.set("Authorization", "Bearer " + env.GITHUB_TOKEN);
  return h;
}
async function fetchObject(requestFn, url, env) {
  const response = await requestFn(url, {headers: sourceHeaders(env)});
  if (!response.ok) throw safeError("source unavailable (GitHub status " + response.status + ")");
  try { return await response.json(); }
  catch { throw safeError("source returned invalid JSON"); }
}
function getHeadings(markdown) {
  let fence = null;
  return markdown.split(/\r?\n/).flatMap((line, index) => {
    const marker = line.match(/^\s*(`{3,}|~{3,})/);
    if (marker) {
      const type = marker[1][0];
      if (!fence) fence = {type, length: marker[1].length};
      else if (fence.type === type && marker[1].length >= fence.length) fence = null;
      return [];
    }
    if (fence) return [];
    const h = line.match(/^(#{2,3})\s+(.+?)\s*#*\s*$/);
    return h ? [{level: h[1].length, title: h[2], line: index+1}] : [];
  });
}
async function digest(text) {
  const bytes = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(text));
  return Array.from(new Uint8Array(bytes), b => b.toString(16).padStart(2, "0")).join("");
}
function decodeContent(encoded) {
  try {
    const bytes = Uint8Array.from(atob(encoded.replace(/\s/g, "")), c => c.charCodeAt(0));
    return new TextDecoder("utf-8", {fatal:true}).decode(bytes);
  } catch { throw safeError("invalid source content encoding"); }
}
export async function sampleObservation(env, {requestFn=fetch, now=()=>new Date().toISOString()}={}) {
  const current = await fetchObject(requestFn, API + "/commits/main", env);
  const commitSha = current?.sha;
  if (typeof commitSha !== "string" || !/^[a-f0-9]{40}$/.test(commitSha)) {
    throw safeError("unverified source commit");
  }
  const file = await fetchObject(requestFn, API + "/contents/" + DOC_PATH + "?ref=" + commitSha, env);
  if (file?.encoding !== "base64" || typeof file.content !== "string" || !/^[a-f0-9]{40}$/.test(file.sha || "")) {
    throw safeError("unverified source file");
  }
  if (file.content.length > 800000) throw safeError("source exceeds bounded sample size");
  const markdown = decodeContent(file.content);
  const hash = await digest(markdown);
  const timestamp = now();
  if (!timestamp || Number.isNaN(Date.parse(timestamp))) throw safeError("invalid observation clock", 500);
  return {
    schema: SCHEMA,
    observation_id: "sha256:" + hash,
    observed_at: timestamp,
    kind: "navigation-only",
    claims_about_current_product: [],
    source: {
      url: "https://github.com/" + REPO + "/blob/" + commitSha + "/" + DOC_PATH,
      repository: REPO,
      commit_sha: commitSha,
      blob_sha: file.sha,
      content_sha256: hash,
      version_verified: true,
      source_reachability_at_observation: "readable"
    },
    headings: getHeadings(markdown)
  };
}
function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
}
export function renderObservationHtml(o) {
  const links = o.headings.map(h => "<li><a href=\"" + escapeHtml(o.source.url) + "#L" + h.line + "\">" + escapeHtml(h.title) + "</a></li>").join("\n");
  return "<!doctype html><html lang=\"pl\"><head><meta charset=\"utf-8\"><title>Medium — źródła</title></head><body><main>" +
    "<h1>Medium — nawigacja po źródłach</h1>" +
    "<p>To tylko indeks źródła, nie ocena aktualnego projektu ani produktowy PASS.</p>" +
    "<p>Odczyt: <time>" + escapeHtml(o.observed_at) + "</time>; rewizja Git: <code>" + escapeHtml(o.source.commit_sha) + "</code>.</p>" +
    "<p>Identyfikator zawartości: <code>" + escapeHtml(o.observation_id) + "</code>.</p>" +
    "<nav aria-label=\"Sekcje dokumentu\"><ol>" + links + "</ol></nav>" +
    "<p><a href=\"" + escapeHtml(o.source.url) + "\">Otwórz dokładne źródło</a></p></main></body></html>";
}
export function createHandler({requestFn=fetch, cache, now=()=>new Date().toISOString()}={}) {
  return async function(request, env={}) {
    const url = new URL(request.url);
    if (request.method !== "GET") return new Response("Method not allowed", {status:405, headers:{"Allow":"GET"}});
    if (url.pathname === "/health") {
      return Response.json({status:"runtime-only", source_health:"not checked", scope:"experiment"}, {headers:{"Cache-Control":"no-store"}});
    }
    if (url.pathname !== "/" && url.pathname !== "/project" && url.pathname !== "/project.json") {
      return new Response("Not found", {status:404});
    }
    const asJson = url.pathname === "/project.json";
    const selectedCache = cache === undefined ? (typeof caches === "undefined" ? null : caches.default) : cache;
    const key = new Request(url.origin + "/__swm_internal/observation-v1", {method:"GET"});
    let cached;
    try {
      if (selectedCache) cached = await selectedCache.match(key);
      let observation;
      let cacheStatus = "BYPASS";
      if (cached) {
        observation = await cached.json();
        if (observation.schema !== SCHEMA) throw safeError("invalid cached observation");
        cacheStatus = "HIT";
      } else {
        observation = await sampleObservation(env, {requestFn, now});
        cacheStatus = selectedCache ? "MISS" : "BYPASS";
        if (selectedCache) {
          const snapshot = new Response(JSON.stringify(observation), {
            headers:{"Content-Type":"application/json; charset=utf-8", "Cache-Control":"public, max-age=" + CACHE_SECONDS}
          });
          try { await selectedCache.put(key, snapshot); }
          catch { cacheStatus = "BYPASS"; }
        }
      }
      const headers = {
        "Cache-Control":"no-store",
        "X-SWM-Observation-Id":observation.observation_id,
        "X-SWM-Cache":cacheStatus,
        "X-SWM-Cache-Scope":"colo-local",
        "X-SWM-Source-Commit":observation.source.commit_sha,
        "X-Content-Type-Options":"nosniff"
      };
      if (asJson) return Response.json(observation,{headers});
      headers["Content-Type"]="text/html; charset=utf-8";
      headers["Content-Security-Policy"]="default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; frame-ancestors 'none'";
      return new Response(renderObservationHtml(observation), {headers});
    } catch (error) {
      const response = {status:"source-unknown", previous_observation_not_revalidated:true, detail:error.message||"source unavailable"};
      if (asJson) return Response.json(response,{status:503,headers:{"Cache-Control":"no-store"}});
      return new Response("<!doctype html><html lang=\"pl\"><meta charset=\"utf-8\"><h1>Brak zweryfikowanej obserwacji</h1><p>Nie można potwierdzić aktualnego stanu źródła.</p></html>",{
        status:503,headers:{"Content-Type":"text/html; charset=utf-8","Cache-Control":"no-store"}
      });
    }
  };
}
export default {
  fetch(request,env) { return createHandler()(request,env); }
};
