# Intelligence · 2/5 · Measuring intelligence, IQ formula, Wechsler, deviation IQ. Run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from series import *
import math
def bell(w=900):
    pts=' '.join(f'{60+i*7:.0f},{300-250*math.exp(-((i-100)/34)**2/2):.1f}' for i in range(201))
    ticks=''.join(f'<path d="M{60+(100+k*34)*7} 300 V316" stroke="#1E1E2A" stroke-width="3"/><text x="{60+(100+k*34)*7}" y="378" text-anchor="middle" font-size="54" font-weight="800" fill="{"#C24A2B" if k in (-2,2) else "#1E1E2A"}">{100+k*15}</text>' for k in (-2,-1,0,1,2))
    return (f'<svg width="{w}" height="{int(w*0.42)}" viewBox="0 0 1520 400" font-family="Manrope">'
            f'<polygon points="60,300 {pts} 1460,300" fill="#DCDAF0"/><polyline points="{pts}" fill="none" stroke="#3D3A8C" stroke-width="8"/>'
            f'<path d="M30 300 H1490" stroke="#1E1E2A" stroke-width="4"/>{ticks}</svg>')
T=9;S=[]
S.append(cover('INTELLIGENCE · 2 OF 5',
 'How is IQ <span style="font-style:italic;color:#C24A2B">actually</span> calculated?',
 'From a French school problem to the tests used today.',badge('🔢',240),112))
S.append(slide(f'''{head('WHERE IT STARTED','Binet &amp; Simon',96)}{GROW}
{card('France’s <b>Ministry of Education</b> asked <b>Alfred Binet</b> and Théodore Simon for a test to find children who learned more slowly and needed <b>remedial education</b> (补救教育).',size=42)}
<div style="margin-top:28px">{ex('Fast learners gave answers like <b>older</b> children. Slow learners gave answers like <b>younger</b> children.',42)}</div>{GROW}''',2,T))
S.append(concept(3,T,'BINET’S KEY IDEA','Mental age','心理年龄','🧒',
 'The <b>average age</b> at which children can successfully answer a particular level of question.',
 'An 8-year-old who answers like a typical 10-year-old has a mental age of <b>10</b>.'))
S.append(slide(f'''{head('THE FORMULA',f'Intelligence quotient {zs("智商 IQ",40)}',80)}
<p style="margin:18px 0 0;font-size:36px;line-height:1.42"><b>Lewis Terman</b> revised Binet’s test (Stanford-Binet) using <b>William Stern</b>’s method.</p>{GROW}
<div style="padding:44px;border-radius:32px;background:#3D3A8C;color:#F7F3EC;text-align:center;font-family:Fraunces,serif;font-weight:700;font-size:84px">IQ = <span style="display:inline-block;vertical-align:middle;text-align:center;font-size:60px;line-height:1.1"><span style="display:block;border-bottom:5px solid #F7F3EC;padding:0 16px">MA</span><span style="display:block;padding:0 16px">CA</span></span> × 100</div>
<div style="margin-top:22px;font-size:34px;text-align:center;color:#5A5A66">MA = mental age (心理年龄) · CA = chronological age (实际年龄)</div>{GROW}''',4,T))
ex1=[('10-year-old, mental age 12','12 ÷ 10 × 100','120'),('10-year-old, mental age 8','8 ÷ 10 × 100','80')]
e1=''.join(f'<div style="display:flex;align-items:center;gap:24px;padding:26px 30px;border-radius:26px;background:#FFFDF8;border:2px solid #E4DDD0"><div style="flex:1"><div style="font-size:34px;font-weight:700">{a}</div><div style="font-size:34px;color:#5A5A66;margin-top:6px">{b}</div></div><div style="font-family:Fraunces,serif;font-weight:800;font-size:80px;color:#C24A2B">{c}</div></div>' for a,b,c in ex1)
S.append(slide(f'''{head('TRY IT','Two quick examples 🧮',90)}{GROW}
<div style="display:flex;flex-direction:column;gap:24px">{e1}</div>{GROW}
{ex('It only works up to about age <b>16</b>. A 40-year-old with a “mental age of 30” doesn’t make sense.',40)}''',5,T))
S.append(slide(f'''{head('TODAY’S TESTS','Wechsler scales',96)}
<div style="margin-top:22px;display:flex;gap:14px">{''.join(f'<div style="flex:1;padding:20px;border-radius:22px;background:#3D3A8C;color:#F7F3EC;text-align:center"><div style="font-family:Fraunces,serif;font-weight:800;font-size:46px">{a}</div><div style="font-size:26px;margin-top:4px">{b}</div></div>' for a,b in [('WAIS','Adults'),('WISC','Children'),('WPPSI','Preschool')])}</div>
<p style="margin:26px 0 0;font-size:36px;line-height:1.42">Verbal and non-verbal items → one <b>overall score</b> plus <b>5 index scores</b>:</p>{GROW}
{bullets(['Verbal comprehension','Visual spatial','Fluid reasoning','Working memory','Processing speed'],size=40,gap=18)}{GROW}''',6,T))
S.append(slide(f'''{head('HOW IT’S SCORED NOW',f'Deviation IQ {zs("离差智商",40)}',84)}
<p style="margin:18px 0 0;font-size:38px;line-height:1.42">Your score is compared with <b>people your age</b>. Scores form a normal curve: <b>mean 100</b>, <b>standard deviation about 15</b>.</p>{GROW}
<div style="display:flex;justify-content:center">{bell(900)}</div>{GROW}
{ex('<b>130</b> = 2 SDs above the mean<br><b>70</b> = 2 SDs below the mean',40)}''',7,T))
S.append(slide(f'''{head('CHEAT SHEET','Save this 📌',90)}
<div style="margin-top:24px">{rows([('Binet','Find kids needing extra help'),('Mental age','Level a child answers at'),('IQ formula','MA ÷ CA × 100 (to ~16)'),('Wechsler','WAIS · WISC · WPPSI; 5 index scores'),('Deviation IQ','Mean 100, SD 15')],38,280)}</div>{GROW}''',8,T))
S.append(last(f'''<div class="lab">YOUR TURN</div>
<h1 style="margin-top:30px;font-size:90px">Have you ever taken an <span style="font-style:italic;color:#C24A2B">IQ test?</span></h1>
<p style="margin:28px 0 0;font-size:44px;line-height:1.4">💬 Online quiz or a real one?</p>{GROW}
{nextup('Dog, car, cat, bird, fish: which one doesn’t belong?')}''',T))
write(S)
