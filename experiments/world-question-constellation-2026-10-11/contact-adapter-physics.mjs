// Actual donor-physics falsifier in isolated SWM CI; no donor repo edits.
// Source-locked Combat B1 Rapier 0.21.0, never a ReflexBrain transfer PASS.
// Preregister before interpreting observations: wing-external contact with
// root-external == 0 demonstrates single-root sensing cannot see every part.
import assert from 'node:assert/strict';
import {mkdir,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {resolve} from 'node:path';
import {pathToFileURL} from 'node:url';

const SHA='24bd930fb1bb83425ea43168660a9c9c75d5b7d6';
const out=resolve('.swm-donor-fixture');
await mkdir(resolve(out,'src'),{recursive:true});
const sources=[];
for(const file of ['m0-world.js','b1-world.js']){
 const url='https://raw.githubusercontent.com/Jozzpoly/Combat-Lab/'+SHA+'/src/'+file;
 const response=await fetch(url);
 if(!response.ok)throw Error('Donor source read '+file+' HTTP '+response.status);
 const content=await response.text();
 assert.ok(content.length>3000&&content.length<25000);
 const imported='import RAPIER from "@dimforge/rapier2d-deterministic";';
 assert.ok(content.includes(imported),'unexpected donor dependency import');
 // Node does not honor the NPM package's module entry (rapier.js), and the
 // distribution has no index.js. Rewrite ONLY the ESM import to a local shim;
 // preserve and hash the original exact-SHA donor source independently.
 const nodeImport=content.replace(imported,'import RAPIER from "./rapier-node-entry.mjs";');
 await writeFile(resolve(out,'src',file),nodeImport);
 sources.push({file,sha256:createHash('sha256').update(content).digest('hex'),bytes:content.length});
}
await writeFile(resolve(out,'package.json'),JSON.stringify({type:'module'}));
await writeFile(resolve(out,'src','rapier-node-entry.mjs'),
  'import * as RAPIER from "@dimforge/rapier2d-deterministic/rapier.js";\n'+
  'if(typeof RAPIER.init==="function") await RAPIER.init();\n'+
  'export default RAPIER;\n');
const {EnvelopeField}=await import(pathToFileURL(resolve(out,'src/b1-world.js')).href);
const partLabels=['root','upper-wing','lower-wing'];
function reportContacts(field){
 const parts=field.actor.parts,owned=new Set(parts.map(p=>p.collider.handle));
 return parts.map((part,i)=>{
  let raw=0,external=0,internal=0,pairs=0;
  field.world.contactPairsWith(part.collider,other=>{
   field.world.contactPair(part.collider,other,(m,flipped)=>{
    let load=0;
    for(let k=0;k<m.numSolverContacts();k++)load+=Math.abs(m.contactImpulse(k));
    if(load<=1e-7)return;
    raw+=load;pairs++;
    if(owned.has(other.handle))internal+=load;else external+=load;
   });
  });
  return {part:partLabels[i],raw,external,internal,pairs};
 });
}
function run(name,obstacles,{selfContact=true,fold=0,steps=120}={}){
 const f=new EnvelopeField({kind:'folding',withGate:false,withMatter:false,
  hingeMount:'front',torqueCap:3,selfContact,holdHeading:true});
 try{
  // Physical external material added in the actual B1 arena, next to
  // wing tips; initial root remains at (10,13.5). No fake contact injection.
  for(const o of obstacles)f.addFixed(o.x,o.y,o.hx,o.hy);
  const trace=[];let examples=[],outside=[0,0,0],inside=[0,0,0],positive=0;
  for(let tick=0;tick<steps;tick++){
   f.step({forward:0,fold});
   const rows=reportContacts(f);
   rows.forEach((p,i)=>{outside[i]=Math.max(outside[i],p.external);inside[i]=Math.max(inside[i],p.internal);});
   const anyWing=rows[1].external+rows[2].external>1e-6,rootClear=rows[0].external<=1e-6;
   if(anyWing&&rootClear){
    positive++;
    if(examples.length<4)examples.push({tick,parts:rows,
      root:f.actor.root.translation(),wings:f.actor.wings.map(w=>({angle:w.body.rotation(),xy:w.body.translation()}))});
   }
   if(tick===0||tick===30||tick===60||tick===119)trace.push({tick,parts:rows});
  }
  return {name,obstacles,selfContact,fold,samples:steps,wingExternalRootClearFrames:positive,
    maxExternalImpulseByPart:outside,maxInternalImpulseByPart:inside,examples,trace};
 }finally{f.dispose();}
}
const cases=[
 run('clear-arena-control',[]),
 run('upper-wing-probe',[{x:10.65,y:12.15,hx:.30,hy:.24}]),
 run('lower-wing-probe',[{x:10.65,y:14.85,hx:.30,hy:.24}]),
 run('two-wing-obstacles',[{x:10.65,y:12.15,hx:.30,hy:.24},{x:10.65,y:14.85,hx:.30,hy:.24}]),
 run('upper-wing-no-self-contact',[{x:10.65,y:12.15,hx:.30,hy:.24}],{selfContact:false})
];
const verdict={
 source:SHA,rapier:'0.21.0 deterministic; Node ESM package-module entry adaptation ONLY',sources,
 preregistered_measure:'wing-external-solver-impulse>1e-6 && root-external-solver-impulse<=1e-6 in same frame',
 results:cases.map(x=>({
   case:x.name,frames:x.wingExternalRootClearFrames,
   maxExternal:x.maxExternalImpulseByPart.map(n=>Number(n.toFixed(5))),
   maxInternal:x.maxInternalImpulseByPart.map(n=>Number(n.toFixed(5))),
   firstExample:x.examples[0]||null
 })),
 note:'Root-only vs wing is actor-owned collider observation; wall identity is used solely to place a test obstacle, not provided to the hypothetical actor.',
 criterionMet:cases.slice(1).some(c=>c.wingExternalRootClearFrames>0),
 allFinite:cases.every(c=>c.maxExternalImpulseByPart.every(Number.isFinite))
};
assert.ok(verdict.allFinite,'nonfinite physics load');
assert.equal(cases[0].maxExternalImpulseByPart.every(n=>n<1e-6),true,'clear control has external impulses');
const path=resolve('/tmp/swm-physics-contact-result.json');
await writeFile(path,JSON.stringify({verdict,cases},null,2));
console.log('SWM_ACTUAL_PHYSICS',JSON.stringify(verdict));
console.log('FALSIFIER_STATUS',verdict.criterionMet?'PART_OBSTRUCTED_ROOT_CLEAR_OBSERVED':'NOT_DEMONSTRATED_IN_TESTED_SCENES');
