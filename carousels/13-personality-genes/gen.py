# Personality Part 2 · 1/4 · Behavioural genetics. Run: python3 gen.py && node ../../tools/render.js .
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tools'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from series import *
T=9;S=[]
S.append(cover('PERSONALITY 2 · 1 OF 4',
 'Is your personality in your <span style="font-style:italic;color:#C24A2B">genes?</span>',
 'What twins, skull bumps and brain scans tell us.',badge('🧬',250),112))
S.append(slide(f'''{head('THE FIELD',f'Behavioural genetics {zs("行为遗传学",40)}',80)}
<p style="margin:26px 0 0;font-size:44px;line-height:1.42">The study of the <b>genetic basis</b> {zs("遗传基础",30)} of personality.</p>{GROW}
{grid([('🐕','Animal breeding','动物育种','Dogs of the same breed often share a similar <b>temperament</b> (气质).'),('👯','Twin &amp; adoption studies','双胞胎与领养研究','Genes explain a lot of personality, whatever the home environment. Seen for <b>shyness</b> and <b>aggressiveness</b>.')],34)}{GROW}''',2,T))
S.append(slide(f'''{head('THE FAMOUS CASE','The “Jim” twins 👯',90)}
<p style="margin:24px 0 0;font-size:40px;line-height:1.42"><b>Identical twins</b> {zs("同卵双胞胎",30)} separated at birth, both named James. Studied at age 39.</p>{GROW}
<div class="k">WHAT THEY HAD IN COMMON</div>
{bullets(['Both into <b>mechanical drawing</b> and <b>carpentry</b> 🪚','Drank and smoked about the <b>same amount</b>','Both divorced a woman named <b>Linda</b>… and married a <b>Betty</b> 😳'],size=42,gap=30)}{GROW}''',3,T))
S.append(slide(f'''{head('BUT WAIT','Genes, or the same environment?',80)}{GROW}
{card('Both were raised in <b>Ohio</b>, by parents with <b>similar socioeconomic backgrounds</b> (社会经济背景).',k='🤔 THE CATCH',size=46)}
<div style="margin-top:30px">{ex('So some of the similarities could come from a similar <b>environment</b>, not just genes. That’s why psychologists look at many twins, not one pair.',44)}</div>{GROW}''',4,T))
S.append(slide(f'''{head('THE NUMBER','About 50%',110)}
<div style="margin-top:12px">{zs("遗传力 heritability",40)}</div>{GROW}
{card('How much of a trait <b>within a population</b> can be put down to genes. Not how much of <i>you</i> is genetic.',k='HERITABILITY',size=44)}
<div style="margin-top:28px">{bullets(['The Big Five are about <b>50% heritable</b>, across cultures','Personality differences: about <b>30–50% inherited</b>','The <b>environment</b> explains the other half 🏠'],size=42,gap=26)}</div>{GROW}''',5,T))
S.append(concept(6,T,'A 1796 IDEA','Phrenology','颅相学 · Franz Joseph Gall','💀',
 'Reading personality from the <b>shape of the skull</b>. A bump meant the brain area under it, and that trait, was strong.',
 'Feel a bump on the back of your head? Phrenology would say you’re very loving. Today it’s seen as <b>pseudoscience</b> (伪科学).',exk='HOW IT “WORKED”'))
S.append(slide(f'''{head('MODERN BRAIN SCANS','DeYoung et al. (2010)',84)}
<p style="margin:22px 0 0;font-size:38px;line-height:1.4">MRI scans {zs("磁共振",28)} + a Big Five questionnaire. Do brain areas differ in size?</p>{GROW}
{card('Bigger <b>medial orbitofrontal cortex</b> (内侧眶额皮层), an area that recognises the value of <b>rewards</b>.',k='🎉 EXTRAVERSION',size=38)}
<div style="margin-top:24px">{card('Smaller areas for <b>threat, punishment and negative emotions</b>. Bigger area for <b>error detection and pain</b>.',k='😟 NEUROTICISM',bg='#FBE3DB',size=38)}</div>{GROW}''',7,T))
S.append(slide(f'''{head('CHEAT SHEET','Save this 📌',90)}
<div style="margin-top:26px">{rows([('Behavioural genetics','Genetic basis of personality'),('Jim twins','Raised apart, very alike, but similar homes'),('Heritability','~50% for the Big Five; environment = the rest'),('Phrenology','Skull bumps; pseudoscience'),('DeYoung 2010','Brain area size links to Big Five traits')],38,330)}</div>{GROW}''',8,T))
S.append(last(f'''<div class="lab">YOUR TURN</div>
<h1 style="margin-top:30px;font-size:90px">Which trait did you get from <span style="font-style:italic;color:#C24A2B">your parents?</span></h1>
<p style="margin:28px 0 0;font-size:44px;line-height:1.4">💬 Comment below</p>{GROW}
{nextup('Why does calling your lecturer by his first name feel wrong?')}
{save_btn('📌 Save for your PSY111 exam')}''',T))
write(S)
