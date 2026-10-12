import assert from 'node:assert/strict';
import {chromium} from 'playwright';
import {mkdir} from 'node:fs/promises';
const sha=process.env.GITHUB_SHA;
assert.match(sha||'',/^[0-9a-f]{40}$/);
const url='https://htmlpreview.github.io/?https://raw.githubusercontent.com/Jozzpoly/Shared-Work-Medium-Lab/'+sha+'/experiments/real-gloop-world-portal-2026-10-12/index.html';
const browser=await chromium.launch({headless:true,executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',args:['--no-sandbox']});
try{
 const page=await browser.newPage({viewport:{width:1550,height:900}}),errors=[];
 page.on('pageerror',e=>errors.push(String(e)));
 await page.goto(url,{waitUntil:'domcontentloaded',timeout:30000});
 try{
  await page.locator('iframe.world').first().waitFor({timeout:25000});
  await page.frameLocator('#world-a').locator('#food').waitFor({timeout:25000});
  await page.frameLocator('#world-b').locator('#food').waitFor({timeout:25000});
  await page.frame({name:'gloop-a'}).waitForFunction(()=>Number(document.querySelector('#food')?.textContent)>0,{timeout:25000});
 }catch(error){
  console.log('PUBLIC_PREVIEW_UNQUALIFIED',JSON.stringify({url,title:await page.title(),body:(await page.locator('body').innerText()).slice(0,300),errors:errors.slice(0,6)}));
  throw error;
 }
 await mkdir('/tmp/medium-real-gloop',{recursive:true});
 await page.screenshot({path:'/tmp/medium-real-gloop/public-preview.png',fullPage:true});
 assert.equal(await page.locator('iframe.world').count(),2);
 assert.deepEqual(errors,[]);
 console.log('PUBLIC HTMLPREVIEW: PASS two loaded real embedded worlds; URL pinned to '+sha+'. Human/product acceptance not evaluated.');
}finally{await browser.close()}
