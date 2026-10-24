'use strict';
// Reproduce URL-fragment propagation through Jaskinia v6.4.1 source functions only.
// Uses synthetic data; never touches real browser storage or the Owner's world.
const fs=require('node:fs');
function assert(ok,msg){if(!ok)throw Error('FAIL: '+msg)}
function between(s,a,b){const from=s.indexOf(a);assert(from!==-1,'missing '+a);const to=s.indexOf(b,from);assert(to>from,'missing '+b);return s.slice(from,to)}
function run(instruments,storage,feedback){
 const checks=[],pass=(name,ok)=>{assert(ok,name);checks.push(name)};
 const tag='PUBLIC_SYNTHETIC_WORLD_DATA';
 const link='https://example.invalid/lab.html#world='+encodeURIComponent(JSON.stringify({tag,changes:[[339,1]]}));
 let captured={};
 const recentFn=new Function('liveRecent','lstr','lsSet','KEY_LIVE_RECENT',
   between(instruments,'function rememberLive(','const LIVE_ALLOW')+'return rememberLive;')(
   ()=>[],(x,n)=>String(x).slice(0,n),(k,v)=>{captured[k]=v;return true},'jaskinia:przyrzady');
 recentFn(link,'Synthetic test',null);
 const recent=JSON.parse(captured['jaskinia:przyrzady']);
 pass('original rememberLive stores complete #world URL',recent[0]?.url===link);
 const sp={name:'Synthetic lab',preset:null,purpose:'',
   L:{tree:{t:'w',id:'w'},wins:{w:{type:'przyrzad',st:{url:link}}},floats:[]}};
 const st={spaces:[sp],cur:'synthetic',sel:null,notes:{},views:{},saved:[],trash:[]};
 const snapshotFn=new Function('store','clone','arr',
   between(storage,'function snapshotAll(','function fromSnapshot(')+'return snapshotAll;')(
   st,x=>JSON.parse(JSON.stringify(x)),x=>Array.isArray(x)?x:[]);
 const snapshot=snapshotFn();
 pass('original snapshotAll keeps full guest URL in window state',
   snapshot.spaces[0].L.wins.w.st.url===link);
 const env={
   D:{estate:{coverage:{collected:1,expected:1},generated:'synthetic'}},
   noteNeedles:()=>[],isoLocal:x=>String(x),VER:'6.4.1',BUILD:{built:'test',host:'test'},PLACE:'test',
   location:{pathname:'/test.html',protocol:'https:'},innerWidth:900,innerHeight:600,screen:{width:900,height:600},
   devicePixelRatio:1,coarse:{matches:false},phone:false,navigator:{userAgent:'Synthetic',language:'pl'},
   storageOK:true,saveProblem:null,snapAgeDays:()=>0,prefs:{},nowContext:()=>({}),store:st,
   spaceName:x=>x.name,allIdsOf:L=>Object.keys(L.wins),uwagi:[],jlog:[],
   scrubNotes:x=>x,L:sp.L,readBackups:()=>[],
   LIVE:new Map([['w',{id:'w',url:link,hello:{name:'Synthetic',version:'1'},since:1,
     state:{t:1,text:'active',data:{}},sigs:new Map(),evs:[],quiet:0,marks:[]}]])
 };
 // Execute original function body with fixtures for its environment; no replica implementation.
 const pkg=new Function('env','with(env){'+between(feedback,'function packageData(','function allIdsOf(')+'return packageData(false)}')(env);
 pass('native package contains guest URL via layout',pkg.uklady[0].uklad.wins.w.st.url===link);
 pass('native package contains guest URL via running instrument',pkg.przyrzady[0].adres===link);
 pass('package contents include encoded synthetic world marker',JSON.stringify(pkg).includes(tag));
 pass('omitting note text does not omit instrument address',pkg.notatki.tresc.includes('pominięta')&&pkg.przyrzady[0].adres===link);
 const single=JSON.parse(JSON.stringify(pkg));
 single.przyrzady[0].adres='[redacted]';
 pass('redacting only instrument URL still leaks through layout',JSON.stringify(single).includes(tag));
 const reverse=JSON.parse(JSON.stringify(pkg));
 reverse.uklady[0].uklad.wins.w.st.url='[redacted]';
 pass('redacting only layout URL still leaks through instrument',JSON.stringify(reverse).includes(tag));
 pass('no real notes or files in test fixture',!Object.keys(st.notes).length&&!st.saved.length);
 return {passed:checks.length,checks,scope:'original source functions with synthetic stubs; no real private data or network',
   carriers:['jaskinia:przyrzady recent URL','workspace snapshot window st.url','package layout st.url','package instrument adres'],
   observation:'URL fragment becomes persistent host metadata; no automatic exfiltration demonstrated'};
}
module.exports={run};
if(require.main===module){
 const files=process.argv.slice(2);if(files.length!==3)throw Error('Usage: node host-url-carriage.cjs 52-przyrzady.js 15-store.js 55-feedback.js');
 console.log(JSON.stringify(run(...files.map(f=>fs.readFileSync(f,'utf8'))),null,2));
}
