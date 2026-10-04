K='#1E1E2A';SK='#EAC9A6'
def wrap(inner,w,h,vb='0 0 240 240'): return f'<svg width="{w}" height="{h}" viewBox="{vb}" fill="none" stroke="{K}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">{inner}</svg>'
def person(cx=120,shirt='#3D3A8C',face=True,s=1):
    return f'''<path d="M{cx-70} 232 C{cx-70} 160 {cx-40} 138 {cx} 138 C{cx+40} 138 {cx+70} 160 {cx+70} 232 Z" fill="{shirt}"/>
<circle cx="{cx}" cy="82" r="40" fill="{SK}"/><path d="M{cx-40} 78 C{cx-40} 36 {cx+40} 36 {cx+40} 78 C{cx+30} 60 {cx-30} 60 {cx-40} 78Z" fill="{K}"/>
<circle cx="{cx-14}" cy="86" r="3.5" fill="{K}" stroke="none"/><circle cx="{cx+14}" cy="86" r="3.5" fill="{K}" stroke="none"/><path d="M{cx-12} 102 Q{cx} 112 {cx+12} 102"/>'''
def psychiatrist(w=240):
    return wrap(person(100,'#FFFDF8')+'<path d="M70 150 C70 196 130 196 130 150" stroke="#3D3A8C"/><circle cx="100" cy="196" r="9" fill="#3D3A8C" stroke="#3D3A8C"/>'
      '<rect x="168" y="150" width="54" height="76" rx="10" fill="#F2785C"/><rect x="162" y="134" width="66" height="22" rx="6" fill="#3D3A8C"/><path d="M195 176v28M181 190h28" stroke="#FFFDF8" stroke-width="6"/>',w,w)
def psychologist(w=240):
    return wrap(person(110,'#3D3A8C')+'<g transform="rotate(-8 170 180)"><rect x="140" y="130" width="76" height="100" rx="10" fill="#FFFDF8"/><rect x="160" y="122" width="36" height="16" rx="5" fill="#F2785C"/><path d="M154 158h48M154 178h48M154 198h32"/></g>',w,w)
def counsellor(w=240):
    return wrap('<path d="M22 40h120a16 16 0 0 1 16 16v54a16 16 0 0 1-16 16H70l-26 24v-24H22a16 16 0 0 1-16-16V56a16 16 0 0 1 16-16z" fill="#3D3A8C"/>'
      '<path d="M218 108H108a16 16 0 0 0-16 16v48a16 16 0 0 0 16 16h78l26 24v-24h6a16 16 0 0 0 16-16v-48a16 16 0 0 0-16-16z" fill="#F2785C"/>'
      '<path d="M163 166c-14-10-26-18-26-30a12 12 0 0 1 26-6 12 12 0 0 1 26 6c0 12-12 20-26 30z" fill="#FFFDF8" stroke="#FFFDF8" stroke-width="3"/>'
      '<circle cx="50" cy="83" r="6" fill="#FFFDF8" stroke="none"/><circle cx="82" cy="83" r="6" fill="#FFFDF8" stroke="none"/><circle cx="114" cy="83" r="6" fill="#FFFDF8" stroke="none"/>',w,w)
def socialworker(w=240):
    return wrap('<path d="M140 110 L190 70 L240 110" stroke-width="5" fill="none"/><rect x="152" y="108" width="76" height="72" fill="#FBE3DB"/><rect x="180" y="140" width="20" height="40" fill="#3D3A8C"/>'
      '<circle cx="62" cy="96" r="26" fill="#EAC9A6"/><path d="M36 92 C36 62 88 62 88 92 C80 80 44 80 36 92Z" fill="#1E1E2A"/><path d="M20 232 C20 170 34 138 62 138 C90 138 104 170 104 232Z" fill="#F2785C"/>'
      '<circle cx="132" cy="160" r="18" fill="#EAC9A6"/><path d="M104 232 C104 196 114 182 132 182 C150 182 160 196 160 232Z" fill="#3D3A8C"/><path d="M96 190 L112 196"/>',w,w)
def quiz(w=240):
    return wrap('<g transform="rotate(-35 120 120)"><path d="M70 90h50v80H70a40 40 0 0 1 0-80z" fill="#F2785C"/><path d="M120 90h50a40 40 0 0 1 0 80h-50z" fill="#3D3A8C"/></g>'
      '<text x="190" y="80" font-family="Fraunces" font-weight="700" font-size="90" fill="#1E1E2A" stroke="none">?</text>',w,w)
def badge(w=240):
    return wrap('<rect x="20" y="70" width="150" height="96" rx="14" fill="#FFFDF8"/><rect x="20" y="70" width="150" height="26" rx="10" fill="#3D3A8C"/><circle cx="56" cy="130" r="16" fill="#EAC9A6"/><path d="M84 124h66M84 144h48"/>'
      '<circle cx="168" cy="160" r="40" fill="#FBE3DB" fill-opacity=".7"/><path d="M198 190 L230 222" stroke-width="12"/>',w,w)
def baby_cry(w=240):
    return wrap('<circle cx="120" cy="120" r="84" fill="#EAC9A6"/><path d="M104 40 C110 20 130 20 124 40" /><path d="M78 108 Q92 98 106 108M134 108 Q148 98 162 108"/>'
      '<ellipse cx="120" cy="158" rx="22" ry="18" fill="#C24A2B"/><path d="M86 118 C82 140 78 150 84 160" stroke="#7FA7D9" stroke-width="7"/><path d="M154 118 C158 140 162 150 156 160" stroke="#7FA7D9" stroke-width="7"/>',w,w)
def rat(w=240):
    return wrap('<path d="M40 190 C10 200 10 230 50 226" stroke="#8A7F74"/><ellipse cx="110" cy="176" rx="72" ry="44" fill="#FFFDF8"/><circle cx="176" cy="150" r="32" fill="#FFFDF8"/>'
      '<circle cx="168" cy="118" r="16" fill="#FBE3DB"/><circle cx="186" cy="146" r="4" fill="#1E1E2A" stroke="none"/><circle cx="206" cy="160" r="5" fill="#F2785C"/><path d="M204 166l24 6M204 166l22 14"/>',w,w)
def bang(w=260):
    pts=[]
    import math
    for i in range(24):
        r=118 if i%2==0 else 78; a=math.pi*2*i/24
        pts.append(f'{130+r*math.cos(a):.0f},{130+r*math.sin(a):.0f}')
    return wrap(f'<polygon points="{" ".join(pts)}" fill="#F2785C"/><text x="130" y="146" text-anchor="middle" font-family="Fraunces" font-weight="800" font-size="38" fill="#1E1E2A" stroke="none">BANG!</text>',w,w,'0 0 260 260')
def exam(w=240):
    return wrap('<g transform="rotate(-6 120 120)"><rect x="46" y="24" width="140" height="190" rx="12" fill="#FFFDF8"/><path d="M70 64h70M70 90h92M70 116h80M70 142h60"/>'
      '<circle cx="152" cy="170" r="34" fill="none" stroke="#C24A2B" stroke-width="6"/><text x="152" y="182" text-anchor="middle" font-family="Fraunces" font-weight="800" font-size="21" fill="#C24A2B" stroke="none">5/10</text></g>'
      '<path d="M206 44 C198 60 194 70 206 78 C218 70 214 60 206 44Z" fill="#7FA7D9" stroke="#7FA7D9" stroke-width="3"/>',w,w)

# ---- Personality series (07–12) ----
def face(cx,cy,r=40,skin=SK,hair=True,mood='smile'):
    m={'smile':f'<path d="M{cx-12} {cy+20} Q{cx} {cy+30} {cx+12} {cy+20}"/>','sad':f'<path d="M{cx-12} {cy+26} Q{cx} {cy+16} {cx+12} {cy+26}"/>','flat':f'<path d="M{cx-11} {cy+22}h22"/>','o':f'<circle cx="{cx}" cy="{cy+22}" r="6"/>'}[mood]
    h=f'<path d="M{cx-r} {cy-4} C{cx-r} {cy-46} {cx+r} {cy-46} {cx+r} {cy-4} C{cx+r*.75} {cy-22} {cx-r*.75} {cy-22} {cx-r} {cy-4}Z" fill="{K}"/>' if hair else ''
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{skin}"/>{h}<circle cx="{cx-14}" cy="{cy+4}" r="3.5" fill="{K}" stroke="none"/><circle cx="{cx+14}" cy="{cy+4}" r="3.5" fill="{K}" stroke="none"/>{m}'
def phone_kid(w=240):
    return wrap(person(110,'#3D3A8C')+'<rect x="150" y="150" width="46" height="78" rx="9" fill="#1E1E2A"/><rect x="157" y="160" width="32" height="54" rx="4" fill="#F2785C" stroke="none"/><path d="M168 186l10 6-10 6z" fill="#FFFDF8" stroke="none"/>',w,w)
def id_toon(w=200):
    return wrap('<circle cx="120" cy="120" r="100" fill="#FBE3DB" stroke="none"/>'+face(120,118,52,hair=False,mood='o')+'<path d="M112 64 C116 48 132 50 126 64"/><circle cx="120" cy="170" r="16" fill="#F2785C"/><path d="M104 170h32" stroke-width="4"/>',w,w)
def ego_toon(w=200):
    return wrap('<circle cx="120" cy="120" r="100" fill="#E4DDD0" stroke="none"/><path d="M60 232 C60 176 84 160 120 160 C156 160 180 176 180 232Z" fill="#FFFDF8"/><path d="M92 166v66M120 160v72M148 166v66" stroke-width="7"/>'+face(120,104,44,mood='flat')+'<path d="M164 128 l30 -8" stroke-width="5"/><rect x="190" y="110" width="22" height="16" rx="6" fill="#3D3A8C"/>',w,w)
def superego_toon(w=200):
    return wrap('<circle cx="120" cy="120" r="100" fill="#DCDAF0" stroke="none"/><path d="M60 232 C60 176 84 160 120 160 C156 160 180 176 180 232Z" fill="#3D3A8C"/>'+face(110,104,44,mood='flat')+'<path d="M176 168 V112" stroke-width="7"/><circle cx="176" cy="104" r="9" fill="#EAC9A6"/><path d="M78 52 h64 l-8 -14 h-48z" fill="#1E1E2A"/>',w,w)
def shield(w=240):
    return wrap('<path d="M120 20 L200 50 V118 C200 170 166 204 120 222 C74 204 40 170 40 118 V50 Z" fill="#3D3A8C"/><path d="M120 50 L172 70 V118 C172 152 152 176 120 190 Z" fill="#F2785C" stroke="none"/>'+face(96,116,24,hair=False,mood='smile'),w,w)
def blame_kid(w=240):
    return wrap(person(90,'#3D3A8C')+'<path d="M140 164 L206 128" stroke-width="10"/><g transform="rotate(8 200 190)"><rect x="160" y="150" width="70" height="86" rx="8" fill="#FFFDF8"/><text x="195" y="214" text-anchor="middle" font-family="Fraunces" font-weight="800" font-size="52" fill="#C24A2B" stroke="none">F</text></g>',w,w)
def nails(w=240):
    return wrap('<path d="M70 230 V120 C70 104 94 104 94 120 V70 C94 54 118 54 118 70 V60 C118 44 142 44 142 60 V74 C142 58 166 58 166 74 V150 C166 196 140 230 110 230Z" fill="#EAC9A6"/><path d="M98 76 l16 0 M122 66 l16 0 M146 80 l16 0" stroke="#C24A2B" stroke-width="6"/><path d="M174 120 l30 -16 l-6 16 l20 0" stroke="#3D3A8C"/>',w,w)
def bottle(w=240):
    return wrap('<path d="M106 30 C106 18 134 18 134 30 L138 56 H102 Z" fill="#F2785C"/><rect x="92" y="56" width="56" height="18" rx="6" fill="#3D3A8C"/><rect x="88" y="74" width="64" height="146" rx="22" fill="#FFFDF8"/><rect x="92" y="130" width="56" height="86" rx="18" fill="#DCE8F5" stroke="none"/><path d="M152 110h-16M152 140h-16M152 170h-16" stroke-width="4"/>',w,w)
def potty(w=240):
    return wrap('<path d="M50 120 H190 C190 176 162 206 120 206 C78 206 50 176 50 120Z" fill="#3D3A8C"/><ellipse cx="120" cy="120" rx="74" ry="20" fill="#FFFDF8"/><ellipse cx="120" cy="120" rx="48" ry="11" fill="#E4DDD0"/><path d="M190 132 C222 128 222 98 196 104" stroke-width="8"/><path d="M84 206 l-10 22 h92 l-10 -22" fill="#F2785C"/>',w,w)
def family(w=240):
    return wrap(f'<path d="M14 232 C14 186 30 168 56 168 C82 168 98 186 98 232Z" fill="#3D3A8C"/>{face(56,128,30,mood="flat")}<path d="M142 232 C142 186 158 168 184 168 C210 168 226 186 226 232Z" fill="#F2785C"/>{face(184,128,30,mood="flat")}<path d="M96 232 C96 204 106 194 120 194 C134 194 144 204 144 232Z" fill="#FFFDF8"/>{face(120,166,22,mood="smile")}<path d="M120 60 C108 46 92 54 100 68 L120 88 L140 68 C148 54 132 46 120 60Z" fill="#C24A2B" stroke="#C24A2B" stroke-width="3"/>',w,w)
def books(w=240):
    return wrap('<rect x="40" y="168" width="160" height="34" rx="6" fill="#3D3A8C"/><rect x="54" y="134" width="140" height="34" rx="6" fill="#F2785C"/><rect x="46" y="100" width="150" height="34" rx="6" fill="#FFFDF8"/><path d="M70 117h80" stroke-width="4"/><path d="M150 96 L176 30 L196 38 L172 104 Z" fill="#EAC9A6"/><path d="M150 96 l8 14 l14 -6"/>',w,w)
def couple(w=240):
    return wrap(f'<path d="M20 232 C20 182 40 164 72 164 C104 164 124 182 124 232Z" fill="#3D3A8C"/>{face(72,118,34)}<path d="M116 232 C116 182 136 164 168 164 C200 164 220 182 220 232Z" fill="#F2785C"/>{face(168,118,34)}<path d="M120 52 C108 38 92 46 100 60 L120 80 L140 60 C148 46 132 38 120 52Z" fill="#C24A2B" stroke="#C24A2B" stroke-width="3"/>',w,w)
def clover(w=240):
    leaf=lambda a:f'<g transform="rotate({a} 120 110)"><path d="M120 110 C92 96 92 52 120 64 C148 52 148 96 120 110Z" fill="#5E9E6E"/></g>'
    return wrap(''.join(leaf(a) for a in (0,90,180,270))+'<path d="M120 112 C126 160 140 190 168 222" stroke="#5E9E6E" stroke-width="8"/>',w,w)
def triangle(w=300):
    return wrap('<path d="M150 40 L260 230 H40 Z" fill="none" stroke="#3D3A8C" stroke-width="5" stroke-dasharray="12 10"/><circle cx="150" cy="40" r="26" fill="#F2785C"/><circle cx="40" cy="230" r="26" fill="#3D3A8C"/><circle cx="260" cy="230" r="26" fill="#1E1E2A"/>',w,w,'-10 0 320 270')
def compare(w=240):
    return wrap(person(80,'#3D3A8C')+'<path d="M140 36h86a12 12 0 0 1 12 12v40a12 12 0 0 1-12 12h-50l-20 18v-18h-16a12 12 0 0 1-12-12V48a12 12 0 0 1 12-12z" fill="#F2785C"/><text x="183" y="80" text-anchor="middle" font-family="Fraunces" font-weight="800" font-size="40" fill="#1E1E2A" stroke="none">A+</text><path d="M150 130h80M150 152h60" stroke="#8A7F74"/>',w,w)
def selves(w=300,gap=60):
    return wrap(f'<circle cx="{150-gap}" cy="130" r="86" fill="#3D3A8C" fill-opacity=".85"/><circle cx="{150+gap}" cy="130" r="86" fill="#F2785C" fill-opacity=".8"/>',w,int(w*0.87),'0 0 300 260')
def headphones(w=240):
    return wrap('<circle cx="40" cy="120" r="20" fill="#E4DDD0" stroke="#B8AFA2"/><circle cx="200" cy="96" r="20" fill="#E4DDD0" stroke="#B8AFA2"/><circle cx="196" cy="160" r="20" fill="#E4DDD0" stroke="#B8AFA2"/>'+person(110,'#3D3A8C')+'<path d="M66 84 C66 26 154 26 154 84" stroke="#F2785C" stroke-width="9"/><rect x="58" y="76" width="18" height="30" rx="7" fill="#F2785C"/><rect x="144" y="76" width="18" height="30" rx="7" fill="#F2785C"/>',w,w)
def iceberg(w=420):
    return wrap('<rect x="0" y="120" width="420" height="300" fill="#DCE8F5" stroke="none"/><path d="M0 120 H420" stroke="#7FA7D9" stroke-width="5"/><path d="M160 120 L196 52 L224 80 L250 40 L284 120Z" fill="#FFFDF8"/><path d="M110 120 H330 L372 236 L300 360 H150 L70 250Z" fill="#3D3A8C" fill-opacity=".85"/>',w,int(w*0.95),'0 0 420 400')
