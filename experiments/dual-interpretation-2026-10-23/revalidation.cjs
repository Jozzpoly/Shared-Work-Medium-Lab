'use strict';
const fs=require('node:fs'),{boot,run}=require('./roundtrip.cjs');
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const assert=(ok,msg)=>{if(!ok)throw Error('FAIL '+msg)};
function pointer(node,type,x,y){const fn=node._listeners?.[type];assert(typeof fn==='function','missing '+type);fn({pointerId:19,clientX:(x+.5)/112*896,clientY:(y+.5)/68*544,preventDefault(){}})}
function test(hydroHtml,signalHtml,capsuleText,legacyHydroHtml,legacySignalHtml){
 const checks=[];const check=(name,ok)=>{assert(ok,name);checks.push(name)};
 const original=run(legacyHydroHtml,legacySignalHtml).evidence;
 check('original loss reproduced',original.geometryPreserved&&!original.metadataPreserved);
 const input=JSON.parse(capsuleText),h=boot(hydroHtml);
 h.__mediumPortable.apply(capsuleText);const carried=h.__mediumPortable.get();
 check('unchanged extension survives',same(carried.mediumSignal,input.mediumSignal)&&!carried.mediumPending);
 const oldReader=boot(legacySignalHtml);oldReader.__mediumSignal.import(carried);
 check('legacy signal receives retained extension',same(oldReader.__mediumSignal.get().mediumSignal.receiver,{x:82,y:40}));
 const wall=h.document.getElementById('tool-wall');assert(typeof wall._listeners?.click==='function','missing wall tool');
 wall._listeners.click({});const canvas=h.document.getElementById('world');
 pointer(canvas,'pointerdown',82,40);pointer(canvas,'pointerup',82,40);
 const changed=h.__mediumPortable.get();
 check('actual paint changes receiver cell',changed.changes.some(p=>p[0]===4562&&p[1]===1));
 check('dirty source quarantines interpretation',changed.mediumPending?.status==='requires-revalidation'&&!changed.mediumSignal&&same(changed.mediumPending.payload.receiver,{x:82,y:40}));
 const exp=h.document.getElementById('variant-export');assert(typeof exp._listeners?.click==='function','missing export event');exp._listeners.click({});
 check('UI export retains uncertain data',same(JSON.parse(h.document.getElementById('variant-json').value),changed));
 check('UI export warns',h.document.getElementById('variant-status').textContent.includes('wymagającą sprawdzenia'));
 const reopened=boot(hydroHtml);reopened.__mediumPortable.apply(JSON.stringify(changed));
 check('pending record survives reimport',same(reopened.__mediumPortable.get().mediumPending,changed.mediumPending));
 const signal=boot(signalHtml);signal.__mediumSignal.import(changed);
 check('receiving instrument pending',signal.__mediumSignal.status().pending);
 check('receiving instrument warning',signal.document.getElementById('message').textContent.includes('wymaga sprawdzenia'));
 check('not silently reauthoring',!signal.__mediumSignal.get().mediumSignal&&!!signal.__mediumSignal.get().mediumPending);
 const before=signal.__mediumSignal.get(),bad=JSON.parse(JSON.stringify(changed));bad.mediumPending.payload.receiver={x:-1,y:0};
 let refused=false;try{signal.__mediumSignal.import(bad)}catch{refused=true}
 check('malformed metadata rejected without mutation',refused&&same(before,signal.__mediumSignal.get()));
 const field=signal.document.getElementById('field');
 pointer(field,'pointerdown',62,52);pointer(field,'pointermove',82,40);pointer(field,'pointerup',82,40);
 check('blocked new position remains pending',signal.__mediumSignal.status().pending);
 pointer(field,'pointerdown',62,52);pointer(field,'pointermove',78,40);pointer(field,'pointerup',78,40);
 const revised=signal.__mediumSignal.get();
 check('direct move to open cell clears pending',!signal.__mediumSignal.status().pending&&!revised.mediumPending&&same(revised.mediumSignal?.receiver,{x:78,y:40}));
 const returnHydro=boot(hydroHtml);returnHydro.__mediumPortable.apply(JSON.stringify(revised));
 const handback=returnHydro.__mediumPortable.get();
 check('handoff returns geometry and meaning',same(handback.changes,revised.changes)&&same(handback.mediumSignal,revised.mediumSignal));
 const finalReader=boot(legacySignalHtml);finalReader.__mediumSignal.import(handback);
 check('original receiver reads repaired document',same(finalReader.__mediumSignal.get().mediumSignal.receiver,{x:78,y:40}));

 // Jaskinia v1 host handshake qualified in source-level frame simulation.
 const framed=boot(signalHtml,false,{parent:true});
 framed.__deliver({jaskinia:1,type:'hi'});
 const initial=framed.__messages.map(e=>e.message.type);
 check('Jaskinia hello/state/signals handshake',
   initial.includes('hello')&&initial.includes('state')&&initial.includes('signals'));
 check('active instrument reports connected without pending',
   framed.__messages.find(e=>e.message.type==='state')?.message.data?.connected===true&&
   framed.__messages.find(e=>e.message.type==='state')?.message.data?.needsReceiverConfirmation===false);
 framed.__mediumSignal.import(changed);
 framed.__messages.length=0;
 framed.__deliver({jaskinia:1,type:'state?'});
 const pendingMsgs=framed.__messages.map(e=>e.message.type);
 check('pending host reports state but no numeric signals',
   pendingMsgs.includes('state')&&!pendingMsgs.includes('signals'));
 check('pending host state describes uncertainty',
   framed.__messages.some(e=>e.message.type==='state'&&e.message.text.includes('wymaga ponownego')));
 check('pending metadata invalidates numeric connected field',
   framed.__messages.some(e=>e.message.type==='state'&&
     e.message.data?.connected===null&&e.message.data?.needsReceiverConfirmation===true));
 check('pending metadata emits one visible event marker',
   framed.__messages.filter(e=>e.message.type==='event').length===1&&
   framed.__messages.some(e=>e.message.type==='event'&&e.message.level==='uwaga'));
 framed.__messages.length=0;
 framed.__deliver({jaskinia:1,type:'state?'});
 check('repeated state request does not spam warning events',
   framed.__messages.length===1&&framed.__messages[0].message.type==='state');
 framed.__messages.length=0;
 framed.__deliver({jaskinia:1,type:'hi'},'https://untrusted.example');
 check('origin spoof refused',framed.__messages.length===0);
 const fp=framed.document.getElementById('field');
 pointer(fp,'pointerdown',62,52);pointer(fp,'pointermove',78,40);pointer(fp,'pointerup',78,40);
 framed.__messages.length=0;
 framed.__deliver({jaskinia:1,type:'state?'});
 check('trusted numeric reporting restored after reauthor',
   framed.__messages.some(e=>e.message.type==='signals')&&!framed.__mediumSignal.status().pending);
 check('reauthored connection status restored without uncertainty',
   framed.__messages.some(e=>e.message.type==='state'&&e.message.data?.connected===true&&
     e.message.data?.needsReceiverConfirmation===false));
 check('explicit postMessage target origin for every response',
   framed.__messages.length>0&&framed.__messages.every(e=>e.origin==='https://jozzpoly.github.io'));
 return {passed:checks.length,total:checks.length,checks,scope:'Original JS through event-capable DOM mock, NOT browser UI or Owner verdict',
  geometry:{before:input.changes.length,after:changed.changes.length},receiver:{before:input.mediumSignal.receiver,after:handback.mediumSignal.receiver}};
}
module.exports={test};
if(require.main===module){const args=process.argv.slice(2);if(args.length!==5)throw Error('Usage: node revalidation.cjs edited-hydro.html edited-signal.html with-lens.json original-hydro.html original-signal.html');console.log(JSON.stringify(test(...args.map(p=>fs.readFileSync(p,'utf8'))),null,2))}
