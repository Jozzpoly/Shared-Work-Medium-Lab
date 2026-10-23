'use strict';
const fs=require('node:fs'),{boot}=require('./roundtrip.cjs');
const ok=(b,m)=>{if(!b)throw Error('FAIL: '+m)};
async function test(html,sourceJSON){
 const results=[],check=(name,value)=>{ok(value,name);results.push(name)};
 const base='https://htmlpreview.github.io/research-world.html';
 const frame=record=>{const hash=record?'#world='+encodeURIComponent(JSON.stringify(record)):'';
   return boot(html,false,null,{hash,href:base+hash})};
 const input=JSON.parse(sourceJSON);
 const first=frame();check('plain URL launches 12 edits',first.__mediumSignal.get().changes.length===12);
 const revised=JSON.parse(sourceJSON);revised.changes.push([2845,1]);
 let a=frame(revised);check('URL rehydrates distinct 13-edit world',a.__mediumSignal.get().changes.length===13&&
   a.document.getElementById('worldlabel').textContent.includes('ODZYSKANY'));
 await a.document.getElementById('share').onclick();
 const link=a.__copied,unpacked=JSON.parse(decodeURIComponent(link.split('#world=')[1]));
 check('share button copies the exact authored capsule',JSON.stringify(unpacked)===JSON.stringify(a.__mediumSignal.get()));
 check('share control exposes URL to copy',a.document.getElementById('sharebox').hidden===false);
 const clicked=frame(unpacked);
 check('copied link rehydrates same world',clicked.__mediumSignal.get().changes.length===13);
 a.document.getElementById('field')._listeners.pointerdown({pointerId:5,clientX:0,clientY:0,preventDefault(){}});
 check('new editing hides stale share-link field',a.document.getElementById('sharebox').hidden===true);
 const pending=JSON.parse(sourceJSON);pending.changes.push([4562,1]);pending.mediumPending={
   status:'requires-revalidation',extension:'mediumSignal',payload:pending.mediumSignal};
 delete pending.mediumSignal;
 const unsettled=frame(pending);
 check('pending capsule is not represented as active world',unsettled.__mediumSignal.status().pending&&
   unsettled.document.getElementById('worldlabel').textContent.includes('NIEPOTWIERDZONY'));
 await unsettled.document.getElementById('share').onclick();
 check('pending state survives sharing',JSON.parse(decodeURIComponent(unsettled.__copied.split('#world=')[1])).mediumPending?.status==='requires-revalidation');
 check('pending share warns owner',unsettled.document.getElementById('message').textContent.includes('wymaga ponownego wskazania'));
 const invalid=boot(html,false,null,{hash:'#world=%FFBADJSON',href:base+'#world=%FFBADJSON'});
 check('invalid link admits failure and displays only example',invalid.document.getElementById('worldlabel').textContent.includes('NIE ODTWORZONO')&&invalid.__mediumSignal.get().changes.length===12);
 const oversized=JSON.parse(sourceJSON);
 for(let y=3;y<=10;y++)for(let x=3;x<90;x++)oversized.changes.push([y*112+x,1]);
 const big=frame();big.__mediumSignal.import(oversized);await big.document.getElementById('share').onclick();
 check('unwieldy link refused and JSON alternative suggested',!big.__copied&&big.document.getElementById('message').textContent.includes('ZAPISZ JSON'));
 return {result:'PASS in event DOM mock; browser link-loading separately verified in Opera',checks:results.length,names:results};
}
module.exports={test};
if(require.main===module){
 const paths=process.argv.slice(2);
 if(paths.length!==2)throw Error('Usage: node worldlink-smoke.cjs worldlink-first-contact.html with-lens.json');
 test(...paths.map(p=>fs.readFileSync(p,'utf8'))).then(x=>console.log(JSON.stringify(x,null,2))).catch(e=>{console.error(e);process.exitCode=1});
}
