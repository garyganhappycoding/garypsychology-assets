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
