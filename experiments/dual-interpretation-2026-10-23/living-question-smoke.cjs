'use strict';
// Agent -> readonly question -> SAME live lab; original ŚLAD source + actual observer JS.
// Source-JS proof only: the real Opera nested-Jaskinia attempt stopped on occupied storage.
const fs=require('node:fs');
const {boot}=require('./roundtrip.cjs');
const eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
function insist(value,label){if(!value)throw Error('FAIL '+label)}
function soleScript(html){const m=[...html.matchAll(/<script[^>]*>([\s\S]*?)<\/script>/g)];insist(m.length===1,'exactly one inline script');return m[0][1]}
function run(labHtml,wrapperHtml,seed){
 const ok=[],check=(name,yes)=>{insist(yes,name);ok.push(name)};
 const wrapperJS=soleScript(wrapperHtml);
 // Honest assumption in this replay: no BroadcastChannel across a cross-site ancestor.
 function instance(extraIndex){
  const cells=new Map(),windowEvents={},docEvents={},timers=[];
  const get=id=>{if(!cells.has(id))cells.set(id,{id,textContent:'',value:'',addEventListener(type,fn){this.actions||={};this.actions[type]=fn}});return cells.get(id)};
  const document={getElementById:get,addEventListener(type,fn){docEvents[type]=fn}};
  const window={addEventListener(type,fn){windowEvents[type]=fn}};
  const location={origin:'https://raw.githack.com',hash:'#ask=3,3'};
  // Use exactly the page's JS; DOM is a thin controlled harness.
  new Function('window','document','location','BroadcastChannel','setTimeout',wrapperJS)(
   window,document,location,undefined,fn=>timers.push(fn));
  docEvents.DOMContentLoaded();
  let lab=null;
  const topMessages=[],requests=[];
  const top={postMessage(message,origin){
   topMessages.push({message,origin});
   if(windowEvents.message)windowEvents.message({data:message,origin,source:lab});
  }};
  const capsule=JSON.parse(JSON.stringify(seed));capsule.changes.push([extraIndex,1]);
  const view={hash:'#world='+encodeURIComponent(JSON.stringify(capsule)),href:'https://raw.githack.com/readonly-lab#world='+encodeURIComponent(JSON.stringify(capsule))};
  lab=boot(labHtml,false,{parent:true,top},view);
  lab.postMessage=(message,origin)=>{requests.push({message,origin});lab.__deliverTop(message,origin)};
  return {lab,windowEvents,document,location,get,timers,topMessages,requests};
 }
 const A=instance(339);
 check('before Jaskinia handshake observer has no material answer',A.get('result').textContent.includes('Pytanie')&&A.topMessages.length===0);
 A.lab.__deliver({jaskinia:1,type:'hi'},'https://attacker.invalid');
 check('fake host origin does not initialize material observation',A.topMessages.length===0&&A.lab.__messages.length===0);
 A.lab.__deliver({jaskinia:1,type:'hi'},'https://rawcdn.githack.com');
 const first=A.get('result').textContent,details=A.get('detail').textContent;
 check('actual host handshake makes read-only answer available',first.includes('(3,3): ŚCIANA'));
 check('native Jaskinia contract hello state signals unchanged',
   eq(A.lab.__messages.map(e=>e.message.type),['hello','state','signals']));
 const before=JSON.stringify(A.lab.__mediumSignal.get());
 A.location.hash='#ask=20,30';A.windowEvents.hashchange();
 const second=A.get('result').textContent,details2=A.get('detail').textContent;
 check('same live world answers second agent question',second.includes('(20,30): WOLNE'));
 const stamp=s=>(s.match(/runtime (\S+)/)||[])[1];
 check('same iframe runtime answered both changes of URL fragment',stamp(details)===stamp(details2)&&!!stamp(details));
 check('both answers identify same authored version',details.includes('świat de')&&details.match(/świat (\w+)/)?.[1]===details2.match(/świat (\w+)/)?.[1]);
 check('queries never mutate world or source',before===JSON.stringify(A.lab.__mediumSignal.get()));
 const beforeMessages=A.topMessages.length;
 A.lab.__deliverTop({tag:'medium-public-inspect-v1',kind:'set-cell',id:'evil',x:3,y:3,value:0});
 check('write-like command rejected',A.topMessages.length===beforeMessages&&before===JSON.stringify(A.lab.__mediumSignal.get()));
 A.lab.__deliverTop({tag:'medium-public-inspect-v1',kind:'ask-cell',id:'evil',x:3,y:3},'https://attacker.invalid');
 check('wrong origin query ignored',A.topMessages.length===beforeMessages);
 A.lab.__deliverTop({tag:'medium-public-inspect-v1',kind:'ask-cell',id:'evil',x:-1,y:3});
 check('out-of-range coordinates refused',A.topMessages.length===beforeMessages);
 A.location.hash='#ask=111,3';A.windowEvents.hashchange();
 check('invalid user-side coordinate yields explicit refusal',A.get('result').textContent.includes('Niepoprawna komórka'));
 // New world B with identical telemetry. Separate controlled top-level wrapper instance.
 const B=instance(3380);
 B.lab.__deliver({jaskinia:1,type:'hi'},'https://rawcdn.githack.com');
 check('different world B answers FREE at the same coordinate',B.get('result').textContent.includes('(3,3): WOLNE'));
 check('A/B have byte-equal original host telemetry',
  eq(A.lab.__messages.map(x=>x.message),B.lab.__messages.map(x=>x.message)));
 check('read-only response references lab-owned live material not copied full grid',
  A.topMessages.some(x=>x.message.kind==='cell-answer'&&x.message.x===3&&x.message.blocked===true)&&
  B.topMessages.some(x=>x.message.kind==='cell-answer'&&x.message.x===3&&x.message.blocked===false)&&
  !A.topMessages.some(x=>Object.keys(x.message).includes('changesMap')));
 // The extra read-only capability must not reintroduce the old false 'connected' claim when pending.
 const pending=JSON.parse(JSON.stringify(seed));
 pending.changes.push([4562,1]);
 pending.mediumPending={status:'requires-revalidation',extension:'mediumSignal',payload:pending.mediumSignal};
 delete pending.mediumSignal;
 const pendingLab=boot(labHtml,false,{parent:true});
 pendingLab.__mediumSignal.import(JSON.stringify(pending));
 pendingLab.__deliver({jaskinia:1,type:'hi'},'https://rawcdn.githack.com');
 const pendingMessages=pendingLab.__messages.map(x=>x.message);
 check('pending receiver reports explicit uncertainty with no live numeric signals',
  pendingMessages.some(x=>x.type==='state'&&x.data.connected===null&&x.data.needsReceiverConfirmation===true)&&
  pendingMessages.some(x=>x.type==='event')&&!pendingMessages.some(x=>x.type==='signals'));
 pendingLab.__messages.length=0;
 pendingLab.__deliver({jaskinia:1,type:'state?'},'https://rawcdn.githack.com');
 check('repeated pending report does not spam an event',pendingLab.__messages.every(x=>x.message.type==='state'));
 check('fully syntactic observer and instrument scripts',!!new Function(wrapperJS)&&!!new Function(soleScript(labHtml)));
 return {passed:ok.length,checks:ok,evidence:{Afirst:first,Asecond:second,Bfirst:B.get('result').textContent,
  originalHostPackets:A.lab.__messages.map(x=>x.message.type),Areadonly:true,noBroadcastChannel:true,
  sameRuntime:stamp(details)===stamp(details2)},
  limit:'Original lab and observer JS under stubbed frames; genuine nested Opera execution blocked by preexisting Jaskinia browser storage. No Owner experience or live-browser PASS.'};
}
module.exports={run};
if(require.main===module){
 const files=process.argv.slice(2);
 if(files.length!==3)throw Error('Usage: node living-question-smoke.cjs slad-live-read-probe-only.html living-jaskinia-question-window.html with-lens.json');
 const a=files.map(f=>fs.readFileSync(f,'utf8'));
 console.log(JSON.stringify(run(a[0],a[1],JSON.parse(a[2])),null,2));
}
