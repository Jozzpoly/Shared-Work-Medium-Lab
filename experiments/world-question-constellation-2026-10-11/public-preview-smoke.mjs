import assert from 'node:assert/strict';
import {chromium} from 'playwright';
const url='https://htmlpreview.github.io/?https://raw.githubusercontent.com/Jozzpoly/Shared-Work-Medium-Lab/911c85af708f08c25213ac3852b291d84513b161/experiments/world-question-constellation-2026-10-11/index.html';
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
 await page.locator('button[data-lens="limits"]').click();
 const portableView=page.url();
 assert.match(portableView,/#view=perception&lens=limits/);
 await page.reload({waitUntil:'domcontentloaded'});
 await page.locator('.node').first().waitFor({timeout:18000});
 assert.equal(await page.locator('[data-view="perception"]').getAttribute('aria-pressed'),'true');
 assert.equal(await page.locator('button[data-lens="limits"]').getAttribute('aria-pressed'),'true');
 const second=await b.newPage({viewport:{width:1100,height:820}});
 await second.goto(portableView,{waitUntil:'domcontentloaded'});
 await second.locator('.node').first().waitFor({timeout:18000});
 assert.equal(await second.locator('[data-view="perception"]').getAttribute('aria-pressed'),'true');
 assert.equal(await second.locator('button[data-lens="limits"]').getAttribute('aria-pressed'),'true');
 await second.close();
 console.log('PASS PUBLIC HTMLPREVIEW: correct World, relation control, cross-page hash viewpoint survives reload and new tab');
}finally{await b.close();}
