# Content for this carousel. Edit text, run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from common import *
T=9
def foot(n): return f'<div class="foot"><span>@garypsychology07</span><div style="display:flex;align-items:center;gap:20px"><span>{n} / {T}</span><div class="bar"><div style="width:{round(180*n/T)}px"></div></div></div></div>'
def zs(t,s=40): return f'<span style="font-family:\'Noto Sans CJK SC\',sans-serif;font-weight:500;font-size:{s}px;color:#8A7F74;letter-spacing:0;white-space:nowrap">{t}</span>'
# phone-style frame around a real screenshot of the site (cropped from the top)
def phone(img,w,h,pos='top',rot=0):
    return (f'<div style="width:{w}px;height:{h}px;border:10px solid #1E1E2A;border-radius:44px;overflow:hidden;background:#fff;'
            f'box-shadow:0 24px 50px rgba(30,30,42,.18);flex-shrink:0;transform:rotate({rot}deg)">'
            f'<img src="{img}" style="display:block;width:100%;height:100%;object-fit:cover;object-position:{pos}"></div>')
def tick(t): return (f'<div style="display:flex;gap:20px;align-items:flex-start"><div class="ic" style="width:52px;height:52px;border-radius:14px;background:#FFFDF8;border:3px solid #3D3A8C;box-sizing:border-box">'
    f'<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#3D3A8C" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></div>'
    f'<div style="font-size:36px;line-height:1.38">{t}</div></div>')
S=[]
# 1 cover
S.append(f'''<div class="s"><div class="lab">HELP PSY111 · MIDTERM REVISION</div>
<h1 style="margin-top:22px;font-size:96px">PSY111 midterm coming? <span style="font-style:italic;color:#C24A2B">Stop re&#8209;reading your&#160;slides.</span></h1>
<p style="margin:30px 0 0;font-size:40px;line-height:1.35;color:#4A4A56">Test yourself instead, with free recall cards made from the lecture slides.</p>
<div style="flex-grow:1"></div>
<div style="display:flex;justify-content:space-between;align-items:flex-end">
<div style="display:flex;flex-direction:column;gap:26px;padding-bottom:6px"><span style="font-size:28px;font-weight:600;color:#5A5A66">@garypsychology07</span>
<div style="display:flex;align-items:center;gap:16px;padding:18px 32px;border-radius:999px;background:#F2785C;color:#1E1E2A;font-size:34px;font-weight:700"><span>swipe</span>{svg("arrow",40,w=2.5)}</div></div>
{phone("shot-clues.png",440,560,rot=3)}</div></div>''')
# 2 setup
card=lambda top,term,zh,desc,bg: (f'<div style="flex:1;padding:34px 34px 38px;border-radius:28px;background:{bg};display:flex;flex-direction:column;gap:14px">'
    f'<div class="k" style="margin:0">{top}</div><div style="font-family:Fraunces,serif;font-weight:700;font-size:54px;line-height:1.05">{term}</div>{zs(zh,34)}'
    f'<div style="margin-top:8px;font-size:32px;line-height:1.4">{desc}</div></div>')
S.append(f'''<div class="s"><div class="lab">WHY RE-READING TRICKS YOU</div>
<h1 style="margin-top:24px;font-size:84px">Familiar <span style="font-style:italic;color:#3D3A8C">≠</span> remembered</h1>
<p style="margin:30px 0 0;font-size:38px;line-height:1.42;color:#4A4A56">Re-reading feels productive because everything looks familiar. But the exam won’t show you the slides.</p>
<div style="flex-grow:1"></div>
<div style="display:flex;gap:24px">
{card("RE-READING","Recognition","认出","You see it and think “I know this”.","#FFFDF8;border:2px solid #E4DDD0")}
{card("THE EXAM","Recall","回忆","Blank paper. You pull the idea out yourself.","#E3E2F4")}
</div>
<div style="flex-grow:1"></div>
<div style="padding:32px 42px;border-radius:32px;background:#FBE3DB;font-family:Fraunces,serif;font-style:italic;font-size:46px;line-height:1.2">So practise recall, not re-reading&#160;👇</div>
{foot(2)}</div>''')
# 3 what I built
TP=[("Personality 1","Freud, defence mechanisms, Bandura, Rogers, Big Five",47),("Personality 2","Genetics, culture, assessments",23),("Motivation","Drives, needs, arousal, hunger",23),("Emotion","Amygdala and 6 theories of emotion",14),("Intelligence","Theories, IQ tests, nature vs nurture",24)]
rows=''.join(f'<div style="display:flex;align-items:center;gap:26px;padding:22px 0;border-bottom:2px solid #E4DDD0"><div class="ic" style="width:96px;height:72px;border-radius:16px;font-family:Fraunces,serif;font-weight:700;font-size:38px">{n}</div><div style="flex:1"><div style="font-size:38px;font-weight:700">{a}</div><div style="font-size:28px;color:#5A5A66;margin-top:4px">{b}</div></div></div>' for a,b,n in TP)
S.append(f'''<div class="s"><div class="lab">WHAT I BUILT</div>
<h1 style="margin-top:24px;font-size:76px"><span style="font-style:italic;color:#3D3A8C">131</span> recall cards {zs("回忆卡",40)}</h1>
<p style="margin:18px 0 0;font-size:34px;line-height:1.4;color:#4A4A56">One card per concept, across the 5 PSY111 topics:</p>
<div style="margin-top:14px">{rows}</div>
<div style="flex-grow:1"></div>
<div style="font-size:25px;color:#8A7F74;line-height:1.4">Made by a student from the lecture slides. Not official HELP material, so check your own slides too.</div>
{foot(3)}</div>''')
# 4 how it works
STEP=[("1","Tap a concept"),("2","Read the clues "+zs("提示",26)),("3","Say it in your own words"),("4","Tap Reveal to check")]
st=''.join(f'<div style="display:flex;align-items:center;gap:16px;width:48%"><div class="ic" style="width:54px;height:54px;font-weight:800;font-size:28px;{"background:#F2785C;color:#1E1E2A" if i%2 else ""}">{a}</div><div style="font-size:32px;font-weight:600;line-height:1.25">{b}</div></div>' for i,(a,b) in enumerate(STEP))
S.append(f'''<div class="s"><div class="lab">HOW IT WORKS</div>
<h1 style="margin-top:22px;font-size:72px">Clues first. <span style="font-style:italic;color:#3D3A8C">Answer last.</span></h1>
<div style="margin-top:34px;display:flex;flex-wrap:wrap;row-gap:22px;justify-content:space-between">{st}</div>
<div style="flex-grow:1"></div>
<div style="display:flex;gap:28px;justify-content:center">
<div style="display:flex;flex-direction:column;align-items:center;gap:14px">{phone("shot-clues.png",420,640)}<span style="font-size:26px;font-weight:700;color:#C24A2B;letter-spacing:.12em">BEFORE</span></div>
<div style="display:flex;flex-direction:column;align-items:center;gap:14px">{phone("shot-reveal.png",420,640,pos="center 62%")}<span style="font-size:26px;font-weight:700;color:#3D3A8C;letter-spacing:.12em">AFTER REVEAL</span></div></div>
{foot(4)}</div>''')
# 5 paraphrase table
S.append(f'''<div class="s"><div class="lab">FOR SHORT-ANSWER QUESTIONS</div>
<h1 style="margin-top:22px;font-size:80px">Paraphrase table {zs("改写表",42)}</h1>
<p style="margin:28px 0 0;font-size:38px;line-height:1.42;color:#4A4A56">Type each concept in <b style="color:#1E1E2A">your own words</b>, then tap <b style="color:#1E1E2A">Show original</b> to compare.</p>
<div style="flex-grow:1"></div>
<div style="display:flex;gap:0;margin-bottom:14px"><div class="k" style="flex:1;margin:0;padding-left:24px">YOUR WORDS · Id</div><div class="k" style="flex:1;margin:0;padding-left:24px;color:#3D3A8C">ORIGINAL</div></div><div style="border:10px solid #1E1E2A;border-radius:32px;overflow:hidden;box-shadow:0 24px 50px rgba(30,30,42,.18);background:#fff"><img src="shot-table.png" style="display:block;width:100%"></div>
<div style="flex-grow:1"></div>
<div style="font-size:30px;color:#4A4A56">✍️ Writing it out is closer to the real exam than reading it.</div>
{foot(5)}</div>''')
# 6 weak spots
S.append(f'''<div class="s"><div class="lab">GO FOR YOUR WEAK SPOTS</div>
<h1 style="margin-top:22px;font-size:76px">Don’t just go <span style="font-style:italic;color:#3D3A8C">top to bottom</span></h1>
<div style="flex-grow:1"></div>
<div style="display:flex;gap:36px;align-items:center">
<div style="flex:1;display:flex;flex-direction:column;gap:34px">
{tick("<b>Shuffle</b> "+zs("打乱",28)+" so you can’t rely on the order")}
{tick("Filter by <b>section</b>, e.g. only Hunger")}
{tick("See how many cards you’ve <b>revealed</b> per topic")}</div>
{phone("shot-motivation.png",420,640)}</div>
<div style="flex-grow:1"></div>
{foot(6)}</div>''')
# 7 progress saves
S.append(f'''<div class="s"><div class="lab">YOUR PROGRESS SAVES</div>
<h1 style="margin-top:22px;font-size:76px">Laptop at home, <span style="font-style:italic;color:#3D3A8C">phone on the bus</span>&#160;🚌</h1>
<div style="flex-grow:1"></div>
<div style="display:flex;gap:36px;align-items:center">
<div style="flex:1;display:flex;flex-direction:column;gap:32px">
{tick("Free account: <b>email + password</b>")}
{tick("No email to confirm. Start straight away")}
{tick("<b>Edit</b> cards or add your own")}</div>
{phone("shot-signup.png",420,640)}</div>
<div style="flex-grow:1"></div>
<div style="font-size:27px;color:#8A7F74">Remember your password: there’s no reset button yet.</div>
{foot(7)}</div>''')
# 8 cheat sheet
RT=[("5 min","Pick one topic. Go through the <b>clues only</b> as a warm-up"),("15 min","Every card once. Say each answer <b>out loud</b>"),("5 min","<b>Shuffle</b> and redo only the ones you got wrong"),("5 min","Write 3 of them in the <b>paraphrase table</b>")]
rt=''.join(f'<div style="display:flex;gap:26px;align-items:flex-start"><div class="ic" style="width:66px;height:66px;font-family:Fraunces,serif;font-weight:800;font-size:36px;{"background:#F2785C;color:#1E1E2A" if i%2 else ""}">{i+1}</div><div style="flex:1"><div class="k" style="margin-bottom:6px">{a}</div><div style="font-size:36px;line-height:1.38">{b}</div></div></div>' for i,(a,b) in enumerate(RT))
S.append(f'''<div class="s"><div class="lab">CHEAT SHEET · SAVE THIS</div>
<h1 style="margin-top:22px;font-size:80px">My <span style="font-style:italic;color:#3D3A8C">30-minute</span> revision routine</h1>
<div style="flex-grow:1"></div>
<div style="padding:40px 42px;border-radius:32px;background:#FFFDF8;border:2px solid #E4DDD0;display:flex;flex-direction:column;gap:34px">{rt}</div>
<div style="flex-grow:1"></div>
<div style="font-size:32px;color:#4A4A56">🔁 Tomorrow: same routine, next topic.</div>
{foot(8)}</div>''')
# 9 CTA
S.append(f'''<div class="s"><div class="lab">TRY IT</div>
<h1 style="margin-top:30px;font-size:120px">Link in bio <span style="font-style:italic;color:#C24A2B">🔗</span></h1>
<p style="margin:30px 0 0;font-size:40px;line-height:1.4;color:#4A4A56">Free. Works on your phone. Made by a PSY111 student, for PSY111 students.</p>
<div style="margin-top:44px;display:flex;flex-wrap:wrap;gap:14px">{"".join(f'<span class="chip" style="font-size:30px;{st}">{t}</span>' for t,st in [("Personality 1",""),("Personality 2","background:#F2785C;color:#1E1E2A"),("Motivation",""),("Emotion","background:#F2785C;color:#1E1E2A"),("Intelligence","")])}</div>
<div style="flex-grow:1"></div>
<div style="font-size:42px;font-weight:700;line-height:1.4">📩 Send this to your PSY111 groupmate before the midterm</div>
<p style="margin:26px 0 0;font-size:32px;line-height:1.45;color:#4A4A56">💬 Which topic are you most worried about? Comment below</p>
<div style="margin-top:40px;display:flex"><span style="padding:20px 40px;border-radius:999px;background:#F2785C;color:#1E1E2A;font-size:38px;font-weight:700">Save · Follow @garypsychology07</span></div>
<div class="foot" style="justify-content:flex-end"><div style="display:flex;align-items:center;gap:20px"><span>9 / 9</span><div class="bar"><div style="width:180px"></div></div></div></div></div>''')
for i,s in enumerate(S,1): open(f'slide-{i:02d}.html','w').write(HEAD+s+'</body></html>')
