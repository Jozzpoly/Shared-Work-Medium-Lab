'use strict';
const fs=require('node:fs');
function assert(ok,msg){if(!ok)throw Error(msg)}
function boot(html,stepHook=false,host=null,view=null){
 const match=[...html.matchAll(/<script[^>]*>([\s\S]*?)<\/script>/g)];
 assert(match.length===1,'One inline script required');let src=match[0][1];
 const mark='window.__mediumPortable={get:()=>capsule(),apply:raw=>importCapsule(raw)};';
 if(stepHook){assert(src.includes(mark),'Missing step hook');src=src.replace(mark,mark+'window.__probeStep=n=>{for(let i=0;i<n;i++)simulate();return window.__kowal.snapshot()};')}
 const els=new Map(),ctx=new Proxy({createImageData:(w,h)=>({data:new Uint8ClampedArray(w*h*4)})},{get(o,k){return k in o?o[k]:()=>{}},set(o,k,v){o[k]=v;return true}});
 function el(id){if(!els.has(id))els.set(id,{id,textContent:'0',value:'',dataset:{},style:{},width:896,height:544,classList:{add(){},remove(){},toggle(){}},getContext:()=>ctx,focus(){},select(){},addEventListener(type,fn){((this._listeners ||= {})[type] ||= []).push(fn)},setAttribute(){},getBoundingClientRect(){return {left:0,top:0,width:896,height:544}},setPointerCapture(){}});return els.get(id)}
 const document={getElementById:el,createElement:el,querySelector:el,querySelectorAll:q=>q==='[data-tool]'?[(el('tool-wall').dataset.tool='wall',el('tool-wall'))]:[],addEventListener(){},body:el('body')};
 const messages=[];
 const window={document,addEventListener(type,fn){(this._listeners ||= {})[type]=fn},location:{origin:'https://htmlpreview.github.io',href:view?.href||'https://htmlpreview.github.io/research.html',hash:view?.hash||''}};
 window.history={state:null,replaceState(state,title,url){this.state=state;window.location.href=String(url);window.location.hash=String(url).includes('#')?'#'+String(url).split('#').slice(1).join('#'):''}};
 const parent=host?.parent?{postMessage(message,origin){messages.push({message,origin})}}:window;
 window.parent=parent;window.__messages=messages;
 window.__deliver=(data,origin='https://jozzpoly.github.io')=>{for(const fn of window._listeners?.message||[])fn({data,origin,source:parent})};
 const navigator={clipboard:{async writeText(text){window.__copied=String(text)}}};
 const env={window,document,navigator,innerWidth:896,BroadcastChannel:host?.BroadcastChannel,performance:{now:()=>0},requestAnimationFrame(){},setInterval(){},setTimeout(){},Blob:class{},URL:{createObjectURL:()=>'',revokeObjectURL(){}}};
 new Function(...Object.keys(env),src)(...Object.values(env));return window;
}
const equal=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
function run(hydraulicHtml,signalHtml){
 const fluid=boot(hydraulicHtml,true),signal=boot(signalHtml),fresh=boot(signalHtml);
 const baseline=fluid.__mediumPortable.get();assert(baseline.changes.length===11,'Donor baseline differs');
 const revised=JSON.parse(JSON.stringify(baseline)),extraIndex=43*112+56;
 assert(signal.__mediumSignal.sample(56,43)===1,'Expected solid cell');
 assert(signal.__mediumSignal.sample(82,40)===0,'Expected empty receiver cell');
 revised.changes.push([extraIndex,0]);revised.mediumSignal={receiver:{x:82,y:40}};
 signal.__mediumSignal.import(revised);const withLens=signal.__mediumSignal.get(),signalStatus=signal.__mediumSignal.status();
 assert(withLens.changes.length===12&&equal(withLens.mediumSignal,revised.mediumSignal),'Signal interpretation not preserved');
 fluid.__mediumPortable.apply(JSON.stringify(withLens));const throughLegacy=fluid.__mediumPortable.get();
 assert(equal(throughLegacy.changes,withLens.changes),'Topology was changed by legacy');
 assert(equal(throughLegacy.source,withLens.source)&&equal(throughLegacy.drain,withLens.drain),'Source/drain changed');
 assert(throughLegacy.mediumSignal===undefined,'Metadata unexpectedly preserved');
 fresh.__mediumSignal.import(throughLegacy);const freshReceiver=fresh.__mediumSignal.get().mediumSignal.receiver;
 assert(equal(freshReceiver,{x:62,y:52}),'Expected default when metadata absent');
 let bad=JSON.parse(JSON.stringify(withLens));bad.mediumSignal.receiver={x:0,y:0};
 let refused=false;try{signal.__mediumSignal.import(bad)}catch{refused=true}
 assert(refused&&equal(signal.__mediumSignal.get(),withLens),'Malformed metadata mutated signal world');
 // Red-team forward preservation: a later geometry edit can invalidate opaque interpreted metadata.
 const conflictingCell=withLens.mediumSignal.receiver.y*112+withLens.mediumSignal.receiver.x;
 const otherFluid=boot(hydraulicHtml),otherLens=boot(signalHtml);
 assert(otherFluid.__kowal.sample(withLens.mediumSignal.receiver.x,withLens.mediumSignal.receiver.y).solid===0,
   'Expected an empty receiver cell in the hydraulic source');
 const blocked={...withLens,changes:[...withLens.changes,[conflictingCell,1]]};
 otherFluid.__mediumPortable.apply(JSON.stringify(blocked));
 const naiveCarry={...otherFluid.__mediumPortable.get(),mediumSignal:withLens.mediumSignal};
 const beforeConflict=otherLens.__mediumSignal.get();
 let rejectedStale=false;
 try{otherLens.__mediumSignal.import(naiveCarry)}catch{rejectedStale=true}
 assert(rejectedStale&&equal(otherLens.__mediumSignal.get(),beforeConflict),
   'Receiver-on-wall interpretation was not safely rejected');
 const physicsBaseline=boot(hydraulicHtml,true).__probeStep(240),physicsChanged=fluid.__probeStep(240);
 assert(physicsChanged.solids===physicsBaseline.solids-1&&physicsChanged.step===240,'Physical test state invalid');
 return {withLens,throughLegacy,evidence:{originalChanges:baseline.changes.length,authorChanges:withLens.changes.length,extraIndex,originalReceiver:withLens.mediumSignal.receiver,freshReceiver,signalReach:signalStatus.reach,signalDistance:signalStatus.travel,fluidMassRightAt240:{original:physicsBaseline.right,changed:physicsChanged.right},malformedRejected:true,staleExtensionRejectedWithoutMutation:true,receiverConflictCell:conflictingCell,geometryPreserved:true,metadataPreserved:false}};
}
module.exports={run,boot};
if(require.main===module){
 const [hydraulic,signal,prefix]=process.argv.slice(2);
 if(!hydraulic||!signal)throw Error('Usage: node roundtrip.cjs hydraulic.html signal.html [prefix]');
 const r=run(fs.readFileSync(hydraulic,'utf8'),fs.readFileSync(signal,'utf8'));
 if(prefix){fs.writeFileSync(prefix+'-with-lens.json',JSON.stringify(r.withLens,null,2)+'\n');fs.writeFileSync(prefix+'-through-legacy.json',JSON.stringify(r.throughLegacy,null,2)+'\n')}
 console.log(JSON.stringify(r.evidence,null,2));
}