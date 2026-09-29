# Content for this carousel. Edit text, run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from common import *
from toons import *
T=9
def foot(n): return f'<div class="foot"><span>@garypsychology07</span><div style="display:flex;align-items:center;gap:20px"><span>{n} / {T}</span><div class="bar"><div style="width:{round(180*n/T)}px"></div></div></div></div>'
def zs(t,s=40): return f'<span style="font-family:\'Noto Sans CJK SC\',sans-serif;font-weight:500;font-size:{s}px;color:#8A7F74;letter-spacing:0">{t}</span>'
S=[]
S.append(f'''<div class="s"><div class="lab">PSYCH CAREERS · MALAYSIA</div>
<h1 style="margin-top:34px;font-size:92px;line-height:1.02">Psychologist, psychiatrist, counsellor, social worker.</h1>
<p style="margin:36px 0 0;font-size:46px;line-height:1.3;color:#4A4A56"><b style="color:#C24A2B">Not the same job.</b> Here’s who does what in Malaysia.</p>
<div style="flex-grow:1"></div>
<div style="display:flex;justify-content:space-between">{psychiatrist(200)}{psychologist(200)}{counsellor(200)}{socialworker(200)}</div>
<div class="foot" style="margin-top:40px"><span>@garypsychology07</span><div style="display:flex;align-items:center;gap:16px;padding:18px 32px;border-radius:999px;background:#F2785C;color:#1E1E2A;font-size:34px;font-weight:700"><span>swipe</span>{svg("arrow",40,w=2.5)}</div></div></div>''')
S.append(f'''<div class="s"><div class="lab">QUICK QUIZ</div>
<div style="flex-grow:1"></div>
<div style="display:flex;justify-content:center">{quiz(360)}</div>
<h1 style="margin-top:40px;font-size:84px;text-align:center">Only <span style="font-style:italic;color:#C24A2B">one</span> of these 4 can prescribe medication.</h1>
<div style="margin-top:20px;text-align:center">{zs("开药",40)}</div>
<p style="margin:40px 0 0;font-size:44px;text-align:center;font-weight:700">Which one? 🤔</p>
<div style="flex-grow:1"></div>
<p style="margin:0;text-align:center;font-size:30px;color:#8A7F74">Answer on the next slide →</p>
{foot(2)}</div>''')
P=[('Psychiatrist','精神科医生',psychiatrist,
   ['A <b>medical doctor</b> who specialised in mental health','Diagnoses mental illness and ✅ <b>can prescribe medication</b> (the quiz answer)'],
   'Medical degree → specialist training in psychiatry','Malaysian Medical Council (National Specialist Register)'),
  ('Clinical psychologist','临床心理学家',psychologist,
   ['Assesses and diagnoses mental health conditions','Gives <b>psychological therapy (心理治疗)</b>, without medication'],
   'Psychology degree → <b>Master’s in clinical psychology</b>','Malaysian Allied Health Professions Council, which issues a <b>practising certificate (执业证书)</b>'),
  ('Counsellor','辅导员 / 心理咨询师',counsellor,
   ['Helps with stress, relationships, career and emotional difficulties through talk-based support','Works in schools, universities, companies and private practice'],
   'A counselling degree','Lembaga Kaunselor Malaysia. You <b>can’t practise</b> without <b>registering (注册)</b>'),
  ('Social worker','社会工作者',socialworker,
   ['<b>Holistic support (全面支援)</b> for social, family, financial, health and safety problems','Connects people to services, e.g. helping a family get financial aid or a child get protection','Works in hospitals, welfare departments, child protection and NGOs'],
   'A social work degree',None)]
for i,(en,zh,toon,pts,path,reg) in enumerate(P):
    rows=''.join(f'<div style="display:flex;gap:20px;align-items:flex-start"><div style="width:14px;height:14px;border-radius:50%;background:#F2785C;margin-top:18px;flex-shrink:0"></div><div style="font-size:38px;line-height:1.42">{z(p)}</div></div>' for p in pts)
    regblk=f'<div style="margin-top:22px"><div class="k">REGULATED BY</div><div style="font-size:34px;line-height:1.4">{z(reg)}</div></div>' if reg else ''
    S.append(f'''<div class="s"><div style="display:flex;justify-content:space-between;align-items:flex-start;gap:20px">
<div style="display:flex;flex-direction:column;gap:18px"><div class="lab">WHO’S WHO · {i+1} OF 4</div>
<h1 style="font-size:{80 if len(en)>13 else 96}px">{en}</h1><div>{zs(zh,40)}</div></div>
<div style="flex-shrink:0">{toon(230)}</div></div>
<div style="margin-top:34px;display:flex;flex-direction:column;gap:22px">{rows}</div>
<div style="flex-grow:1"></div>
<div style="padding:36px 44px;border-radius:32px;background:#FFFDF8;border:2px solid #E4DDD0"><div class="k">PATH</div><div style="font-size:36px;line-height:1.4">{z(path)}</div>{regblk}</div>
{foot(i+3)}</div>''')
S.append(f'''<div class="s"><div style="display:flex;justify-content:space-between;align-items:flex-start"><div class="lab">SURPRISING FACT</div>{badge(220)}</div>
<h1 style="margin-top:10px;font-size:84px;line-height:1.08">In Malaysia, <span style="font-style:italic;color:#3D3A8C">“psychologist”</span> on its own isn’t a legally protected title.</h1>
<p style="margin:44px 0 0;font-size:42px;line-height:1.45"><b>“Clinical psychologist”</b> is the regulated one.</p>
<div style="flex-grow:1"></div>
<div style="padding:36px 44px;border-radius:32px;background:#FBE3DB;font-size:40px;line-height:1.45">💡 Before booking someone, check their {z("<b>registration (注册)</b>")}.</div>
{foot(7)}</div>''')
W=[('Severe symptoms, or you might need medication','Psychiatrist',psychiatrist),('Assessment or therapy for a mental health condition','Clinical psychologist',psychologist),('Stress, relationships, career worries','Counsellor',counsellor),('Family, financial or safety problems, or getting access to help','Social worker',socialworker)]
wr=''.join(f'<div style="display:flex;align-items:center;gap:24px;padding:22px 0;border-bottom:2px solid #E4DDD0">{t(92)}<div style="flex:1"><div style="font-size:31px;line-height:1.35;color:#4A4A56">{a}</div><div style="font-family:Fraunces,serif;font-weight:700;font-size:42px;margin-top:4px">→ {b}</div></div></div>' for a,b,t in W)
S.append(f'''<div class="s"><div class="lab">SAVE THIS SLIDE</div>
<h1 style="margin-top:22px;font-size:92px">Who do I <span style="font-style:italic;color:#3D3A8C">go to?</span></h1>
<div style="margin-top:26px">{wr}</div>
<div style="flex-grow:1"></div>
<div style="padding:28px 40px;border-radius:28px;background:#1E1E2A;color:#F7F3EC;font-size:34px;line-height:1.4">🚨 In a crisis, go to the <b>nearest hospital emergency department</b> {zs("(急诊部)",26)}</div>
{foot(8)}</div>''')
S.append(f'''<div class="s"><div class="lab">AND ME?</div>
<h1 style="margin-top:30px;font-size:88px">Year 1 psychology student.</h1>
<p style="margin:40px 0 0;font-size:42px;line-height:1.45">A psych degree alone <b>doesn’t</b> make you a clinical psychologist. That takes a <b>master’s</b>.</p>
<div style="flex-grow:1"></div><div style="display:flex;justify-content:space-between;opacity:.9">{psychiatrist(180)}{psychologist(180)}{counsellor(180)}{socialworker(180)}</div><div style="flex-grow:1"></div>
<div style="font-size:38px;font-weight:700;line-height:1.4">💬 Which two did you think were the same thing? Comment below</div>
<div style="margin-top:32px;display:flex"><span style="padding:20px 40px;border-radius:999px;background:#F2785C;color:#1E1E2A;font-size:36px;font-weight:700">📌 Save & share with someone who mixes them up</span></div>
<p style="margin:28px 0 0;font-size:24px;color:#8A7F74">Student notes, not professional advice · Follow @garypsychology07</p>
<div class="foot" style="justify-content:flex-end"><div style="display:flex;align-items:center;gap:20px"><span>9 / 9</span><div class="bar"><div style="width:180px"></div></div></div></div></div>''')
for i,s in enumerate(S,1): open(f'slide-{i:02d}.html','w').write(HEAD+s+'</body></html>')
