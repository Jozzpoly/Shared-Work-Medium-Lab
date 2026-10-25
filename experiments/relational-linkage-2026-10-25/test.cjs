'use strict';
// Run from this folder: node test.cjs
// Original standalone HTML contains the same physics core that the visitor runs.
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const page=fs.readFileSync(__dirname+'/workbench.html','utf8');
const scripts=[...page.matchAll(/<script[^>]*>([\s\S]*?)<\/script>/g)].map(m=>m[1]);
assert.equal(scripts.length,2);scripts.forEach(s=>new vm.Script(s));
const scope=vm.createContext({Math,JSON});vm.runInContext(scripts[0],scope);
const {Linkage,validate,fresh,DT}=scope.LINKAGE_CORE,copy=x=>JSON.parse(JSON.stringify(x));
const cases=[];const test=(name,fn)=>{fn();cases.push(name)};
test('default physically linked four-bar scene',()=>{
 const m=new Linkage();assert.equal(m.nodes.length,4);assert.equal(m.rods.length,3);assert.equal(m.motor,1);assert.equal(m.nodes.filter(n=>n.pin).length,2);
});
test('physics changes the output and retains reasonable distance constraints',()=>{
 const m=new Linkage(),b={...m.node(3)},anchors=m.nodes.filter(n=>n.pin).map(n=>({...n}));
 m.running=true;for(let i=0;i<1000;i++)m.step(DT);
 assert.ok(Math.hypot(m.node(3).x-b.x,m.node(3).y-b.y)>5);assert.ok(m.maxError()<70);
 for(const n of anchors){assert.equal(m.node(n.id).x,n.x);assert.equal(m.node(n.id).y,n.y)}
 for(const n of m.nodes)assert.ok(Number.isFinite(n.x)&&Number.isFinite(n.y));
});
test('paused physics advances no simulation',()=>{
 const m=new Linkage(),prior=JSON.stringify(m.serial());for(let i=0;i<600;i++)m.step(DT);assert.equal(JSON.stringify(m.serial()),prior);
});
test('user creates and removes genuine new relations',()=>{
 const m=new Linkage(),n=m.addNode(650,340);assert.ok(n);assert.ok(m.addRod(3,n.id));assert.ok(m.addRod(4,n.id));
 assert.equal(m.rods.length,5);assert.equal(m.addRod(3,n.id),null);assert.ok(m.removeNode(n.id));assert.equal(m.rods.length,3);
});
test('pin changes invalidate a motor that lost its fixed/free pair',()=>{
 const m=new Linkage();assert.ok(m.togglePin(2));assert.equal(m.motor,null);assert.equal(m.toggleMotor(1),false);
 assert.ok(m.togglePin(2));assert.ok(m.toggleMotor(1));
});
test('new motor couples to different world-anchored link',()=>{
 const m=new Linkage();assert.ok(m.toggleMotor(3));m.running=true;for(let i=0;i<250;i++)m.step(DT);assert.ok(Number.isFinite(m.maxError()));
});
test('dragging a paused node transmits geometry through rods',()=>{
 const m=new Linkage(),before={...m.node(3)};m.dragging=2;assert.ok(m.moveNode(2,400,270));
 assert.ok(Math.hypot(m.node(3).x-before.x,m.node(3).y-before.y)>1);m.dragging=null;
});
test('explicit JSON roundtrip preserves topology and exact authoring fields',()=>{
 const m=new Linkage(),n=m.addNode(700,500);m.addRod(4,n.id);
 const source=JSON.parse(JSON.stringify(m.serial()));assert.equal(JSON.stringify(new Linkage(source).serial()),JSON.stringify(source));
});
test('bad references leave running work unchanged',()=>{
 const m=new Linkage(),prior=JSON.stringify(m.serial()),bad=copy(m.serial());bad.rods[0].a=10003;
 assert.throws(()=>m.load(bad));assert.equal(JSON.stringify(m.serial()),prior);
});
test('duplicated rods, IDs and malformed motor are refused',()=>{
 const a=copy(fresh());a.rods.push({...a.rods[0],id:88});assert.throws(()=>validate(a));
 const b=copy(fresh());b.points[1].id=b.points[0].id;assert.throws(()=>validate(b));
 const c=copy(fresh());c.motor=123;assert.throws(()=>validate(c));
});
test('bad numeric values and out-of-world coordinates refused',()=>{
 const a=copy(fresh());a.points[0].x=Infinity;assert.throws(()=>validate(a));
 const b=copy(fresh());b.points[0].x=-1;assert.throws(()=>validate(b));
});
test('impossible anchored geometry remains explicitly strained, not fake-solved',()=>{
 const m=new Linkage();const r=m.addRod(1,4);assert.ok(r);
 m.moveNode(4,800,220);
 assert.ok(m.maxError()>6);assert.equal(m.node(4).x,800);
 assert.equal(m.rods.find(x=>x.id===r.id).length,260);
});
test('exposes current source-versus-runtime snapshot boundary after pure simulation',()=>{
 const m=new Linkage(),start=m.serial();
 m.running=true;for(let i=0;i<400;i++)m.step(DT);
 const after=m.serial();
 assert.deepEqual(after.rods,start.rods);assert.equal(after.motor,start.motor);
 assert.ok(after.points.some((p,i)=>Math.hypot(p.x-start.points[i].x,p.y-start.points[i].y)>10));
 const clone=new Linkage(JSON.parse(JSON.stringify(after)));
 assert.equal(JSON.stringify(clone.serial()),JSON.stringify(after));
 // This PASS documents a dangerous semantic gap; it is NOT export-of-authored-rest acceptance.
});
test('pure simulated time cannot rewrite last authored design',()=>{
 const m=new Linkage(),original=JSON.stringify(m.authored());
 m.running=true;for(let i=0;i<400;i++)m.step(DT);
 assert.equal(JSON.stringify(m.authored()),original);
 assert.notEqual(JSON.stringify(m.serial()),original);
});
test('design and pose are explicit transfer kinds with the same v1 material geometry',()=>{
 const m=new Linkage();m.running=true;for(let i=0;i<400;i++)m.step(DT);
 const authored=m.transfer('design'),pose=m.transfer('pose');
 assert.equal(authored.schema,'medium.linkage.transfer.v1');assert.equal(pose.schema,authored.schema);
 assert.equal(authored.kind,'design');assert.equal(pose.kind,'pose');
 assert.equal(authored.document.schema,'medium.linkage.v1');assert.equal(pose.document.schema,'medium.linkage.v1');
 assert.notEqual(JSON.stringify(authored.document),JSON.stringify(pose.document));
 const decode=scope.LINKAGE_CORE.decodeTransfer;
 assert.equal(decode(authored).kind,'design');assert.equal(decode(pose).kind,'pose');
 assert.equal(JSON.stringify(new Linkage(decode(authored).document).serial()),JSON.stringify(authored.document));
 assert.equal(JSON.stringify(new Linkage(decode(pose).document).serial()),JSON.stringify(pose.document));
});
test('runtime pose transfer deliberately excludes time, previous positions and history',()=>{
 const m=new Linkage();m.running=true;for(let i=0;i<240;i++)m.step(DT);
 const file=m.transfer('pose'),newWorld=new Linkage(file.document);
 assert.equal(newWorld.t,0);assert.equal(newWorld.running,false);
 assert.equal(file.document.points.every(n=>!Object.hasOwn(n,'px')&&!Object.hasOwn(n,'py')),true);
 assert.equal(file.document.points.some(n=>Object.hasOwn(n,'vx')),false);
});
test('a deliberate authoring commit changes design without later simulated rewriting',()=>{
 const m=new Linkage(),old=JSON.stringify(m.authored());
 const n=m.addNode(690,510);assert.ok(n);m.addRod(3,n.id);m.commitDesign();
 const newDesign=JSON.stringify(m.authored());assert.notEqual(newDesign,old);
 assert.equal(m.authored().points.length,5);assert.equal(m.authored().rods.length,4);
 m.running=true;for(let i=0;i<100;i++)m.step(DT);
 assert.equal(JSON.stringify(m.authored()),newDesign);
});
test('uncommitted runtime manipulation is not automatically credited as authoring',()=>{
 const m=new Linkage(),before=JSON.stringify(m.authored());
 m.moveNode(3,700,480);
 assert.equal(JSON.stringify(m.authored()),before);
 m.commitDesign();assert.notEqual(JSON.stringify(m.authored()),before);
});
test('explicit authored transfer is a defensive copy',()=>{
 const m=new Linkage(),f=m.transfer('design');
 f.document.points[0].x=990;
 assert.equal(m.authored().points[0].x,220);
});
test('v1 legacy transfer stays importable but origin has unknown semantics',()=>{
 const decode=scope.LINKAGE_CORE.decodeTransfer,m=new Linkage();
 const legacy=decode(JSON.parse(JSON.stringify(m.serial())));
 assert.equal(legacy.kind,'legacy-untagged');
 assert.equal(legacy.document.schema,'medium.linkage.v1');
});
test('invalid transfer metadata and forged material references fail closed',()=>{
 const decode=scope.LINKAGE_CORE.decodeTransfer;
 const m=new Linkage(),correct=m.transfer('design'),before=JSON.stringify(m.authored());
 assert.throws(()=>decode({...correct,kind:'video'}));
 const forged=JSON.parse(JSON.stringify(correct));forged.document.rods[0].a=9999;
 assert.throws(()=>decode(forged));
 assert.throws(()=>m.transfer('arbitrary'));
 assert.equal(JSON.stringify(m.authored()),before);
});
test('clearing last motor link clears the motor',()=>{
 const m=new Linkage();assert.ok(m.removeRod(1));assert.equal(m.motor,null);
});
console.log('PASS '+cases.length+'/'+cases.length+' - '+cases.join(' | '));
