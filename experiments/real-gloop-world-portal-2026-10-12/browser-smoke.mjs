import assert from 'node:assert/strict';
import { chromium } from 'playwright';
import { fileURLToPath } from 'node:url';
import { readFileSync, mkdirSync } from 'node:fs';
const path=fileURLToPath(new URL('./index.html',import.meta.url));
const html=readFileSync(path,'utf8');
assert.equal((html.match(/sandbox="allow-scripts"/g)||[]).length,2);
assert.equal((html.match(/allow-same-origin/g)||[]).length,1,'boundary note only');
const content=html.match(/<script id="donor-source" type="application\/octet-stream">([A-Za-z0-9+/=]+)<\/script>/)?.[1];
assert.ok(content,'actual embedded donor source must exist');
const decoded=Buffer.from(content,'base64').toString('utf8');
assert.ok(decoded.includes('class Simulation')&&decoded.includes('sim.setSize(W,H)')&&decoded.includes('ui.burst.onclick'));
assert.ok(decoded.endsWith('</html>\n'));
const browser=await chromium.launch({headless:true,executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',args:['--no-sandbox']});
try{
 const page=await browser.newPage({viewport:{width:1660,height:980}});
 const errors=[];
 page.on('pageerror',e=>errors.push(String(e)));
 page.on('console',m=>{if(m.type()==='error')errors.push('console '+m.text())});
 await page.goto('file://'+path,{waitUntil:'load'});
 assert.equal(await page.locator('iframe.world').count(),2);
 await page.frameLocator('#world-a').locator('#world').waitFor();
 await page.frameLocator('#world-b').locator('#world').waitFor();
 const a=page.frame({name:'gloop-a'}),b=page.frame({name:'gloop-b'});
 assert.ok(a&&b,'two real child worlds must be present');
 await a.waitForFunction(()=>Number(document.querySelector('#food')?.textContent)>0);
 await b.waitForFunction(()=>Number(document.querySelector('#food')?.textContent)>0);
 const dims=()=>Promise.all([a,b].map(f=>f.evaluate(()=>({w:innerWidth,h:innerHeight,canvasW:document.querySelector('canvas').getBoundingClientRect().width,canvasH:document.querySelector('canvas').getBoundingClientRect().height,bitmapW:document.querySelector('canvas').width,bitmapH:document.querySelector('canvas').height}))));
 async function visualClick(frame, selector, id){
  const fr=await page.locator(id).boundingBox();
  const child=await frame.evaluate(sel=>{
   const target=document.querySelector(sel);
   const r=target.getBoundingClientRect();
   return {x:r.x+r.width/2,y:r.y+r.height/2,width:r.width,height:r.height};
  },selector);
  const point={x:fr.x+child.x*fr.width/1210,y:fr.y+child.y*fr.height/700};
  console.log('POINTER_MAP '+JSON.stringify({selector,id,point,frame:fr,child}));
  await page.mouse.click(point.x,point.y);
 }
 async function visualSnapshot(frame){
  return frame.evaluate(()=>{
   const c=document.querySelector('#world'),ctx=c.getContext('2d');
   const points=[[20,20],[450,350],[880,680]];
   return {style:getComputedStyle(c).backgroundColor,internal:[innerWidth,innerHeight],
    pix:points.map(([x,y])=>Array.from(ctx.getImageData(x,y,1,1).data)),
    t:document.querySelector('#age').textContent,seed:document.querySelector('#seed').textContent};
  });
 }
 console.log('CANVAS_BEFORE '+JSON.stringify({a:await visualSnapshot(a),b:await visualSnapshot(b)}));
 const first=await dims();
 mkdirSync('/tmp/medium-real-gloop',{recursive:true});
 await page.screenshot({path:'/tmp/medium-real-gloop/pre-dims.png',fullPage:true});
 assert.deepEqual(first,[{w:1210,h:700,canvasW:900,canvasH:700,bitmapW:900,bitmapH:700},{w:1210,h:700,canvasW:900,canvasH:700,bitmapW:900,bitmapH:700}]);
 mkdirSync('/tmp/medium-real-gloop',{recursive:true});
 await page.screenshot({path:'/tmp/medium-real-gloop/pre-interaction.png',fullPage:true});
 const positions={
  viewport:page.viewportSize(),
  parentA:await page.locator('#world-a').boundingBox(),
  parentB:await page.locator('#world-b').boundingBox(),
  pauseA:await a.locator('#pause').boundingBox(),
  pauseB:await b.locator('#pause').boundingBox(),
  surfaceA:await page.locator('.pane[data-which=a] .surface').boundingBox()
 };
 console.log('GEOMETRY_DEBUG '+JSON.stringify(positions));
 await visualClick(a,'#pause','#world-a');
 assert.equal(await a.locator('#pause').innerText(),'Wznów','true screen click must activate left pause');
 await visualClick(b,'#pause','#world-b');
 assert.equal(await b.locator('#pause').innerText(),'Wznów','true screen click must activate right pause');
 const beforeA=Number(await a.locator('#food').innerText()),beforeB=Number(await b.locator('#food').innerText());
 await visualClick(a,'#burst','#world-a');
 console.log('CANVAS_AFTER_ACTION '+JSON.stringify({a:await visualSnapshot(a),b:await visualSnapshot(b),
  afterFoodA:await a.locator('#food').innerText(),beforeA,beforeB}));
 await a.waitForFunction(n=>Number(document.querySelector('#food').textContent)===n+50,beforeA);
 assert.equal(Number(await b.locator('#food').innerText()),beforeB,'world B must not receive A burst');
 await page.setViewportSize({width:1120,height:900});
 await page.waitForTimeout(250);
 assert.deepEqual(await dims(),first,'presentation resize must not mutate game viewport');
 await page.locator('[data-view-control=a]').click();
 await page.waitForTimeout(180);
 assert.deepEqual(await dims(),first,'solo focus must not mutate original simulation dimensions');
 const inaccessible=await page.evaluate(()=>{try{return Boolean(document.querySelector('#world-a').contentDocument?.body)}catch{return false}});
 assert.equal(inaccessible,false,'sandbox world must be origin-isolated from parent');
 await page.locator('[data-view-control=both]').click();
 mkdirSync('/tmp/medium-real-gloop',{recursive:true});
 await page.setViewportSize({width:1660,height:980});
 await page.waitForTimeout(250);
 await page.screenshot({path:'/tmp/medium-real-gloop/two-real-worlds.png',fullPage:true});
 assert.deepEqual(errors,[],'no JS/console errors in real embedded worlds');
 console.log(JSON.stringify({result:'PASS',actualDonor:'bd8bfab5079bb1d1f596f9621d98ac522571b75a',donorBytes:Buffer.byteLength(decoded),snapshots:{first,after:await dims()},food:{worldABefore:beforeA,worldAAfter:beforeA+50,worldBBefore:beforeB,worldBAfter:Number(await b.locator('#food').innerText())},sandboxBlocked:true}));
}finally{await browser.close()}