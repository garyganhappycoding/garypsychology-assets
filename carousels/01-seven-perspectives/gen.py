# Content for this carousel. Edit text, run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from common import *
from toons import *
P=[
('Psychodynamic','心理动力学','key','Carl Jung · Anna Freud · Erik Erikson','your <b>sense of self (自我意识)</b> and <b>hidden motives (潜在动机)</b>','Deep down, failing feels like proof of who you are, or of disappointing the people you love.',"What's the hidden motive?"),
('Behavioural','行为主义','repeat','B.F. Skinner','voluntary behaviour learned through <b>consequences (后果)</b> and <b>reinforcement (强化)</b>','Avoiding revision felt like <b>relief (如释重负)</b>, so the relief reinforced the avoiding. Now you walk in underprepared.','What was learned, and what reinforced it?'),
('Humanistic','人本主义','sprout','Abraham Maslow · Carl Rogers','<b>free will (自由意志)</b> and <b>self-actualisation (自我实现)</b>','When your <b>self-worth (自我价值)</b> depends on your grades, every exam feels like a <b>verdict (判决)</b> on you.','Are you studying to grow, or to prove your worth?'),
('Cognitive','认知','bulb','Noam Chomsky · Elizabeth Loftus · Howard Gardner','<b>memory (记忆)</b>, <b>thought (思维)</b>, <b>problem solving (解决问题)</b>','Thoughts like “I’m going to fail” take up the mental space you need to <b>recall (回忆)</b> answers.','What are you thinking, and how is it affecting memory?'),
('Sociocultural','社会文化','users','Albert Bandura · Philip Zimbardo · Stanley Milgram','groups, <b>social roles (社会角色)</b> and <b>culture (文化)</b>','Results decide your future, results get compared with your cousins’, and your classmates’ panic spreads to you.','What does your environment expect from you?'),
('Biopsychological','生物心理学','pulse','Paul Broca · Roger Sperry · Carl Wernicke · John O’Keefe','<b>genes (基因)</b>, <b>hormones (激素)</b>, the <b>nervous system (神经系统)</b>','<b>Adrenaline (肾上腺素)</b> and <b>cortisol (皮质醇)</b> trigger <b>fight-or-flight (战斗或逃跑反应)</b>: racing heart, shaky hands, a brain focused on threat instead of recall.','What’s happening in the body?'),
('Evolutionary','进化','branch','Richard Dawkins','behaviours that helped our ancestors <b>survive (生存)</b>','Fight-or-flight evolved to escape predators, not to answer Question 3.','Why would this reaction have helped us survive?'),
]
slides=[]
# 1 cover
icons=''.join(f'<div class="ic" style="width:104px;height:104px;{"background:#F2785C;color:#1E1E2A" if i==6 else ""}">{svg(p[2],48)}</div>' for i,p in enumerate(P))
slides.append(f'''<div class="s"><div class="lab">PSYCH NOTES · YEAR 1</div>
<h1 style="margin-top:40px;font-size:138px">Why do you <span style="font-style:italic;color:#3D3A8C">blank out</span> in exams?</h1>
<p style="margin:44px 0 0;font-size:44px;line-height:1.3;color:#4A4A56">7 psychologists would give you 7 different answers</p>
<div style="flex-grow:1"></div><div style="display:flex;gap:20px">{icons}</div>
<div class="foot" style="margin-top:64px"><span>@garypsychology07</span><div style="display:flex;align-items:center;gap:16px;padding:18px 32px;border-radius:999px;background:#F2785C;color:#1E1E2A;font-size:34px;font-weight:700"><span>swipe</span>{svg("arrow",40,w=2.5)}</div></div></div>''')
# 2 setup
slides.append(f'''<div class="s"><div class="lab">THE SAME MOMENT</div>
<h1 style="margin-top:48px;font-size:104px;line-height:1.08">Same student.<br>Same exam.<br><span style="font-style:italic;color:#3D3A8C">Same blank mind.</span></h1>
<div style="flex-grow:1"></div>
<p style="margin:0;font-size:42px;line-height:1.4">Psychology has <b>7 perspectives</b> <span class="zh">(7种视角)</span>, 7 different lenses on the same behaviour.</p>
<div style="margin-top:48px;padding:40px 44px;border-radius:32px;background:#FBE3DB;font-family:Fraunces,serif;font-style:italic;font-size:50px;line-height:1.15">Can one lens explain everything? Keep swiping →</div>
{foot(2)}</div>''')
for i,(en,zh,ic,people,focus,mind,ask) in enumerate(P):
    n=i+3
    slides.append(f'''<div class="s"><div style="display:flex;justify-content:space-between;align-items:flex-start;gap:28px">
<div style="display:flex;flex-direction:column;gap:22px"><div class="lab">PERSPECTIVE {i+1} OF 7</div>
<h1 style="font-size:{84 if len(en)>13 else 96}px">{en}</h1><div style="font-family:'Noto Sans CJK SC',sans-serif;font-weight:500;font-size:40px;color:#8A7F74">{zh}</div></div>
<div class="ic" style="width:160px;height:160px">{svg(ic,76,w=1.8)}</div></div>
<div style="margin-top:30px"><span class="chip">{people}</span></div>
<div style="margin-top:44px"><div class="k">FOCUS</div><div style="font-size:40px;line-height:1.4">{z(focus)}</div></div>
<div style="flex-grow:1;min-height:30px"></div>
<div style="padding:38px 44px;border-radius:32px;background:#FBE3DB"><div class="k">YOUR BLANK MIND</div><div style="font-size:40px;line-height:1.42">{z(mind)}</div></div>
<div style="margin-top:36px;display:flex;gap:18px;align-items:baseline"><span style="font-size:24px;font-weight:700;letter-spacing:.16em;color:#3D3A8C;white-space:nowrap">ASK YOURSELF</span><span style="font-family:Fraunces,serif;font-style:italic;font-weight:500;font-size:44px;line-height:1.15;color:#3D3A8C">{ask}</span></div>
{foot(n)}</div>''')
KW=['hidden motives','reinforcement','self-worth','thoughts & memory','environment','body','survival']
rows=''.join(f'''<div style="display:flex;align-items:center;gap:26px"><div class="ic" style="width:64px;height:64px;{"background:#F2785C;color:#1E1E2A" if i==6 else ""}">{svg(p[2],30)}</div>
<div style="width:350px;flex-shrink:0"><div style="font-family:Fraunces,serif;font-weight:700;font-size:40px;line-height:1">{p[0]}</div><div style="font-family:'Noto Sans CJK SC',sans-serif;font-size:22px;color:#8A7F74;margin-top:4px">{p[1]}</div></div>
{svg("arrow",30,"#C24A2B",2.5)}<div style="font-size:32px;font-weight:600;color:#3D3A8C;white-space:nowrap">{KW[i]}</div></div>''' for i,p in enumerate(P))
slides.append(f'''<div class="s"><div class="lab">SAVE THIS SLIDE</div>
<h1 style="margin-top:22px;font-size:76px">No single lens <span style="font-style:italic;color:#3D3A8C">explains it all</span></h1>
<div style="margin-top:40px;padding:36px 40px;border-radius:32px;background:#FFFDF8;border:2px solid #E4DDD0;display:flex;flex-direction:column;gap:22px">{rows}</div>
<div style="flex-grow:1"></div>
<div style="font-size:34px;font-weight:700">💬 Which one sounds most like you? Comment below</div>
<div style="margin-top:14px;font-size:28px;color:#4A4A56">📌 Save for your psych exam · Next up: Psychology’s 4 goals</div>
{foot(10)}</div>''')
for i,s in enumerate(slides,1):
    open(f'slide-{i:02d}.html','w').write(HEAD+s+'</body></html>')
