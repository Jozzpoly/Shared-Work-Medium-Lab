// Runs inside an actual Chromium/Vite browser, using Combat's exact donor ESM.
import RAPIER from '@dimforge/rapier2d-deterministic';
import {EnvelopeField} from '../../.swm-donor-fixture/src/b1-world.js';
const labels=['root','negative-wing','positive-wing'];
function readParts(w){
 const owned=new Set(w.actor.parts.map(p=>p.collider.handle));
 return w.actor.parts.map((part,i)=>{
  const result={label:labels[i],external:0,internal:0,all:0,contactPairs:0};
  w.world.contactPairsWith(part.collider,other=>{
   w.world.contactPair(part.collider,other,m=>{
    let load=0;
    for(let k=0;k<m.numSolverContacts();k++)load+=Math.abs(m.contactImpulse(k));
    if(load<=1e-7)return;
    result.all+=load;result.contactPairs++;
    if(owned.has(other.handle))result.internal+=load;
    else result.external+=load;
   });
  });
  return result;
 });
}
function one(name,obstacles,{selfContact=true,fold=0,steps=110}={}){
 const w=new EnvelopeField({kind:'folding',withGate:false,withMatter:false,
  hingeMount:'front',torqueCap:3,selfContact,holdHeading:true});
 try{
  for(const p of obstacles)w.addFixed(p.x,p.y,p.hx,p.hy);
  const max=[0,0,0],internal=[0,0,0],examples=[];let frames=0,nonfinite=0;
  for(let tick=0;tick<steps;tick++){
   w.step({forward:0,fold});
   const s=readParts(w);
   for(let i=0;i<s.length;i++){
    max[i]=Math.max(max[i],s[i].external);
    internal[i]=Math.max(internal[i],s[i].internal);
    if(!Number.isFinite(s[i].all))nonfinite++;
   }
   if(s[0].external<=1e-6 && s.slice(1).some(x=>x.external>1e-6)){
    frames++;
    if(examples.length<3)examples.push({tick,parts:s,root:w.actor.root.translation(),
      wings:w.actor.wings.map(x=>({at:x.body.translation(),angle:x.body.rotation()}))});
   }
  }
  return {name,frames,max,internal,nonfinite,examples};
 }finally{w.dispose();}
}
try{
 if(typeof RAPIER.init==='function')await RAPIER.init();
 // No donor code: distinguish a Vite/Rapier WASM bridge failure from B1 physics.
 const bareWorld=new RAPIER.World({x:0,y:0});
 const bareBody=bareWorld.createRigidBody(RAPIER.RigidBodyDesc.dynamic().setTranslation(0,0));
 const barePose=bareBody.translation();
 if(!Number.isFinite(barePose.x)||!Number.isFinite(barePose.y))throw Error('bare Rapier body position is nonfinite');
 bareWorld.free();
 const cases=[
  one('clear',[]),
  one('negative-wing-contact',[{x:10.65,y:12.15,hx:.30,hy:.24}]),
  one('positive-wing-contact',[{x:10.65,y:14.85,hx:.30,hy:.24}]),
  one('both-wing-contacts',[{x:10.65,y:12.15,hx:.30,hy:.24},{x:10.65,y:14.85,hx:.30,hy:.24}]),
  one('one-wing-self-contact-disabled',[{x:10.65,y:12.15,hx:.30,hy:.24}],{selfContact:false})
 ];
 const control=cases[0].max.every(v=>v<1e-6);
 const verified=cases.slice(1).some(c=>c.frames>0);
 window.__swmPhysics={
  success:true,runtime:'Real Chromium + Vite; exact donor ES modules and @dimforge/rapier2d-deterministic@0.21.0',
  source:'24bd930fb1bb83425ea43168660a9c9c75d5b7d6',
  control,verified,results:cases,
  interpretation: verified?'found genuine solver contact at wing while root external contact=0':'NOT OBSERVED in these bounded physical scenes',
  noClaim:'This does not implement ReflexBrain sensor, autonomous cognition or donor integration.'
 };
}catch(error){window.__swmPhysics={success:false,error:String(error.stack||error)};}
