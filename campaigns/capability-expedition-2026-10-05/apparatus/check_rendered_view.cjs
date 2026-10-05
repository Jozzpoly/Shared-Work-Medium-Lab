const fs = require('fs');
const crypto = require('crypto');
const path = require('path');
const { chromium } = require('playwright');
const root = path.resolve(process.argv[2] || path.join(__dirname, '..'));
const base=new URL(process.argv[3] || 'http://127.0.0.1:8793/').href;
const output=process.argv[5];
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
(async()=>{
  const manifest=JSON.parse(fs.readFileSync(path.join(root,'site/manifest.json'),'utf8'));
  const object=manifest.objects[0];
  const exactCopies=[];
  for(const [source,projected] of [
    ['packages/browser-piece/object.json',object.raw_object],
    ['packages/browser-piece/workpiece.md',object.body.relative],
    ['packages/browser-piece/public-comment-capture.json',object.provenance[0].href],
    ...manifest.records.map(r=>['packages/'+(r.relative==='record.json'?'browser-follow-up':r.relative==='consumer-result.json'?'procedural-consumer':'codex-observation')+'/'+r.relative,r.raw_href]),
    ['packages/codex-observation/medium.refs.json',manifest.records.find(r=>r.relative==='check-result.json').refs_href],
    ['packages/browser-follow-up/medium.refs.json',manifest.records.find(r=>r.relative==='record.json').refs_href],
    ['packages/procedural-consumer/medium.refs.json',manifest.records.find(r=>r.relative==='consumer-result.json').refs_href],
  ]){
    const a=fs.readFileSync(path.join(root,source)), b=fs.readFileSync(path.join(root,'site',projected));
    exactCopies.push({source,projected,sha256:hash(a),bytes:a.length,exact:a.equals(b)});
  }
  const browser=await chromium.launch({executablePath:process.argv[4] || undefined,headless:true});
  const health={console_errors:[],page_errors:[],failed_requests:[]};
  const page=await browser.newPage({viewport:{width:1280,height:900}});
  page.on('console',m=>{if(m.type()==='error')health.console_errors.push(m.text());});
  page.on('pageerror',e=>health.page_errors.push(String(e)));
  page.on('requestfailed',r=>health.failed_requests.push({url:r.url(),failure:r.failure()}));
  await page.goto(base,{waitUntil:'networkidle'});
  const entryTitle=await page.locator('h1').innerText();
  await page.getByRole('link',{name:'Wejdź',exact:true}).click();
  const objectTitle=await page.locator('h1').innerText();
  const sourceLabels=await page.locator('h2').allTextContents();
  await page.locator('summary').filter({hasText:'Podgląd pasywnej treści'}).click();
  const bodyText=await page.locator('pre').first().innerText();
  const bodyVisible=await page.locator('pre').first().isVisible();
  const recordCards=await page.locator('article.note').count();
  if(output)await page.screenshot({path:path.join(output,'medium-capability-workpiece-2026-10-05.png'),fullPage:true});
  const links=await page.locator('a').evaluateAll(a=>a.map(x=>x.href));
  const localChecks=[];
  for(const url of [...new Set(links)].filter(x=>x.startsWith(base))){
    const response=await page.request.get(url);
    localChecks.push({url,status:response.status(),bytes:(await response.body()).length});
  }
  await page.getByRole('link',{name:'Dane techniczne / surowe',exact:true}).click();
  const technicalTitle=await page.locator('h1').innerText();
  const rawHref=await page.getByRole('link',{name:'Exact object.json',exact:true}).getAttribute('href');
  const rawResponse=await page.request.get(new URL(rawHref,base).href);
  const rawObjectBytes=await rawResponse.body();
  const rawObjectMatches=rawObjectBytes.equals(fs.readFileSync(path.join(root,'packages/browser-piece/object.json')));
  const mobile=await browser.newPage({viewport:{width:390,height:844}});
  await mobile.goto(base+object.owner_page,{waitUntil:'networkidle'});
  await mobile.locator('summary').filter({hasText:'Szczegóły i oryginał'}).click();
  const mobileLayout=await mobile.evaluate(()=>({innerWidth,scrollWidth:document.documentElement.scrollWidth,overflow:document.documentElement.scrollWidth>innerWidth}));
  if(output)await mobile.screenshot({path:path.join(output,'medium-capability-workpiece-mobile-2026-10-05.png'),fullPage:true});
  const noJS=await browser.newContext({javaScriptEnabled:false,viewport:{width:1280,height:900}});
  const noJSPage=await noJS.newPage();
  await noJSPage.goto(base+object.owner_page);
  const noJSTitle=await noJSPage.locator('h1').innerText();
  const noJSRecordCards=await noJSPage.locator('article.note').count();
  await browser.close();
  const checksPass=exactCopies.every(x=>x.exact)&&localChecks.every(x=>x.status===200)&&rawObjectMatches&&bodyVisible&&recordCards===6&&noJSRecordCards===6&&!mobileLayout.overflow&&Object.values(health).every(a=>a.length===0);
  const result={scope:'Existing unmodified Open Substrate adapter applied to new campaign data',donor_manifest_campaign:manifest.campaign,actual_campaign:'capability-expedition-2026-10-05',entryTitle,objectTitle,technicalTitle,sourceLabels,bodyVisible,bodyContainsBrowserHeading:bodyText.includes('Browser workpiece 01'),recordCards,exactCopies,localChecks,rawObjectMatches,mobileLayout,noJSTitle,noJSRecordCards,health,checksPass,boundaries:['Local preview, not public deployment','Unmodified adapter retains its own older campaign label','No causal or ecological adoption claim']};
  fs.writeFileSync(path.join(root,'evidence/relay-verification.json'),JSON.stringify(result,null,2)+'\n');
  console.log(JSON.stringify({checksPass,recordCards,exactCopyCount:exactCopies.length,mobileLayout,health,failedLocalLinks:localChecks.filter(x=>x.status!==200)},null,2));
  if(!checksPass)process.exitCode=1;
})().catch(e=>{console.error(e);process.exitCode=1;});
