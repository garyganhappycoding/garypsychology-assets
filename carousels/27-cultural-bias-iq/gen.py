# Intelligence · 3/5 · Cultural bias, reliability, validity, standardisation, usefulness. Run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from series import *
def matrix(w=420):
    # original 3x3 pattern puzzle: shapes rotate along rows, fill darkens down columns
    sh=['<circle cx="0" cy="0" r="34"/>','<rect x="-32" y="-32" width="64" height="64" rx="6"/>','<polygon points="0,-38 36,30 -36,30"/>']
    fills=['#FFFDF8','#C9C6EA','#3D3A8C']
    cells=''
    for r in range(3):
        for c in range(3):
            x=70+c*140;y=70+r*140
            cells+=f'<rect x="{x-62}" y="{y-62}" width="124" height="124" rx="16" fill="#F7F3EC" stroke="#E4DDD0" stroke-width="4"/>'
            if (r,c)==(2,2): cells+=f'<text x="{x}" y="{y+26}" text-anchor="middle" font-family="Fraunces" font-weight="800" font-size="76" fill="#C24A2B">?</text>'
            else: cells+=f'<g transform="translate({x} {y})" fill="{fills[r]}" stroke="#1E1E2A" stroke-width="5">{sh[(c+r)%3]}</g>'
    return f'<svg width="{w}" height="{w}" viewBox="0 0 420 420">{cells}</svg>'
T=9;S=[]
words=''.join(f'<span style="padding:16px 26px;border-radius:20px;background:#3D3A8C;color:#F7F3EC;font-family:Fraunces,serif;font-weight:800;font-size:72px">{w}</span>' for w in ['DOG','CAR','CAT','BIRD','FISH'])
S.append(f'''<div class="s"><div class="lab">INTELLIGENCE · 3 OF 5</div>
<h1 style="margin-top:20px;font-size:98px">Which one <span style="font-style:italic;color:#C24A2B">doesn’t belong?</span></h1>
<div style="flex-grow:1"></div><div style="display:flex;flex-wrap:wrap;gap:18px;justify-content:center">{words}</div><div style="flex-grow:1"></div>
<p style="margin:0;font-size:42px;line-height:1.3;color:#4A4A56">Pick one before you swipe. Your answer may depend on your culture.</p>{swipe()}</div>''')
S.append(slide(f'''{head('THE PROBLEM','More than one “right” answer',80)}{GROW}
{grid([('🚗','CAR','汽车','The only thing that isn’t an animal.'),('🐟','FISH','鱼','The only one that lives in water.'),('🐦','BIRD','鸟','The only one that flies.'),('🐶','DOG / CAT','狗 / 猫','Depends what you count as a “pet”.')],32)}{GROW}
{ex('The test designer had <b>one</b> answer in mind. You might reason differently.',40)}''',2,T))
S.append(concept(3,T,'THE ISSUE','Cultural bias','文化偏差','🌏',
 'When an IQ test reflects the <b>language, dialect and content</b> of the test designer’s culture.',
 'Someone raised in an Asian culture may find some items from a Western test don’t apply or don’t make sense.'))
S.append(slide(f'''{head('THE FIX',f'Culture-fair tests {zs("文化公平测验",36)}',84)}
<p style="margin:20px 0 0;font-size:40px;line-height:1.42">Use <b>non-verbal</b> abilities. E.g. <b>Raven’s Progressive Matrices</b> {zs("瑞文推理测验",28)}: find the pattern, fill the gap.</p>{GROW}
<div style="display:flex;justify-content:center">{matrix(600)}</div>{GROW}
<div style="font-size:30px;color:#8A7F74">An original puzzle in the same style, not a real Raven’s item.</div>''',4,T))
S.append(slide(f'''{head('GOOD TEST RULE 1 &amp; 2','Reliable vs valid',90)}{GROW}
{duo(('🔁','Reliability','信度','Gives the <b>same scores</b> again and again to the same people.'),('🎯','Validity','效度','Actually measures <b>what it’s supposed to</b> measure.'),40)}
<div style="margin-top:26px">{ex('⚖️ A scale that always shows you 5 kg heavier is <b>reliable</b>, but not <b>valid</b>.',40)}</div>{GROW}''',5,T))
S.append(concept(6,T,'GOOD TEST RULE 3','Standardisation','标准化','📊',
 'Giving the test to a <b>large group</b> that represents the people it’s designed for. Their scores become the <b>norms</b> (常模).',
 'Most tests end up following a <b>normal curve</b>, like the IQ bell curve from my last post.',exk='🔁 CONNECTS TO'))
S.append(slide(f'''{head('SO, ARE IQ TESTS USEFUL?','Yes, for some things',84)}{GROW}
{card('Generally valid for predicting <b>academic success</b> and <b>job performance</b>.',k='✅ PREDICTS',size=42)}
<div style="margin-top:26px">{card('In <b>neuropsychology</b>, to assess <b>head injuries</b>, <b>learning disabilities</b> and neuropsychological disorders.',k='🩺 USED FOR',bg='#FBE3DB',size=42)}</div>{GROW}''',7,T))
S.append(slide(f'''{head('CHEAT SHEET','Save this 📌',90)}
<div style="margin-top:24px">{rows([('Cultural bias','Test reflects the designer’s culture'),('Culture-fair','Non-verbal, e.g. Raven’s'),('Reliability','Same score every time'),('Validity','Measures what it should'),('Standardisation','Large representative group → norms')],38,330)}</div>{GROW}''',8,T))
S.append(last(f'''<div class="lab">YOUR TURN</div>
<h1 style="margin-top:30px;font-size:96px">So, which one did you <span style="font-style:italic;color:#C24A2B">pick?</span></h1>
<p style="margin:28px 0 0;font-size:44px;line-height:1.4">💬 Comment your answer and why</p>{GROW}
{nextup('Are smart kids born or made?')}''',T))
write(S)
