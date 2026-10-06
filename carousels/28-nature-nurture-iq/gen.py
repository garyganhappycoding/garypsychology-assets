# Intelligence · 4/5 · Nature vs nurture, Flynn effect, stereotype threat, giftedness. Run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from series import *
T=9;S=[]
S.append(cover('INTELLIGENCE · 4 OF 5',
 'Are smart kids <span style="font-style:italic;color:#3D3A8C">born</span> or <span style="font-style:italic;color:#C24A2B">made?</span>',
 'What psychology says about nature vs nurture.',badge('🌱',250),112))
S.append(slide(f'''{head('NATURE',f'Twin &amp; adoption studies {zs("双胞胎与领养研究",34)}',76)}{GROW}
{card('The more <b>genetically related</b> two people are, the <b>more similar</b> their IQ scores.',size=44)}
<div style="margin-top:30px;display:flex;align-items:center;gap:30px;padding:34px;border-radius:30px;background:#3D3A8C;color:#F7F3EC"><div style="font-family:Fraunces,serif;font-weight:800;font-size:120px">~50%</div><div style="font-size:38px;line-height:1.38">Estimated <b>heritability</b> of IQ</div></div>{GROW}
{ex('🔁 Same as personality: heritability is about a <b>population</b>, not one person.',38)}''',2,T))
S.append(concept(3,T,'NURTURE','The Flynn effect','弗林效应','📈',
 'IQ scores have been <b>steadily rising over time</b> in modernised countries.',
 'Genes don’t change that fast across a few generations, so the <b>environment</b> must be playing a big part.',exk='WHY IT MATTERS'))
S.append(concept(4,T,'NURTURE','Stereotype threat','刻板印象威胁','😟',
 'Being <b>aware of a negative stereotype</b> about your group can make you <b>score worse</b> on intelligence tests.',
 'Being reminded that “your group is bad at maths” right before a maths test can drag your score down.'))
S.append(slide(f'''{head('A CONTROVERSY',f'The Bell Curve {zs("《钟形曲线》",36)}',88)}{GROW}
{card('A <b>controversial</b> 1994 book by <b>Herrnstein &amp; Murray</b> that made claims about how much intelligence is <b>inherited</b>.',size=44)}
<div style="margin-top:28px">{ex('Stereotype threat and the Flynn effect are two reasons psychologists are careful with claims like these.',40)}</div>{GROW}''',5,T))
S.append(concept(6,T,'THE TOP 2%',f'Giftedness','天赋','⭐',
 'About <b>2%</b> of people have an <b>IQ of 130 or above</b>, at the top end of the normal curve.',
 '<b>Lewis Terman</b> followed gifted children for years: most grew up to be <b>successful adults</b>.<br>⚠️ Criticism: he got <b>too involved</b> in the lives of the children he studied to stay objective.',exk='TERMAN’S LONG STUDY'))
S.append(slide(f'''{head('THE ANSWER','Born or made?',100)}{GROW}
{duo(('🧬','Nature','先天','Twin studies: about <b>50%</b> heritable.'),('🏫','Nurture','后天','The <b>Flynn effect</b> and <b>stereotype threat</b> show the environment matters.'),40)}{GROW}
<div style="font-family:Fraunces,serif;font-weight:700;font-size:64px;text-align:center">Both. 🤝</div>{GROW}''',7,T))
S.append(slide(f'''{head('CHEAT SHEET','Save this 📌',90)}
<div style="margin-top:24px">{rows([('Twin studies','Closer genes → closer IQ'),('Heritability','About 50%'),('Flynn effect','IQ rising over time'),('Stereotype threat','Negative stereotypes lower scores'),('Giftedness','~2% with IQ 130+ · Terman')],38,330)}</div>{GROW}''',8,T))
S.append(last(f'''<div class="lab">YOUR TURN</div>
<h1 style="margin-top:30px;font-size:88px">What shaped your brain more: <span style="color:#3D3A8C">genes</span> or <span style="color:#C24A2B">environment?</span></h1>
<p style="margin:28px 0 0;font-size:44px;line-height:1.4">💬 Comment below</p>{GROW}
{nextup('Finale: does EQ matter more than IQ?')}''',T))
write(S)
