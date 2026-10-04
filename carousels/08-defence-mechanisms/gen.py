# Personality series 2/6 · Defence mechanisms. Run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from series import *
from toons import blame_kid,shield,id_toon,superego_toon
T=9;S=[]
S.append(cover('PERSONALITY · PART 2 OF 6',
 'Why do we blame the <span style="font-style:italic;color:#C24A2B">lecturer</span> when we fail?',
 '5 ways your mind protects you without telling you.',blame_kid(240),104))
S.append(slide(f'''{head('WHERE THIS COMES FROM','Your mind has a <span style="font-style:italic;color:#3D3A8C">shield</span>',84)}
<div style="margin-top:40px;display:flex;align-items:center;gap:20px;justify-content:center">{id_toon(170)}<div style="font-family:Fraunces,serif;font-weight:800;font-size:60px;color:#C24A2B">VS</div>{superego_toon(170)}</div>
<p style="margin:30px 0 0;font-size:44px;line-height:1.42;text-align:center">When the <b>id</b> and <b>superego</b> clash → you feel anxious {zs("焦虑",32)}</p>{GROW}
<div style="display:flex;gap:30px;align-items:center"><div style="flex-shrink:0">{shield(190)}</div><div style="font-size:44px;line-height:1.42">So the mind uses <b>defence mechanisms</b> {zs("防御机制",32)}. They <b>unconsciously</b> {zs("无意识地",32)} bend how you see reality.</div></div>''',2,T))
def mech(n,lab,name,zh,emoji,defin,example):
    return slide(f'''<div style="display:flex;justify-content:space-between;align-items:flex-start"><div><div class="lab">{lab}</div>
<h1 style="margin-top:22px;font-size:104px">{name}</h1><div style="margin-top:14px">{zs(zh,54)}</div></div>
<div style="width:190px;height:190px;border-radius:50%;background:#FBE3DB;display:flex;align-items:center;justify-content:center;font-size:110px">{emoji}</div></div>
{GROW}{card(defin,k='WHAT IT IS',size=50)}<div style="margin-top:34px">{card(example,k='STUDENT EXAMPLE',bg='#FBE3DB',size=50)}</div>{GROW}''',n,T)
M=[('DEFENCE 1 OF 5','Denial','否认','🙈','Refusing to accept a <b>threatening situation</b>.','“My grades are fine.” <i>(They aren’t.)</i>'),
   ('DEFENCE 2 OF 5','Repression','压抑','😶','Pushing a painful memory <b>out of conscious awareness</b>.','You can’t remember anything about the presentation that went badly.'),
   ('DEFENCE 3 OF 5','Rationalisation','合理化','🙃','Making up an <b>acceptable excuse</b> for a mistake.','“The lecturer set an unfair paper. That’s why I failed.”'),
   ('DEFENCE 4 OF 5','Displacement','转移','😤','Taking your emotions out on a target that <b>didn’t cause them</b>.','Scolded by your lecturer → you snap at your younger brother.'),
   ('DEFENCE 5 OF 5','Sublimation','升华','🥊','Turning socially <b>unacceptable</b> urges into <b>acceptable</b> behaviour.','Anger → a hard gym session or a boxing class.')]
for i,m in enumerate(M): S.append(mech(i+3,*m))
S.append(slide(f'''{head('CHEAT SHEET','5 defences, 1 line each 📌',80)}
<div style="margin-top:30px">{rows([('Denial','“It’s not happening”'),('Repression','Forgotten'),('Rationalisation','An excuse'),('Displacement','The wrong target'),('Sublimation','Turned into something good')],42,390)}</div>{GROW}
{card('All 5 are <b>unconscious</b>.',k='💡 EXAM TIP',bg='#FBE3DB',size=44)}''',8,T))
S.append(last(f'''<div class="lab">YOUR TURN</div>
<h1 style="margin-top:30px;font-size:90px">Which one do <span style="font-style:italic;color:#3D3A8C">you</span> use the most?</h1>
<p style="margin:30px 0 0;font-size:44px;line-height:1.4">💬 Comment the defence below</p>{GROW}
{nextup('Freud’s strangest theory, and why many psychologists don’t buy it')}
{save_btn('📌 Save for your PSY111 exam')}''',T))
write(S)
