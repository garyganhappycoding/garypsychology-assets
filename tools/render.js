// Usage: node tools/render.js carousels/NN-name   -> renders slide-*.html to slide-*.png, reports overflow
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const dir=path.resolve(process.argv[2]);
(async()=>{const b=await chromium.launch({executablePath:fs.existsSync('/opt/pw-browsers/chromium')?'/opt/pw-browsers/chromium':undefined});
const p=await b.newPage({viewport:{width:1080,height:1350}});
for(const f of fs.readdirSync(dir).filter(f=>/^slide-\d+\.html$/.test(f)).sort()){
 await p.goto('file://'+path.join(dir,f));await p.evaluate(()=>document.fonts.ready);
 const o=await p.evaluate(()=>{const s=document.querySelector('.s');return s.scrollHeight>s.clientHeight+1||s.scrollWidth>s.clientWidth+1});
 if(o)console.log('OVERFLOW',f);
 await p.screenshot({path:path.join(dir,f.replace('.html','.png')),clip:{x:0,y:0,width:1080,height:1350}});}
await b.close();console.log('done');})();
