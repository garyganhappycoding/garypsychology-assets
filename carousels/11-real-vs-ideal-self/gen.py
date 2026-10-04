# Personality series 5/6 · Rogers: real vs ideal self. Run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from series import *
from toons import compare,selves
T=9;S=[]
S.append(cover('PERSONALITY · PART 5 OF 6',
 '“Why can’t you be like your <span style="font-style:italic;color:#C24A2B">cousin?</span>”',
 'Why it hurts so much, according to psychology.',compare(250),100))
S.append(slide(f'''{head('THE HUMANISTIC VIEW','It starts with your <span style="white-space:nowrap">self-concept</span>',80)}
<div style="margin-top:14px">{zs("人本主义 · 自我概念",40)}</div>{GROW}
{bullets(['Focuses on what makes us <b>uniquely human</b>: feelings, free choice, growth','<b>Carl Rogers</b>: your <b>self-concept</b> (自我概念) is the image of yourself you build through <b>people who matter to you</b>'],size=46,gap=40)}{GROW}
{ex('Parents, teachers, friends… what they say becomes part of how you see yourself.',42)}''',2,T))
def self_card(name,zh,col,txt,bg,fg='#1E1E2A'):
    return f'<div style="flex:1;padding:34px;border-radius:28px;background:{bg};color:{fg}"><div style="width:90px;height:90px;border-radius:50%;background:{col}"></div><div style="font-family:Fraunces,serif;font-weight:700;font-size:58px;margin-top:20px">{name}</div><div style="font-size:32px;opacity:.75">{zh}</div><div style="margin-top:18px;font-size:40px;line-height:1.4">{txt}</div></div>'
S.append(slide(f'''{head('TWO SELVES','The real you vs the “should” you',80)}{GROW}
<div style="display:flex;gap:26px">{self_card('Real self','真实自我','#F7F3EC','How you <b>actually</b> see your traits and abilities','#3D3A8C','#F7F3EC')}{self_card('Ideal self','理想自我','#F2785C','Who you think you <b>should</b> be, or would like to be','#FBE3DB')}</div>{GROW}''',3,T))
S.append(slide(f'''{head('THE GAP','Why comparison hurts',88)}
<div style="margin-top:30px;display:flex;gap:40px;align-items:center;justify-content:center">
<div style="display:flex;flex-direction:column;align-items:center;gap:10px">{selves(300,14)}<div style="font-size:34px;font-weight:700;color:#3D3A8C">Close match</div><div style="font-size:30px">→ competent, capable</div></div>
<div style="display:flex;flex-direction:column;align-items:center;gap:10px">{selves(300,56)}<div style="font-size:34px;font-weight:700;color:#C24A2B">Big mismatch</div><div style="font-size:30px">→ anxiety, neurotic behaviour</div></div></div>
<div style="margin-top:14px;text-align:center">{zs("神经质行为",30)}</div>{GROW}
{ex('📏 Every “why can’t you be like…” pushes your ideal self further from your real self.',44)}''',4,T))
S.append(slide(f'''{head('LOVE WITH CONDITIONS','Conditional positive regard',80)}
<div style="margin-top:14px">{zs("有条件积极关注",40)}</div>{GROW}
{card('Love and approval given <b>only when someone’s expectations are met</b>.',k='WHAT IT IS',size=48)}
<div style="margin-top:28px">{ex('🗣️ “I’m proud of you <i>when</i> you get straight As.”',48)}</div>{GROW}''',5,T))
S.append(slide(f'''{head('LOVE WITHOUT CONDITIONS','Unconditional positive regard',78)}
<div style="margin-top:14px">{zs("无条件积极关注",40)}</div>{GROW}
{card('Love, affection and respect with <b>no strings attached</b>.',k='WHAT IT IS',size=48)}
<div style="margin-top:28px">{card('Rogers said you need this to explore your <b>full potential</b>. 🌱',bg='#DCDAF0',size=48)}</div>{GROW}''',6,T))
S.append(slide(f'''{head('THE GOAL','Becoming fully yourself',88)}{GROW}
{card('Striving to reach your <b>full potential</b>.',k='SELF-ACTUALISATION · 自我实现',size=46)}
<div style="margin-top:28px">{card('Trusts their own feelings, and their <b>real self</b> and <b>ideal self</b> match. Needs unconditional positive regard.',k='FULLY FUNCTIONING PERSON · 充分发挥功能的人',size=46)}</div>{GROW}''',7,T))
S.append(slide(f'''{head('REVIEW','Is it good science?',88)}{GROW}
{card('Too idealistic · hard to test · more philosophy than psychology',k='❌ CRITICISMS',size=44)}
<div style="margin-top:28px">{card('Therapies for self-growth and self-understanding · shares ideas with <b>positive psychology</b> (积极心理学)',k='✅ CONTRIBUTIONS',bg='#FBE3DB',size=44)}</div>{GROW}''',8,T))
S.append(last(f'''<div class="lab">CHEAT SHEET 📌</div>
<div style="margin-top:20px">{rows([('Real vs ideal','Close = capable · gap = anxiety'),('Conditional','Love <i>if</i> you meet expectations'),('Unconditional','Love, no strings attached'),('Goal','Self-actualisation')],40,320)}</div>{GROW}
<div style="font-size:40px;font-weight:700">📤 Send this to someone who needs to hear it</div>
<div style="margin-top:26px">{nextup('Finale: introvert, or just shy?')}</div>''',T))
write(S)
