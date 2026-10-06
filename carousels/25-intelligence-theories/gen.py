# Intelligence · 1/5 · Theories of intelligence. Run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from series import *
T=10;S=[]
S.append(cover('INTELLIGENCE · 1 OF 5',
 'Is there only <span style="font-style:italic;color:#C24A2B">one way</span> to be smart?',
 '5 theories of intelligence, in one swipe.',badge('🧠',250),110))
S.append(slide(f'''{head('DEFINITION',f'Intelligence {zs("智力",48)}',100)}{GROW}
<div style="font-family:Fraunces,serif;font-size:56px;line-height:1.22">The ability to <span style="color:#3D3A8C">learn from experience</span>, <span style="color:#3D3A8C">gain knowledge</span> and <span style="color:#3D3A8C">use resources well</span> to adapt to new situations or <span style="color:#C24A2B">solve problems</span>.</div>{GROW}
<div style="display:flex;flex-wrap:wrap;gap:14px">{''.join(f'<span class="chip" style="font-size:32px">{t}</span>' for t in ['Spearman','Gardner','Sternberg','CHC','Neuroscience'])}</div>''',2,T))
S.append(slide(f'''{head('THEORY 1',f'Spearman’s g factor {zs("一般智力因素",36)}',80)}{GROW}
{duo(('🌐','g factor','一般智力','<b>General intelligence</b>: the ability to reason and solve problems.'),('🎯','s factor','特殊智力','<b>Specific intelligence</b>: the ability to excel in certain areas.'),40)}
<div style="margin-top:24px">{card('Spearman believed being better at one type <b>predicts</b> being better overall.',size=38)}</div>{GROW}
{ex('⚠️ Criticism: <b>oversimplified</b> intelligence.',38)}''',3,T))
GM=['🗣️ Linguistic','🔢 Logical-mathematical','🧩 Spatial','🎵 Musical','🏃 Bodily-kinaesthetic','🤝 Interpersonal','🪞 Intrapersonal','🌿 Naturalist','🌌 Existential']
gm=''.join(f'<div style="padding:16px 22px;border-radius:999px;background:{"#3D3A8C" if i%2 else "#FFFDF8"};color:{"#F7F3EC" if i%2 else "#1E1E2A"};border:2px solid #E4DDD0;font-size:32px;font-weight:700">{t}</div>' for i,t in enumerate(GM))
S.append(slide(f'''{head('THEORY 2',f'Gardner’s multiple intelligences {zs("多元智能",34)}',72)}
<p style="margin:20px 0 0;font-size:38px;line-height:1.42">Reason, logic and knowledge are <b>different aspects</b> of intelligence, alongside other abilities. <b>9 kinds</b> (originally 7):</p>{GROW}
<div style="display:flex;flex-wrap:wrap;gap:14px">{gm}</div>{GROW}
{card('Little or no evidence · these are <b>abilities</b>, not intelligence (Hunt, 2001)',k='⚠️ CRITICISMS',bg='#FBE3DB',size=34)}''',4,T))
S.append(slide(f'''{head('THEORY 3',f'Sternberg’s triarchic theory {zs("三元智力理论",34)}',74)}{GROW}
<div style="display:flex;flex-direction:column;gap:22px">
{card('Breaking a problem into <b>parts</b> to solve it. 📊 Acing a data-analysis question.',k='🔬 ANALYTICAL · 分析性',size=38)}
{card('Dealing with <b>new ideas</b> and finding new ways to solve problems. 🎨 Designing a new app.',k='💡 CREATIVE · 创造性',size=38)}
{card('Using information to <b>get along in life</b> and succeed. 🧭 Knowing how to talk to your boss.',k='🛠️ PRACTICAL · 实践性',bg='#FBE3DB',size=38)}</div>{GROW}''',5,T))
S.append(slide(f'''{head('THEORY 4',f'CHC theory {zs("卡特尔-霍恩-卡罗尔理论",32)}',90)}
<p style="margin:16px 0 0;font-size:36px;color:#5A5A66">Three researchers, one theory built step by step:</p>{GROW}
{vflow([('Raymond Cattell','Spearman’s student'),('Crystallised + fluid intelligence',''),('John Horn','Cattell’s student'),('Added other abilities',''),('John Carroll','3-tier model of abilities')],42)}{GROW}''',6,T))
S.append(slide(f'''{head('CHC · THE CORE','Crystallised vs fluid',90)}{GROW}
{duo(('📚','Crystallised','晶体智力','<b>Knowledge and skills</b> you have acquired. Your SPM vocab and formulas.'),('🌊','Fluid','流体智力','<b>Problem solving and adapting</b> in unfamiliar situations. A puzzle you’ve never seen.'),38)}
<div style="margin-top:24px">{card('Also: visual and auditory processing, memory, processing speed, reaction time, quantitative and reading-writing skills. The <b>most researched and supported</b> theory; many new IQ tests use it.',size=32)}</div>{GROW}''',7,T))
S.append(slide(f'''{head('THEORY 5',f'Neuroscience: P-FIT {zs("顶叶-额叶整合理论",32)}',80)}{GROW}
{card('<b>Parieto-Frontal Integration Theory</b>: <b>frontal</b> and <b>parietal</b> brain areas play key roles in intelligence.',k='🧠 THE IDEA',size=42)}
<div style="margin-top:26px">{card('Posterior cingulate cortex, insular cortex and some areas deep in the brain.',k='ALSO INVOLVED',size=38)}</div>
<div style="margin-top:26px">{ex('🔗 <b>Working memory</b> (工作记忆) is linked to <b>fluid intelligence</b>.',40)}</div>{GROW}''',8,T))
S.append(slide(f'''{head('CHEAT SHEET','Save this 📌',90)}
<div style="margin-top:24px">{rows([('Spearman','g (general) + s (specific)'),('Gardner','9 intelligences; weak evidence'),('Sternberg','Analytical · creative · practical'),('CHC','Crystallised + fluid; most supported'),('P-FIT','Frontal + parietal brain areas')],38,260)}</div>{GROW}''',9,T))
S.append(last(f'''<div class="lab">YOUR TURN</div>
<h1 style="margin-top:30px;font-size:86px">Analytical, creative or practical: which is <span style="font-style:italic;color:#C24A2B">your</span> strongest?</h1>
<p style="margin:28px 0 0;font-size:44px;line-height:1.4">💬 Comment below</p>{GROW}
{nextup('How is IQ actually calculated?')}''',T))
write(S)
