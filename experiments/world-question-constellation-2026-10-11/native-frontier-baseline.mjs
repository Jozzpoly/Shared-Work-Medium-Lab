import assert from 'node:assert/strict';

// Direct-native public HTTP baseline for the SAME known B1 x F3A source task.
// No browser UI, secret or auth: this measures request fan-out only.
const targets=[
 {repo:'Combat-Lab',number:10,document:'docs/B1_PHYSICAL_ENVELOPE_DUAL_AFFORDANCE_2026-10-10.md',word:'physical envelope'},
 {repo:'ReflexBrain-Lab',number:56,document:'docs/competence-runs/RB-F3A_RESULT.md',word:'actor-private'}
];
const record={mode:'DIRECT_PUBLIC_GITHUB',requests:[],receipts:[],qualified:false};
async function read(url){
 const res=await fetch(url,{headers:{Accept:'application/vnd.github+json'},cache:'no-store'});
 record.requests.push({host:new URL(url).host,status:res.status,pathname:new URL(url).pathname});
 if(!res.ok)throw Error(new URL(url).pathname+' HTTP '+res.status);
 return res;
}
try{
 for(const target of targets){
  const stem='https://api.github.com/repos/Jozzpoly/'+target.repo+'/pulls';
  const listing=await(await read(stem+'?state=open&per_page=15')).json();
  assert.ok(Array.isArray(listing)&&listing.some(x=>x.number===target.number),'PR absent from bounded native list');
  const live=await(await read(stem+'/'+target.number)).json();
  assert.match(live.head.sha,/^[a-f0-9]{40}$/);
  const files=await(await read(stem+'/'+target.number+'/files?per_page=100')).json();
  assert.ok(files.some(f=>f.filename===target.document&&f.status!=='removed'),'document not in PR change list');
  const source='https://raw.githubusercontent.com/Jozzpoly/'+target.repo+'/'+live.head.sha+'/'+target.document;
  const text=await(await read(source)).text();
  assert.ok(text.toLowerCase().includes(target.word.toLowerCase()),'source text mismatch');
  record.receipts.push({repo:target.repo,pr:target.number,sha:live.head.sha,lines:text.replace(/\r\n?/g,'\n').split('\n').length});
 }
 const api=record.requests.filter(x=>x.host==='api.github.com');
 const docs=record.requests.filter(x=>x.host==='raw.githubusercontent.com');
 assert.equal(api.length,6);assert.equal(docs.length,2);assert.equal(record.requests.length,8);
 record.qualified=true;
 record.request_accounting={public_github_api_reads:api.length,public_markdown_reads:docs.length,total_observed_requests:record.requests.length};
 console.log('NETWORK_ACCOUNTING_DIRECT',JSON.stringify(record.request_accounting));
 console.log('PASS exact-native public B1 and F3A source receipts');
}catch(error){record.failure=String(error.message||error);}
finally{console.log(JSON.stringify(record,null,2));if(!record.qualified)process.exitCode=1;}
