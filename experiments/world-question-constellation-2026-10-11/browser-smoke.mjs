import assert from 'node:assert/strict';
import {chromium} from 'playwright';
import {fileURLToPath} from 'node:url';
import {mkdir} from 'node:fs/promises';
const source=fileURLToPath(new URL('./index.html',import.meta.url));
const browser=await chromium.launch({headless:true,executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',args:['--no-sandbox']});
try{
  for(const viewport of [{width:1440,height:900},{width:390,height:844}]){
    const page=await browser.newPage({viewport});
    const failures=[],outgoing=[];
    page.on('pageerror',e=>failures.push(String(e)));
    page.on('request',r=>{if(!r.url().startsWith('file:'))outgoing.push(r.url());});
    await page.goto('file://'+source,{waitUntil:'load'});
    assert.match(await page.locator('#name').innerText(),/Combat Lab/);
    assert.equal(await page.locator('.node').count(),5);
    assert.equal(await page.locator('.seam').count(),5);
    await page.locator('[data-view="material"]').click();
    assert.match(await page.locator('#name').innerText(),/fizycznych/i);
    assert.equal(await page.locator('#source-links a').count(),2);
    assert.match(page.url(),/view=material/);
    await page.locator('button[data-lens="limits"]').click();
    assert.match(page.url(),/lens=limits/);
    assert.match(await page.locator('#detail').innerText(),/nie ma|nie udowodniono|nie jest/i);
    await page.reload();
    assert.equal(await page.locator('[data-view="material"]').getAttribute('aria-pressed'),'true');
    assert.equal(await page.locator('button[data-lens="limits"]').getAttribute('aria-pressed'),'true');
    await page.locator('[data-view="reflex"]').click();
    assert.match(await page.locator('#source-links a').last().getAttribute('href'),/research\/pre-o0-foundations-campaign/);
    assert.equal(await page.locator('.node[aria-pressed="true"]').count(),1);
    const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1);
    assert.equal(overflow,false,viewport.width+'px horizontal overflow');
    assert.deepEqual(failures,[]);assert.deepEqual(outgoing,[]);
    await mkdir('/tmp/medium-world',{recursive:true});
    await page.screenshot({path:'/tmp/medium-world/'+viewport.width+'.png',fullPage:true});
    console.log('PASS real browser '+viewport.width+'px: navigation, relation, provenance, restored viewpoint, no overflow/no external calls');
    await page.close();
  }
} finally {await browser.close();}
