# Motivation · 1/5 · Intrinsic vs extrinsic, instincts, drive reduction. Run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from series import *
T=9;S=[]
S.append(cover('MOTIVATION · 1 OF 5',
 'Do you study for the <span style="font-style:italic;color:#C24A2B">A</span>, or for the <span style="font-style:italic;color:#3D3A8C">fun?</span>',
 'Psychology’s first answers to why we do anything at all.',badge('📚',240),110))
S.append(slide(f'''{head('DEFINITION',f'Motivation {zs("动机",48)}',100)}
<p style="margin:24px 0 0;font-size:42px;line-height:1.42">What <b>“moves”</b> you. The process that <b>starts</b>, <b>directs</b> and <b>continues</b> an activity to meet a need or want.</p>{GROW}
<div class="k">EXAMPLE: YOU FEEL HUNGRY 🍜</div>
{vflow([('Stop reading','started · 开始'),('Walk to the kitchen','directed · 指向'),('Find something to eat','continued · 持续')],42)}{GROW}''',2,T))
S.append(slide(f'''{head('TWO KINDS','Outside or inside?',96)}{GROW}
{duo(('🏅','Extrinsic','外在动机','You do it for an <b>outcome outside you</b>: the A, the scholarship, your parents’ praise.'),('💡','Intrinsic','内在动机','The activity is <b>rewarding in itself</b>: you read psychology because it’s interesting.'),38)}{GROW}
{ex('Most of us mix both. Which one got you through SPM? 🤔',42)}''',3,T))
S.append(concept(4,T,'THEORY 1 · EARLY','Instinct approach','本能论','🐣',
 '<b>Instincts</b>: biologically determined, inborn patterns of behaviour in people and animals. <b>McDougall (1908)</b> listed curiosity, flight, acquisition and aggression.',
 '✅ Showed some behaviour comes from <b>heredity</b>.<br>❌ Never explained <b>why</b> instincts exist.',exk='VERDICT',size=90))
S.append(slide(f'''{head('THEORY 2',f'Drive reduction {zs("驱力减降理论",40)}',84)}
<p style="margin:22px 0 0;font-size:40px;line-height:1.42">Behaviour comes from <b>internal drives</b> that push you to meet a body need and <b>reduce tension</b>.</p>{GROW}
{vflow([('Need 需求','your body lacks water'),('Drive 驱力','tension: you feel thirsty'),('Act','you drink'),('Tension reduced ✅','')],42)}{GROW}''',5,T))
S.append(slide(f'''{head('TWO KINDS OF DRIVES','Born with it, or learned?',84)}{GROW}
{duo(('🥤','Primary drives','初级驱力','Survival needs of the body: <b>hunger</b> and <b>thirst</b>.'),('💰','Acquired drives','习得驱力','Learned through experience or conditioning: <b>money</b>, <b>social approval</b>.'),40)}{GROW}''',6,T))
S.append(concept(7,T,'THE GOAL OF DRIVES','Homeostasis','体内平衡','🌡️',
 'The body’s tendency to keep a <b>steady state</b>, like an air-con that keeps the room at 24°C.',
 '❓ Why do we eat when we’re <b>not hungry</b>?<br>❓ Why do some people <b>look for more</b> excitement?',exk='WHAT DRIVE REDUCTION CAN’T EXPLAIN'))
S.append(slide(f'''{head('CHEAT SHEET','Save this 📌',90)}
<div style="margin-top:26px">{rows([('Motivation','Starts, directs, continues behaviour'),('Extrinsic','For an outside reward'),('Intrinsic','The activity itself is rewarding'),('Instinct','Inborn patterns · McDougall'),('Drive reduction','Need → drive → act → less tension'),('Homeostasis','Keeping a steady state')],38,320)}</div>{GROW}''',8,T))
S.append(last(f'''<div class="lab">YOUR TURN</div>
<h1 style="margin-top:30px;font-size:90px"><span style="color:#C24A2B">Extrinsic</span> or <span style="color:#3D3A8C">intrinsic</span>: what keeps you studying?</h1>
<p style="margin:28px 0 0;font-size:44px;line-height:1.4">💬 Comment below</p>{GROW}
{nextup('Why do you blank out when you’re too nervous?')}
{save_btn('📌 Save for your PSY111 exam')}''',T))
write(S)
