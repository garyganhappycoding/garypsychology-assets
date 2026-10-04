# Personality series 1/6 · Id, ego, superego. Run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from series import *
from toons import phone_kid,id_toon,ego_toon,superego_toon
T=9;S=[]
S.append(cover('PERSONALITY · PART 1 OF 6',
 'You know you should study. So why are you still on <span style="font-style:italic;color:#C24A2B">TikTok?</span>',
 'Freud says there are 3 voices in your head.',phone_kid(230),100))
voices=[(id_toon(190),'“One more video.”'),(superego_toon(190),'“You’ll regret this.”'),(ego_toon(190),'“Okay, let’s make a deal…”')]
vs=''.join(f'<div style="display:flex;align-items:center;gap:30px">{a}<div style="font-family:Fraunces,serif;font-style:italic;font-size:54px;line-height:1.15">{b}</div></div>' for a,b in voices)
S.append(slide(f'''{head('THE SCENE','11pm. Exam tomorrow.',92)}
<div style="margin-top:50px;display:flex;flex-direction:column;gap:30px">{vs}</div>{GROW}
{ex('Freud gave each voice a name. 👉')}''',2,T))
S.append(slide(f'''{head('VOICE 1',f'The id {zs("本我",56)}',96,id_toon(260))}
<div style="margin-top:56px">{bullets(size=46,gap=40,items=['Completely <b>unconscious</b> (无意识), present from birth','Basic drives: hunger, self-preservation','Runs on the <b>pleasure principle</b> (快乐原则): if it feels good, do it, <i>now</i>'])}</div>{GROW}
{ex('📱 “One more video.”',46)}''',3,T))
S.append(slide(f'''{head('VOICE 2',f'The superego {zs("超我",50)}',80,superego_toon(260))}
<div style="margin-top:56px">{bullets(size=46,gap=40,items=['Your <b>moral centre</b> (道德中心)','Develops as you learn society’s rules and expectations','Includes the <b>conscience</b> (良心), which makes you feel guilty (内疚) after doing wrong'])}</div>{GROW}
{ex('😔 “You should be ashamed.”',46)}''',4,T))
S.append(slide(f'''{head('VOICE 3',f'The ego {zs("自我",56)}',96,ego_toon(260))}
<div style="margin-top:56px">{bullets(size=46,gap=40,items=['Mostly conscious, rational, deals with reality','Runs on the <b>reality principle</b> (现实原则): lets the id have its way only when it won’t cause trouble'])}</div>{GROW}
{ex('⏱️ “Study 45 minutes first, then 10 minutes of TikTok.”',46)}''',5,T))
three=''.join(f'<div style="display:flex;align-items:center;gap:26px;padding:22px 0;border-bottom:2px solid #E4DDD0">{a}<div style="font-size:44px;line-height:1.35">{b}</div></div>' for a,b in [(id_toon(150),'<b>Id wins</b> → you keep scrolling'),(superego_toon(150),'<b>Superego wins</b> → you feel guilty'),(ego_toon(150),'<b>Ego in charge</b> → you get things done')])
S.append(slide(f'''{head('THE REFEREE','The ego is the <span style="font-style:italic;color:#3D3A8C">referee</span>',84)}
<p style="margin:26px 0 0;font-size:36px;line-height:1.42">The <b>executive director</b> {zs("执行者",26)} between the id and the superego.</p>
{GROW}<div>{three}</div>{GROW}''',6,T))
S.append(slide(f'''{head('DON’T GET THIS WRONG','Not real brain parts',92)}{GROW}
{card('The id, ego and superego are parts of the <b>mind</b>.',k='✅ THEY ARE',size=50)}
<div style="margin-top:26px">{card('Real structures inside the brain (不是大脑的实际部位).',k='❌ THEY ARE NOT',size=50)}</div>{GROW}
<div style="font-size:36px;color:#5A5A66">💡 A common exam trap.</div>''',7,T))
S.append(slide(f'''{head('CHEAT SHEET','Save this 📌',90)}
<div style="margin-top:36px">{rows([('Id','Wants it now · <b>pleasure principle</b> (快乐原则) · unconscious'),('Ego','Deals with reality · <b>reality principle</b> (现实原则) · the referee'),('Superego','Rules and guilt · <b>conscience</b> (良心) · moral centre')],42,250)}</div>{GROW}''',8,T))
S.append(last(f'''<div class="lab">WHAT HAPPENS NEXT</div>
<p style="margin:30px 0 0;font-size:52px;line-height:1.4">When the id and superego clash, you feel <b>anxious</b> {zs("焦虑",32)}. Freud said the mind protects itself without you knowing.</p>{GROW}
{nextup('Why do we blame the lecturer when we fail?')}
{save_btn('📌 Save for your PSY111 exam')}''',T))
write(S)
