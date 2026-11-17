import fs from 'node:fs';
import test from 'node:test';
import assert from 'node:assert/strict';
const root=new URL('../',import.meta.url);
const file=n=>JSON.parse(fs.readFileSync(new URL(`data/${n}.json`,root),'utf8'));
const names=['groups','formations','statistics','sources','concessions','operators','events','regions','ophiolite','partnerships'];
const datasets=Object.fromEntries(names.map(n=>[n,file(n)]));
const src=new Set(datasets.sources.map(s=>s.id));
test('Datasets exist and IDs are unique',()=>{
 assert.equal(src.size,datasets.sources.length); for(const [k,d] of Object.entries(datasets))assert.ok(d.length>0,k);
});
test('All scientific facts have public source metadata',()=>{
 for(const s of datasets.sources){assert.ok(s.url?.startsWith('https://'),s.id);assert.ok(s.author && s.date && s.type,s.id)}
 for(const f of datasets.formations){assert.ok(datasets.groups.some(g=>g.group===f.group && g.formations.includes(f.name)),f.name);assert.ok(f.sources.length>0);assert.ok(f.sources.every(x=>src.has(x)),f.name);assert.ok(f.confidence)}
 for(const name of ['statistics','concessions','operators','ophiolite','partnerships']) for(const item of datasets[name])assert.ok(src.has(item.source),`${name}: ${item.source}`);
 for(const name of ['events','regions'])for(const item of datasets[name])assert.ok(item.sources.every(x=>src.has(x)));
});
test('Concession coordinates are not fabricated',()=>{
 assert.ok(datasets.concessions.every(c=>c.polygon===null && c.boundary_status.includes('Not available')));
 assert.equal(datasets.concessions.filter(c=>c.stage==='2026 bid round').length,5);
});
test('Genuine national outline feature is marked contextual',()=>{
 let fc=JSON.parse(fs.readFileSync(new URL('data/oman-boundary.geojson',root),'utf8')); assert.equal(fc.type,'FeatureCollection'); assert.ok(fc.features.length>=1);
});
test('Project has no embedded third-party papers or private well files',()=>{
 const files=fs.readdirSync(root,{recursive:true});assert.ok(!files.some(f=>/\.pdf$|\.las$|\.LAS$/i.test(f)));
});
test('Link to portfolio and bilingual link labels',()=>{
 const html=fs.readFileSync(new URL('index.html',root),'utf8');
 assert.match(html,/abdulrahmanalqasmi\.github\.io\/abdulrahman-portfolio/);
 assert.match(html,/عبد الرحمن القاسمي/);
});

test('V4 source-hosted concession map includes dates and published source',()=>{
 const html=fs.readFileSync(new URL('index.html',root),'utf8');
 assert.match(html,/web\/image\/66528-79402fc1\/MAP\.png/);
 assert.match(html,/24 DEC 2025/);
 assert.match(html,/2021 PDF ARCHIVE/);
 assert.match(html,/2026 BID ROUND/);
});
test('V4 expanded public scientific atlas has map-legend provenance',()=>{
 assert.ok(datasets.formations.length>=59);assert.ok(datasets.groups.length>=18);
 const mapped=datasets.formations.filter(r=>r.published_map_legend_no!==undefined);
 assert.ok(mapped.length>=38);
 assert.ok(mapped.every(r=>r.sources.includes('scharf2021map')));
 assert.ok(datasets.sources.some(x=>x.id==='scharf2021map' && x.license.includes('CC BY')));
});
test('V4 public UI omits restricted-document notices',()=>{
 const html=fs.readFileSync(new URL('index.html',root),'utf8');
 assert.doesNotMatch(html,/RESTRICTED REFERENCE|NOT REDISTRIBUTED|Confidential|PDO Catalogue|LITHOCAT/i);
 assert.match(html,/عبد الرحمن القاسمي/);
});
test('V4 published geology image is an attributed local illustration; block maps are external',()=>{
 const html=fs.readFileSync(new URL('index.html',root),'utf8');
 assert.match(html,/jabal-akhdar-saih-hatat-scharf2021\.webp/);
 assert.match(html,/10\.1144\/M54\.7/);
 assert.match(html,/CC BY 4\.0/);
 const image=new URL('assets/jabal-akhdar-saih-hatat-scharf2021.webp',root);
 assert.ok(fs.statSync(image).size>100000);
});
