# Motivation · 3/5 · McClelland's needs, Dweck's self-theory. Run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from series import *
T=8;S=[]
S.append(cover('MOTIVATION · 3 OF 5',
 '“I’m just not a <span style="font-style:italic;color:#C24A2B">maths person</span>.” True?',
 'What you believe about your brain changes how hard you try.',badge('🧮',240),106))
S.append(slide(f'''{head('McCLELLAND',f'3 psychological needs {zs("心理需求",36)}',80)}{GROW}
<div style="display:flex;flex-direction:column;gap:24px">
{card('A strong desire to <b>succeed</b> at goals, not only realistic ones but <b>challenging</b> ones.',k='🏆 NEED FOR ACHIEVEMENT · nAch · 成就需求',size=40)}
{card('The need for <b>friendly social interaction</b> and relationships.',k='🤝 NEED FOR AFFILIATION · nAff · 亲和需求',size=40)}
{card('The need to have <b>control or influence</b> over others.',k='👑 NEED FOR POWER · nPow · 权力需求',bg='#FBE3DB',size=40)}</div>{GROW}''',2,T))
S.append(concept(3,T,'CAROL DWECK','Self-theory of motivation','自我理论','🪞',
 'Your need for achievement is linked to how you <b>see yourself</b>, and that changes how you read your own success or failure.',
 'Remember <b>locus of control</b> (控制点) from my personality series? Dweck connects to it.',exk='🔁 CONNECTS TO',size=84))
def chain(top,a,b,c,dark):
    bg,fg=('#3D3A8C','#F7F3EC') if dark else ('#FBE3DB','#1E1E2A')
    arr='<div style="font-size:40px;color:#C24A2B;font-weight:800;text-align:center">↓</div>'
    box=lambda t:f'<div style="padding:36px 22px;border-radius:22px;background:{bg};color:{fg};text-align:center;font-size:40px;font-weight:700;line-height:1.3">{t}</div>'
    return f'<div style="flex:1;display:flex;flex-direction:column;gap:6px"><div class="k" style="text-align:center">{top}</div>{box(a)}{arr}{box(b)}{arr}{box(c)}</div>'
S.append(slide(f'''{head('DWECK’S MODEL','Two beliefs, two paths',84)}{GROW}
<div style="display:flex;gap:26px">{chain('BELIEF A','Intelligence is <b>fixed</b><br><span style="font-size:28px">智力是固定的</span>','External locus of control','<b>Low</b> achievement motivation',False)}{chain('BELIEF B','Intelligence is <b>changeable</b><br><span style="font-size:28px">智力可以改变</span>','Internal locus of control','<b>High</b> achievement motivation',True)}</div>{GROW}''',4,T))
S.append(slide(f'''{head('SAME QUIZ, TWO REACTIONS','You fail a maths quiz 📉',80)}{GROW}
{duo(('🧱','“Fixed” thinking','固定观','“I’m just bad at maths.” → you stop trying.'),('🌱','“Changeable” thinking','可变观','“I haven’t learned this method yet.” → you practise more.'),40)}{GROW}
{ex('So, “not a maths person”? It might be the <b>belief</b> holding you back, not your brain.',42)}''',5,T))
S.append(slide(f'''{head('TRY THIS','Change the sentence ✍️',90)}{GROW}
{rows([('Instead of','“I can’t do this.”'),('Try','“I can’t do this <b>yet</b>.”'),('Instead of','“I’m not smart enough.”'),('Try','“What <b>strategy</b> haven’t I tried?”')],42,280)}{GROW}''',6,T))
S.append(slide(f'''{head('CHEAT SHEET','Save this 📌',90)}
<div style="margin-top:26px">{rows([('nAch','Need for achievement'),('nAff','Need for affiliation'),('nPow','Need for power'),('Dweck: fixed','External locus → low motivation'),('Dweck: changeable','Internal locus → high motivation')],38,350)}</div>{GROW}''',7,T))
S.append(last(f'''<div class="lab">YOUR TURN</div>
<h1 style="margin-top:30px;font-size:84px">Which need is strongest for you: <span style="color:#3D3A8C">achievement</span>, <span style="color:#C24A2B">affiliation</span> or power?</h1>
<p style="margin:28px 0 0;font-size:44px;line-height:1.4">💬 Comment below</p>{GROW}
{nextup('Why do you lose motivation when your parents force you?')}''',T))
write(S)
