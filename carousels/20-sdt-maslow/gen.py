# Motivation · 4/5 · Self-determination theory, Maslow. Run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from series import *
def pyramid(w=860):
    L=[('Self-actualisation','自我实现','#F2785C','#1E1E2A'),('Esteem','尊重','#3D3A8C','#F7F3EC'),('Love &amp; belonging','归属与爱','#5A57A8','#F7F3EC'),('Safety','安全','#8A87C4','#1E1E2A'),('Physiological','生理','#C9C6EA','#1E1E2A')]
    out='';H=108
    for i,(t,zh,c,f) in enumerate(L):
        y=10+i*H; wt=260+i*110; wb=260+(i+1)*110
        out+=(f'<path d="M{360-wt/2} {y} H{360+wt/2} L{360+wb/2} {y+H-8} H{360-wb/2} Z" fill="{c}"/>'
              f'<text x="360" y="{y+48}" text-anchor="middle" font-size="31" font-weight="800" fill="{f}" font-family="Manrope">{t}</text>'
              f'<text x="360" y="{y+84}" text-anchor="middle" font-size="24" fill="{f}" font-family="Noto Sans CJK SC">{zh}</text>')
    return f'<svg width="{w}" height="{int(w*560/860)}" viewBox="-60 0 840 550">{out}</svg>'
T=9;S=[]
S.append(cover('MOTIVATION · 4 OF 5',
 'Why do you lose motivation when your parents <span style="font-style:italic;color:#C24A2B">force</span> you?',
 'Psychologists say you need 3 things to stay motivated.',badge('😮‍💨',240),98))
S.append(concept(2,T,'RYAN &amp; DECI (2000)','Self-determination theory','自我决定理论 · SDT','🧭',
 'The <b>social context</b> around an action changes the <b>type of motivation</b> you have for it.',
 'Same subject, different feeling: studying because you chose it vs because you were told to.',size=82))
S.append(slide(f'''{head('SDT','3 needs to feel motivated',84)}{GROW}
<div style="display:flex;flex-direction:column;gap:24px">
{card('Being in <b>control</b> of your own behaviour and goals.',k='🕹️ AUTONOMY · 自主性',size=42)}
{card('Being able to <b>master</b> the challenging tasks in your life.',k='💪 COMPETENCE · 胜任感',size=42)}
{card('Feeling <b>belonging</b>, closeness and security with others.',k='🤝 RELATEDNESS · 归属感',bg='#FBE3DB',size=42)}</div>{GROW}''',3,T))
S.append(slide(f'''{head('← THE HOOK','Forced vs supported',90)}{GROW}
{duo(('🚫','“Do medicine. We decided.”','被强迫','<b>Autonomy</b> is taken away → motivation turns extrinsic and fragile.'),('🌱','“What do you want to do? We’ll help.”','被支持','All 3 needs can be met → more <b>intrinsic</b> motivation.'),36)}{GROW}''',4,T))
S.append(slide(f'''{head('THE RESULT','A supportive environment',84)}{GROW}
<div style="font-size:42px;line-height:1.45">When autonomy, competence and relatedness are met, you get:</div>
<div style="margin-top:30px">{bullets(['🌿 <b>Healthy psychological growth</b>','🔥 <b>More intrinsic motivation</b> (内在动机)'],size=48,gap=34)}</div>{GROW}
{ex('🔁 Intrinsic motivation was the first post in this series.',40)}''',5,T))
S.append(slide(f'''{head('MASLOW',f'Hierarchy of needs {zs("需求层次",40)}',84)}
<div style="margin-top:6px;display:flex;justify-content:center">{pyramid(880)}</div>{GROW}
<div style="font-size:36px;line-height:1.42">Lower levels are <b>deficiency needs</b> {zs("缺失需求",26)}; the top is a <b>growth need</b> {zs("成长需求",26)}. You work up towards <b>self-actualisation</b>.</div>''',6,T))
S.append(concept(7,T,'MASLOW','Peak experiences','高峰体验','⛰️',
 'Moments when you <b>temporarily reach self-actualisation</b>.',
 'Totally absorbed on stage, in a game or in your art, and everything just clicks.'))
S.append(slide(f'''{head('CHEAT SHEET','Save this 📌',90)}
<div style="margin-top:26px">{rows([('SDT','Social context shapes motivation'),('Autonomy','Control over your choices'),('Competence','Mastering challenges'),('Relatedness','Belonging and closeness'),('Maslow','Deficiency → growth needs → self-actualisation'),('Peak experience','Brief self-actualisation')],38,320)}</div>{GROW}''',8,T))
S.append(last(f'''<div class="lab">YOUR TURN</div>
<h1 style="margin-top:30px;font-size:90px">Which need is <span style="font-style:italic;color:#C24A2B">missing</span> for you right now?</h1>
<p style="margin:28px 0 0;font-size:44px;line-height:1.4">💬 Autonomy, competence or relatedness?</p>{GROW}
{nextup('Why is there always room for dessert?')}
{save_btn('📌 Save for your PSY111 exam')}''',T))
write(S)
