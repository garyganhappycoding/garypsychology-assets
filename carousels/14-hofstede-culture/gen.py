# Personality Part 2 · 2/4 · Hofstede's cultural dimensions. Run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from series import *
T=9;S=[]
S.append(cover('PERSONALITY 2 · 2 OF 4',
 'Why does calling your lecturer by his <span style="font-style:italic;color:#C24A2B">first name</span> feel wrong?',
 'Culture shapes personality too. Hofstede found 4 ways cultures differ.',badge('🌏',240),96))
S.append(slide(f'''{head('GEERT HOFSTEDE','4 dimensions of culture',84)}
<div style="margin-top:12px">{zs("文化人格的四个维度",40)}</div>{GROW}
{grid([('👥','Individualism vs collectivism','个人主义 vs 集体主义','Me first, or the group first?'),('🪜','Power distance','权力距离','How much do we accept that power sits at the top?'),('🏆','Masculinity vs femininity','男性化 vs 女性化','Compete, or care?'),('📏','Uncertainty avoidance','不确定性规避','How much do we need clear rules?')],32)}{GROW}''',2,T))
S.append(slide(f'''{head('DIMENSION 1','Me, or us?',96)}
<div style="margin-top:28px">{duo(('🧍','Individualistic','个人主义','Values <b>autonomy</b>, change, youth, individual security and <b>equality</b>.'),('👨‍👩‍👧','Collectivistic','集体主义','Values <b>duty</b>, order, tradition, <b>respect for elders</b>, group security and hierarchy.'),36)}</div>{GROW}
{ex('🎓 Did you choose your course for <b>you</b>, or for your <b>family</b>?',44)}''',3,T))
S.append(concept(4,T,'DIMENSION 2','Power distance','权力距离','🪜',
 'How much less powerful people <b>accept and expect</b> power to be held by a few, not shared equally.',
 '<b>High:</b> it’s “Dr Tan”, and you don’t question him in class.<br><b>Low:</b> you call him “Kevin” and debate him openly.',exk='← THE HOOK'))
S.append(slide(f'''{head('DIMENSION 3','Compete, or care?',96)}
<div style="margin-top:30px">{duo(('🏆','“Masculine” cultures','男性化文化','<b>Assertive</b> and <b>competitive</b>, more so for men.'),('🤲','“Feminine” cultures','女性化文化','More <b>modest</b> and <b>caring</b>, for men and women.'),38)}</div>{GROW}
<div style="font-size:32px;color:#5A5A66;line-height:1.4">These are Hofstede’s labels for cultures, not for individual people.</div>''',5,T))
S.append(slide(f'''{head('DIMENSION 4',f'Uncertainty avoidance {zs("不确定性规避",36)}',74)}
<p style="margin:22px 0 0;font-size:40px;line-height:1.4">How comfortable a culture is with <b>uncertainty</b> and unstructured situations.</p>{GROW}
{duo(('📏','Less tolerant','低容忍','<b>Strict rules</b>, lots of safety measures, leans towards “One Truth”.'),('🌈','More tolerant','高容忍','Open to different opinions, <b>fewer rules</b>, different religions side by side, less anxious.'),36)}{GROW}''',6,T))
qs=[('Your group project gets credit, not you, and that feels fair.','Collectivism'),('You ask your manager before every small decision.','High power distance'),('The exam rules are printed on 5 pages.','Low tolerance of uncertainty')]
qq=''.join(f'<div style="padding:24px 30px;border-radius:24px;background:#FFFDF8;border:2px solid #E4DDD0"><div style="font-size:38px;line-height:1.35">{i+1}. {q}</div><div style="margin-top:10px;font-size:30px;font-weight:700;color:#C24A2B">→ {a}</div></div>' for i,(q,a) in enumerate(qs))
S.append(slide(f'''{head('QUICK QUIZ','Which dimension? 🤔',90)}{GROW}
<div style="display:flex;flex-direction:column;gap:22px">{qq}</div>{GROW}''',7,T))
S.append(slide(f'''{head('CHEAT SHEET','Save this 📌',90)}
<div style="margin-top:26px">{rows([('Individualism','Autonomy, equality, change'),('Collectivism','Duty, tradition, elders, hierarchy'),('Power distance','Accepting power held by a few'),('Masc. vs fem.','Assertive and competitive vs modest and caring'),('Uncertainty avoidance','Need for rules vs comfort with ambiguity')],38,350)}</div>{GROW}''',8,T))
S.append(last(f'''<div class="lab">YOUR TURN</div>
<h1 style="margin-top:30px;font-size:88px">Which dimension describes <span style="font-style:italic;color:#C24A2B">your family</span> best?</h1>
<p style="margin:28px 0 0;font-size:44px;line-height:1.4">💬 Comment below</p>{GROW}
{nextup('Is MBTI actually legit?')}
{save_btn('📌 Save for your PSY111 exam')}''',T))
write(S)
