# Shared template for @garypsychology07 carousels: brand CSS, icons, helpers.
import os, re
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'node_modules')
HEAD=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><style>
@font-face{{font-family:'Fraunces';font-style:normal;font-weight:100 900;src:url(file://{R}/@fontsource-variable/fraunces/files/fraunces-latin-full-normal.woff2)}}
@font-face{{font-family:'Fraunces';font-style:italic;font-weight:100 900;src:url(file://{R}/@fontsource-variable/fraunces/files/fraunces-latin-full-italic.woff2)}}
""" + "".join(f"@font-face{{font-family:'Manrope';font-weight:{w};src:url(file://{R}/@fontsource/manrope/files/manrope-latin-{w}-normal.woff2)}}\n" for w in (400,600,700,800)) + """
body{margin:0}
.s{width:1080px;height:1350px;box-sizing:border-box;padding:100px 96px 90px;display:flex;flex-direction:column;background:#F7F3EC;background-image:radial-gradient(rgba(30,30,42,.10) 1.5px,transparent 1.5px);background-size:36px 36px;font-family:'Manrope','Noto Sans CJK SC',sans-serif;color:#1E1E2A}
.lab{font-size:26px;font-weight:700;letter-spacing:.18em;color:#C24A2B}
.zh{white-space:nowrap;font-family:'Noto Sans CJK SC','Noto Sans SC',sans-serif;font-weight:500;font-size:.7em;color:#8A7F74;letter-spacing:0}
h1{margin:0;font-family:'Fraunces',serif;font-weight:700;letter-spacing:-.02em;line-height:.98}
.ic{border-radius:50%;background:#3D3A8C;color:#F7F3EC;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.chip{display:inline-block;padding:12px 26px;border-radius:999px;background:#3D3A8C;color:#F7F3EC;font-size:26px;font-weight:600}
.k{font-size:24px;font-weight:700;letter-spacing:.16em;color:#C24A2B;margin-bottom:12px}
.foot{margin-top:40px;display:flex;justify-content:space-between;align-items:center;font-size:28px;font-weight:600;color:#5A5A66}
.bar{width:180px;height:8px;border-radius:4px;background:#E4DDD0;overflow:hidden}.bar div{height:8px;background:#3D3A8C}
</style></head><body>"""
ICON={
'key':'<circle cx="7.5" cy="15.5" r="5.5"/><path d="m21 2-9.6 9.6"/><path d="m15.5 7.5 3 3L22 7l-3-3"/>',
'repeat':'<path d="m17 2 4 4-4 4"/><path d="M3 11v-1a4 4 0 0 1 4-4h14"/><path d="m7 22-4-4 4-4"/><path d="M21 13v1a4 4 0 0 1-4 4H3"/>',
'sprout':'<path d="M7 20h10"/><path d="M10 20c5.5-2.5.8-6.4 3-10"/><path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5.4-4.8-.3-1.2-.6-2.3-1.9-3-4.2 2.8-.5 4.4 0 5.5.8z"/><path d="M14.1 6a7 7 0 0 0-1.1 4c1.9-.1 3.3-.6 4.3-1.4 1-1 1.6-2.3 1.7-4.6-2.7.1-4 1-4.9 2z"/>',
'bulb':'<path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/>',
'users':'<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
'pulse':'<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>',
'branch':'<line x1="6" x2="6" y1="3" y2="15"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9a9 9 0 0 1-9 9"/>',
'arrow':'<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
'book':'<path d="m19 21-7-4-7 4V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16z"/>',
}
def svg(n,s,c='currentColor',w=2): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{ICON[n]}</svg>'
def z(t): return re.sub(r'\(([^)]*[一-鿿][^)]*)\)', r'<span class="zh">(\1)</span>', t)
def foot(n,handle=True): return f'<div class="foot"><span>{"@garypsychology07" if handle else ""}</span><div style="display:flex;align-items:center;gap:20px"><span>{n} / 10</span><div class="bar"><div style="width:{18*n}px"></div></div></div></div>'

def foot(n,T=10,handle=True):
    return f'<div class="foot"><span>{"@garypsychology07" if handle else ""}</span><div style="display:flex;align-items:center;gap:20px"><span>{n} / {T}</span><div class="bar"><div style="width:{round(180*n/T)}px"></div></div></div></div>'
def zs(t,s=40): return f'<span style="font-family:&quot;Noto Sans CJK SC&quot;,sans-serif;font-weight:500;font-size:{s}px;color:#8A7F74;letter-spacing:0;white-space:nowrap">{t}</span>'
def write(slides,outdir='.'):
    for i,s in enumerate(slides,1): open(os.path.join(outdir,f'slide-{i:02d}.html'),'w').write(HEAD+s+'</body></html>')
