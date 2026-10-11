import assert from 'node:assert/strict';
import {chromium} from 'playwright';
import {fileURLToPath} from 'node:url';
import {mkdir} from 'node:fs/promises';

const source=fileURLToPath(new URL('./index.html',import.meta.url));
const base='https://api.github.com/repos/Jozzpoly/';
const combatSha='24bd930fb1bb83425ea43168660a9c9c75d5b7d6';
const reflexSha='25b4fe148e9949ef5be7049cfbb656ca3960411a';
const fixture={
  'Combat-Lab':{n:10,sha:combatSha,title:'B1 physical fold vs rigid envelope',
    doc:'docs/B1_PHYSICAL_ENVELOPE_DUAL_AFFORDANCE_2026-10-10.md'},
  'ReflexBrain-Lab':{n:56,sha:reflexSha,title:'RB-F3A frozen action vs touch',
    doc:'docs/competence-runs/RB-F3A_RESULT.md'}
};
const browser=await chromium.launch({headless:true,executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',args:['--no-sandbox']});
async function setup(page){
 await page.goto('file://'+source,{waitUntil:'load'});
 await page.locator('#enter-atelier').click();
 await page.locator('#pair-right').selectOption('reflex');
 await page.locator('#apply-pair').click();
 await page.waitForFunction(()=>document.querySelector('#left-state')?.textContent?.startsWith('ODCZYTANO')&&
   document.querySelector('#right-state')?.textContent?.startsWith('ODCZYTANO'),{timeout:30000});
}
try{
 const page=await browser.newPage({viewport:{width:1440,height:900}});
 const errors=[],calls=[];
 page.on('pageerror',error=>errors.push(String(error)));
 await page.route(base+'**',async route=>{
   const url=new URL(route.request().url()),matched=url.pathname.match(/^\/repos\/Jozzpoly\/([A-Za-z0-9-]+)\/pulls(?:\/(\d+)(?:\/(files))?)?$/);
   if(!matched)return route.fulfill({status:404,body:'outside bounded route'});
   const f=fixture[matched[1]];if(!f)return route.fulfill({status:403,body:'unauthorized project'});
   calls.push(url.pathname+url.search);
   if(!matched[2])return route.fulfill({status:200,contentType:'application/json',body:JSON.stringify([
     {number:f.n,head:{sha:f.sha},title:f.title,draft:true,updated_at:'2026-10-11T01:57:00Z'}])});
   if(Number(matched[2])!==f.n)return route.fulfill({status:404,body:'wrong pr'});
   if(!matched[3])return route.fulfill({status:200,contentType:'application/json',body:JSON.stringify({head:{sha:f.sha}})});
   return route.fulfill({status:200,contentType:'application/json',body:JSON.stringify([{filename:f.doc,status:'added'}])});
 });
 await setup(page);
 for(const [side,repo] of [['left','Combat-Lab'],['right','ReflexBrain-Lab']]){
   await page.locator('#'+side+'-frontier summary').click();
   await page.locator('#'+side+'-frontier-load').click();
   await page.locator('#'+side+'-frontier-list .frontier-item').first().waitFor({timeout:12000});
   await page.locator('#'+side+'-frontier-list .frontier-item button').first().click();
   await page.locator('#'+side+'-frontier-list .frontier-file').first().waitFor({timeout:12000});
   assert.match(await page.locator('#'+side+'-frontier-list .frontier-file').first().innerText(),new RegExp(fixture[repo].doc.split('/').at(-1)));
   await page.locator('#'+side+'-frontier-list .frontier-file').first().click();
   await page.waitForFunction(s=>document.querySelector('#'+s+'-state')?.textContent?.startsWith('ODCZYTANO'),side,{timeout:20000});
   assert.match(await page.locator('#'+side+'-name').innerText(),new RegExp('PR #'+fixture[repo].n));
   assert.ok((await page.locator('#'+side+'-link').getAttribute('href')).includes(fixture[repo].sha+'/'+fixture[repo].doc));
   await page.locator('#'+side+'-pin').click();
 }
 assert.equal(await page.locator('.clip').count(),2);
 await page.locator('#make-note').click();
 const note=await page.locator('#export-text').inputValue();
 assert.ok(note.includes(combatSha));
 assert.ok(note.includes(reflexSha));
 assert.ok(note.includes('B1_PHYSICAL_ENVELOPE'));
 assert.ok(note.includes('RB-F3A_RESULT'));
 await mkdir('/tmp/medium-world',{recursive:true});
 await page.screenshot({path:'/tmp/medium-world/frontier-controlled-receipt.png',fullPage:true});
 assert.equal(calls.length,6,'two public GitHub calls per PR selection plus one listing');
 assert.deepEqual(errors,[]);
 console.log('PASS pinned frontier route: two PR-head-verified changing-doc snapshots, source excerpts and full SHA handoff (fixture API, real raw docs)');
 await page.close();

 // Critical negative control: never open changed files from a PR that moved after listing.
 const stale=await browser.newPage({viewport:{width:1060,height:800}});
 await stale.route(base+'**',route=>{
   const url=new URL(route.request().url());
   const f=fixture['Combat-Lab'];
   if(url.pathname.endsWith('/pulls'))return route.fulfill({status:200,contentType:'application/json',body:JSON.stringify([
     {number:f.n,head:{sha:f.sha},title:f.title,draft:true,updated_at:'2026-10-11T00:00:00Z'}])});
   if(url.pathname.endsWith('/pulls/'+f.n))return route.fulfill({status:200,contentType:'application/json',body:JSON.stringify({head:{sha:'f'.repeat(40)}})});
   if(url.pathname.endsWith('/files'))return route.fulfill({status:200,contentType:'application/json',body:JSON.stringify([{filename:f.doc,status:'added'}])});
   return route.fulfill({status:403,body:'forbidden'});
 });
 await setup(stale);
 await stale.locator('#left-frontier summary').click();
 await stale.locator('#left-frontier-load').click();
 await stale.locator('#left-frontier-list .frontier-item').first().waitFor({timeout:12000});
 await stale.locator('#left-frontier-list .frontier-item button').first().click();
 await stale.waitForFunction(()=>document.querySelector('#left-frontier-list')?.textContent?.includes('HEAD PR uległ zmianie'),{timeout:12000});
 assert.equal(await stale.locator('#left-frontier-list .frontier-file').count(),0);
 assert.equal(await stale.locator('#left-name').innerText(),'Combat Lab');
 console.log('PASS moving-head negative control: refuses reinterpreting stale PR file list');
 await stale.close();

 // A network failure is neither "no work" nor an invitation to invent PRs.
 const blocked=await browser.newPage({viewport:{width:1060,height:800}});
 await blocked.route(base+'**',r=>r.fulfill({status:403,body:'rate limit'}));
 await setup(blocked);
 await blocked.locator('#left-frontier summary').click();
 await blocked.locator('#left-frontier-load').click();
 await blocked.waitForFunction(()=>document.querySelector('#left-frontier-status')?.dataset?.error==='true',{timeout:12000});
 assert.equal(await blocked.locator('#left-frontier-list .frontier-item').count(),0);
 assert.match(await blocked.locator('#left-frontier-status').innerText(),/NIEZWERYFIKOWANE.*403/);
 console.log('PASS HTTP 403 negative control: refuses false live frontier and shows native fallback');
 await blocked.close();
}finally{await browser.close();}
