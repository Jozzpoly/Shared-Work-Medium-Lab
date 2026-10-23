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
 return {passed:checks.length,total:checks.length,checks,scope:'Original JS through event-capable DOM mock, NOT browser UI or Owner verdict',
  geometry:{before:input.changes.length,after:changed.changes.length},receiver:{before:input.mediumSignal.receiver,after:handback.mediumSignal.receiver}};
}
module.exports={test};
if(require.main===module){const args=process.argv.slice(2);if(args.length!==5)throw Error('Usage: node revalidation.cjs edited-hydro.html edited-signal.html with-lens.json original-hydro.html original-signal.html');console.log(JSON.stringify(test(...args.map(p=>fs.readFileSync(p,'utf8'))),null,2))}
