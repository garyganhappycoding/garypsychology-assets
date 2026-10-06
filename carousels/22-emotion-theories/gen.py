# Emotion · 1/3 · Theories of emotion. Run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from series import *
def theory(n,lab,name,zh,who,defin,steps,extra=''):
    return slide(f'''{head(lab,f'{name} {zs(zh,36)}',78)}
<div style="margin-top:12px;font-size:32px;color:#5A5A66">{who}</div>
<p style="margin:20px 0 0;font-size:40px;line-height:1.42">{defin}</p>{GROW}
{vflow(steps,40)}{GROW}{extra}''',n,T)
T=10;S=[]
S.append(cover('EMOTION · 1 OF 3',
 'Are you scared because you <span style="font-style:italic;color:#C24A2B">run</span>, or do you run because you’re <span style="font-style:italic;color:#3D3A8C">scared?</span>',
 '5 theories of emotion, one snarling dog 🐕',badge('🐕',230),92))
S.append(slide(f'''{head('FIRST',f'What is an emotion? {zs("情绪",40)}',84)}{GROW}
{grid([('💓','Physical arousal','生理唤醒','Heart races, breathing speeds up, pupils dilate (sympathetic nervous system 交感神经系统).'),('😬','Behaviour','行为','What shows the emotion to the outside world.'),('🏷️','Inner awareness','内在觉察','Knowing and <b>labelling</b> what you feel.'),('🧠','Linked to','联系','Both your <b>thinking</b> and your <b>actions</b>.')],32)}{GROW}''',2,T))
S.append(theory(3,'THEORY 1','Common sense theory','常识理论','The “obvious” version',
 'Feel the emotion first, then the body reacts.',[('See the snarling dog 🐕',''),('Feel fear','情绪'),('Body shakes','arousal')]))
S.append(theory(4,'THEORY 2','James-Lange theory','詹姆斯-兰格理论','William James &amp; Carl Lange',
 'The body reacts <b>first</b>. You then read that arousal as an emotion.',[('See the dog 🐕',''),('Body shakes, heart races','arousal'),('“I must be afraid”','emotion')],
 ex('← The hook: you’re scared <b>because</b> your body reacts.',38)))
S.append(slide(f'''{head('TESTING JAMES-LANGE','But what if the body can’t react?',78)}{GROW}
{card('People who are <b>paralysed</b> report feeling emotions as strongly as before their injury.',k='🧑‍🦽 FINDING 1',size=42)}
<div style="margin-top:26px">{card('People with <b>pure autonomic failure</b> (单纯自主神经衰竭) feel the same emotions, but <b>less intensely</b>.',k='🫀 FINDING 2',size=42)}</div>{GROW}
{ex('So the body isn’t the whole story. Other factors are involved.',40)}''',5,T))
S.append(theory(6,'THEORY 3','Cannon-Bard theory','坎农-巴德理论','Walter Cannon &amp; Philip Bard',
 'Body reaction and emotion happen <b>at the same time</b>. The <b>thalamus</b> (丘脑) sends the signal to both.',[('See the dog 🐕',''),('Brain (thalamus)','丘脑'),('Fear + shaking, together ⚡','')],
 card('Later research found the <b>vagus nerve</b> (迷走神经) sends body feedback to the brain, which makes it less convincing.',k='⚠️ CRITICISM',bg='#FBE3DB',size=34)))
S.append(theory(7,'THEORY 4','Cognitive arousal theory','认知唤醒理论','Schachter &amp; Singer · “two-factor theory” 双因素理论',
 'You need <b>arousal</b> plus a <b>label</b> taken from the situation.',[('See the dog 🐕',''),('Arousal + “there’s a dog, that’s why”','label'),('Fear','emotion')]))
S.append(theory(8,'THEORY 5','Cognitive-mediational theory','认知中介理论','Richard Lazarus',
 'You <b>appraise</b> (评估) the situation first. The appraisal decides the emotion.',[('See the dog 🐕',''),('“It’s snarling and there’s no fence. Dangerous.”','appraisal'),('Fear','emotion'),('Body reacts','')]))
mn=[('🕴️','James-Lange','James Bond is all action: the <b>body acts first</b>, then you name the emotion.'),('💥','Cannon-Bard','A wonky cannon fires <b>two ways at once</b>: emotion and body reaction together.'),('🎤','Schachter-Singer','A singer hears clapping (arousal), then <b>realises</b> she’s good (label), then feels proud.')]
mm=''.join(f'<div style="display:flex;gap:24px;align-items:flex-start;padding:22px 0;border-bottom:2px solid #E4DDD0"><div style="font-size:70px">{e}</div><div><div style="font-family:Fraunces,serif;font-weight:700;font-size:42px;color:#3D3A8C">{t}</div><div style="margin-top:6px;font-size:34px;line-height:1.38">{b}</div></div></div>' for e,t,b in mn)
S.append(slide(f'''{head('MEMORY TRICK','Remember them like this',84)}
<div style="margin-top:16px">{mm}</div>{GROW}
<div style="font-size:26px;color:#8A7F74">Memory trick from my lecture slides.</div>''',9,T))
S.append(last(f'''<div class="lab">YOUR TURN</div>
<h1 style="margin-top:30px;font-size:88px">Which theory feels most <span style="font-style:italic;color:#C24A2B">true</span> to you?</h1>
<p style="margin:28px 0 0;font-size:44px;line-height:1.4">💬 Comment the number: 1–5</p>{GROW}
{nextup('Can smiling actually make you happier?')}
{save_btn('📌 Save for your PSY111 exam')}''',T))
write(S)
