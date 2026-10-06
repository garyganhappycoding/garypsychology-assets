# Emotion · 3/3 · Labelling emotion, culture (Tsai et al., 2004). Run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from series import *
T=8;S=[]
S.append(cover('EMOTION · 3 OF 3',
 'Why do Chinese parents say “<span style="font-style:italic;color:#C24A2B">have you eaten?</span>” instead of “I love you”?',
 'Culture changes how we put feelings into words.',badge('🍚',230),88))
S.append(concept(2,T,'THE THINKING PART','Labelling emotion','情绪标签','🏷️',
 'Making sense of a feeling by <b>giving it a name</b>. It’s a <b>learned</b> skill, shaped by your <b>language and culture</b>.',
 'Two people can feel the same thing and describe it in completely different words.',exk='WHY IT MATTERS'))
S.append(slide(f'''{head('THE STUDY','Tsai et al. (2004)',96)}
<p style="margin:22px 0 0;font-size:40px;line-height:1.42">Researchers compared how different groups in the US <b>talk about emotion</b>.</p>{GROW}
{bullets(['<b>Chinese Americans</b> still firmly rooted in Chinese culture','<b>More “Americanised”</b> Chinese Americans','<b>European Americans</b>'],size=44,gap=30)}{GROW}''',3,T))
S.append(slide(f'''{head('WHAT THEY FOUND','Two ways to say it',90)}{GROW}
{duo(('🫀','Body &amp; relationships','身体与关系','More traditional Chinese Americans used words about <b>body sensations</b> (“dizzy”) or <b>relationships</b> (“friendship”).'),('💬','Direct emotion words','直接情绪词','More Americanised Chinese Americans and European Americans used words like <b>“liking”</b> and <b>“love”</b>.'),36)}{GROW}''',4,T))
S.append(slide(f'''{head('← BACK TO THE HOOK','“Have you eaten?” 🍚',90)}{GROW}
{card('In many Chinese families, care is said through <b>everyday actions and relationships</b>: feeding you, asking if you’ve eaten, telling you to wear more clothes.',size=44)}
<div style="margin-top:28px">{ex('That fits the study: feelings expressed through <b>the body and relationships</b>, not direct emotion words.',42)}</div>{GROW}''',5,T))
S.append(slide(f'''{head('FOR FUTURE PSYCHOLOGISTS','Listen beyond the words',84)}{GROW}
{card('Someone who says they feel <b>“tired”</b> or have a <b>“heavy chest”</b> may be describing an emotion, not just a body feeling.',size=44)}
<div style="margin-top:28px">{ex('Understanding <b>cultural differences</b> helps psychologists and counsellors understand clients better.',42)}</div>{GROW}''',6,T))
S.append(slide(f'''{head('EMOTION · MODULE RECAP','Save this 📌',90)}
<div style="margin-top:24px">{rows([('3 parts','Arousal · behaviour · inner label'),('Theories','Common sense · James-Lange · Cannon-Bard · facial feedback · Schachter-Singer · Lazarus'),('Brain','Amygdala: low road and high road'),('Culture','Shapes how we label feelings')],38,250)}</div>{GROW}''',7,T))
S.append(last(f'''<div class="lab">YOUR TURN</div>
<h1 style="margin-top:30px;font-size:84px">How does your family say “I love you” <span style="font-style:italic;color:#C24A2B">without saying it?</span></h1>
<p style="margin:28px 0 0;font-size:44px;line-height:1.4">💬 Comment below 🍚</p>{GROW}
{nextup('New module: Intelligence. Is there only one way to be smart?')}''',T))
write(S)
