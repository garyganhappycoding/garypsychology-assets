# Content for this carousel. Edit text, run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from common import *
from toons import *
T=9
def foot(n): return f'<div class="foot"><span>@garypsychology07</span><div style="display:flex;align-items:center;gap:20px"><span>{n} / {T}</span><div class="bar"><div style="width:{round(180*n/T)}px"></div></div></div></div>'
G=[('Describe','描述','What is happening?','Students who scroll their phones right up to the exam seem to score lower than students who don’t.','Just the <b>observation (观察)</b>. No cause yet.'),
('Explain','解释','Why is it happening?','<b>If</b> scrolling fills your head with distracting information, <b>then</b> you’ll recall less of what you studied.','This is a <b>testable hypothesis (可检验的假设)</b>, not a fact.'),
('Predict','预测','When will it happen again?','In the next exam, students who scroll in the 10 minutes before will score lower than students who review their notes.','A <b>forecast (预判)</b> that follows from the explanation, not a new hypothesis.'),
('Control','控制','How can it be changed?','Try a phone-free 10-minute review before exams, then check whether scores improve.','A real-world <b>intervention (干预)</b> based on what you found.')]
def num(n,size,cur=False): return f'<div class="ic" style="width:{size}px;height:{size}px;font-family:Fraunces,serif;font-weight:700;font-size:{int(size*.45)}px;{"background:#F2785C;color:#1E1E2A" if cur else ""}">{n}</div>'
S=[]
S.append(f'''<div class="s"><div class="lab">PSYCH NOTES · YEAR 1</div>
<h1 style="margin-top:40px;font-size:150px">Psychology isn’t <span style="font-style:italic;color:#3D3A8C">guessing.</span></h1>
<p style="margin:44px 0 0;font-size:44px;line-height:1.3;color:#4A4A56">Every study works towards the same 4 goals</p>
<div style="flex-grow:1"></div><div style="display:flex;gap:24px;align-items:center">{"".join(num(i+1,120) for i in range(4))}</div>
<div class="foot" style="margin-top:64px"><span>@garypsychology07</span><div style="display:flex;align-items:center;gap:16px;padding:18px 32px;border-radius:999px;background:#F2785C;color:#1E1E2A;font-size:34px;font-weight:700"><span>swipe</span>{svg("arrow",40,w=2.5)}</div></div></div>''')
rows=''.join(f'<div style="display:flex;align-items:center;gap:32px">{num(i+1,96)}<div><div style="font-family:Fraunces,serif;font-weight:700;font-size:60px;line-height:1">{g[0]} <span class="zh" style="font-size:34px">{g[1]}</span></div><div style="font-size:36px;color:#4A4A56;margin-top:8px">{g[2]}</div></div></div>' for i,g in enumerate(G))
S.append(f'''<div class="s"><div class="lab">THE 4 GOALS OF PSYCHOLOGY</div>
<div style="margin-top:60px;display:flex;flex-direction:column;gap:52px">{rows}</div>
<div style="flex-grow:1"></div>
<div style="padding:36px 44px;border-radius:32px;background:#FBE3DB;font-family:Fraunces,serif;font-style:italic;font-size:44px;line-height:1.2">Let’s run one example through all&#160;four&#160;→</div>
{foot(2)}</div>''')
for i,(en,zh,q,ex,warn) in enumerate(G):
    prog=''.join(num(j+1,64,j==i) if j<=i else f'<div style="width:64px;height:64px;border-radius:50%;border:3px solid #D9D2C4;box-sizing:border-box;display:flex;align-items:center;justify-content:center;font-family:Fraunces,serif;font-weight:700;font-size:28px;color:#B8AFA2">{j+1}</div>' for j in range(4))
    S.append(f'''<div class="s"><div style="display:flex;justify-content:space-between;align-items:center"><div class="lab">GOAL {i+1} OF 4</div><div style="display:flex;gap:14px">{prog}</div></div>
<h1 style="margin-top:40px;font-size:120px">{en} <span style="font-family:'Noto Sans CJK SC',sans-serif;font-weight:500;font-size:52px;color:#8A7F74;letter-spacing:0">{zh}</span></h1>
<div style="margin-top:20px;font-family:Fraunces,serif;font-style:italic;font-weight:500;font-size:60px;color:#3D3A8C">{q}</div>
<div style="flex-grow:1"></div>
<div style="padding:40px 44px;border-radius:32px;background:#FFFDF8;border:2px solid #E4DDD0"><div class="k">EXAMPLE</div><div style="font-size:42px;line-height:1.4">{ex}</div><div style="margin-top:18px;font-size:22px;color:#8A7F74">Example only, not real data</div></div>
<div style="margin-top:28px;padding:34px 44px;border-radius:32px;background:#FBE3DB;display:flex;gap:20px;align-items:flex-start"><span style="font-size:40px;line-height:1.3">⚠️</span><div style="font-size:38px;line-height:1.4">{z(warn)}</div></div>
{foot(i+3)}</div>''')
steps=[('Perceive the question','发现问题'),('Form a hypothesis','提出假设'),('Test the hypothesis','检验假设'),('Draw conclusions','得出结论'),('Report results','报告结果')]
sr=''.join(f'<div style="display:flex;align-items:center;gap:28px">{num(i+1,72)}<div style="font-size:42px;font-weight:600">{a} <span class="zh">{b}</span></div></div>' for i,(a,b) in enumerate(steps))
S.append(f'''<div class="s"><div class="lab">HOW RESEARCHERS GET THERE</div>
<h1 style="margin-top:28px;font-size:88px">The 5 steps of the <span style="font-style:italic;color:#3D3A8C">scientific method</span> <span style="font-family:'Noto Sans CJK SC',sans-serif;font-weight:500;font-size:40px;color:#8A7F74;letter-spacing:0">科学方法</span></h1>
<div style="margin-top:56px;display:flex;flex-direction:column;gap:30px">{sr}</div>
<div style="flex-grow:1"></div>
<div style="padding:36px 44px;border-radius:32px;background:#FBE3DB;font-size:36px;line-height:1.45">💡 It’s a system for gathering data that reduces {z("<b>bias (偏差)</b> and <b>measurement error (测量误差)</b>")}.</div>
{foot(7)}</div>''')
cs=[('Describe','描述','what you see (no cause)'),('Explain','解释','an if-then hypothesis'),('Predict','预测','a forecast from that hypothesis'),('Control','控制','an intervention that changes the outcome')]
cr=''.join(f'<div style="display:flex;align-items:center;gap:26px">{num(i+1,64)}<div style="width:250px;flex-shrink:0"><div style="font-family:Fraunces,serif;font-weight:700;font-size:44px;line-height:1">{a}</div><div style="font-family:\'Noto Sans CJK SC\',sans-serif;font-size:24px;color:#8A7F74;margin-top:4px">{b}</div></div><div style="font-size:34px;font-weight:600;color:#3D3A8C;line-height:1.3">= {c}</div></div>' for i,(a,b,c) in enumerate(cs))
S.append(f'''<div class="s"><div class="lab">SAVE THIS SLIDE</div>
<h1 style="margin-top:22px;font-size:110px">Cheat <span style="font-style:italic;color:#3D3A8C">sheet</span></h1>
<div style="margin-top:44px;padding:40px 44px;border-radius:32px;background:#FFFDF8;border:2px solid #E4DDD0;display:flex;flex-direction:column;gap:34px">{cr}</div>
<div style="flex-grow:1"></div>
<div style="padding:34px 44px;border-radius:32px;background:#FBE3DB;font-size:36px;line-height:1.45">❌ <b>Common mistake:</b> writing all four as the same opinion in different words</div>
{foot(8)}</div>''')
S.append(f'''<div class="s"><div class="ic" style="width:136px;height:136px">{svg("book",64)}</div>
<h1 style="margin-top:52px;font-size:112px">Save this for your <span style="font-style:italic;color:#3D3A8C">psych exam</span></h1>
<p style="margin:40px 0 0;font-size:40px;line-height:1.4">💬 <b>Try it:</b> pick something you’ve noticed about students and run it through the 4 goals in the comments</p>
<div style="flex-grow:1"></div>
<div style="padding:40px 44px;border-radius:32px;background:#FFFDF8;border:2px solid #E4DDD0"><div class="k">NEXT UP</div><div style="font-family:Fraunces,serif;font-weight:700;font-size:54px;line-height:1.1">Would Little Albert be allowed today?</div></div>
<div style="margin-top:40px;display:flex"><span style="padding:22px 44px;border-radius:999px;background:#F2785C;color:#1E1E2A;font-size:42px;font-weight:700">Follow @garypsychology07</span></div>
<div class="foot" style="justify-content:flex-end"><div style="display:flex;align-items:center;gap:20px"><span>9 / 9</span><div class="bar"><div style="width:180px"></div></div></div></div></div>''')
for i,s in enumerate(S,1): open(f'slide-{i:02d}.html','w').write(HEAD+s+'</body></html>')
