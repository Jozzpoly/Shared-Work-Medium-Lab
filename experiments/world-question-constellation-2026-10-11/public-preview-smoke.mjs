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
 console.log('PASS PUBLIC HTMLPREVIEW: displayed correct Medium World and working relation controls');
}finally{await b.close();}
