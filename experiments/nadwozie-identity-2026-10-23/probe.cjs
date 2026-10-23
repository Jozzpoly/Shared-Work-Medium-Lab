'use strict';
// Medium research: rigid glTF geometry fingerprints, NOT an importer or stable-ID system.
// Narrowly supports a single skinned mesh with one embedded buffer and aligned primitives.
function decode(s,n) {
  const abc='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/', map=new Int16Array(128).fill(-1);
  for(let i=0;i<64;i++)map[abc.charCodeAt(i)]=i;
  const out=new Uint8Array(n);let word=0,bits=0,p=0;
  for(let i=0;i<s.length;i++){let c=s.charCodeAt(i),v=c<128?map[c]:-1;if(v<0)continue;
    word=(word<<6)|v;bits+=6;if(bits>=8){bits-=8;if(p>=n)throw Error('Buffer overrun');out[p++]=word>>>bits&255}}
  if(p!==n)throw Error('Wrong buffer length');return new DataView(out.buffer);
}
function check(ok,msg){if(!ok)throw Error(msg)}
function parts(text,opts={}) {
  const g=JSON.parse(text),mesh=g.meshes?.[0],skin=g.skins?.[0];
  check(g.asset?.version==='2.0' && g.meshes?.length===1 && g.skins?.length===1,'Only 1 skinned glTF 2 mesh');
  const b=g.buffers?.[0];check(g.buffers.length===1 && b.uri?.startsWith('data:application/octet-stream;base64,'),'Only embedded binary buffer');
  const view=decode(b.uri.split(',')[1],b.byteLength);
  function acc(i) {
    let a=g.accessors[i],v=g.bufferViews[a.bufferView],count={SCALAR:1,VEC3:3,VEC4:4}[a.type],size=a.componentType===5126?4:a.componentType===5123?2:0;
    check(count && size && !a.sparse,'Unsupported accessor');
    let pos=(v.byteOffset||0)+(a.byteOffset||0),step=v.byteStride||count*size;
    return Array.from({length:a.count},(_,k)=>Array.from({length:count},(_,j)=>a.componentType===5126?
      view.getFloat32(pos+k*step+j*size,true):view.getUint16(pos+k*step+j*size,true)));
  }
  const ps=mesh.primitives;check(ps.length>0,'No primitives');
  const channels=ps[0].attributes;
  check(ps.every(p=>p.mode===4 && p.attributes.POSITION===channels.POSITION && p.attributes.JOINTS_0===channels.JOINTS_0 && p.attributes.WEIGHTS_0===channels.WEIGHTS_0),'Unsupported primitives');
  const xyz=acc(channels.POSITION).map(v=>v.map((n,k)=>n+(opts.translation?.[k]||0)));
  const jj=acc(channels.JOINTS_0),ww=acc(channels.WEIGHTS_0);
  check(xyz.length===jj.length && xyz.length===ww.length,'Vertex count mismatch');
  const bones=ww.map((v,i)=>{
    const active=v.map((weight,j)=>weight>1e-6?j:-1).filter(j=>j>=0);
    check(active.length===1 && Math.abs(v[active[0]]-1)<1e-5,'Reject soft skin');
    return jj[i][active[0]];
  });
  let faces=ps.flatMap(p=>{let idx=acc(p.indices).map(row=>row[0]);check(idx.length%3===0,'Bad indices');
    return Array.from({length:idx.length/3},(_,i)=>idx.slice(3*i,3*i+3));});
  if(opts.reverseTriangles)faces.reverse();
  const parent=faces.map((_,i)=>i),rank=parent.map(()=>0),seen=new Map();
  const find=x=>{while(x!==parent[x]){parent[x]=parent[parent[x]];x=parent[x]}return x};
  const unite=(a,b)=>{a=find(a);b=find(b);if(a===b)return;if(rank[a]<rank[b]){let z=a;a=b;b=z}parent[b]=a;if(rank[a]===rank[b])rank[a]++};
  const q=1e-5,key=i=>xyz[i].map(x=>Math.round(x/q)).join(',');
  for(let t=0;t<faces.length;t++){const f=faces[t];check(f.every(i=>i>=0 && i<xyz.length),'Bad vertex ref');
    check(new Set(f.map(i=>bones[i])).size===1,'Triangle crosses joints');
    for(const v of f){const k=bones[v]+'@'+key(v);if(seen.has(k))unite(t,seen.get(k));else seen.set(k,t)}}
  const found=new Map();for(let i=0;i<faces.length;i++){const k=find(i),f=faces[i];
    if(!found.has(k))found.set(k,{bone:bones[f[0]],tris:0,vert:new Set()});
    let x=found.get(k);x.tris++;f.forEach(v=>x.vert.add(v))}
  const out=[...found.values()].map(x=>{
    const points=[...x.vert].map(i=>xyz[i]),min=[0,1,2].map(k=>Math.min(...points.map(p=>p[k]))),max=[0,1,2].map(k=>Math.max(...points.map(p=>p[k])));
    const shape=[...new Set(points.map(p=>p.map((v,k)=>Math.round((v-min[k])/q)).join(':')))].sort().join('|');
    const position=min.map((v,k)=>Math.round((v+max[k])/2/q)).join('|');
    const bbox=min.map((v,k)=>Math.round((max[k]-v)/q)).join('|');
    const node=g.nodes[skin.joints[x.bone]];check(node,'Bone unknown');
    return {triangles:x.tris,bone:x.bone,shape,position,bbox,name:opts.renameBones?'RENAMED'+x.bone:node.name};
  });
  return {triangles:faces.length,vertices:xyz.length,out};
}
function counts(a){const m=new Map();a.forEach(x=>m.set(x,(m.get(x)||0)+1));const values=[...m.values()];
  return {distinct:m.size,ambiguousInstances:values.filter(n=>n>1).reduce((a,b)=>a+b,0),largestCluster:Math.max(...values)}}
function audit(text,opt={}) {
  const x=parts(text,opt),p=x.out,keys={
    shape:p.map(v=>v.shape),shapeAndBone:p.map(v=>v.shape+'@'+v.name),
    shapeAndPosition:p.map(v=>v.shape+'@'+v.position),bbox:p.map(v=>v.bbox)
  },triHistogram={};
  p.forEach(x=>triHistogram[x.triangles]=(triHistogram[x.triangles]||0)+1);
  return {triangles:x.triangles,vertices:x.vertices,islands:p.length,joints:new Set(p.map(x=>x.bone)).size,
    triangleHistogram:triHistogram,collisions:Object.fromEntries(Object.entries(keys).map(([k,v])=>[k,counts(v)])),keys};
}
function selfTest(text) {
  const o=audit(text),shuffle=audit(text,{reverseTriangles:true}),move=audit(text,{translation:[20,0,0]}),rename=audit(text,{renameBones:true});
  const same=(x,y)=>JSON.stringify([...x].sort())===JSON.stringify([...y].sort());
  check(o.islands===121 && o.triangles===1632 && o.joints===11,'Specimen baseline changed');
  check(o.collisions.shape.ambiguousInstances===106,'Shape ambiguity changed');
  check(o.collisions.shapeAndBone.ambiguousInstances===72,'Joint ambiguity changed');
  check(o.collisions.shapeAndPosition.distinct===121,'Geometry-location uniqueness changed');
  check(same(o.keys.shapeAndPosition,shuffle.keys.shapeAndPosition),'Triangle order dependence');
  check(same(o.keys.shape,move.keys.shape),'Translation changes relative shape');
  const moved=new Set(move.keys.shapeAndPosition);
  check(o.keys.shapeAndPosition.every(k=>!moved.has(k)),'Unexpected position match after translation');
  check(same(o.keys.shapeAndPosition,rename.keys.shapeAndPosition),'Renaming changes geometry');
  check(!same(o.keys.shapeAndBone,rename.keys.shapeAndBone),'Name dependence missing');
  return ['source baseline','ambiguous repeated shapes','ambiguous shapes within bones',
    'unique anchored locations at current revision','triangle reordering negative control',
    'shape invariant under synthetic translation','anchored identities lost after translation',
    'geometry unchanged by rename','name-dependent signature changes'].length;
}
module.exports={audit,selfTest};
if(require.main===module){
  const fs=require('node:fs'),file=process.argv[2];if(!file)throw Error('Usage: node probe.cjs Nadwozie.gltf');
  const text=fs.readFileSync(file,'utf8'),r=audit(text),n=selfTest(text);delete r.keys;
  console.log(JSON.stringify({specimen:'Nadwozie.gltf',checksPassed:n,...r},null,2));
}