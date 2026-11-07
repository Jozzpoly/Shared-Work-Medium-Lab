/**
 * GitHub-native, transport-neutral comparison baseline.
 * Navigational projection only; it NEVER infers accepted/current project claims.
 */
import { createHash } from "node:crypto";
import { readFileSync, mkdirSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const SOURCE_URL = "https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/main/docs/RESEARCH_STATE.md";

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
export function createObservation(markdown, {observedAt, sourceUrl=SOURCE_URL}={}) {
  if (typeof markdown !== "string") throw new TypeError("markdown must be text");
  if (!observedAt || Number.isNaN(Date.parse(observedAt))) throw new TypeError("observedAt required");
  if (!/^https:\/\/github\.com\/Jozzpoly\/Shared-Work-Medium-Lab\/blob\//.test(sourceUrl)) {
    throw new TypeError("only the bounded public SWM source is allowed");
  }
  const digest = createHash("sha256").update(markdown,"utf8").digest("hex");
  return {
    schema:"swm.source-navigation-observation.v0",
    observation_id:"sha256:"+digest,
    observed_at:observedAt,
    source:{url:sourceUrl,version:null,version_verified:false,content_sha256:digest},
    kind:"navigation-only",
    claims_about_current_product:[],
    headings:headings(markdown)
  };
}
function esc(x) {
  return String(x).replace(/[&<>"']/g,ch=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[ch]));
}
export function renderHtml(observation) {
  const links=observation.headings.map(h=>'<li><a href="'+esc(observation.source.url)+'#L'+h.line+'">'+esc(h.title)+'</a></li>').join("\n");
  return '<!doctype html><html lang="pl"><head><meta charset="utf-8"><title>Medium — source navigation</title></head><body><main>'+
    '<h1>Medium — nawigacja po źródle</h1>'+
    '<p>Próbka odczytu: <time>'+esc(observation.observed_at)+'</time>. Źródło jest ruchome; wersja Git niezweryfikowana.</p>'+
    '<p>To mapa źródła, nie interpretacja aktualnego Medium ani produktowy PASS.</p>'+
    '<p>Obserwacja: <code>'+esc(observation.observation_id)+'</code></p>'+
    '<nav aria-label="Sekcje dokumentu"><ol>'+links+'</ol></nav>'+
    '<p><a href="'+esc(observation.source.url)+'">Otwórz pełne źródło</a></p></main></body></html>';
}
export function renderJson(observation) {
  return JSON.stringify(observation,null,2)+"\n";
}
if (process.argv[1] && fileURLToPath(import.meta.url) === resolve(process.argv[1])) {
  const target=resolve(process.argv[2] || "/tmp/swm-source-navigation");
  const raw=readFileSync(new URL("../../docs/RESEARCH_STATE.md",import.meta.url),"utf8");
  const observation=createObservation(raw,{observedAt:new Date().toISOString()});
  mkdirSync(target,{recursive:true});
  writeFileSync(resolve(target,"observation.json"),renderJson(observation));
  writeFileSync(resolve(target,"index.html"),renderHtml(observation));
  process.stdout.write("headings="+observation.headings.length+" id="+observation.observation_id+"\n");
}
