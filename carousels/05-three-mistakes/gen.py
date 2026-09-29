# Content for this carousel. Edit text, run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from common import *
from toons import *
T=8
def foot(n): return f'<div class="foot"><span>@garypsychology07</span><div style="display:flex;align-items:center;gap:20px"><span>{n} / {T}</span><div class="bar"><div style="width:{round(180*n/T)}px"></div></div></div></div>'
def zs(t,s=40): return f'<span style="font-family:\'Noto Sans CJK SC\',sans-serif;font-weight:500;font-size:{s}px;color:#8A7F74;letter-spacing:0;white-space:nowrap">{t}</span>'
def bad(t): return f'<div style="padding:30px 38px;border-radius:28px;background:#FFFDF8;border:2px solid #E4DDD0"><div class="k">❌ WHAT I DID</div><div style="font-size:36px;line-height:1.42">{z(t)}</div></div>'
S=[]
S.append(f'''<div class="s"><div style="display:flex;justify-content:space-between;align-items:flex-start"><div class="lab">MY PSYCH JOURNEY · YEAR 1</div>{exam(230)}</div>
<h1 style="margin-top:6px;font-size:112px">I scored <span style="font-style:italic;color:#C24A2B">5/10</span> on a question I thought I nailed.</h1>
<p style="margin:40px 0 0;font-size:44px;line-height:1.3;color:#4A4A56">3 mistakes from my first psychology essay practice</p>
<div style="flex-grow:1"></div>
<div class="foot"><span>@garypsychology07</span><div style="display:flex;align-items:center;gap:16px;padding:18px 32px;border-radius:999px;background:#F2785C;color:#1E1E2A;font-size:34px;font-weight:700"><span>swipe</span>{svg("arrow",40,w=2.5)}</div></div></div>''')
S.append(f'''<div class="s"><div class="lab">CONTEXT</div>
<p style="margin:40px 0 0;font-size:48px;line-height:1.45">Year 1, Module 0. I answered <b>6 practice essay questions</b> and marked them against the lecture notes.</p>
<div style="flex-grow:1"></div>
<div style="display:flex;gap:24px;align-items:flex-end;justify-content:center">
{"".join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:12px"><div style="font-family:Fraunces,serif;font-weight:700;font-size:34px">{v}</div><div style="width:110px;height:{int(float(v)*40)}px;border-radius:14px 14px 0 0;background:{"#F2785C" if float(v)<6 else "#3D3A8C"}"></div><div style="font-size:26px;color:#5A5A66">Q{i+1}</div></div>' for i,v in enumerate(["9","8.5","5.5","5","7","6.5"]))}
</div>
<div style="margin-top:16px;text-align:center;font-size:24px;color:#8A7F74">Q1–Q2 scores are after revising my answers</div>
<div style="flex-grow:1"></div>
<div style="padding:34px 44px;border-radius:32px;background:#FBE3DB;font-family:Fraunces,serif;font-style:italic;font-size:48px;line-height:1.2">The same 3 mistakes kept coming&#160;back&#160;👇</div>
{foot(2)}</div>''')
S.append(f'''<div class="s"><div class="lab">MISTAKE 1 OF 3</div>
<h1 style="margin-top:24px;font-size:80px">Mixing up <span style="font-style:italic;color:#3D3A8C">classical</span> and <span style="font-style:italic;color:#3D3A8C">operant</span> conditioning</h1>
<div style="flex-grow:1"></div>
{bad("I used “conditioned stimulus / conditioned response” when writing about Skinner’s operant conditioning.")}
<div style="margin-top:24px">{bad("I said Watson <b>discovered</b> classical conditioning. It was <b>Pavlov</b>. Watson applied it to humans (Little Albert).")}</div>
<div style="margin-top:24px;padding:30px 38px;border-radius:28px;background:#FBE3DB"><div class="k">✅ THE FIX</div><div style="font-size:36px;line-height:1.42">Each type has its <b>own vocabulary</b>. Don’t mix them. Next slide 👉</div></div>
{foot(3)}</div>''')
terms=[('NS','Neutral stimulus','中性刺激','Rat (before)'),('UCS','Unconditioned stimulus','无条件刺激','Loud bang'),('UCR','Unconditioned response','无条件反应','Fear of the bang'),('CS','Conditioned stimulus','条件刺激','Rat (after)'),('CR','Conditioned response','条件反应','Fear of the rat')]
tr=''.join(f'<div style="display:flex;align-items:center;gap:22px;padding:20px 0;border-bottom:2px solid #E4DDD0"><div class="ic" style="width:92px;height:60px;border-radius:14px;font-weight:800;font-size:28px">{a}</div><div style="flex:1"><div style="font-size:35px;font-weight:700">{b} {zs(c,24)}</div></div><div style="font-size:27px;color:#C24A2B;font-weight:600;text-align:right;width:230px">{d}</div></div>' for a,b,c,d in terms)
S.append(f'''<div class="s"><div class="lab">MISTAKE 1 · THE TERMS</div>
<h1 style="margin-top:20px;font-size:62px">Classical {zs("经典条件反射",32)} · Pavlov</h1>
<div style="margin-top:6px;font-size:28px;color:#5A5A66">Involuntary response · stimulus → response · <span style="color:#C24A2B;font-weight:600">Little Albert example</span></div>
<div style="margin-top:14px">{tr}</div>
<div style="flex-grow:1"></div>
<h1 style="font-size:62px">Operant {zs("操作性条件反射",32)} · Skinner</h1>
<div style="margin-top:6px;font-size:28px;color:#5A5A66">Voluntary behaviour · behaviour → consequence</div>
<div style="margin-top:18px;display:flex;flex-wrap:wrap;gap:14px">{"".join(f'<span class="chip" style="font-size:28px;padding:12px 24px;{s2}">{t}</span>' for t,s2 in [("Reinforcement 强化",""),("Positive reinforcement 正强化",""),("Negative reinforcement 负强化",""),("Punishment 惩罚","background:#F2785C;color:#1E1E2A")])}</div>
{foot(4)}</div>''')
S.append(f'''<div class="s"><div class="lab">MISTAKE 2 OF 3 · SCORE 5.5/10</div>
<h1 style="margin-top:24px;font-size:84px">Blurring the <span style="font-style:italic;color:#3D3A8C">4 goals</span></h1>
<div style="margin-top:36px">{bad("I wrote all 4 goals as the same opinion in different words, and wrote my “explanation” as if it were a fact.")}</div>
<div style="flex-grow:1"></div>
<div style="padding:34px 40px;border-radius:28px;background:#FBE3DB"><div class="k">✅ THE FIX</div><div style="display:flex;flex-direction:column;gap:18px;font-size:36px;line-height:1.35">
<div><b>Describe</b> {zs("描述",26)} = what you see, no cause</div>
<div><b>Explain</b> {zs("解释",26)} = a testable if-then <b>hypothesis</b> {zs("假设",26)}</div>
<div><b>Predict</b> {zs("预测",26)} = a forecast that follows from it</div>
<div><b>Control</b> {zs("控制",26)} = a real-world <b>intervention</b> {zs("干预",26)}</div></div></div>
{foot(5)}</div>''')
PR=[('P','Protection from risk','风险保护'),('R','Right to withdraw','退出权'),('I','Informed consent','知情同意'),('C','Confidentiality','保密'),('E','Ethics board approval','伦理审查'),('D','Debriefing (+ justify any deception)','事后说明')]
pr=''.join(f'<div style="display:flex;align-items:center;gap:24px"><div class="ic" style="width:74px;height:74px;font-family:Fraunces,serif;font-weight:800;font-size:40px;{"background:#F2785C;color:#1E1E2A" if i%2 else ""}">{a}</div><div style="font-size:34px;font-weight:600;line-height:1.25">{b} {zs(c,24)}</div></div>' for i,(a,b,c) in enumerate(PR))
S.append(f'''<div class="s"><div class="lab">MISTAKE 3 OF 3 · SCORE 5/10</div>
<h1 style="margin-top:20px;font-size:70px">Only listing 1–2 <span style="font-style:italic;color:#3D3A8C">ethics rules</span></h1>
<div style="margin-top:22px;font-size:32px;line-height:1.4;color:#4A4A56">❌ I stopped at consent, deception and debriefing.</div>
<div style="margin-top:26px;padding:32px 38px;border-radius:28px;background:#FFFDF8;border:2px solid #E4DDD0"><div style="font-family:Fraunces,serif;font-size:44px;font-weight:700;margin-bottom:22px">✅ Remember: good research is <span style="color:#C24A2B;letter-spacing:.06em">PRICED</span></div><div style="display:flex;flex-direction:column;gap:16px">{pr}</div></div>
<div style="flex-grow:1"></div>
<div style="font-size:24px;color:#8A7F74">PRICED is my own memory trick, not an official acronym.</div>
{foot(6)}</div>''')
S.append(f'''<div class="s"><div class="lab">WHAT I DO DIFFERENTLY NOW</div>
<h1 style="margin-top:24px;font-size:88px">My <span style="font-style:italic;color:#3D3A8C">checklist</span></h1>
<div style="flex-grow:1"></div>
<div style="display:flex;flex-direction:column;gap:34px">{"".join(f'<div style="display:flex;gap:24px;align-items:flex-start"><div class="ic" style="width:60px;height:60px;border-radius:14px;background:#FFFDF8;border:3px solid #3D3A8C;box-sizing:border-box;color:#3D3A8C">{svg("arrow",0) if False else ""}<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#3D3A8C" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></div><div style="font-size:40px;line-height:1.4">{t}</div></div>' for t in ["Check which <b>theorist</b> goes with which idea","Keep each concept’s <b>vocabulary</b> separate","For “list” questions, aim for <b>3+ points</b>, not 1","Reread the question: <i>explain</i>, <i>predict</i> and <i>apply</i> ask for different things"])}</div>
<div style="flex-grow:1"></div>
{foot(7)}</div>''')
S.append(f'''<div class="s"><div class="lab">KEEP GOING</div>
<h1 style="margin-top:30px;font-size:84px">Low marks in practice = finding the gaps <span style="font-style:italic;color:#3D3A8C">before</span> the real exam.</h1>
<div style="flex-grow:1"></div>
<div style="font-size:40px;font-weight:700;line-height:1.4">💬 What’s the mistake you keep making in exams? Comment below</div>
<p style="margin:28px 0 0;font-size:32px;line-height:1.45;color:#4A4A56">📌 My 4 goals and Little Albert posts go deeper on mistakes 2 and 3</p>
<div style="margin-top:36px;display:flex"><span style="padding:20px 40px;border-radius:999px;background:#F2785C;color:#1E1E2A;font-size:38px;font-weight:700">Save · Follow @garypsychology07</span></div>
<div class="foot" style="justify-content:flex-end"><div style="display:flex;align-items:center;gap:20px"><span>8 / 8</span><div class="bar"><div style="width:180px"></div></div></div></div></div>''')
for i,s in enumerate(S,1): open(f'slide-{i:02d}.html','w').write(HEAD+s+'</body></html>')
