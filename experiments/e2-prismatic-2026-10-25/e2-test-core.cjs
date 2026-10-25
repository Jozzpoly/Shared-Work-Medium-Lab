'use strict';
// E2 falsifier: embedded original ŁĄCZNIK distance solver vs analytical prismatic reference.
// node e2-test-core.cjs
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const html=fs.readFileSync(__dirname+'/e2-rail-witness.html','utf8');
const scripts=[...html.matchAll(/<script[^>]*>([\s\S]*?)<\/script>/g)].map(x=>x[1]);
assert.equal(scripts.length,2);scripts.forEach(x=>new vm.Script(x));
const context=vm.createContext({window:{}});vm.runInContext(scripts[0],context);
const {Linkage,DT}=context.window.LINKAGE_CORE;
const initial={schema:'medium.linkage.v1',
 points:[{id:1,x:160,y:260,pin:true},{id:2,x:220,y:260,pin:false},{id:3,x:400,y:260,pin:false}],
 rods:[{id:1,a:1,b:2,length:60},{id:2,a:2,b:3,length:180}],motor:1,motorSpeed:1.05};
const m=new Linkage(initial),checks=[];
function check(name,value){assert.ok(value,name);checks.push(name)}
check('actual model has only two distance constraints',m.rods.length===2&&m.nodes.length===3&&m.motor===1);
check('only crank center is pinned',m.nodes[0].pin&&!m.nodes[1].pin&&!m.nodes[2].pin);
let maxDrift=0,maxStrain=0,maxTargetError=0,minX=Infinity,maxX=-Infinity,samples=[];
m.running=true;
for(let i=0;i<720;i++){
 m.step(DT);
 const b=m.node(2),c=m.node(3),rail=260,L=180;
 const idealX=b.x+Math.sqrt(Math.max(0,L*L-(rail-b.y)**2));
 maxDrift=Math.max(maxDrift,Math.abs(c.y-rail));
 maxStrain=Math.max(maxStrain,m.maxError());
 maxTargetError=Math.max(maxTargetError,Math.abs(Math.hypot(idealX-b.x,rail-b.y)-L));
 minX=Math.min(minX,idealX);maxX=Math.max(maxX,idealX);
 if(i%120===0)samples.push({t:+m.t.toFixed(2),freeY:+c.y.toFixed(3),offRail:+Math.abs(c.y-rail).toFixed(3),idealX:+idealX.toFixed(3),idealY:rail});
}
check('pin is unchanged',m.node(1).y===260);
check('free endpoint travels far off the depicted guide',maxDrift>120);
check('distance constraints remain satisfied',maxStrain<2);
check('analytic target satisfies exact link length',maxTargetError<1e-6);
check('analytic target moves horizontally',maxX-minX>80);
check('no native rail in material schema',!Object.hasOwn(m.serial(),'rail'));
check('six simulated physical seconds passed',Math.abs(m.t-6)<1e-7);
check('passive simulation does not modify authored rest document',m.authored().points[2].y===260);
check('no script imported an external library',!html.includes('src="https://')&&!html.includes('import('));

const guidedClass=scripts[1].match(/class GuidedLinkage extends Linkage\{[\s\S]*?\n\}\nlet world=/);
check('guided model is a subclass of the same Linkage solver',!!guidedClass);
vm.runInContext('const Linkage=window.LINKAGE_CORE.Linkage;\n'+guidedClass[0].replace(/\nlet world=$/,'')+'\nwindow.GuidedLinkage=GuidedLinkage;',context);
const guided=new context.window.GuidedLinkage(initial);
guided.running=true;
let mxGuidedDrift=0,mxGuidedStrain=0,maxCrankMismatch=0;
const other=new Linkage(initial);other.running=true;
for(let i=0;i<720;i++){
 guided.step(DT);other.step(DT);
 mxGuidedDrift=Math.max(mxGuidedDrift,Math.abs(guided.node(3).y-260));
 mxGuidedStrain=Math.max(mxGuidedStrain,guided.maxError());
 maxCrankMismatch=Math.max(maxCrankMismatch,Math.hypot(guided.node(2).x-other.node(2).x,guided.node(2).y-other.node(2).y));
}
check('same solver with rail projects endpoint exactly to a horizontal guide',mxGuidedDrift<1e-8);
check('same solver satisfies rod constraints even with the extra rail',mxGuidedStrain<.01);
check('same motor drives both models identically',maxCrankMismatch<1e-8);

const report={passed:checks.length,checks,maxOffRail:+maxDrift.toFixed(3),maxRodStrain:+maxStrain.toFixed(6),maxReferenceRodError:+maxTargetError.toFixed(8),referenceExcursion:+(maxX-minX).toFixed(3),guidedMaxOffRail:mxGuidedDrift,guidedMaxStrain:mxGuidedStrain,maxCrankMismatch,samples,limit:'An analytic target is NOT a competing physics engine. A distance-only example lacking a prismatic joint is not proof that all approximate guide mechanisms are impossible.'};
console.log(JSON.stringify(report,null,2));
