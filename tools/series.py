# Layout helpers for text-heavy concept carousels (personality series 07–12).
# Same brand as common.py; each gen.py sets T and calls these.
from common import HEAD, svg, z

def zs(t, s=30):
    return (f'<span style="font-family:\'Noto Sans CJK SC\',sans-serif;font-weight:500;font-size:{s}px;'
            f'color:#8A7F74;letter-spacing:0;white-space:nowrap">{t}</span>')

def foot(n, T):
    w = round(180 * n / T)
    return (f'<div class="foot"><span>@garypsychology07</span><div style="display:flex;align-items:center;gap:20px">'
            f'<span>{n} / {T}</span><div class="bar"><div style="width:{w}px"></div></div></div></div>')

def swipe():
    return ('<div class="foot"><span>@garypsychology07</span><div style="display:flex;align-items:center;gap:16px;'
            'padding:18px 32px;border-radius:999px;background:#F2785C;color:#1E1E2A;font-size:34px;font-weight:700">'
            f'<span>swipe</span>{svg("arrow",40,w=2.5)}</div></div>')

def cover(lab, title, sub, art, size=104):
    return (f'<div class="s"><div style="display:flex;justify-content:space-between;align-items:flex-start">'
            f'<div class="lab">{lab}</div>{art}</div>'
            f'<h1 style="margin-top:6px;font-size:{size}px">{title}</h1>'
            f'<p style="margin:36px 0 0;font-size:42px;line-height:1.3;color:#4A4A56">{sub}</p>'
            f'<div style="flex-grow:1"></div>{swipe()}</div>')

def head(lab, title, size=84, art=''):
    t = (f'<div class="lab">{lab}</div><h1 style="margin-top:22px;font-size:{size}px">{title}</h1>')
    if art:
        return (f'<div style="display:flex;justify-content:space-between;align-items:flex-start;gap:24px">'
                f'<div style="flex:1">{t}</div><div style="flex-shrink:0">{art}</div></div>')
    return t

def card(body, k='', bg='#FFFDF8', size=42):
    border = 'border:2px solid #E4DDD0;' if bg == '#FFFDF8' else ''
    kk = f'<div class="k">{k}</div>' if k else ''
    return (f'<div style="padding:30px 38px;border-radius:28px;background:{bg};{border}">{kk}'
            f'<div style="font-size:{size}px;line-height:1.42">{z(body)}</div></div>')

def ex(body, size=42):
    """Coral example box."""
    return card(body, '', '#FBE3DB', size)

def bullets(items, size=46, gap=38):
    rows = ''.join(
        f'<div style="display:flex;gap:22px;align-items:flex-start"><div style="width:16px;height:16px;'
        f'border-radius:50%;background:#3D3A8C;margin-top:{int(size*0.5)}px;flex-shrink:0"></div>'
        f'<div style="font-size:{size}px;line-height:1.4">{z(t)}</div></div>' for t in items)
    return f'<div style="display:flex;flex-direction:column;gap:{gap}px">{rows}</div>'

def rows(items, size=40, label_w=250):
    """Cheat-sheet rows: (label, text)."""
    out = ''.join(
        f'<div style="display:flex;gap:24px;align-items:baseline;padding:20px 0;border-bottom:2px solid #E4DDD0">'
        f'<div style="width:{label_w}px;flex-shrink:0;font-family:Fraunces,serif;font-weight:700;font-size:{size+6}px;color:#3D3A8C">{a}</div>'
        f'<div style="font-size:{size}px;line-height:1.38">{z(b)}</div></div>' for a, b in items)
    return f'<div>{out}</div>'

def slide(inner, n, T):
    return f'<div class="s">{inner}{foot(n, T)}</div>'

def last(inner, T):
    return (f'<div class="s">{inner}<div class="foot" style="justify-content:flex-end"><div style="display:flex;'
            f'align-items:center;gap:20px"><span>{T} / {T}</span><div class="bar"><div style="width:180px">'
            f'</div></div></div></div></div>')

def nextup(text):
    return (f'<div style="padding:30px 38px;border-radius:28px;background:#3D3A8C;color:#F7F3EC">'
            f'<div class="k" style="color:#F2B8A6">NEXT UP</div><div style="font-family:Fraunces,serif;'
            f'font-weight:700;font-size:46px;line-height:1.15">{text}</div></div>')

def save_btn(text='Save · Follow @garypsychology07'):
    return (f'<div style="margin-top:32px;display:flex"><span style="padding:20px 40px;border-radius:999px;'
            f'background:#F2785C;color:#1E1E2A;font-size:38px;font-weight:700">{text}</span></div>')

GROW = '<div style="flex-grow:1"></div>'

def write(S):
    for i, s in enumerate(S, 1):
        open(f'slide-{i:02d}.html', 'w').write(HEAD + s + '</body></html>')
