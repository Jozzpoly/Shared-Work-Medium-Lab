// Reproducible browser-native donor physics experiment. Neither donor edited.
import assert from 'node:assert/strict';
import {mkdir,writeFile} from 'node:fs/promises';
import {resolve} from 'node:path';
import {createHash} from 'node:crypto';
import {createServer} from 'vite';
import {chromium} from 'playwright';
const SHA='24bd930fb1bb83425ea43168660a9c9c75d5b7d6';
await mkdir('.swm-donor-fixture/src',{recursive:true});
const provenance=[];
for(const file of ['m0-world.js','b1-world.js']){
 const url='https://raw.githubusercontent.com/Jozzpoly/Combat-Lab/'+SHA+'/src/'+file;
 const r=await fetch(url);
 assert.equal(r.status,200,'donor read');
 const source=await r.text();
 assert.ok(source.includes('@dimforge/rapier2d-deterministic'));
 await writeFile('.swm-donor-fixture/src/'+file,source);
 provenance.push({file,sourceSha:SHA,sha256:createHash('sha256').update(source).digest('hex'),bytes:source.length});
}
await writeFile('.swm-donor-fixture/index.html',
 '<!doctype html><html><head><meta charset="utf-8"></head><body><main id="state">Physical test loading</main>'+
 '<script type="module" src="/experiments/world-question-constellation-2026-10-11/contact-adapter-browser-entry.js"></script></body></html>');
const server=await createServer({configFile:false,root:process.cwd(),server:{host:'127.0.0.1',port:0,strictPort:false},
  optimizeDeps:{include:['@dimforge/rapier2d-deterministic']}});
await server.listen();
const addr=server.httpServer.address(),origin='http://127.0.0.1:'+addr.port;
const browser=await chromium.launch({headless:true,executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',args:['--no-sandbox']});
let report={success:false,source:SHA,provenance};
try{
 const page=await browser.newPage();
 const errors=[];
 page.on('pageerror',e=>errors.push(String(e)));
 page.on('console',m=>{if(m.type()==='error')errors.push('console:'+m.text().slice(0,280))});
 await page.goto(origin+'/.swm-donor-fixture/index.html',{waitUntil:'load',timeout:35000});
 await page.waitForFunction(()=>Boolean(window.__swmPhysics),{timeout:30000});
 const result=await page.evaluate(()=>window.__swmPhysics);
 report={...result,provenance,pageErrors:errors};
 if(!result.success)throw Error(result.error);
 assert.ok(result.control,'no-obstacle free-control has external contact');
 assert.ok(result.results.every(x=>x.nonfinite===0),'finite impulses');
 console.log('SWM_PHYSICS_BROWSER',JSON.stringify({
  success:result.success,control:result.control,verified:result.verified,source:SHA,
  cases:result.results.map(x=>({name:x.name,frames:x.frames,maxExternal:x.max,internal:x.internal})),
  provenance,pageErrors:errors
 }));
 if(errors.length)throw Error('browser console / module errors: '+errors.join(', '));
}catch(e){report.failure=String(e.message||e);console.log('PHYSICS_BROWSER_UNQUALIFIED',report.failure);process.exitCode=1;}
finally{
 await writeFile('/tmp/swm-physics-contact-result.json',JSON.stringify(report,null,2));
 await browser.close();await server.close();
}
