# Motivation · 2/5 · Arousal theory, Yerkes-Dodson, sensation seekers, incentives. Run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from series import *
def curve(w=860,peak=0.5,label=True):
    # inverted U; peak = x position 0..1
    px=60+peak*700
    lab=('<text x="70" y="330" font-size="32" fill="#5A5A66">😴 too low</text>'
         f'<text x="{px-80}" y="44" font-size="32" fill="#C24A2B" font-weight="700">✨ best</text>'
         '<text x="640" y="330" font-size="32" fill="#5A5A66">😱 too high</text>') if label else ''
    return (f'<svg width="{w}" height="{int(w*0.45)}" viewBox="-30 0 850 375" font-family="Manrope">'
            '<path d="M50 300 H790" stroke="#1E1E2A" stroke-width="4"/><path d="M50 300 V20" stroke="#1E1E2A" stroke-width="4"/>'
            f'<path d="M60 290 C{px-200} 290 {px-150} 70 {px} 70 C{px+150} 70 {px+200} 290 780 290" fill="none" stroke="#3D3A8C" stroke-width="10" stroke-linecap="round"/>'
            f'<circle cx="{px}" cy="70" r="16" fill="#F2785C"/>{lab}'
            '<text x="420" y="362" text-anchor="middle" font-size="32" font-weight="700" fill="#1E1E2A">Arousal (唤醒) →</text>'
            '<text x="18" y="160" font-size="32" font-weight="700" fill="#1E1E2A" transform="rotate(-90 18 160)" text-anchor="middle">Performance</text></svg>')
T=9;S=[]
S.append(cover('MOTIVATION · 2 OF 5',
 'Why do you <span style="font-style:italic;color:#C24A2B">blank out</span> when you’re too nervous?',
 'Your performance has a sweet spot.',badge('😵',240),106))
S.append(concept(2,T,'THEORY 3','Arousal theory','唤醒理论','🎚️',
 'Everyone has an <b>optimal level of tension</b>. You raise or lower stimulation to stay there.',
 'Bored in a lecture → you scroll your phone (more stimulation).<br>Overwhelmed → you take a break (less).'))
S.append(slide(f'''{head('THE LAW',f'Yerkes-Dodson law {zs("耶克斯-多德森定律",34)}',80)}
<p style="margin:20px 0 0;font-size:40px;line-height:1.42"><b>Moderate</b> arousal gives better performance than arousal that’s too low or too high.</p>{GROW}
<div style="display:flex;justify-content:center">{curve(880)}</div>{GROW}''',3,T))
S.append(slide(f'''{head('THE TWIST','The best level depends on the task',78)}{GROW}
{duo(('🏃','Easy task','简单任务','Needs <b>high-moderate</b> arousal. Get hyped for a run.'),('🧮','Hard task','困难任务','Needs <b>low-moderate</b> arousal. Stay calm for a hard exam.'),40)}{GROW}
{ex('💡 That’s why you blank out: a hard exam + very high arousal = performance drops.',42)}''',4,T))
S.append(concept(5,T,'SOME PEOPLE NEED MORE','Sensation seekers','感觉寻求者','🎢',
 'People who need <b>more arousal</b> than others to feel at their best.',
 'Roller coasters, extreme sports, horror films: the more intense, the better.',exk='YOU MIGHT KNOW ONE'))
S.append(slide(f'''{head('EXTRA KNOWLEDGE','The climber with a calm amygdala',76)}{GROW}
{bullets(['<b>Alex Honnold</b>: a <b>free solo</b> climber who climbs without a rope or safety gear 🧗','Scientists showed him <b>scary photos</b> inside an <b>fMRI</b> scanner','His <b>amygdala</b> (杏仁核), a fear-related brain area, reacted <b>less</b> than other people’s'],size=44,gap=34)}{GROW}''',6,T))
S.append(slide(f'''{head('THEORY 4',f'Incentive approach {zs("诱因理论",40)}',84)}
<p style="margin:20px 0 0;font-size:40px;line-height:1.42"><b>Incentives</b> are things that <b>pull</b> you into action, whether or not you have a need.</p>{GROW}
{duo(('➡️','Push','推力','Internal <b>needs and drives</b> push you.'),('🧋','Pull','拉力','A <b>rewarding</b> outside thing pulls you: bubble tea when you’re not even thirsty.'),38)}{GROW}
<div style="font-size:34px;line-height:1.4">Many theorists today say motivation = <b>push + pull</b>.</div>''',7,T))
S.append(slide(f'''{head('CHEAT SHEET','Save this 📌',90)}
<div style="margin-top:26px">{rows([('Arousal theory','Keep tension at your optimal level'),('Yerkes-Dodson','Moderate arousal = best performance'),('Easy task','High-moderate arousal'),('Hard task','Low-moderate arousal'),('Sensation seeker','Needs more arousal'),('Incentives','Pull of outside rewards')],38,330)}</div>{GROW}''',8,T))
S.append(last(f'''<div class="lab">YOUR TURN</div>
<h1 style="margin-top:30px;font-size:96px">Are you a <span style="font-style:italic;color:#C24A2B">sensation seeker?</span> 🎢</h1>
<p style="margin:28px 0 0;font-size:44px;line-height:1.4">💬 Comment the most intense thing you’ve done</p>{GROW}
{nextup('“I’m just not a maths person.” True?')}
{save_btn('📌 Save for your PSY111 exam')}''',T))
write(S)
