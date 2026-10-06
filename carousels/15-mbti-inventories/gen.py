# Personality Part 2 · 3/4 · Personality inventories (MBTI, NEO-PI-3, MMPI-3). Run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from series import *
T=9;S=[]
S.append(cover('PERSONALITY 2 · 3 OF 4',
 'Is <span style="font-style:italic;color:#C24A2B">MBTI</span> actually legit?',
 'And what psychologists use to measure personality instead.',badge('🧾',240),120))
S.append(slide(f'''{head('FIRST','Why measure personality?',84)}{GROW}
{card('Psychologists take an <b>eclectic view</b> (折衷观): they pick the parts of different theories that fit the situation, instead of sticking to one.',k='HOW PROS THINK',size=42)}
<div style="margin-top:28px">{duo(('🔬','Researchers','研究者','Sort participants into <b>personality traits</b>.'),('🩺','Clinical &amp; counselling psychologists','临床与咨询心理学家','Diagnose <b>personality disorders</b> (人格障碍).'),34)}</div>{GROW}''',2,T))
S.append(slide(f'''{head('THE TOOLKIT','4 types of assessment',84)}{GROW}
{grid([('🎤','Interviews','面谈','Ask questions, let the client answer.'),('👀','Behavioural assessments','行为评估','Watch and count real behaviour.'),('📝','Personality inventories','人格量表','Standard questionnaires. <b>Today’s post.</b>'),('🎨','Projective tests','投射测验','Inkblots and pictures. <b>Next post.</b>')],32)}{GROW}''',3,T))
S.append(concept(4,T,'TODAY’S TOOL','Personality inventory','人格量表','📝',
 'A questionnaire with a <b>standard list of statements</b>. You answer yes/no or true/false, on paper or a computer. A form of <b>self-report</b> (自我报告), loved by trait theorists.',
 '16PF · NEO-PI-3 · MBTI · EPQ · Keirsey · CPI · MMPI',exk='EXAMPLES FROM THE LECTURE',size=86))
mb=''.join(f'<div style="flex:1;padding:44px 10px;border-radius:24px;background:#3D3A8C;color:#F7F3EC;text-align:center"><div style="font-family:Fraunces,serif;font-weight:800;font-size:62px">{a}</div><div style="font-size:28px;margin-top:12px;line-height:1.35">{b}</div></div>' for a,b in [('I / E','Introversion<br>Extraversion'),('S / N','Sensing<br>Intuition'),('T / F','Thinking<br>Feeling'),('P / J','Perceiving<br>Judging')])
S.append(slide(f'''{head('THE FAMOUS ONE',f'MBTI {zs("迈尔斯-布里格斯类型指标",34)}',96)}
<p style="margin:20px 0 0;font-size:38px;line-height:1.4">Based on <b>Carl Jung</b>’s ideas. 4 dimensions → <b>16 types</b>. Often used for <b>career guidance</b>.</p>
{GROW}<div style="display:flex;gap:16px">{mb}</div>{GROW}
{card('Psychologists point out <b>limits in its validity</b> (效度) <b>and reliability</b> (信度). Fun for self-reflection, but not the strongest tool.',k='⚠️ THE CATCH',bg='#FBE3DB',size=40)}''',5,T))
S.append(concept(6,T,'THE BIG FIVE TEST','NEO-PI-3','大五人格量表','🌊',
 'Named after <b>N</b>euroticism, <b>E</b>xtraversion and <b>O</b>penness. A <b>detailed</b> test of all five Big Five traits (OCEAN), with <b>240 items</b>.',
 'Remember my Big Five post? This is one way psychologists actually measure it.',exk='🔁 CONNECTS TO'))
S.append(slide(f'''{head('THE CLINICAL ONE',f'MMPI-3 {zs("明尼苏达多相人格问卷",34)}',96)}
<p style="margin:20px 0 0;font-size:40px;line-height:1.4">Tests for <b>abnormal behaviour and thinking patterns</b> in personality and <b>psychopathology</b> {zs("精神病理学",28)}.</p>{GROW}
<div style="display:flex;gap:22px">
<div style="flex:1;padding:30px;border-radius:26px;background:#3D3A8C;color:#F7F3EC;text-align:center"><div style="font-family:Fraunces,serif;font-weight:800;font-size:88px">335</div><div style="font-size:30px">statements</div></div>
<div style="flex:1.4;padding:30px;border-radius:26px;background:#FBE3DB"><div style="font-size:58px">🕵️</div><div style="font-size:34px;line-height:1.38;margin-top:8px"><b>10 validity scales</b> catch people who over- or under-report.</div></div></div>
<div style="margin-top:24px;font-size:34px;line-height:1.4">Also used for <b>job screening</b> and career guidance.</div>{GROW}''',7,T))
S.append(slide(f'''{head('VERDICT','Inventories: pros vs cons',80)}{GROW}
{duo(('✅','Pros','优点','<b>Standardised</b> and more objective · computer scoring avoids bias · much better validity and reliability'),('⚠️','Cons','缺点','People <b>fake</b> socially acceptable answers · read questions differently · answer in different styles'),34)}{GROW}''',8,T))
S.append(last(f'''<div class="lab">YOUR TURN</div>
<h1 style="margin-top:30px;font-size:92px">What’s your <span style="font-style:italic;color:#C24A2B">MBTI?</span> 👀</h1>
<p style="margin:28px 0 0;font-size:44px;line-height:1.4">💬 Comment your 4 letters. Does it feel accurate?</p>{GROW}
{nextup('What do you see in this inkblot?')}
{save_btn('📌 Save for your PSY111 exam')}''',T))
write(S)
