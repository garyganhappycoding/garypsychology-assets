# Personality series 4/6 · Locus of control, self-efficacy. Run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from series import *
from toons import clover,blame_kid,person,wrap,triangle
T=9;S=[]
S.append(cover('PERSONALITY · PART 4 OF 6',
 'Did you fail because of <span style="font-style:italic;color:#5E9E6E">bad luck</span>, or because of <span style="font-style:italic;color:#C24A2B">you?</span>',
 'Your answer says a lot about your personality.',clover(240),96))
def stu(shirt,quote,lab):
    return f'''<div style="flex:1;padding:30px;border-radius:28px;background:#FFFDF8;border:2px solid #E4DDD0;display:flex;flex-direction:column;align-items:center;gap:16px">
{wrap(person(120,shirt),190,190)}<div class="k" style="margin:0">{lab}</div><div style="font-family:Fraunces,serif;font-style:italic;font-size:44px;line-height:1.2;text-align:center">{quote}</div></div>'''
S.append(slide(f'''{head('TWO STUDENTS, ONE QUIZ','Both failed. 📝',96)}{GROW}
<div style="display:flex;gap:28px">{stu('#3D3A8C','“I didn’t revise enough.”','STUDENT A')}{stu('#F2785C','“The questions were just unlucky.”','STUDENT B')}</div>{GROW}
{ex('The <b>social cognitive view</b> (社会认知观) explains the difference. 👉',44)}''',2,T))
S.append(slide(f'''{head('ROTTER',f'Locus of control {zs("控制点",44)}',84)}{GROW}
<div style="display:flex;gap:26px">
<div style="flex:1;padding:34px;border-radius:28px;background:#3D3A8C;color:#F7F3EC"><div style="font-size:90px">🫵</div><div style="font-family:Fraunces,serif;font-weight:700;font-size:56px;margin-top:10px">Internal</div><div style="font-size:30px;color:#C9C6EA">内控</div><div style="margin-top:18px;font-size:38px;line-height:1.38">Outcomes come from <b>my own actions</b></div><div style="margin-top:18px;font-size:34px;color:#F2B8A6;font-weight:700">= Student A</div></div>
<div style="flex:1;padding:34px;border-radius:28px;background:#FBE3DB"><div style="font-size:90px">🍀</div><div style="font-family:Fraunces,serif;font-weight:700;font-size:56px;margin-top:10px">External</div><div style="font-size:30px;color:#8A7F74">外控</div><div style="margin-top:18px;font-size:38px;line-height:1.38">Outcomes come from <b>fate or other people</b></div><div style="margin-top:18px;font-size:34px;color:#C24A2B;font-weight:700">= Student B</div></div></div>{GROW}''',3,T))
S.append(slide(f'''{head('ROTTER’S SOCIAL LEARNING THEORY','2 factors behind your choices',74)}{GROW}
{card('Do I believe a reward will follow if I act?',k='① EXPECTANCY · 期望',size=46)}
<div style="margin-top:28px">{card('How much do I want <b>this</b> reward over others?',k='② REINFORCEMENT VALUE · 强化值',size=46)}</div>{GROW}
{ex('📚 “If I revise, will I pass? And do I even care about getting an A?”',44)}''',4,T))
S.append(slide(f'''{head('BANDURA',f'Self-efficacy {zs("自我效能",44)}',90)}{GROW}
{card('Your expectation of <b>how effective your efforts will be</b> in reaching a goal.',k='WHAT IT IS',size=48)}
<div style="margin-top:28px">{card('🔁 <b>Past experience</b><br>💪 <b>How competent you feel</b>, from yourself and from what others tell you',k='SHAPED BY',size=44)}</div>{GROW}
{ex('“I passed the last quiz, so I can do this one.” = high self-efficacy',42)}''',5,T))
S.append(slide(f'''{head('BANDURA',f'Reciprocal determinism {zs("交互决定论",40)}',74)}
<div style="position:relative;margin-top:30px;height:520px;display:flex;justify-content:center">{triangle(560)}
<div style="position:absolute;top:0;left:50%;transform:translateX(-50%);font-size:34px;font-weight:700;background:#F7F3EC;padding:4px 14px">Behaviour</div>
<div style="position:absolute;bottom:20px;left:0;font-size:34px;font-weight:700;background:#F7F3EC;padding:4px 14px">Environment</div>
<div style="position:absolute;bottom:20px;right:0;font-size:34px;font-weight:700;background:#F7F3EC;padding:4px 14px;text-align:right">Personal /<br>cognitive</div></div>
<p style="margin:10px 0 0;font-size:40px;line-height:1.4">All three <b>influence each other</b>, both ways.</p>{GROW}
{ex('🔁 Noisy hostel → you study less → your confidence drops → you avoid the library',40)}''',6,T))
S.append(slide(f'''{head('VS BEHAVIOURISM','What’s the difference?',84)}{GROW}
{card('Personality = <b>learned responses</b> (习得反应) from classical and operant conditioning. Mental processes aren’t enough to explain behaviour.',k='BEHAVIOURAL VIEW · SKINNER',size=42)}
<div style="margin-top:28px">{card('Adds your <b>thoughts and expectations</b>, plus learning by watching others: <b>observational learning</b> (观察学习).',k='SOCIAL COGNITIVE VIEW · BANDURA, ROTTER',bg='#FBE3DB',size=42)}</div>{GROW}''',7,T))
S.append(slide(f'''{head('CHEAT SHEET','Save this 📌',90)}
<div style="margin-top:30px">{rows([('Rotter','Locus of control · expectancy · reinforcement value'),('Bandura','Self-efficacy · reciprocal determinism'),('Criticism','Behaviourists ignore mental processes; overgeneralising can lead to errors'),('Contribution','Effective therapies')],40,320)}</div>{GROW}''',8,T))
S.append(last(f'''<div class="lab">BE HONEST</div>
<h1 style="margin-top:30px;font-size:96px"><span style="color:#3D3A8C">Internal</span> or <span style="color:#5E9E6E">external</span>?</h1>
<p style="margin:30px 0 0;font-size:44px;line-height:1.4">💬 Which are you? Comment below</p>{GROW}
{nextup('Why does being compared to your cousin hurt so much?')}
{save_btn('📌 Save for your PSY111 exam')}''',T))
write(S)
