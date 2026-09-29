# Content for this carousel. Edit text, run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from common import *
from toons import *
ICON['rat']='<path d="M13 22H4a2 2 0 0 1 0-4h12"/><path d="M13.236 18a3 3 0 0 0-2.2-5"/><path d="M16 9h.01"/><path d="M16.82 3.94a3 3 0 1 1 3.237 4.868l1.815 2.587a1.5 1.5 0 0 1-1.5 2.1l-2.872-.453a3 3 0 0 0-3.5 3"/><path d="M17 4.988a3 3 0 1 0-5.2 2.052A7 7 0 0 0 4 14.015 4 4 0 0 0 8 18"/>'
ICON['x']='<path d="M18 6 6 18"/><path d="m6 6 12 12"/>'
ICON['q']='<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/>'
ICON['shield']='<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/>'
T=9
def foot(n): return f'<div class="foot"><span>@garypsychology07</span><div style="display:flex;align-items:center;gap:20px"><span>{n} / {T}</span><div class="bar"><div style="width:{round(180*n/T)}px"></div></div></div></div>'
def zhspan(t,s=40): return f'<span style="font-family:\'Noto Sans CJK SC\',sans-serif;font-weight:500;font-size:{s}px;color:#8A7F74;letter-spacing:0">{t}</span>'
S=[]
S.append(f'''<div class="s"><div style="display:flex;justify-content:space-between;align-items:flex-start"><div class="lab">PSYCH NOTES · RESEARCH ETHICS</div><div class="ic" style="width:150px;height:150px">{svg("rat",78,w=1.6)}</div></div>
<h1 style="margin-top:30px;font-size:118px">This experiment taught a baby to be <span style="font-style:italic;color:#3D3A8C">afraid.</span></h1>
<p style="margin:48px 0 0;font-size:50px;line-height:1.3;color:#4A4A56;font-weight:600">Would it be allowed today?</p>
<div style="flex-grow:1"></div>
<div class="foot"><span>@garypsychology07</span><div style="display:flex;align-items:center;gap:16px;padding:18px 32px;border-radius:999px;background:#F2785C;color:#1E1E2A;font-size:34px;font-weight:700"><span>swipe</span>{svg("arrow",40,w=2.5)}</div></div></div>''')
S.append(f'''<div class="s"><div class="lab">THE STUDY · 1920</div>
<h1 style="margin-top:30px;font-size:120px">“Little Albert”</h1>
<div style="margin-top:30px"><span class="chip">John B. Watson · Rosalie Rayner</span></div>
<p style="margin:56px 0 0;font-size:44px;line-height:1.45">A baby known as <b>“Little Albert”</b>, less than a year old.</p>
<p style="margin:28px 0 0;font-size:44px;line-height:1.45">First, they showed him a <b>white rat</b>.</p>
<div style="flex-grow:1"></div>
<div style="padding:40px 44px;border-radius:32px;background:#FFFDF8;border:2px solid #E4DDD0;font-family:Fraunces,serif;font-size:56px;line-height:1.15"><b>No fear.</b> <span style="font-style:italic">He reached out to touch it.</span></div>
{foot(2)}</div>''')
steps=[('Each time Albert touched the rat, they made a <b>loud bang</b> behind his head.'),('After repeated pairings, Albert <b>cried at the rat alone</b>.'),('His fear spread to other furry things: a rabbit, a dog, a fur coat. This is called <b>generalisation (泛化)</b>.')]
sr=''.join(f'<div style="display:flex;gap:30px;align-items:flex-start"><div class="ic" style="width:76px;height:76px;font-family:Fraunces,serif;font-weight:700;font-size:36px">{i+1}</div><div style="font-size:42px;line-height:1.45;padding-top:6px">{z(t)}</div></div>' for i,t in enumerate(steps))
S.append(f'''<div class="s"><div class="lab">WHAT THEY DID</div>
<h1 style="margin-top:30px;font-size:96px">Then came the <span style="font-style:italic;color:#3D3A8C">loud bang.</span></h1>
<div style="flex-grow:1"></div><div style="display:flex;flex-direction:column;gap:48px">{sr}</div><div style="flex-grow:1"></div>
{foot(3)}</div>''')
def box(en,zh,fill='#FFFDF8',col='#1E1E2A'): return f'<div style="flex:1;padding:22px 24px;border-radius:24px;background:{fill};border:2px solid #E4DDD0;text-align:center"><div style="font-family:Fraunces,serif;font-weight:700;font-size:40px;color:{col}">{en}</div></div>'
def lbl(a,b): return f'<div style="font-size:26px;line-height:1.35;color:#5A5A66;text-align:center">{a}<br><span style="font-family:\'Noto Sans CJK SC\',sans-serif">{b}</span></div>'
arrow=f'<div style="display:flex;align-items:center;padding:0 6px">{svg("arrow",40,"#C24A2B",2.5)}</div>'
plus='<div style="display:flex;align-items:center;font-family:Fraunces,serif;font-size:48px;color:#C24A2B;padding:0 4px">+</div>'
before=f'''<div style="display:flex;align-items:stretch;gap:8px">{box("Rat","")}{plus}{box("Loud bang","")}{arrow}{box("Fear","",'#FBE3DB')}</div>
<div style="display:grid;grid-template-columns:1fr 60px 1fr 56px 1fr;margin-top:12px">{lbl("neutral stimulus","中性刺激")}<div></div>{lbl("unconditioned stimulus","无条件刺激")}<div></div>{lbl("unconditioned response","无条件反应")}</div>'''
after=f'''<div style="display:flex;align-items:stretch;gap:8px">{box("Rat","")}{arrow}{box("Fear","",'#FBE3DB')}</div>
<div style="display:grid;grid-template-columns:1fr 56px 1fr;margin-top:12px">{lbl("conditioned stimulus","条件刺激")}<div></div>{lbl("conditioned response","条件反应")}</div>'''
S.append(f'''<div class="s"><div class="lab">THE PSYCHOLOGY BEHIND IT</div>
<h1 style="margin-top:24px;font-size:88px">Classical conditioning</h1><div style="margin-top:12px">{zhspan("经典条件反射",40)}</div>
<div style="margin-top:56px"><div class="k">BEFORE · DURING PAIRING</div>{before}</div>
<div style="margin-top:52px"><div class="k">AFTER</div>{after}</div>
<div style="flex-grow:1"></div>
<div style="padding:34px 44px;border-radius:32px;background:#FBE3DB;font-size:40px;line-height:1.4">💡 It showed that emotions like fear can be <b>learned</b>.</div>
{foot(4)}</div>''')
S.append(f'''<div class="s"><div class="lab">THE PROBLEM</div>
<div style="flex-grow:1"></div>
<h1 style="font-size:92px;line-height:1.08">There’s no record that Watson ever <span style="font-style:italic;color:#C24A2B">removed Albert’s fear.</span></h1>
<p style="margin:56px 0 0;font-size:44px;line-height:1.45;color:#4A4A56">A baby was deliberately frightened, and the fear was left in place.</p>
<div style="flex-grow:1"></div>
{foot(5)}</div>''')
def mark(m):
    if m=='x': return f'<div class="ic" style="width:64px;height:64px;background:#F2785C;color:#1E1E2A">{svg("x",32,w=2.6)}</div>'
    if m=='q': return f'<div class="ic" style="width:64px;height:64px;background:#E4DDD0;color:#5A5A66;font-family:Fraunces,serif;font-weight:700;font-size:36px">?</div>'
    return f'<div class="ic" style="width:64px;height:64px;background:transparent;border:3px solid #D9D2C4;box-sizing:border-box;color:#8A7F74;font-size:32px;font-weight:700">–</div>'
def rules(rs): return ''.join(f'<div style="display:flex;gap:28px;align-items:flex-start">{mark(m)}<div><div style="font-size:40px;font-weight:700;line-height:1.25">{z(t)}</div><div style="font-size:32px;line-height:1.4;color:#4A4A56;margin-top:6px">{r}</div></div></div>' for m,t,r in rs)
R1=[('x','Protect participants from risk (风险)','Deliberately causing fear is harm.'),('x','Weigh harm against scientific value (科学价值)','The harm to a baby is hard to justify.'),('q','Informed consent (知情同意)','Records of what his mother was told are unclear.'),('x','Right to withdraw (退出权)','A baby can’t say “stop”.')]
R2=[('x','Debriefing (事后说明)','No one explained or undid what happened.'),('x','Correct undesirable consequences','The fear wasn’t undone.'),('n','Confidentiality (保密)','His real identity is still debated today.'),('n','Deception (欺骗) must be justified','A rule every modern study must meet.')]
for k,(RS,n) in enumerate(((R1,6),(R2,7))):
    S.append(f'''<div class="s"><div class="lab">TODAY’S RULES, CHECKED · {k+1}/2</div>
<h1 style="margin-top:24px;font-size:84px">Does it <span style="font-style:italic;color:#3D3A8C">pass?</span></h1>
<div style="flex-grow:1"></div><div style="display:flex;flex-direction:column;gap:46px">{rules(RS)}</div><div style="flex-grow:1"></div>
{foot(n)}</div>''')
S.append(f'''<div class="s"><div style="display:flex;justify-content:space-between;align-items:flex-start"><div class="lab">WHO CHECKS NOW</div><div class="ic" style="width:120px;height:120px">{svg("shield",60,w=1.8)}</div></div>
<p style="margin:30px 0 0;font-size:44px;line-height:1.45">Before a study can run today, an <b>ethics review board</b> {zhspan("(伦理审查委员会)",30)} has to approve it.</p>
<p style="margin:28px 0 0;font-size:44px;line-height:1.45">At HELP University, that’s the <b>HELP Ethics Review Board</b>.</p>
<div style="flex-grow:1"></div>
<div style="padding:48px 48px;border-radius:32px;background:#1E1E2A;color:#F7F3EC"><div class="k" style="color:#F2785C">VERDICT {zhspan("判决",24)}</div><div style="font-family:Fraunces,serif;font-weight:700;font-size:72px;line-height:1.08">❌ Little Albert would <span style="font-style:italic;color:#F2785C">not</span> be approved today.</div></div>
{foot(8)}</div>''')
S.append(f'''<div class="s"><div class="lab">EXAM TIP</div>
<p style="margin:30px 0 0;font-size:44px;line-height:1.45">Ethics questions usually expect <b>several</b> guidelines, not just one:</p>
<div style="margin-top:36px;display:flex;flex-wrap:wrap;gap:16px">{"".join(f'<span class="chip" style="font-size:30px;padding:14px 28px">{c}</span>' for c in ["Informed consent","Right to withdraw","Confidentiality","Protection from risk","Debriefing","Ethics board approval"])}</div>
<div style="flex-grow:1"></div>
<div style="font-size:38px;font-weight:700;line-height:1.4">💬 Should famous-but-unethical studies still be taught? Comment below</div>
<div style="margin-top:36px;padding:36px 44px;border-radius:32px;background:#FFFDF8;border:2px solid #E4DDD0"><div class="k">NEXT UP</div><div style="font-family:Fraunces,serif;font-weight:700;font-size:46px;line-height:1.15">Psychologist vs psychiatrist vs counsellor vs social worker</div></div>
<div style="margin-top:32px;display:flex"><span style="padding:20px 40px;border-radius:999px;background:#F2785C;color:#1E1E2A;font-size:38px;font-weight:700">📌 Save · Follow @garypsychology07</span></div>
<div class="foot" style="justify-content:flex-end"><div style="display:flex;align-items:center;gap:20px"><span>9 / 9</span><div class="bar"><div style="width:180px"></div></div></div></div></div>''')

import os
PH='file://'+os.path.abspath('albert.png')
S[1]=f'''<div class="s"><div class="lab">THE STUDY · 1920</div>
<h1 style="margin-top:24px;font-size:100px">“Little Albert”</h1>
<div style="margin-top:22px"><span class="chip">John B. Watson · Rosalie Rayner</span></div>
<div style="margin-top:34px;border-radius:28px;overflow:hidden;border:2px solid #E4DDD0;height:500px;background:#1E1E2A"><img src="{PH}" style="width:100%;height:100%;object-fit:cover;filter:sepia(.25) contrast(1.05)"></div>
<div style="margin-top:12px;font-size:22px;color:#8A7F74">Still from the original 1920 film of the study</div>
<div style="flex-grow:1"></div>
<p style="margin:0;font-size:40px;line-height:1.45">A baby, less than a year old. First, they showed him a <b>white rat</b>. <span style="font-family:Fraunces,serif;font-weight:700">No fear.</span> He reached out to touch it.</p>
{foot(2)}</div>'''
S[2]=S[2].replace('<div style="flex-grow:1"></div><div style="display:flex;flex-direction:column;gap:48px">',
 f'<div style="margin-top:36px;display:flex;align-items:center;justify-content:center;gap:10px">{rat(220)}{bang(240)}{baby_cry(220)}</div><div style="flex-grow:1"></div><div style="display:flex;flex-direction:column;gap:40px">',1)
S[2]=S[2].replace('font-size:42px;line-height:1.45;padding-top:6px','font-size:38px;line-height:1.42;padding-top:6px')

for i,s in enumerate(S,1): open(f'slide-{i:02d}.html','w').write(HEAD+s+'</body></html>')
