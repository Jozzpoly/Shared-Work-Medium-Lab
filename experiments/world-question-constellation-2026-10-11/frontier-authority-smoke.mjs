import assert from 'node:assert/strict';
import {chromium} from 'playwright';
import {fileURLToPath} from 'node:url';
const html=fileURLToPath(new URL('./index.html',import.meta.url));
const sha='a'.repeat(40),gate='quality/p1-owner-readiness.json';
const b=await chromium.launch({headless:true,executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',args:['--no-sandbox']});
async function runCase(kind){
 const page=await b.newPage({viewport:{width:1280,height:900}}),calls=[];
 const file=(p,n=0)=>({filename:p,status:'added',changes:2});
 const files1=Array.from({length:100},(_,i)=>file(i<5?'docs/report'+i+'.md':'src/source'+i+'.js'));
 const files2=Array.from({length:kind==='cap'?100:97},(_,i)=>file(i===29?gate:'src/page2-'+i+'.js'));
 const files3=Array.from({length:100},(_,i)=>file('src/page3-'+i+'.js'));
 await page.route('https://raw.githubusercontent.com/**',route=>route.fulfill({status:200,contentType:'text/plain',body:route.request().url().endsWith(gate)?'{\n "status": "BLOCKED",\n "promotion_authorized": false\n}\n':'# Source fixture\nLine 2\n'}));
 await page.route('https://api.github.com/**',route=>{
  const u=new URL(route.request().url());calls.push(u.pathname+u.search);
  if(!u.pathname.includes('/FrameMatter-Lab/'))return route.fulfill({status:403,body:'other repo'});
  if(u.pathname.endsWith('/pulls'))return route.fulfill({status:200,contentType:'application/json',body:JSON.stringify([{number:1,title:'FrameMatter P1',head:{sha},updated_at:'2026-10-12T02:00:00Z'}])});
  if(u.pathname.endsWith('/pulls/1'))return route.fulfill({status:200,contentType:'application/json',body:JSON.stringify({head:{sha:kind==='moved'?'f'.repeat(40):sha}})});
  if(u.pathname.endsWith('/files')){
   const p=Number(u.searchParams.get('page'));
   if(kind==='denied'&&p===2)return route.fulfill({status:403,body:'rate limit'});
   return route.fulfill({status:200,contentType:'application/json',body:JSON.stringify(p===1?files1:p===2?files2:kind==='cap'?files3:[])});
  }
  return route.fulfill({status:404,body:'unexpected'});
 });
 try{
  await page.goto('file://'+html);
  await page.locator('#enter-atelier').click();
  await page.locator('#pair-left').selectOption('matter');
  await page.locator('#pair-right').selectOption('reflex');
  await page.locator('#apply-pair').click();
  assert.match(await page.locator('#pair-feedback').innerText(),/Własne zestawienie/);
  await page.locator('#left-frontier summary').click();
  await page.locator('#left-frontier-load').click();
  try{await page.locator('#left-frontier-list .frontier-item').first().waitFor({timeout:10000});}
  catch(error){
   await page.screenshot({path:'/tmp/world-frontier-authority-first-fail.png',fullPage:true});
   throw new Error('PR card absent: '+JSON.stringify({
    case:kind,
    requests:calls,
    selected:await page.locator('#pair-left').inputValue(),
    reader:await page.locator('#left-name').innerText(),
    frontier:await page.locator('#left-frontier-status').innerText(),
    list:await page.locator('#left-frontier-list').innerText()
   })+'; '+error.message);
  }
  await page.locator('#left-frontier-list .frontier-item button').first().click();
  await page.waitForFunction(()=>document.querySelector('#left-frontier-list .frontier-files')?.textContent?.includes('PR #1')||
    document.querySelector('#left-frontier-list .frontier-files')?.textContent?.includes('NIEZWERYFIKOWANE'));
  const area=page.locator('#left-frontier-list .frontier-files');
  if(kind==='denied'){assert.match(await area.innerText(),/NIEZWERYFIKOWANE.*403/);assert.equal(await area.locator('.frontier-file').count(),0);}
  else if(kind==='moved'){assert.match(await area.innerText(),/HEAD PR uległ zmianie/);assert.equal(await area.locator('.frontier-file').count(),0);}
  else{
   assert.match(await area.innerText(),kind==='cap'?/NIEPEŁNE: limit 300/:/197 plików \/ 2 stron/);
   await area.locator('input[type=search]').fill('readiness');
   assert.equal(await area.locator('.frontier-file').count(),1);
   assert.match(await area.locator('.frontier-file').innerText(),/quality\/p1-owner-readiness\.json/);
   await area.locator('.frontier-file').click();
   await page.waitForFunction(()=>document.querySelector('#left-state')?.textContent?.startsWith('ODCZYTANO'));
   assert.match(await page.locator('#left-excerpt').innerText(),/BLOCKED/);
   assert.match(await page.locator('#left-link').getAttribute('href'),/quality\/p1-owner-readiness\.json/);
   if(kind==='cap')assert.match(await area.innerText(),/niepełne pokrycie/);
  }
  assert.ok(calls.some(c=>c.includes('files?per_page=100&page=2')));
  assert.ok(calls.every(c=>!c.includes('page=4')));
  console.log('PASS '+kind+' '+calls.length+' GitHub fixture calls');
 }finally{await page.close();}
}
try{for(const c of ['normal','moved','denied','cap'])await runCase(c);}finally{await b.close();}
