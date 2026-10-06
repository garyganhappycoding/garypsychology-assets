# Intelligence · 5/5 · Emotional intelligence + module recap. Run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from series import *
T=8;S=[]
S.append(cover('INTELLIGENCE · 5 OF 5',
 'Does <span style="font-style:italic;color:#C24A2B">EQ</span> matter more than <span style="font-style:italic;color:#3D3A8C">IQ?</span>',
 'What emotional intelligence is, and what it predicts.',badge('💛',250),120))
S.append(concept(2,T,'DEFINITION','Emotional intelligence','情绪智力 · 情商 EQ','💛',
 'Being <b>aware of</b> and able to <b>manage</b> your own emotions to help you think and reach goals, and being able to <b>understand what others feel</b>.',
 'Staying calm enough to finish a group project, and noticing when a groupmate is quietly stressed.',size=80))
S.append(slide(f'''{head('TWO SIDES','You, and other people',90)}{GROW}
{duo(('🪞','Your own emotions','自己的情绪','<b>Notice</b> what you feel, and <b>manage</b> it so it helps your thinking.'),('🤝','Other people’s','他人的情绪','<b>Understand</b> what others are feeling.'),40)}{GROW}''',3,T))
S.append(slide(f'''{head('WHAT IT PREDICTS','Higher EQ comes with…',84)}{GROW}
{bullets(['🧠 Higher <b>general intelligence</b>','🤝 Better <b>social relationships</b>','😊 Being seen <b>more positively</b> by others','📈 Better <b>academic and job performance</b>','🌿 Greater <b>psychological well-being</b>'],size=46,gap=32)}{GROW}''',4,T))
S.append(slide(f'''{head('← THE ANSWER','EQ vs IQ?',100)}{GROW}
{card('EQ is seen as a <b>powerful influence on success in life</b>, compared with traditional views of intelligence.',size=44)}
<div style="margin-top:28px">{ex('But it’s not either/or: higher EQ <b>goes together</b> with higher general intelligence. You want both. 🤝',44)}</div>{GROW}''',5,T))
S.append(slide(f'''{head('INTELLIGENCE · MODULE RECAP','Save this 📌',80)}
<div style="margin-top:22px">{rows([('Theories','Spearman · Gardner · Sternberg · CHC · P-FIT'),('Measuring','Binet → IQ = MA ÷ CA × 100 → Wechsler'),('Good tests','Reliable · valid · standardised · culture-fair'),('Nature/nurture','~50% heritable + Flynn effect'),('EQ','Managing and understanding emotions')],36,350)}</div>{GROW}''',6,T))
S.append(slide(f'''{head('PSY111 SO FAR','4 modules, 1 account 📚',84)}{GROW}
{grid([('🧩','Personality','人格','Freud to the Big Five, genes, culture, tests'),('🔥','Motivation','动机','Drives, arousal, Dweck, SDT, hunger'),('💓','Emotion','情绪','6 theories, the amygdala, culture'),('🧠','Intelligence','智力','Theories, IQ, bias, nature vs nurture, EQ')],32)}{GROW}''',7,T))
S.append(last(f'''<div class="lab">YOUR TURN</div>
<h1 style="margin-top:30px;font-size:90px">What should I <span style="font-style:italic;color:#C24A2B">explain next?</span></h1>
<p style="margin:28px 0 0;font-size:44px;line-height:1.4">💬 Comment a psychology topic you want to understand</p>{GROW}
{save_btn('📌 Save the whole series')}''',T))
write(S)
