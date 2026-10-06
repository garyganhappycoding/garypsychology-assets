# Personality Part 2 · 4/4 · Projective tests, interviews, behavioural assessment. Run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from series import *
def inkblot(w=520,col='#1E1E2A'):
    # original symmetric blot: one half drawn, mirrored
    half=('<path d="M250 40 C214 44 200 80 214 104 C180 96 150 116 160 146 C118 140 92 172 112 202 C70 214 64 262 104 274 '
          'C86 306 108 340 146 330 C150 366 186 384 214 360 C224 392 246 402 250 400 Z"/>'
          '<circle cx="128" cy="118" r="16"/><circle cx="96" cy="150" r="9"/><circle cx="70" cy="300" r="12"/>'
          '<path d="M176 230 C150 236 140 262 162 270 C186 276 196 246 176 230Z" fill="#F7F3EC"/>')
    return (f'<svg width="{w}" height="{int(w*0.88)}" viewBox="40 20 420 400"><g fill="{col}">{half}</g>'
            f'<g fill="{col}" transform="translate(500 0) scale(-1 1)">{half}</g></svg>')
T=10;S=[]
S.append(f'''<div class="s"><div class="lab">PERSONALITY 2 · 4 OF 4</div>
<h1 style="margin-top:20px;font-size:104px">What do you see in this <span style="font-style:italic;color:#C24A2B">inkblot?</span></h1>
<div style="flex-grow:1"></div><div style="display:flex;justify-content:center">{inkblot(560)}</div><div style="flex-grow:1"></div>
<p style="margin:0;font-size:40px;line-height:1.3;color:#4A4A56">Keep your answer in mind. Swipe 👉</p>{swipe()}</div>''')
S.append(concept(2,T,'THE IDEA','Projective tests','投射测验','🎨',
 'Show the client an <b>ambiguous</b> (模糊的) picture and ask them to say <b>whatever comes to mind</b>.',
 'The idea: with no “right” answer, you <b>project</b> your own thoughts and feelings onto it.',exk='WHY IT MIGHT WORK'))
S.append(slide(f'''{head('TEST 1',f'Rorschach inkblots {zs("罗夏墨迹测验",36)}',80,inkblot(220))}{GROW}
{bullets(['By <b>Hermann Rorschach</b>, a Swiss psychiatrist','<b>10 inkblots</b>. Say what each one looks like to you','Scored on: <b>colour</b>, <b>shape</b>, figures you see, the <b>whole</b> blot or <b>details</b>','Used to describe personality, diagnose mental disorders and predict behaviour'],size=40,gap=26)}{GROW}''',3,T))
S.append(slide(f'''{head('TEST 2',f'Thematic Apperception Test {zs("主题统觉测验 TAT",34)}',72)}{GROW}
{bullets(['By <b>Henry Murray</b> and colleagues','<b>20 ambiguous pictures</b> of people','You <b>tell a story</b> about the person or people in each one','Psychoanalysts look for <b>revealing statements</b> and problems you <b>project</b> onto the picture'],size=42,gap=30)}{GROW}
{ex('🖼️ A picture of a boy staring at a violin. Is he bored? Dreaming? Pressured by his parents? Your story says something about you.',38)}''',4,T))
S.append(slide(f'''{head('THE PROBLEM','Why many doubt them',90)}{GROW}
{bullets(['<b>Very subjective</b> (主观)','<b>No standard grading scales</b> → problems with reliability (信度) and validity (效度)','People may answer <b>differently depending on context</b>'],size=46,gap=36)}{GROW}
{card('The latest versions are <b>still used</b> by psychologists today.',k='BUT',bg='#FBE3DB',size=42)}''',5,T))
S.append(slide(f'''{head('OTHER TOOL 1',f'Interviews {zs("面谈",44)}',92)}{GROW}
{duo(('🌊','Unstructured','非结构化','Flows <b>naturally</b> between client and psychologist.'),('📋','Semi-structured','半结构化','<b>Specific questions</b> with follow-up items.'),38)}
<div style="margin-top:26px">{card('<b>Halo / horn effect</b> (光环/尖角效应): one good or bad trait colours everything · questionable validity · <b>interviewer bias</b>',k='⚠️ LIMITATIONS',size=36)}</div>{GROW}''',6,T))
S.append(slide(f'''{head('OTHER TOOL 2',f'Behavioural assessment {zs("行为评估",36)}',76)}{GROW}
{grid([('👀','Direct observation','直接观察','Watch everyday behaviour, in a clinic or a natural setting.'),('🔢','Rating scale','评定量表','Give a number to a behaviour.'),('⏱️','Frequency count','频率计数','Count a behaviour in a set time, e.g. how often a child leaves their seat in 30 minutes.'),('⚠️','Limitations','局限','<b>Observer effect &amp; bias</b>; no control over the environment.')],30)}{GROW}''',7,T))
S.append(slide(f'''{head('CHEAT SHEET','4 assessment types 📌',84)}
<div style="margin-top:24px">{rows([('Interviews','Self-report · halo/horn effect, interviewer bias'),('Behavioural','Observe, rate, count · observer effect and bias'),('Inventories','Standard questions · most objective, but people can fake'),('Projective','Inkblots, TAT · very subjective')],38,300)}</div>{GROW}''',8,T))
S.append(slide(f'''{head('MODULE RECAP','Personality, done ✅',88)}{GROW}
{bullets(['<b>4 theories</b>: psychodynamic, behavioural &amp; social cognitive, humanistic, trait','<b>Genes</b>: about 50% heritable, the environment explains the rest','<b>Culture</b>: Hofstede’s 4 dimensions','<b>Assessment</b>: interviews, behavioural, inventories, projective'],size=42,gap=32)}{GROW}''',9,T))
S.append(last(f'''<div class="lab">YOUR TURN</div>
<h1 style="margin-top:30px;font-size:96px">So, what did you <span style="font-style:italic;color:#C24A2B">see?</span></h1>
<p style="margin:28px 0 0;font-size:44px;line-height:1.4">💬 Comment what the inkblot on slide 1 looked like to you</p>{GROW}
{nextup('New module: Motivation. Do you study for the A, or for the fun?')}
{save_btn('📌 Save the Personality series')}''',T))
write(S)
