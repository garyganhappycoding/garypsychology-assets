# Emotion · 2/3 · Facial feedback, amygdala, brain and emotion regulation. Run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from series import *
T=9;S=[]
S.append(cover('EMOTION · 2 OF 3',
 'Can smiling actually make you <span style="font-style:italic;color:#C24A2B">happier?</span>',
 'What your face and your brain do when you feel something.',badge('🙂',250),110))
S.append(slide(f'''{head('THEORY 6',f'Facial feedback hypothesis {zs("面部反馈假说",34)}',74)}
<p style="margin:20px 0 0;font-size:40px;line-height:1.42">Your <b>facial expression</b> sends feedback to your brain, which <b>causes and intensifies</b> the emotion.</p>{GROW}
{vflow([('See the dog 🐕',''),('Your face shows fear 😨',''),('Brain reads your face','feedback'),('Fear gets stronger','')],40)}{GROW}
<div style="font-size:28px;color:#8A7F74">Tested by Strack, Martin &amp; Stepper (1988)</div>''',2,T))
S.append(slide(f'''{head('← THE ANSWER','So, does smiling work?',88)}{GROW}
<div style="font-family:Fraunces,serif;font-size:110px;text-align:center">🙂 → 😄</div>
<div style="margin-top:30px">{card('According to this hypothesis, <b>yes</b>: the more you smile, the happier you can feel.',size=46)}</div>
<div style="margin-top:26px">{ex('Bonus: facial expressions seem to be <b>universal</b> (普遍的). A smile reads as happy across cultures.',40)}</div>{GROW}''',3,T))
S.append(concept(4,T,'THE BRAIN','Amygdala','杏仁核','🧠',
 'Linked to <b>fear</b> and <b>pleasure</b>, and to <b>recognising facial expressions</b>.',
 'Emotional signals reach it by <b>two roads</b>. Next slide 👉',exk='HOW SIGNALS GET THERE'))
S.append(slide(f'''{head('YOU SEE A SHARK 🦈','Low road vs high road',86)}{GROW}
{duo(('⚡','Low road','低通路','<b>Fast and rough.</b> Below the cortex. You react before you even know what it is.<br><br>“<b>DANGER!</b>”'),('🔍','High road','高通路','<b>Slower, more detailed.</b> Through the cortex. You recognise it and can take control.<br><br>“It’s a <b>shark</b>.”'),36)}{GROW}
<div style="font-size:36px;line-height:1.4">The low road shouts first. The high road explains later.</div>''',5,T))
S.append(slide(f'''{head('LEFT VS RIGHT','Emotion in the brain',88)}{GROW}
{duo(('😊','Left frontal lobe','左额叶','Linked to <b>positive</b> emotions.'),('😟','Right frontal lobe','右额叶','Linked to <b>negative</b> emotions.'),40)}
<div style="margin-top:26px">{ex('The <b>right hemisphere</b> is more active when you read emotions from <b>faces</b>. (Davidson, 2003)',40)}</div>{GROW}''',6,T))
S.append(slide(f'''{head('CALMING DOWN',f'Regulating emotions {zs("情绪调节",36)}',80)}{GROW}
{duo(('🎧','Distraction','分心','Uses the <b>anterior cingulate cortex</b> (前扣带皮层).<br><br>Before an exam: listen to music.'),('🔄','Reappraisal','重新评估','Uses the <b>lateral orbitofrontal cortex</b> (外侧眶额皮层).<br><br>Before an exam: “nervous means I care.”'),34)}
<div style="margin-top:24px">{ex('Both strategies come with <b>lower amygdala activity</b>.',40)}</div>{GROW}''',7,T))
S.append(slide(f'''{head('CHEAT SHEET','Save this 📌',90)}
<div style="margin-top:26px">{rows([('Facial feedback','Expression → brain → stronger emotion'),('Amygdala','Fear, pleasure, reading faces'),('Low road','Fast, rough, before awareness'),('High road','Slower, conscious control'),('Left / right','Positive / negative emotions'),('Regulation','Distraction or reappraisal')],38,330)}</div>{GROW}''',8,T))
S.append(last(f'''<div class="lab">YOUR TURN</div>
<h1 style="margin-top:30px;font-size:90px"><span style="color:#3D3A8C">Distraction</span> or <span style="color:#C24A2B">reappraisal</span>: which do you use?</h1>
<p style="margin:28px 0 0;font-size:44px;line-height:1.4">💬 Comment below</p>{GROW}
{nextup('Why do Chinese parents say “have you eaten?” instead of “I love you”?')}''',T))
write(S)
