import assert from 'node:assert/strict';
import {chromium} from 'playwright';
const url='https://htmlpreview.github.io/?https://raw.githubusercontent.com/Jozzpoly/Shared-Work-Medium-Lab/ef95019e4b13ab025bee9e6fef7c45b264e14dbc/experiments/world-question-constellation-2026-10-11/index.html';
const b=await chromium.launch({headless:true,executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',args:['--no-sandbox']});
try{
 const page=await b.newPage({viewport:{width:1280,height:900}});
 const errs=[];page.on('pageerror',e=>errs.push(e.message));
 await page.goto(url,{waitUntil:'domcontentloaded',timeout:30000});
 try{await page.locator('.node').first().waitFor({timeout:18000});}
 catch(e){
   console.log('PUBLIC_PREVIEW_NOT_QUALIFIED',JSON.stringify({
     title:await page.title(),url:page.url(),body:(await page.locator('body').innerText()).slice(0,350),errors:errs.slice(0,5)
   }));
   throw e;
 }
 assert.equal(await page.locator('.node').count(),5);
 await page.locator('[data-view="perception"]').click();
 assert.match(await page.locator('#name').innerText(),/ograniczonego|przez mieszkańca|aktora|Percepcja/i);
 assert.equal(await page.locator('#source-links a').count(),2);
 await page.locator('#enter-atelier').click();
 await page.waitForFunction(()=>document.querySelector('#left-state')?.textContent?.startsWith('ODCZYTANO')&&document.querySelector('#right-state')?.textContent?.startsWith('ODCZYTANO'),{timeout:25000});
 assert.ok(await page.locator('#left-results button').count()>0);
 assert.ok(await page.locator('#right-results button').count()>0);
 await page.locator('#left-pin').click();
 await page.locator('#right-pin').click();
 await page.locator('#make-note').click();
 assert.equal(await page.locator('.clip').count(),2);
 assert.match(await page.locator('#export-text').inputValue(),/Jozzpoly\/ReflexBrain-Lab\/blob/);
 await page.locator('#leave-atelier').click();
 await page.locator('button[data-lens="limits"]').click();
 assert.equal(await page.locator('button[data-lens="limits"]').getAttribute('aria-pressed'),'true');
 // HTMLPreview injects the app into its own context: the browser's outer URL
 // remains unchanged and therefore cannot carry this perspective to another reader.
 assert.equal(page.url(),url);
 console.log('PUBLIC PREVIEW LIMIT VERIFIED: lens works but outer URL is unchanged; no shareable viewpoint contract');
 console.log('PASS PUBLIC HTMLPREVIEW: World, two actual source reads and evidence export; outer URL nonportable as documented');
}finally{await b.close();}
