'use strict';
// Original HTML UI handlers exercised in a synthetic DOM; NOT a real-browser / Owner acceptance.
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const page=fs.readFileSync(__dirname+'/workbench.html','utf8');
const scripts=[...page.matchAll(/<script[^>]*>([\s\S]*?)<\/script>/g)].map(x=>x[1]);
assert.equal(scripts.length,2);
const handlers=new Map(),events=new Map(),elements=new Map();
const tools=['move','point','rod','pin','motor','delete'].map(mode=>({
 dataset:{mode},classList:{toggle(){}},
 addEventListener(name,fn){handlers.set('tool-'+mode+'-'+name,fn)}
}));
const fakeCtx=new Proxy({},{get:()=>()=>{},set:(o,k,v)=>{o[k]=v;return true}});
const el=id=>{
 if(!elements.has(id))elements.set(id,{id,textContent:'',value:'',disabled:false,files:[],
  classList:{toggle(){}},addEventListener(type,fn){handlers.set(id+'-'+type,fn)},
  focus(){},setPointerCapture(){},click(){},append(){},remove(){},
  getContext:()=>fakeCtx,getBoundingClientRect:()=>({left:0,top:0,width:1000,height:650})});
 return elements.get(id);
};
const doc={getElementById:el,querySelectorAll:()=>tools,createElement:x=>el('new-'+x),
 body:{append(){}},hidden:false,addEventListener:(t,fn)=>events.set('doc-'+t,fn)};
const sent=[],parent={postMessage:(m,o)=>sent.push({message:m,origin:o})};
const win={parent,devicePixelRatio:1,addEventListener:(t,fn)=>events.set('win-'+t,fn)};
let raf=null;
const ctx=vm.createContext({window:win,document:doc,console,Blob,
 URL:{createObjectURL:()=> 'blob:synthetic',revokeObjectURL(){}},setTimeout(){},
 requestAnimationFrame(fn){raf=fn}});
scripts.forEach(s=>vm.runInContext(s,ctx));
const {model}=win.LINKAGE_TEST_ACCESS;
const cases=[],check=(n,fn)=>{fn();cases.push(n)};
const pointer=(kind,x,y)=>handlers.get('stage-'+kind)({clientX:x,clientY:y,pointerId:7,button:0});
check('boots with paused authored mechanism',()=>{assert.equal(model.nodes.length,4);assert.equal(model.running,false)});
check('hello receives constrained host telemetry only',()=>{
 events.get('win-message')({source:parent,origin:'https://test-host',data:{jaskinia:1,type:'hi'}});
 assert.deepEqual(sent.map(x=>x.message.type),['hello','state','signals']);assert.equal(sent[1].message.data.rods,3);
 assert.equal('points' in sent[1].message.data,false);
});
check('wrong-origin state request rejected',()=>{
 const n=sent.length;
 events.get('win-message')({source:parent,origin:'https://other',data:{jaskinia:1,type:'state?'}});
 assert.equal(sent.length,n);
 events.get('win-message')({source:parent,origin:'https://test-host',data:{jaskinia:1,type:'state?'}});
 assert.equal(sent.length,n+2);
});
check('UI creates new point through real pointerdown handler',()=>{
 handlers.get('tool-point-click')();pointer('pointerdown',700,410);assert.equal(model.nodes.length,5);
});
check('UI connects two existing points through tool and taps',()=>{
 handlers.get('tool-rod-click')();pointer('pointerdown',473,380);pointer('pointerup',473,380);
 pointer('pointerdown',700,410);pointer('pointerup',700,410);assert.equal(model.rods.length,4);
});
check('pin applies to real material node',()=>{
 handlers.get('tool-pin-click')();pointer('pointerdown',700,410);assert.equal(model.node(5).pin,true);
});
check('play frames advance actual engine',()=>{
 handlers.get('play-click')();for(let i=1;i<=150;i++)raf(i*16.66667);
 assert.equal(model.running,true);assert.ok(model.t>1);assert.ok(el('stage').width>0);
});
check('undo restores previous authored pin decision',()=>{
 handlers.get('undo-click')();assert.equal(model.running,false);assert.equal(model.node(5).pin,false);
});
check('foreign finger cannot drag or release another pointer',()=>{
 handlers.get('tool-move-click')();
 pointer('pointerdown',290,260);
 handlers.get('stage-pointermove')({clientX:710,clientY:510,pointerId:9,button:0});
 handlers.get('stage-pointerup')({clientX:710,clientY:510,pointerId:9,button:0});
 assert.equal(model.dragging,2);assert.equal(model.node(2).x,290);
 handlers.get('stage-pointermove')({clientX:330,clientY:250,pointerId:7,button:0});
 assert.equal(model.node(2).x,330);
 handlers.get('stage-pointerup')({clientX:330,clientY:250,pointerId:7,button:0});
 assert.equal(model.dragging,null);
});
check('foreign iframe cannot impersonate host',()=>{
 const n=sent.length;
 events.get('win-message')({source:{},origin:'https://test-host',data:{jaskinia:1,type:'hi'}});
 assert.equal(sent.length,n);
});
console.log('PASS '+cases.length+'/'+cases.length+' synthetic UI cases (not live Chromium)');
