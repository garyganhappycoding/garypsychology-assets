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

# ---- added for modules: personality part 2, motivation, emotion, intelligence ----
def badge(emoji, size=240, bg='#FBE3DB'):
    return (f'<div style="width:{size}px;height:{size}px;border-radius:50%;background:{bg};display:flex;'
            f'align-items:center;justify-content:center;font-size:{int(size*0.55)}px;flex-shrink:0">{emoji}</div>')

def concept(n, T, lab, name, zh, emoji, defin, example, exk='EXAMPLE', size=100, extra=''):
    """One-term slide: name + Chinese + emoji badge, definition card, example card."""
    return slide(f'''<div style="display:flex;justify-content:space-between;align-items:flex-start;gap:20px"><div style="flex:1"><div class="lab">{lab}</div>
<h1 style="margin-top:22px;font-size:{size}px">{name}</h1><div style="margin-top:12px">{zs(zh,48)}</div></div>{badge(emoji,190)}</div>
{GROW}{card(defin,k='WHAT IT IS',size=46)}<div style="margin-top:30px">{card(example,k=exk,bg='#FBE3DB',size=46)}</div>{extra}{GROW}''', n, T)

def duo(a, b, size=38):
    """Two side-by-side cards. a/b = (emoji, title, zh, body); a is indigo, b is coral-tint."""
    def one(x, dark):
        e, t, zh, body = x
        bg, fg, sub = ('#3D3A8C', '#F7F3EC', '#C9C6EA') if dark else ('#FBE3DB', '#1E1E2A', '#8A7F74')
        return (f'<div style="flex:1;padding:34px;border-radius:28px;background:{bg};color:{fg}">'
                f'<div style="font-size:84px">{e}</div><div style="font-family:Fraunces,serif;font-weight:700;font-size:50px;margin-top:10px;line-height:1.05">{t}</div>'
                f'<div style="font-size:30px;color:{sub};margin-top:6px">{zh}</div>'
                f'<div style="margin-top:18px;font-size:{size}px;line-height:1.38">{z(body)}</div></div>')
    return f'<div style="display:flex;gap:26px">{one(a,True)}{one(b,False)}</div>'

def grid(items, size=32):
    """2x2 (or 2xN) tiles: (emoji, title, zh, body)."""
    cells = ''.join(
        f'<div style="width:calc(50% - 13px);box-sizing:border-box;padding:28px;border-radius:26px;background:#FFFDF8;border:2px solid #E4DDD0">'
        f'<div style="font-size:64px">{e}</div><div style="font-family:Fraunces,serif;font-weight:700;font-size:42px;margin-top:8px;line-height:1.08">{t}</div>'
        f'<div style="font-size:26px;color:#8A7F74;margin-top:4px">{zh}</div><div style="margin-top:12px;font-size:{size}px;line-height:1.36">{z(b)}</div></div>'
        for e, t, zh, b in items)
    return f'<div style="display:flex;flex-wrap:wrap;gap:26px">{cells}</div>'

def flow(steps, size=34):
    """Horizontal arrow chain of short labels."""
    arrow = '<div style="font-size:44px;color:#C24A2B;font-weight:800">→</div>'
    boxes = arrow.join(f'<div style="flex:1;padding:22px 16px;border-radius:22px;background:{"#3D3A8C" if i==len(steps)-1 else "#FFFDF8"};'
                       f'color:{"#F7F3EC" if i==len(steps)-1 else "#1E1E2A"};border:2px solid #E4DDD0;text-align:center;font-size:{size}px;font-weight:700;line-height:1.25">{s}</div>'
                       for i, s in enumerate(steps))
    return f'<div style="display:flex;align-items:center;gap:12px">{boxes}</div>'

def vflow(steps, size=40):
    """Vertical arrow chain: steps = list of (main, sub). Last step highlighted."""
    arr = '<div style="font-size:44px;color:#C24A2B;font-weight:800;text-align:center;line-height:1">↓</div>'
    out = []
    for i, (m, sub) in enumerate(steps):
        last = i == len(steps) - 1
        bg, fg, sc = ('#3D3A8C', '#F7F3EC', '#C9C6EA') if last else ('#FFFDF8', '#1E1E2A', '#8A7F74')
        s = f'<span style="font-size:{int(size*0.72)}px;font-weight:500;color:{sc};margin-left:14px">{sub}</span>' if sub else ''
        out.append(f'<div style="padding:22px 30px;border-radius:22px;background:{bg};color:{fg};border:2px solid #E4DDD0;font-size:{size}px;font-weight:700">{m}{s}</div>')
    return f'<div style="display:flex;flex-direction:column;gap:8px">{arr.join(out)}</div>'
