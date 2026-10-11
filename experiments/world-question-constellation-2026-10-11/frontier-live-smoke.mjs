import assert from 'node:assert/strict';
import {chromium} from 'playwright';
const base='https://htmlpreview.github.io/?https://raw.githubusercontent.com/Jozzpoly/Shared-Work-Medium-Lab/17f660376e8bee97e83d999f7561ea77931e0b7e/'+
  'experiments/world-question-constellation-2026-10-11/index.html';
const b=await chromium.launch({headless:true,executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',args:['--no-sandbox']});
const result={test:'swm-real-public-frontier-v0',chrome_public_url:base,qualified:false,sides:[],failure:null};
try{
 const page=await b.newPage({viewport:{width:1440,height:920}});
 const errs=[];
 page.on('pageerror',e=>errs.push(e.message));
 const api=[];
 page.on('response',r=>{if(r.url().startsWith('https://api.github.com/repos/Jozzpoly/'))api.push({url:r.url(),status:r.status()});});
 await page.goto(base,{waitUntil:'domcontentloaded',timeout:30000});
 await page.locator('.node').first().waitFor({timeout:20000});
 await page.locator('#enter-atelier').click();
 await page.locator('#pair-right').selectOption('reflex');
 await page.locator('#apply-pair').click();
 await page.waitForFunction(()=>document.querySelector('#left-state')?.textContent?.startsWith('ODCZYTANO')&&
  document.querySelector('#right-state')?.textContent?.startsWith('ODCZYTANO'),{timeout:25000});
 for(const [side,number,doc] of [['left',10,'B1_PHYSICAL_ENVELOPE'],['right',56,'RB-F3A_RESULT']]){
  await page.locator('#'+side+'-frontier summary').click();
  await page.locator('#'+side+'-frontier-load').click();
  await page.waitForFunction(s=>/Odczyt |NIEZWERYFIKOWANE/.test(document.getElementById(s+'-frontier-status')?.textContent||''),
    side,{timeout:15000});
  const status=await page.locator('#'+side+'-frontier-status').innerText();
  if(status.includes('NIEZWERYFIKOWANE'))throw Error(side+' GET public frontier failed: '+status);
  const pr=page.locator('#'+side+'-frontier-list .frontier-item').filter({hasText:'#'+number+' '}).first();
  if(await pr.count()!==1)throw Error('Current PR #'+number+' not in sampled open subset');
  await pr.getByRole('button',{name:'Sprawdź dokumenty tego PR'}).click();
  const source=pr.locator('.frontier-file').filter({hasText:doc}).first();
  await source.waitFor({timeout:15000});
  await source.click();
  await page.waitForFunction(s=>document.getElementById(s+'-state')?.textContent?.startsWith('ODCZYTANO'),side,{timeout:25000});
  await page.locator('#'+side+'-pin').click();
  result.sides.push({side,number,source:await page.locator('#'+side+'-link').getAttribute('href'),status});
 }
 await page.locator('#make-note').click();
 const note=await page.locator('#export-text').inputValue();
 assert.equal(await page.locator('.clip').count(),2);
 assert.match(note,/B1_PHYSICAL_ENVELOPE/);
 assert.match(note,/RB-F3A_RESULT/);
 assert.equal(api.length,6);
 assert.ok(api.every(x=>x.status===200));
 assert.deepEqual(errs,[]);
 result.qualified=true;result.api=api.map(a=>({status:a.status,path:new URL(a.url).pathname}));
 console.log('PASS live public GitHub PR frontier → exact B1/F3A source receipts');
}catch(e){result.failure=String(e.message||e);}
finally{
 console.log(JSON.stringify(result,null,2));
 await b.close();
 if(!result.qualified)process.exitCode=1;
}
