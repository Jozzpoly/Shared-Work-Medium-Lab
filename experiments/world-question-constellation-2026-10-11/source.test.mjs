import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
const html=readFileSync(new URL('./index.html',import.meta.url),'utf8');
const script=html.match(/<script>([\s\S]*?)<\/script>/)?.[1];
if(!script)throw Error('missing inline script');
const modelText=script.match(/const model=(\{[\s\S]*?\});const lenses=/)?.[1];
if(!modelText)throw Error('missing model');
const model=JSON.parse(modelText),worlds=Object.entries(model).filter(([,v])=>v.kind==='world'),seams=Object.entries(model).filter(([,v])=>v.kind==='seam');
test('five source-qualified worlds and five bounded questions',()=>{
 assert.equal(worlds.length,5);assert.equal(seams.length,5);
 assert.deepEqual(worlds.map(([id])=>id).sort(),['combat','matter','medium','npc','reflex']);
 for(const [id,x] of worlds){
  assert.match(x.sha,/^[a-f0-9]{40}$/);
  assert.match(x.repo,/^[A-Za-z0-9-]+$/);
  for(const field of ['summary','worlds','bridges','limits','risk'])assert.ok(x[field]?.length>35,id+' missing '+field);
 }
 for(const [id,x] of seams){assert.equal(model[x.from]?.kind,'world');assert.equal(model[x.to]?.kind,'world');assert.notEqual(x.from,x.to);}
});
test('read-only runtime and bounded immutable public source reads',()=>{
 assert.match(html,/Content-Security-Policy/);assert.match(html,/default-src 'none'/);
 assert.equal((html.match(/\bfetch\s*\(/g)||[]).length,3);
 assert.match(html,/connect-src https:\/\/raw\.githubusercontent\.com/);
 assert.match(html,/function rawLink\(e\)/);
 assert.match(html,/function exportObservation\(\)/);
 assert.match(html,/function sampleMovingMain\(side\)/);
 assert.match(html,/id="radar-form"/);
 assert.match(html,/radarCache\.set\(id,lines\)/);
 assert.ok(!/\blocalStorage\b|\bsessionStorage\b|\bXMLHttpRequest\b|\bsendBeacon\b/.test(html));
 assert.ok(!/<img\b/.test(html));
 assert.equal((html.match(/data-view="/g)||[]).length,10);
 assert.equal((html.match(/<button[^>]*data-lens="/g)||[]).length,3);
});
test('inline script parses and static exits target source-native github',()=>{
 new vm.Script(script,{filename:'world.js'});
 const urls=[...html.matchAll(/href="(https:[^"]+)"/g)].map(x=>x[1]);
 assert.ok(urls.length>=6);
 for(const url of urls)assert.equal(new URL(url).hostname,'github.com');
});
