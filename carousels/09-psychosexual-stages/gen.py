# Personality series 3/6 · Psychosexual stages + criticisms. Run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from series import *
from toons import nails,bottle,potty,family,books,couple
T=11;S=[]
S.append(cover('PERSONALITY · PART 3 OF 6',
 'Do you bite your <span style="font-style:italic;color:#C24A2B">nails?</span>',
 'Freud had a strange theory about that, plus 3 reasons it’s criticised.',nails(300),120))
steps=''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px;width:168px"><div style="width:150px;height:150px;border-radius:50%;background:#FFFDF8;border:2px solid #E4DDD0;display:flex;align-items:center;justify-content:center">{t(110)}</div><div style="font-size:26px;font-weight:700">{n}</div></div>' for t,n in [(bottle,'Oral'),(potty,'Anal'),(family,'Phallic'),(books,'Latency'),(couple,'Genital')])
S.append(slide(f'''{head('FREUD’S BIG IDEA',f'5 childhood stages {zs("性心理发展阶段",36)}',80)}
<div style="margin-top:40px;display:flex;justify-content:space-between">{steps}</div>{GROW}
{bullets(['Personality forms in childhood through 5 <b>psychosexual stages</b>.','Each stage has a body focus. Unresolved conflict → <b>fixation</b> (固着).','You get “stuck” and carry it into adulthood.'],size=42,gap=28)}{GROW}''',2,T))
def stage(n,num,name,zh,age,art,focus,conflict,fix,extra=''):
    r=lambda k,v:f'<div style="display:flex;gap:22px;align-items:baseline;padding:18px 0;border-bottom:2px solid #E4DDD0"><div class="k" style="width:190px;flex-shrink:0;margin:0">{k}</div><div style="font-size:40px;line-height:1.38">{z(v)}</div></div>'
    return slide(f'''<div style="display:flex;justify-content:space-between;align-items:flex-start;gap:20px"><div><div class="lab">STAGE {num} OF 5</div>
<h1 style="margin-top:20px;font-size:96px">{name}</h1><div style="margin-top:10px">{zs(zh,48)}</div>
<div style="margin-top:22px"><span class="chip" style="font-size:32px">{age}</span></div></div>
<div style="width:280px;height:280px;border-radius:50%;background:#FBE3DB;display:flex;align-items:center;justify-content:center;flex-shrink:0">{art(210)}</div></div>
<div style="margin-top:34px">{r('FOCUS',focus)}{r('CONFLICT',conflict)}{r('IF STUCK',fix)}</div>{GROW}{extra}''',n,T)
S.append(stage(3,1,'Oral','口腔期','First 18 months',bottle,'The mouth (嘴巴)','<b>Weaning</b> (断奶)','Overeating, chain smoking, <b>nail biting</b> 💅',
  ex('🍼 Baby = everything goes into the mouth. Freud said if this stage goes wrong, the mouth habits stay.',38)))
S.append(stage(4,2,'Anal','肛门期','18–36 months',potty,'The anus (肛门)','<b>Toilet training</b> (如厕训练)',
  '<b>Anal retentive</b> (肛门滞留型人格) or <b>anal expulsive</b> (肛门排放型人格) personality',
  card('<b>Retentive</b> = overly neat, stingy, controlling 🧹<br><b>Expulsive</b> = messy, careless, disorganised 🌪️',k='WHAT THEY MEAN',bg='#FBE3DB',size=36)))
S.append(stage(5,3,'Phallic','性器期','3–6 years',family,'The genitals (生殖器)','Awakening of sexual feelings → the <b>Oedipus</b> / <b>Electra complex</b>','Promiscuous sexual behaviour (性滥交)',
  ex('👀 The two complexes are the famous part of this stage. Explained on the next slide 👉',40)))
S.append(slide(f'''{head('STAGE 3 · THE COMPLEXES','Oedipus vs Electra',90,family(220))}
<div style="margin-top:36px">{card('<b>Oedipus complex</b> (俄狄浦斯情结 · 恋母情结)<br>A <b>boy</b> unconsciously wants his <b>mother</b> and sees his <b>father</b> as a rival.',k='👦 BOYS',size=40)}</div>
<div style="margin-top:26px">{card('<b>Electra complex</b> (厄勒克特拉情结 · 恋父情结)<br>A <b>girl</b> unconsciously wants her <b>father</b> and sees her <b>mother</b> as a rival.',k='👧 GIRLS',size=40)}</div>{GROW}
{ex('💡 Freud said it’s resolved when the child starts to <b>identify with</b> the same-sex parent.',38)}''',6,T))
def mini(art,name,zh,age,text):
    return f'''<div style="display:flex;gap:34px;align-items:center;padding:30px 34px;border-radius:28px;background:#FFFDF8;border:2px solid #E4DDD0">
<div style="width:200px;height:200px;border-radius:50%;background:#FBE3DB;display:flex;align-items:center;justify-content:center;flex-shrink:0">{art(150)}</div>
<div><div style="font-family:Fraunces,serif;font-weight:700;font-size:58px">{name} {zs(zh,34)}</div><div style="margin-top:6px"><span class="chip" style="font-size:28px">{age}</span></div>
<div style="margin-top:16px;font-size:36px;line-height:1.4">{text}</div></div></div>'''
S.append(slide(f'''{head('STAGES 4 + 5','The last two stages',84)}{GROW}
{mini(books,'Latency','潜伏期','6 years → puberty','Sexual feelings are <b>repressed</b> while you grow intellectually, physically and socially. The opposite sex seems “awful” 🙅')}
<div style="margin-top:30px">{mini(couple,'Genital','生殖期','Puberty onward','Sexual feelings can’t be ignored any more → attraction to others and <b>adult relationships</b> begin 💞')}</div>{GROW}''',7,T))
def crit(n,num,title,zh,emoji,body,extra=''):
    return slide(f'''<div class="lab">CRITICISM {num} OF 3</div>
<div style="display:flex;justify-content:space-between;align-items:center;margin-top:24px"><h1 style="font-size:100px">{title}</h1><div style="font-size:140px">{emoji}</div></div>
<div style="margin-top:10px">{zs(zh,52)}</div>{GROW}{card(body,size=48)}{GROW}{extra}''',n,T)
S.append(crit(8,1,'Not scientific','不科学','🧪','Freud ran <b>no experiments</b>. Everything came from observing <b>his own patients</b>.'))
S.append(crit(9,2,'Too ambiguous','太模糊','🌫️','Based on interpreting <b>dreams</b> and <b>free association</b> (自由联想). You can’t prove it wrong, so you can’t really test it.',
  ex('🔁 Remember my 4 goals post? A good explanation has to be <b>testable</b>.',40)))
S.append(crit(10,3,'Limited sample','样本有限','👒','His patients were mostly <b>wealthy Austrian women</b> in the Victorian era, when sexual repression was common. Hard to apply to everyone else.'))
tl=''.join(f'<div style="display:flex;align-items:center;gap:22px;padding:12px 0;border-bottom:2px solid #E4DDD0"><div style="width:96px;height:96px;border-radius:50%;background:#FBE3DB;display:flex;align-items:center;justify-content:center;flex-shrink:0">{t(72)}</div><div style="width:200px;font-family:Fraunces,serif;font-weight:700;font-size:40px;color:#3D3A8C">{n}</div><div style="font-size:32px;line-height:1.3">{z(v)}</div></div>' for t,n,v in [(bottle,'Oral','0–18 mo · weaning'),(potty,'Anal','18–36 mo · toilet training'),(family,'Phallic','3–6 yrs · Oedipus / Electra'),(books,'Latency','6 yrs–puberty · repressed'),(couple,'Genital','Puberty+ · adult relationships')])
S.append(last(f'''<div class="lab">CHEAT SHEET 📌</div>
<div style="margin-top:18px">{tl}</div>
<div style="margin-top:22px;font-size:34px;line-height:1.45"><b>Fixation</b> {zs("固着",26)} = stuck at a stage · <b>3 criticisms:</b> not scientific · too ambiguous · limited sample</div>{GROW}
{nextup('Freud says your past controls you. Others say <i>you</i> do. Next: bad luck, or&#160;you?')}''',T))
write(S)
