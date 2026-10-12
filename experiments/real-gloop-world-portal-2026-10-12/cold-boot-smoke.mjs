import assert from 'node:assert/strict';
import {chromium} from 'playwright';
import {fileURLToPath} from 'node:url';
const source=fileURLToPath(new URL('./index.html',import.meta.url));
const browser=await chromium.launch({headless:true,executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',args:['--no-sandbox']});
try{
 for(let i=0;i<16;i++){
  const page=await browser.newPage({viewport:{width:1660,height:980},deviceScaleFactor:1});
  try{
   await page.goto('file://'+source,{waitUntil:'domcontentloaded'});
   for(const id of ['world-a','world-b']){
    const frame=page.frameLocator('#'+id);
    await frame.locator('#food').waitFor({timeout:8000});
    const dims=await frame.locator('#world').evaluate(c=>({w:c.width,h:c.height,rectW:c.getBoundingClientRect().width,rectH:c.getBoundingClientRect().height}));
    assert.deepEqual(dims,{w:900,h:700,rectW:900,rectH:700},'cold start '+i+' '+id+' cannot paint a 1×1 stretched canvas');
   }
  }finally{await page.close();}
 }
 console.log('PASS 16 independent cold-start page loads / 32 native canvases with exact bitmap dimensions');
}finally{await browser.close()}
