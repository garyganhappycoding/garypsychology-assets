# Motivation · 5/5 · Hunger. Obesity/BMI deliberately left out. Run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from series import *
T=9;S=[]
S.append(cover('MOTIVATION · 5 OF 5',
 'Why is there always room for <span style="font-style:italic;color:#C24A2B">dessert?</span>',
 'Hunger isn’t just your stomach talking.',badge('🍰',250),110))
S.append(slide(f'''{head('HUNGER',f'More than survival {zs("饥饿",44)}',90)}{GROW}
{duo(('🍚','A primary need','初级需求','Satisfying hunger is a <b>primary drive</b> for survival.'),('🎉','Entertainment','娱乐','For many people, eating is <b>also fun</b>: makan with friends, trying new food.'),38)}{GROW}''',2,T))
S.append(slide(f'''{head('THE HORMONES','3 chemical messengers',84)}{GROW}
<div style="display:flex;flex-direction:column;gap:22px">
{card('From the <b>pancreas</b> (胰腺). <b>Lowers</b> glucose in your blood.',k='⬇️ INSULIN · 胰岛素',size=40)}
{card('Also from the pancreas. <b>Raises</b> glucose in your blood.',k='⬆️ GLUCAGON · 胰高血糖素',size=40)}
{card('Tells the <b>hypothalamus</b> “that’s enough food” → appetite down, fullness up.',k='🛑 LEPTIN · 瘦素',bg='#FBE3DB',size=40)}</div>{GROW}''',3,T))
S.append(slide(f'''{head('THE BRAIN',f'Hypothalamus {zs("下丘脑",44)}',96)}
<p style="margin:20px 0 0;font-size:40px;line-height:1.42">Seems to <b>control eating</b>. Two areas matter:</p>{GROW}
{duo(('🛑','VMH','腹内侧下丘脑','Helps <b>stop</b> eating when glucose goes up. Damaged → <b>overeating</b>.'),('▶️','LH','外侧下丘脑','Helps <b>start</b> eating when insulin goes up. Damaged → stops eating unless <b>force-fed</b>.'),36)}{GROW}''',4,T))
S.append(slide(f'''{head('YOUR BODY’S TARGET','Set point and BMR',90)}{GROW}
{card('The weight your body <b>tries to maintain</b>. <b>Metabolism</b> and <b>exercise</b> both play a part.',k='🎯 WEIGHT SET POINT · 体重设定点',size=42)}
<div style="margin-top:28px">{card('How fast your body <b>burns energy while resting</b>.',k='🔋 BASAL METABOLIC RATE · 基础代谢率',bg='#FBE3DB',size=42)}</div>{GROW}''',5,T))
S.append(slide(f'''{head('IT’S ALSO SOCIAL','Why we eat when not hungry',80)}{GROW}
{grid([('👀','Social cues','社交暗示','Everyone at the table is ordering.'),('😋','Food preferences','食物偏好','You just love durian.'),('🌏','Culture','文化','What “a proper meal” means where you grew up.'),('🛋️','Comfort','安慰','Eating to escape stress or boredom.')],32)}{GROW}''',6,T))
S.append(slide(f'''{head('← THE ANSWER','Room for dessert 🍰',96)}{GROW}
{vflow([('See dessert 🍰',''),('Expect to eat',''),('Insulin rises','胰岛素'),('Feel hungry again','')],40)}{GROW}
{card('Some people produce an <b>insulin response</b> just from <b>expecting</b> to eat. Add eating-as-entertainment, and the “dessert stomach” makes sense.',size=42)}{GROW}''',7,T))
S.append(slide(f'''{head('CHEAT SHEET','Save this 📌',90)}
<div style="margin-top:26px">{rows([('Insulin','Lowers blood glucose'),('Glucagon','Raises blood glucose'),('Leptin','“I’m full” signal'),('VMH','Stop eating'),('LH','Start eating'),('Set point','Weight the body defends'),('BMR','Energy burned at rest')],38,260)}</div>{GROW}''',8,T))
S.append(last(f'''<div class="lab">YOUR TURN</div>
<h1 style="margin-top:30px;font-size:92px">What dessert do you <span style="font-style:italic;color:#C24A2B">always</span> have room for?</h1>
<p style="margin:28px 0 0;font-size:44px;line-height:1.4">💬 Comment below 🍧</p>{GROW}
{nextup('New module: Emotion. Are you scared because you run, or do you run because you’re scared?')}''',T))
write(S)
