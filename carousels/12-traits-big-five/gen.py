# Personality series 6/6 · Trait theories + Big Five. Run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from series import *
from toons import headphones,iceberg
T=9;S=[]
S.append(cover('PERSONALITY · PART 6 OF 6',
 'Are you an <span style="font-style:italic;color:#3D3A8C">introvert</span>, or just <span style="font-style:italic;color:#C24A2B">shy?</span>',
 'Psychology says they’re not the same level of personality.',headphones(260),110))
S.append(slide(f'''{head('WHAT TRAIT THEORIES DO','Describe + predict',96)}
<div style="margin-top:14px">{zs("特质理论",40)}</div>{GROW}
{bullets(['They don’t ask <b>why</b> you’re like this.','They <b>describe</b> personality and <b>predict</b> future behaviour.'],size=48,gap=36)}{GROW}
{card('A consistent, lasting way of thinking, feeling or behaving.',k='TRAIT · 特质',size=46)}
<div style="margin-top:24px">{ex('🔁 Describe and predict = 2 of the 4 goals of psychology from my earlier post.',40)}</div>''',2,T))
S.append(slide(f'''{head('WHERE IT STARTED','Allport &amp; Odbert 📖',88)}{GROW}
{bullets(['Pulled about <b>200 trait words</b> from the dictionary','Believed traits were wired into the <b>nervous system</b>, without scientific evidence at the time','Later research found some evidence that traits are <b>heritable</b> (可遗传)'],size=46,gap=40)}{GROW}''',3,T))
S.append(slide(f'''{head('CATTELL','Surface vs source traits',84)}
<div style="position:relative;margin-top:24px;display:flex;justify-content:center">{iceberg(640)}
<div style="position:absolute;top:30px;left:0;font-size:34px;line-height:1.3"><b>Surface traits</b> {zs("表面特质",26)}<br><span style="color:#5A5A66">what others can see</span></div>
<div style="position:absolute;top:280px;left:50%;transform:translateX(-50%);text-align:center;color:#F7F3EC;font-size:34px;line-height:1.3"><b>Source traits</b> <span style="font-family:'Noto Sans CJK SC';font-size:26px;color:#DCDAF0">根源特质</span><br>the core underneath</div></div>
{GROW}{ex('<b>Introversion</b> (source) → shyness, quietness, disliking crowds (surface). So shyness can be one <i>sign</i> of introversion.',40)}''',4,T))
S.append(slide(f'''{head('CATTELL','The 16PF questionnaire',84)}{GROW}
<div style="display:flex;flex-wrap:wrap;gap:16px;justify-content:center">{''.join(f'<div style="width:96px;height:96px;border-radius:22px;background:{"#3D3A8C" if i%3 else "#F2785C"};color:#F7F3EC;display:flex;align-items:center;justify-content:center;font-family:Fraunces,serif;font-weight:800;font-size:40px">{i+1}</div>' for i in range(16))}</div>{GROW}
{card('Measures <b>16 source traits</b>. Each trait is a scale, with <b>opposite traits</b> at either end.',size=46)}{GROW}''',5,T))
O=[('O','Openness','开放性','#3D3A8C'),('C','Conscientiousness','尽责性','#F2785C'),('E','Extraversion','外向性','#3D3A8C'),('A','Agreeableness','宜人性','#F2785C'),('N','Neuroticism','神经质','#3D3A8C')]
oc=''.join(f'<div style="display:flex;align-items:center;gap:26px;padding:12px 0"><div style="width:96px;height:96px;border-radius:22px;background:{c};color:#F7F3EC;display:flex;align-items:center;justify-content:center;font-family:Fraunces,serif;font-weight:800;font-size:56px">{l}</div><div style="font-size:46px;font-weight:700">{n} {zs(zh,32)}</div></div>' for l,n,zh,c in O)
S.append(slide(f'''{head('THE BIG FIVE · OCEAN',f'5 traits {zs("大五人格",40)}',90)}
<div style="margin-top:20px">{oc}</div>{GROW}
{ex('The 5 are <b>independent</b> of each other. Openness is linked to better cognition and intellect.',38)}''',6,T))
S.append(slide(f'''{head('TRAIT × SITUATION','Same person, different setting',80)}
<div style="margin-top:10px">{zs("特质-情境交互作用",36)}</div>{GROW}
<div style="display:flex;gap:26px">
<div style="flex:1;padding:34px;border-radius:28px;background:#FBE3DB;text-align:center"><div style="font-size:100px">🎉</div><div style="font-size:40px;font-weight:700;margin-top:10px">Party</div><div style="font-size:36px;margin-top:8px">Extravert jokes around</div></div>
<div style="flex:1;padding:34px;border-radius:28px;background:#E4DDD0;text-align:center"><div style="font-size:100px">🕯️</div><div style="font-size:40px;font-weight:700;margin-top:10px">Funeral</div><div style="font-size:36px;margin-top:8px">Same extravert stays quiet</div></div></div>{GROW}
{card('Big Five results are largely consistent across cultures, languages, and self vs observer ratings, though some regional differences remain.',size=38)}''',7,T))
S.append(slide(f'''{head('SERIES CHEAT SHEET','4 views of personality 📌',78)}
<div style="margin-top:24px">{rows([('Psychodynamic','The unconscious mind · Freud'),('Behavioural &amp; social cognitive','Environment and learning · Skinner, Bandura, Rotter'),('Humanistic','Self-concept and growth · Rogers, Maslow'),('Trait','Describe and predict · Cattell, Big Five')],38,330)}</div>{GROW}''',8,T))
S.append(last(f'''<div class="lab">YOUR TURN</div>
<h1 style="margin-top:30px;font-size:92px">Which Big Five trait is your <span style="font-style:italic;color:#C24A2B">highest?</span></h1>
<p style="margin:30px 0 0;font-size:46px;line-height:1.4">💬 Comment the letter: O, C, E, A or N</p>{GROW}
<div style="font-size:40px;line-height:1.45">That’s the end of the personality series. Thanks for following along 🧠</div>
{save_btn('📌 Save the series for your PSY111 midterm')}''',T))
write(S)
