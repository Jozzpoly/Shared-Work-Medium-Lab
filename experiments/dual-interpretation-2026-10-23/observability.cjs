'use strict';
// Exact original source JS through the same DOM/message harness; no browser/Owner interaction.
// Illustrates that two distinct material worlds can have identical public Jaskinia telemetry.
const fs=require('node:fs');
const {boot}=require('./roundtrip.cjs');
const clone=x=>JSON.parse(JSON.stringify(x));
const eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
function insist(ok,why){if(!ok)throw Error('FAIL: '+why)}
function observe(source,v){
 const app=boot(source,false,{parent:true});
 app.__mediumSignal.import(JSON.stringify(v));
 app.__deliver({jaskinia:1,type:'hi'});
 return {
  authored:app.__mediumSignal.get(),
  local:app.__mediumSignal.status(),
  packets:app.__messages.map(x=>x.message).filter(x=>['hello','state','signals','event'].includes(x.type)),
  occupancy:{at3_3:app.__mediumSignal.sample(3,3),at20_30:app.__mediumSignal.sample(20,30)}
 };
}
function run(source,fixture){
 const x=clone(fixture);
 insist(x.schema==='medium.przesmyk.variant.v1'&&x.changes.length===12,'fixture source and 12 changes');
 const make=(index,value)=>{const v=clone(x);v.changes.push([index,value]);return v};
 // Two locally different material obstructions, neither changes the currently measured route.
 const a=observe(source,make(3+3*112,1));
 const b=observe(source,make(20+30*112,1));
 insist(a.authored.changes.length===13&&b.authored.changes.length===13,'13 edits in each variant');
 insist(!eq(a.authored.changes,b.authored.changes),'different authored grid changes');
 insist(eq(a.occupancy,{at3_3:1,at20_30:0}),'A block/collision independent reality');
 insist(eq(b.occupancy,{at3_3:0,at20_30:1}),'B block/collision independent reality');
 insist(eq(a.packets,b.packets),'host receives byte-equal telemetry objects');
 insist(a.packets.length===3&&a.packets.map(p=>p.type).join(',')==='hello,state,signals','3 complete host packets');
 insist(a.local.reach&&b.local.reach&&a.local.travel===b.local.travel&&a.local.pathLength===b.local.pathLength,'local travel and path length match too');
 insist(a.packets.find(p=>p.type==='signals')?.values?.zmiany===13,'identical edit count, not missing update');
 // The same later receiver-placement request differs in these two material realities.
 const probeA=make(3+3*112,1),probeB=make(20+30*112,1);
 probeA.mediumSignal.receiver={x:3,y:3};probeB.mediumSignal.receiver={x:3,y:3};
 let refusedA=false;
 try{observe(source,probeA)}catch(e){refusedA=String(e).includes('pustej komórce')}
 insist(refusedA,'same receiver request refused in A: target is wall');
 const acceptedB=observe(source,probeB);
 insist(acceptedB.authored.mediumSignal.receiver.x===3&&acceptedB.authored.mediumSignal.receiver.y===3,'same receiver request accepted in B: target is free');
 const negative=make(3+3*112,1);
 negative.mediumSignal.receiver={x:78,y:40};
 const c=observe(source,negative);
 insist(c.authored.changes.length===13,'same number of edits for negative control');
 insist(c.local.reach&&c.local.travel!==a.local.travel,'negative control locally changes measured cost');
 insist(!eq(c.packets,a.packets),'negative control host sees changed signal');
 return {passed:12,kind:'source-JS plus Jaskinia v1 packet-level falsifier; no live Opera navigation',
  specimens:{
   A:{wallAt:[3,3],edits:13,occupancy:a.occupancy},
   B:{wallAt:[20,30],edits:13,occupancy:b.occupancy}
  },
  sameHostPackets:a.packets,
  samePreciseLocalTravel:a.local.travel,
  samePathLength:a.local.pathLength,
  sameFutureAction:{moveReceiverTo:[3,3],worldA:'rejected: wall',worldB:'accepted: free'},
  negativeControl:{receiver:[78,40],travel:c.local.travel,hostSignal:c.packets.find(p=>p.type==='signals').values},
  conclusion:'same reported facts do not determine grid topology or all future interactions'};
}
module.exports={run};
if(require.main===module){
 const f=process.argv.slice(2);
 if(f.length!==2)throw Error('Usage: node observability.cjs original-slad.html with-lens.json');
 console.log(JSON.stringify(run(fs.readFileSync(f[0],'utf8'),JSON.parse(fs.readFileSync(f[1],'utf8'))),null,2));
}
