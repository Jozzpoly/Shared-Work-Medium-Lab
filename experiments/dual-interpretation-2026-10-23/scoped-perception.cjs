'use strict';
const fs=require('node:fs');
const {boot}=require('./roundtrip.cjs');
const equal=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
function assert(x,why){if(!x)throw Error('FAIL: '+why)}
function originalAsk(host) {
 const a=host.indexOf('function askState('),b=host.indexOf('function liveCtxOf(',a);
 assert(a>=0&&b>a,'source anchor');
 const timers=[],sent=[];
 const fn=new Function('liveTalk','setTimeout',host.slice(a,b)+'return askState;')(
  (_,message)=>sent.push(message),(callback,delay)=>timers.push({callback,delay}));
 return {fn,timers,sent,expire(){for(const t of timers.splice(0))t.callback()}};
}
function report(html,v){
 const app=boot(html,false,{parent:true});
 app.__mediumSignal.import(JSON.stringify(v));
 app.__deliver({jaskinia:1,type:'hi'});
 return app.__messages.map(x=>x.message).filter(x=>x.type==='state'||x.type==='signals');
}
function withProbe(html,x,y){
 const from="instrumentSend('state',{text:q.text,data:{mode:'route',connected:pending?null:reach,needsReceiverConfirmation:pending}});";
 assert(html.includes(from),'instrument report anchor');
 const to="instrumentSend('state',{text:q.text,data:{mode:'route',connected:pending?null:reach,needsReceiverConfirmation:pending,localProbe:{cell:["+x+","+y+"],solid:solid[idx("+x+","+y+")]===1}}});";
 return html.replace(from,to);
}
async function run(host,html,fixture){
 const tests=[],check=(name,truth)=>{assert(truth,name);tests.push(name)};
 const item=(state={t:100,text:'OLD',data:{}},hello={name:'lab'})=>({state,hello,waiting:[]});
 const slow=originalAsk(host),one=item(),pending=slow.fn(one);
 check('request contains only state?',equal(slow.sent,[{type:'state?'}]));
 check('native timeout is 400 ms',slow.timers[0]?.delay===400);
 slow.expire();
 const older=await pending;
 check('timeout supplies cached rather than freshly measured state',older.text==='OLD'&&older.t===100);
 check('callback remains queued after timeout',one.waiting.length===1);
 const fast=originalAsk(host),two=item(),live=fast.fn(two);
 check('native message handler flushes waiter list',host.includes('for (const f of e.waiting.splice(0)) f(e.state);'));
 two.state={t:300,text:'NEW',data:{}};for(const fn of two.waiting.splice(0))fn(two.state);
 check('state received before timeout supplies new content',(await live).text==='NEW');
 const missingHello=originalAsk(host),three=item(undefined,null),noHello=await missingHello.fn(three);
 check('no hello returns cached state without requesting',missingHello.sent.length===0&&noHello.text==='OLD');
 const absent=originalAsk(host),four=item(null),waiting=absent.fn(four);absent.expire();
 check('no cached state and no response returns null',await waiting===null);
 const simultaneous=originalAsk(host),five=item(),p=simultaneous.fn(five),q=simultaneous.fn(five);
 five.state={t:500,text:'UNRELATED',data:{}};for(const fn of five.waiting.splice(0))fn(five.state);
 check('one message can settle two outstanding asks',(await p).text==='UNRELATED'&&(await q).text==='UNRELATED'&&simultaneous.sent.length===2);
 const a=JSON.parse(JSON.stringify(fixture)),b=JSON.parse(JSON.stringify(fixture));
 a.changes.push([339,1]);b.changes.push([3380,1]);
 check('authored worlds are different',!equal(a.changes,b.changes));
 check('original two worlds yield identical host messages',equal(report(html,a),report(html,b)));
 const instrument=withProbe(html,3,3),ar=report(instrument,a),br=report(instrument,b);
 check('single selected cell differentiates them',ar[0].data.localProbe.solid===true&&br[0].data.localProbe.solid===false);
 const lens=[ar,br].map(z=>JSON.stringify(z[0].data).length);
 check('specific answer fits existing host data limit',Math.max(...lens)<=Number(host.match(/LIVE_DATA = (\d+)/)?.[1]));
 check('answer to unrelated cell does not distinguish worlds',equal(report(withProbe(html,40,55),a),report(withProbe(html,40,55),b)));
 check('host does not carry a coordinate question in state?',host.includes("liveTalk(e, { type: 'state?' });"));
 return {passed:tests.length,checks:tests,observations:{freshness:'400ms fallback may return old state',waiter:'callback remains queued on timeout',localProbe:{cell:[3,3],worldA:true,worldB:false,serializedSizes:lens},scope:'no runtime agent query surface built'},limit:'Native host JS function + real instrument source JS under test DOM. Not actual user or browser test.'};
}
module.exports={run};
if(require.main===module){
 const files=process.argv.slice(2);if(files.length!==3)throw Error('Usage: node scoped-perception.cjs 52-przyrzady.js slad-revalidate-interpretation.html with-lens.json');
 run(fs.readFileSync(files[0],'utf8'),fs.readFileSync(files[1],'utf8'),JSON.parse(fs.readFileSync(files[2],'utf8'))).then(x=>console.log(JSON.stringify(x,null,2))).catch(e=>{console.error(e);process.exitCode=1});
}
