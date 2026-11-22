"""Animirani Reel 1080x1920 za @pametnija.firma: fotke sa laganim zumom, animirani tekst,
telefon sa porukama, brojač, upozorenja, muzika i zvučni efekti.
Svaka scena je funkcija f(t, trajanje) -> PIL slika. Video se piše kroz ffmpeg pipe."""
import math, os, subprocess, sys, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
W, H, FPS = 1080, 1920, 30
G = (14, 26, 43); R = (19, 36, 58); A = (34, 195, 230); WH = (255, 255, 255); B = (197, 208, 220)
RED = (235, 87, 87); GRN = (76, 201, 120)
HANDLE = "@pametnija.firma"
FD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
_fc = {}


def f(name, size):
    k = (name, size)
    if k not in _fc:
        _fc[k] = ImageFont.truetype(os.path.join(FD, name), size)
    return _fc[k]


def ease(x):
    x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3


def prog(t, start, dur):
    return ease((t - start) / dur) if dur > 0 else float(t >= start)


def wrap(d, text, font, maxw):
    out, cur = [], ""
    for w in text.split():
        c = (cur + " " + w).strip()
        if d.textlength(c, font=font) <= maxw: cur = c
        else: out.append(cur); cur = w
    return out + [cur] if cur else out


_photo = {}


def photo_bg(path, t, dur, z0=1.0, z1=1.12, fx=0.5, fy=0.5, dark=0.45):
    if path not in _photo:
        im = Image.open(path).convert("RGB")
        sc = max(W / im.width, H / im.height)
        _photo[path] = im.resize((math.ceil(im.width * sc * 1.25), math.ceil(im.height * sc * 1.25)), Image.LANCZOS)
    big = _photo[path]
    z = z0 + (z1 - z0) * (t / dur)
    base = max(W / big.width, H / big.height) * z * 1.0
    cw, ch = W / base, H / base
    x = (big.width - cw) * fx; y = (big.height - ch) * fy
    im = big.resize((W, H), Image.BILINEAR, box=(x, y, x + cw, y + ch))
    if dark:
        grad = Image.new("L", (1, H))
        for yy in range(H):
            grad.putpixel((0, yy), int(255 * dark * (0.55 + 0.45 * (yy / H) ** 1.5)))
        im = Image.composite(Image.new("RGB", (W, H), G), im, grad.resize((W, H)))
    return im


def blank():
    return Image.new("RGB", (W, H), G)


def overlay_text(im, t, start, title, sub=None, y=1380, label=None):
    """Kartica sa naslovom koja klizne odozdo."""
    p = prog(t, start, 0.5)
    if p <= 0: return im
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    fT = f("InterDisplay-Bold.otf", 72); fS = f("Inter-Regular.otf", 42)
    tl = wrap(d, title, fT, W - 260); sl = wrap(d, sub, fS, W - 260) if sub else []
    h = 70 + len(tl) * 86 + (20 + len(sl) * 56 if sl else 0) + 50 + (56 if label else 0)
    dy = int((1 - p) * 120); a = int(255 * p)
    x0, y0 = 90, y + dy
    d.rounded_rectangle([x0, y0, W - 90, y0 + h], radius=32, fill=R + (int(235 * p),), outline=A + (a,), width=4)
    yy = y0 + 46
    if label:
        d.text((x0 + 44, yy), label, font=f("Inter-SemiBold.otf", 34), fill=A + (a,)); yy += 56
    for ln in tl:
        d.text((x0 + 44, yy), ln, font=fT, fill=WH + (a,)); yy += 86
    yy += 20
    for ln in sl:
        d.text((x0 + 44, yy), ln, font=fS, fill=B + (a,)); yy += 56
    im = im.convert("RGBA"); im.alpha_composite(lay); return im.convert("RGB")


def handle_bar(im):
    d = ImageDraw.Draw(im)
    d.ellipse([90, 120, 130, 160], outline=A, width=6); d.ellipse([104, 134, 116, 146], fill=A)
    d.text((148, 140), HANDLE, font=f("Inter-Medium.otf", 36), fill=WH, anchor="lm")
    return im


def big_center(im, t, start, text, size=120, y=760, color=WH, font="InterDisplay-Bold.otf"):
    p = prog(t, start, 0.45)
    if p <= 0: return im
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    fo = f(font, size); lines = wrap(d, text, fo, W - 160)
    yy = y - (len(lines) - 1) * size * 0.55 + (1 - p) * 60
    for ln in lines:
        d.text((W / 2, yy), ln, font=fo, fill=color + (int(255 * p),), anchor="mm"); yy += size * 1.1
    im = im.convert("RGBA"); im.alpha_composite(lay); return im.convert("RGB")


def phone(im, t, x0=200, y0=300, w=680, h=1180, header="", time="", bubbles=(), notes=()):
    """Telefon sa razgovorom. bubbles: (start, strana 'l'/'r', tekst). notes: (start, boja, naslov, tekst)."""
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([x0, y0, x0 + w, y0 + h], radius=70, fill=(8, 14, 24, 255), outline=(60, 72, 90, 255), width=10)
    d.rounded_rectangle([x0 + w / 2 - 70, y0 + 22, x0 + w / 2 + 70, y0 + 46], radius=12, fill=(30, 36, 46, 255))
    if time:
        d.text((x0 + 60, y0 + 34), time, font=f("Inter-SemiBold.otf", 30), fill=WH, anchor="lm")
    yy = y0 + 90
    if header:
        d.rectangle([x0 + 10, yy, x0 + w - 10, yy + 90], fill=(22, 30, 44, 255))
        d.ellipse([x0 + 34, yy + 18, x0 + 88, yy + 72], fill=A)
        d.text((x0 + 104, yy + 45), header, font=f("Inter-SemiBold.otf", 38), fill=WH, anchor="lm")
        yy += 120
    fo = f("Inter-Regular.otf", 40)
    for (st, side, text) in bubbles:
        p = prog(t, st, 0.3)
        if p <= 0: continue
        if text == "...":
            bw, bh = 130, 70
            bx = x0 + 34 if side == "l" else x0 + w - 34 - bw
            d.rounded_rectangle([bx, yy, bx + bw, yy + bh], radius=30, fill=(40, 50, 66, int(255 * p)))
            for i in range(3):
                ph = (t * 4 + i * 0.6) % 2
                r = 9 if ph < 1 else 7
                d.ellipse([bx + 30 + i * 32 - r, yy + 35 - r, bx + 30 + i * 32 + r, yy + 35 + r], fill=B + (int(255 * p),))
            yy += bh + 22; continue
        lines = wrap(d, text, fo, w - 200)
        bw = max(d.textlength(l, font=fo) for l in lines) + 56; bh = len(lines) * 52 + 40
        bx = x0 + 34 if side == "l" else x0 + w - 34 - bw
        col = (40, 50, 66) if side == "l" else (24, 120, 150)
        sc = 0.85 + 0.15 * p
        d.rounded_rectangle([bx, yy + (1 - sc) * bh, bx + bw, yy + bh], radius=30, fill=col + (int(255 * p),))
        ty = yy + 18
        for ln in lines:
            d.text((bx + 28, ty), ln, font=fo, fill=WH + (int(255 * p),)); ty += 52
        yy += bh + 22
    ny = y0 + 140
    for (st, colr, title, text) in notes:
        p = prog(t, st, 0.4)
        if p <= 0: continue
        oy = ny - (1 - p) * 120
        d.rounded_rectangle([x0 + 30, oy, x0 + w - 30, oy + 200], radius=34, fill=(30, 40, 58, int(250 * p)), outline=colr + (int(255 * p),), width=4)
        d.ellipse([x0 + 62, oy + 44, x0 + 106, oy + 88], fill=colr + (int(255 * p),))
        d.text((x0 + 126, oy + 66), title, font=f("Inter-SemiBold.otf", 44), fill=WH + (int(255 * p),), anchor="lm")
        d.text((x0 + 62, oy + 140), text, font=f("Inter-Regular.otf", 40), fill=B + (int(255 * p),), anchor="lm")
        ny += 235
    im = im.convert("RGBA"); im.alpha_composite(lay); return im.convert("RGB")


def end_card(t, title, sub):
    im = blank(); d = ImageDraw.Draw(im)
    p = prog(t, 0, 0.5)
    cx, cy = W / 2, 640
    r = 110 * (0.7 + 0.3 * p)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=A)
    fo = f("InterDisplay-Bold.otf", int(120 * (0.7 + 0.3 * p)))
    d.text((cx, cy - 6), "PF", font=fo, fill=G, anchor="mm")
    d.text((cx, cy + 180), HANDLE, font=f("Inter-Medium.otf", 44), fill=B, anchor="mm")
    im = big_center(im, t, 0.3, title, size=78, y=1020)
    im = big_center(im, t, 0.6, sub, size=48, y=1230, color=A, font="Inter-SemiBold.otf")
    return im


def render(scenes, out, sfx=(), seed="pf", voice=(), xf=8):
    """scenes: [(trajanje, funkcija)], sfx: [(vrijeme, vrsta)]. Prelaz: 8 frejmova pretapanja."""
    total = sum(s[0] for s in scenes)
    tmp = out + ".tmp.mp4"
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
           "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-pix_fmt", "yuv420p", tmp]
    pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    prev_last = None; XF = xf
    for i, (dur, fn) in enumerate(scenes):
        n = int(round(dur * FPS))
        for k in range(n):
            im = fn(k / FPS, dur)
            if prev_last is not None and k < XF:
                im = Image.blend(prev_last, im, (k + 1) / (XF + 1))
            if k == n - 1: prev_last = im
            pr.stdin.write(im.tobytes())
    pr.stdin.close(); pr.wait()
    wav = out + ".wav"; make_audio(wav, total, sfx, seed, voice)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-i", wav, "-c:v", "copy", "-c:a", "aac", "-b:a", "160k",
                    "-shortest", "-movflags", "+faststart", out], check=True)
    os.remove(tmp); os.remove(wav)
    return out


SR = 44100


def _tone(fr, dur, decay=8.0, vol=0.5):
    t = np.arange(int(SR * dur)) / SR
    return vol * np.sin(2 * np.pi * fr * t) * np.exp(-t * decay)


def sfx_sound(kind):
    if kind == "pop":
        t = np.arange(int(SR * 0.12)) / SR
        return 0.45 * np.sin(2 * np.pi * (500 + 900 * t / 0.12) * t) * np.exp(-t * 30)
    if kind == "ping":
        return _tone(1318, 0.9, 5, 0.35) + _tone(1976, 0.9, 7, 0.2)
    if kind == "alarm":
        return np.concatenate([_tone(880, 0.18, 3, 0.35), np.zeros(int(SR * 0.06)), _tone(660, 0.25, 3, 0.35)])
    if kind == "ring":
        t = np.arange(int(SR * 1.0)) / SR
        s = 0.25 * (np.sin(2 * np.pi * 440 * t) + np.sin(2 * np.pi * 480 * t)) * (np.sin(2 * np.pi * 20 * t) > 0)
        return s * np.minimum(1, (1.0 - t) * 10)
    if kind == "whoosh":
        n = int(SR * 0.4); noise = np.random.default_rng(1).standard_normal(n)
        env = np.sin(np.linspace(0, np.pi, n)) ** 2
        k = np.ones(40) / 40
        return 0.25 * np.convolve(noise, k, "same") * env
    if kind == "tick":
        return _tone(2200, 0.04, 60, 0.3)
    return np.zeros(1)


def read_wav(p):
    with wave.open(p) as w:
        ch = w.getnchannels(); sr = w.getframerate()
        d = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    if ch == 2: d = d.reshape(-1, 2).mean(axis=1)
    if sr != SR: d = np.interp(np.linspace(0, len(d), int(len(d) * SR / sr), endpoint=False), np.arange(len(d)), d)
    return d


def wav_len(p):
    with wave.open(p) as w: return w.getnframes() / w.getframerate()


def make_audio(path, total, sfx, seed, voice=()):
    import muzika
    mpath = path + ".m.wav"
    muzika.main(mpath, total + 0.2, seed)
    with wave.open(mpath) as w:
        ch = w.getnchannels(); data = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
        if ch == 2: data = data.reshape(-1, 2).mean(axis=1)
        sr = w.getframerate()
    os.remove(mpath)
    if sr != SR:
        data = np.interp(np.linspace(0, len(data), int(len(data) * SR / sr)), np.arange(len(data)), data)
    n = int(SR * total)
    mus = np.zeros(n); m = data[:n]; mus[:len(m)] = m
    vo = np.zeros(n)
    for (tt, vp) in voice:
        v = read_wav(vp); v = v / max(1e-6, np.abs(v).max()) * 0.9
        i = int(tt * SR); j = min(n, i + len(v))
        if i < n: vo[i:j] += v[:j - i]
    duck = np.ones(n) * 0.55
    if len(voice):
        env = (np.abs(vo) > 0.02).astype(np.float32)
        k = int(SR * 0.35); env = np.convolve(env, np.ones(k) / k, "same") > 0.01
        sm = np.convolve(env.astype(np.float32), np.ones(int(SR * 0.2)) / int(SR * 0.2), "same")
        duck = 0.55 - 0.40 * np.clip(sm, 0, 1)
    mix = mus * duck + vo
    sf = np.zeros(n)
    for (tt, kind) in sfx:
        s = sfx_sound(kind); i = int(tt * SR); j = min(n, i + len(s))
        if i < n: sf[i:j] += s[:j - i]
    mix = mix + sf * (0.6 if len(voice) else 1.0)
    fade = int(SR * 0.6); mix[-fade:] *= np.linspace(1, 0, fade)
    mix = np.clip(mix / max(1, np.abs(mix).max() / 0.95), -1, 1)
    st = np.repeat((mix * 32767).astype(np.int16)[:, None], 2, axis=1)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes())


def top_pill(im, t, start, text, sub=None, y=250, color=A, size=96):
    p = prog(t, start, 0.4)
    if p <= 0: return im
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    fo = f("InterDisplay-Bold.otf", size); fs = f("Inter-SemiBold.otf", 44)
    tw = d.textlength(text, font=fo); sw = d.textlength(sub, font=fs) if sub else 0
    bw = max(tw, sw) + 100; bh = int(size * 1.55) + (70 if sub else 0)
    x0 = (W - bw) / 2; y0 = y - (1 - p) * 50; a = int(255 * p)
    d.rounded_rectangle([x0, y0, x0 + bw, y0 + bh], radius=36, fill=G + (int(225 * p),))
    d.text((W / 2, y0 + size * 0.8), text, font=fo, fill=WH + (a,), anchor="mm")
    if sub: d.text((W / 2, y0 + size * 1.55 + 22), sub, font=fs, fill=color + (a,), anchor="mm")
    im = im.convert("RGBA"); im.alpha_composite(lay); return im.convert("RGB")


def grid_bg():
    im = blank(); d = ImageDraw.Draw(im)
    for x in range(0, W, 60): d.line([x, 0, x, H], fill=(22, 40, 60), width=2)
    for y in range(0, H, 60): d.line([0, y, W, y], fill=(22, 40, 60), width=2)
    return im


def tiles(im, t, start, items, x0=150, y0=1100, w=780):
    """Mali pregled stanja: items = [(naziv, ok)] u dvije kolone."""
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    cw = (w - 30) / 2
    for i, (name, ok) in enumerate(items):
        p = prog(t, start + i * 0.15, 0.3)
        if p <= 0: continue
        cx = x0 + (i % 2) * (cw + 30); cy = y0 + (i // 2) * 120
        col = GRN if ok else RED
        d.rounded_rectangle([cx, cy, cx + cw, cy + 96], radius=22, fill=(22, 32, 48, int(255 * p)), outline=col + (int(255 * p),), width=3)
        d.ellipse([cx + 26, cy + 34, cx + 54, cy + 62], fill=col + (int(255 * p),))
        d.text((cx + 72, cy + 48), name, font=f("Inter-SemiBold.otf", 36), fill=WH + (int(255 * p),), anchor="lm")
    im = im.convert("RGBA"); im.alpha_composite(lay); return im.convert("RGB")


def list_items(im, t, start, items, y0=520, gap=150, every=0.7, num=True, colr=None):
    """Stavke koje se pojavljuju jedna po jedna (broj u krugu + tekst)."""
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    fo = f("Inter-SemiBold.otf", 50)
    for i, txt in enumerate(items):
        p = prog(t, start + i * every, 0.35)
        if p <= 0: continue
        a = int(255 * p); x = 110 + (1 - p) * 60; y = y0 + i * gap
        c = colr[i] if colr else A
        d.rounded_rectangle([x, y, W - 110, y + gap - 30], radius=28, fill=R + (int(230 * p),), outline=c + (a,), width=3)
        if num:
            d.ellipse([x + 26, y + (gap - 30) / 2 - 34, x + 94, y + (gap - 30) / 2 + 34], fill=c + (a,))
            d.text((x + 60, y + (gap - 30) / 2), str(i + 1), font=f("InterDisplay-Bold.otf", 44), fill=G + (a,), anchor="mm")
        lines = wrap(d, txt, fo, W - 220 - 130)
        ty = y + (gap - 30) / 2 - (len(lines) - 1) * 30
        for ln in lines:
            d.text((x + 124, ty), ln, font=fo, fill=WH + (a,), anchor="lm"); ty += 60
    im = im.convert("RGBA"); im.alpha_composite(lay); return im.convert("RGB")


def steps(im, t, start, items, y0=560, every=0.9):
    """Koraci postupka povezani strelicama, svaki dobije zelenu kvačicu."""
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    fo = f("Inter-SemiBold.otf", 50); bh = 150; gap = 90
    for i, txt in enumerate(items):
        p = prog(t, start + i * every, 0.35)
        if p <= 0: continue
        a = int(255 * p); y = y0 + i * (bh + gap)
        done = t >= start + i * every + 0.5
        col = GRN if done else A
        d.rounded_rectangle([140, y, W - 140, y + bh], radius=30, fill=R + (int(235 * p),), outline=col + (a,), width=4)
        d.text((200, y + bh / 2), txt, font=fo, fill=WH + (a,), anchor="lm")
        if done:
            cx, cy = W - 210, y + bh / 2
            d.ellipse([cx - 34, cy - 34, cx + 34, cy + 34], fill=GRN + (a,))
            d.line([cx - 16, cy, cx - 4, cy + 13, cx + 18, cy - 14], fill=G + (a,), width=8)
        if i < len(items) - 1 and prog(t, start + (i + 1) * every, 0.3) > 0:
            ax = W / 2; ay0 = y + bh + 12; ay1 = y + bh + gap - 12
            d.line([ax, ay0, ax, ay1], fill=A + (a,), width=6)
            d.polygon([(ax - 16, ay1 - 18), (ax + 16, ay1 - 18), (ax, ay1)], fill=A + (a,))
    im = im.convert("RGBA"); im.alpha_composite(lay); return im.convert("RGB")


# ---- brzi rez (od 22.11.2026): tekst koji udari, titl, grafikon, mail ----
def slam(im, t, start, text, size=130, y=760, color=WH, box=True, font="InterDisplay-Bold.otf"):
    """Tekst udari odmah: skala 1.35 -> 1.0 za 0.18 s, sa tamnom podlogom."""
    if t < start: return im
    p = prog(t, start, 0.18); sc = 1.35 - 0.35 * p
    fo = f(font, int(size * sc))
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    lines = wrap(d, text, fo, W - 140); lh = size * sc * 1.08
    yy = y - (len(lines) - 1) * lh / 2
    if box:
        bw = max(d.textlength(l, font=fo) for l in lines) + 90; bh = len(lines) * lh + 60
        d.rounded_rectangle([(W - bw) / 2, yy - lh / 2 - 30, (W + bw) / 2, yy - lh / 2 - 30 + bh], radius=30, fill=G + (215,))
    for ln in lines:
        d.text((W / 2, yy), ln, font=fo, fill=color + (255,), anchor="mm"); yy += lh
    im = im.convert("RGBA"); im.alpha_composite(lay); return im.convert("RGB")


def caption(im, t, text, y=1560, start=0.0, hl=None):
    """Titl glasa: bijeli tekst na tamnoj traci; hl = riječ koja je tirkizna."""
    if t < start or not text: return im
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    fo = f("InterDisplay-Bold.otf", 64); lines = wrap(d, text, fo, W - 200)
    lh = 80; h = len(lines) * lh + 40; yy = y - h / 2
    bw = max(d.textlength(l, font=fo) for l in lines) + 80
    d.rounded_rectangle([(W - bw) / 2, yy, (W + bw) / 2, yy + h], radius=24, fill=(0, 0, 0, 170))
    yy += 20 + lh / 2
    for ln in lines:
        x = W / 2 - d.textlength(ln, font=fo) / 2
        for w in ln.split(" "):
            c = A if hl and w.strip(".,:?!").lower() in hl else WH
            d.text((x, yy), w, font=fo, fill=c + (255,), anchor="lm"); x += d.textlength(w + " ", font=fo)
        yy += lh
    im = im.convert("RGBA"); im.alpha_composite(lay); return im.convert("RGB")


def line_chart(im, t, start, label, crash_at=0.6, y0=520, h=520, dur=2.0):
    """Graf rada sistema koji se crta i na crash_at padne na nulu (crveno)."""
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    x0, x1 = 110, W - 110
    d.rounded_rectangle([x0 - 30, y0 - 90, x1 + 30, y0 + h + 40], radius=30, fill=R + (235,), outline=(50, 70, 95, 255), width=3)
    d.text((x0, y0 - 45), label, font=f("Inter-SemiBold.otf", 40), fill=B + (255,), anchor="lm")
    p = max(0.0, min(1.0, (t - start) / dur)); n = 80; pts = []
    for i in range(int(n * p) + 1):
        u = i / n; x = x0 + (x1 - x0) * u
        v = 0.0 if u > crash_at else 0.62 + 0.12 * math.sin(u * 23) + 0.06 * math.sin(u * 61)
        pts.append((x, y0 + h - v * h))
    for i in range(1, len(pts)):
        col = RED if (pts[i][0] - x0) / (x1 - x0) > crash_at else GRN
        d.line([pts[i - 1], pts[i]], fill=col + (255,), width=8)
    im = im.convert("RGBA"); im.alpha_composite(lay); return im.convert("RGB")


def mail_card(im, t, start, od, predmet, tekst, mark=None, y0=430):
    """Mail u inboxu; mark = dio teksta koji se zacrveni nakon 1 s."""
    p = prog(t, start, 0.3)
    if p <= 0: return im
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    a = int(255 * p); x0, x1 = 90, W - 90; yy = y0 + (1 - p) * 80
    d.rounded_rectangle([x0, yy, x1, yy + 760], radius=34, fill=(246, 248, 251, a))
    d.text((x0 + 50, yy + 70), "Od:", font=f("Inter-Regular.otf", 38), fill=(110, 120, 135, a), anchor="lm")
    hot = mark and t > start + 1.0
    d.text((x0 + 130, yy + 70), od, font=f("Inter-SemiBold.otf", 40), fill=(RED if hot else (20, 30, 45)) + (a,), anchor="lm")
    d.line([x0 + 40, yy + 125, x1 - 40, yy + 125], fill=(220, 225, 232, a), width=3)
    ty = yy + 190
    for ln in wrap(d, predmet, f("InterDisplay-Bold.otf", 52), x1 - x0 - 100):
        d.text((x0 + 50, ty), ln, font=f("InterDisplay-Bold.otf", 52), fill=(20, 30, 45, a), anchor="lm"); ty += 66
    ty += 30
    for ln in wrap(d, tekst, f("Inter-Regular.otf", 42), x1 - x0 - 100):
        c = RED if (hot and mark in ln) else (60, 70, 85)
        d.text((x0 + 50, ty), ln, font=f("Inter-Regular.otf", 42), fill=c + (a,), anchor="lm"); ty += 58
    im = im.convert("RGBA"); im.alpha_composite(lay); return im.convert("RGB")


def cflow(im, t, d, text, y=1560, hl=None, lead=0.1, tail=0.3, maxw=4):
    """Titl koji teče uz glas: po 2-4 riječi, vrijeme po broju slova."""
    words = text.split(); chunks, cur = [], []
    SLABE = {'i', 'a', 'u', 'za', 'na', 'da', 'od', 'do', 'sa', 'iz', 'po', 'o', 'pa', 'ili', 'ne', 'je', 'se', 'to'}
    for w in words:
        cur.append(w)
        if w[-1] in '.,:?!' or (len(cur) >= maxw and w.lower() not in SLABE) or len(cur) >= maxw + 2:
            chunks.append(' '.join(cur)); cur = []
    if cur: chunks.append(' '.join(cur))
    if len(chunks) > 1 and len(chunks[-1].split()) == 1 and len(chunks[-2].split()) <= 5 and chunks[-2][-1] not in '.?!':
        chunks[-2:] = [chunks[-2] + ' ' + chunks[-1]]   # bez usamljene zadnje riječi
    tot = sum(len(c) for c in chunks); span = max(0.5, d - lead - tail); acc = lead
    for c in chunks:
        dur = span * len(c) / tot
        if t < acc + dur or c is chunks[-1]:
            return caption(im, t, c, y=y, hl=hl)
        acc += dur
    return im


_vid = {}


def video_bg(path, t, dur, dark=0.4, zoom=1.0):
    """Kadar iz video klipa (npr. Gemini Omni), razvučen na trajanje scene, sa istim zatamnjenjem kao photo_bg."""
    if path not in _vid:
        n = int(subprocess.check_output(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0",
                                          "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", path]).strip())
        raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", path, "-vf",
                                       f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}",
                                       "-f", "rawvideo", "-pix_fmt", "rgb24", "-"])
        fr = [Image.frombytes("RGB", (W, H), raw[i * W * H * 3:(i + 1) * W * H * 3]) for i in range(len(raw) // (W * H * 3))]
        _vid[path] = fr
    fr = _vid[path]
    im = fr[min(len(fr) - 1, int(len(fr) * t / dur))]
    if zoom != 1.0:
        cw, ch = W / zoom, H / zoom
        im = im.resize((W, H), Image.BILINEAR, box=((W - cw) / 2, (H - ch) / 2, (W + cw) / 2, (H + ch) / 2))
    if dark:
        grad = Image.new("L", (1, H))
        for yy in range(H):
            grad.putpixel((0, yy), int(255 * dark * (0.55 + 0.45 * (yy / H) ** 1.5)))
        im = Image.composite(Image.new("RGB", (W, H), G), im, grad.resize((W, H)))
    return im


# ---- nadzor sistema (izgled kao kod alata za nadzor tipa Zabbix, bez imena i logotipa) ----
SEV = {"info": ((80, 140, 220), "Info"), "upoz": ((230, 190, 60), "Upozorenje"),
       "visoko": ((240, 130, 50), "Visoko"), "krit": ((235, 87, 87), "Kritično")}


def problem_table(im, t, start, rows, y0=560, x0=60, x1=None):
    """Tabela problema: rows = [(od_s, vrijeme, sev, host, problem, rijeseno_od_s ili None)]."""
    x1 = x1 or W - 60
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    p0 = prog(t, start, 0.3)
    if p0 <= 0: return im
    a0 = int(255 * p0)
    d.rounded_rectangle([x0, y0, x1, y0 + 90 + len(rows) * 150], radius=24, fill=(16, 28, 44, int(245 * p0)), outline=(50, 70, 95, a0), width=3)
    fh = f("Inter-SemiBold.otf", 30)
    for xx, txt in ((x0 + 30, "Vrijeme"), (x0 + 200, "Ozbiljnost"), (x0 + 450, "Server / problem")):
        d.text((xx, y0 + 45), txt, font=fh, fill=B + (a0,), anchor="lm")
    d.text((x1 - 30, y0 + 45), "Status", font=fh, fill=B + (a0,), anchor="rm")
    for i, (st, vr, sev, host, prob, res) in enumerate(rows):
        p = prog(t, start + st, 0.3)
        if p <= 0: continue
        a = int(255 * p); y = y0 + 90 + i * 150
        done = res is not None and t >= start + res
        col, lab = SEV[sev]
        d.line([x0 + 20, y, x1 - 20, y], fill=(40, 58, 80, a), width=2)
        d.text((x0 + 30, y + 75), vr, font=f("Inter-SemiBold.otf", 34), fill=WH + (a,), anchor="lm")
        d.rounded_rectangle([x0 + 190, y + 40, x0 + 420, y + 110], radius=12, fill=(GRN if done else col) + (a,))
        d.text((x0 + 305, y + 75), "OK" if done else lab, font=f("Inter-SemiBold.otf", 30), fill=G + (a,), anchor="mm")
        d.text((x0 + 450, y + 50), host, font=f("Inter-SemiBold.otf", 32), fill=A + (a,), anchor="lm")
        stt = "RIJEŠENO" if done else "PROBLEM"
        d.text((x1 - 30, y + 50), stt, font=f("InterDisplay-Bold.otf", 30), fill=(GRN if done else RED) + (a,), anchor="rm")
        d.text((x0 + 450, y + 102), prob, font=f("Inter-Regular.otf", 30), fill=WH + (a,), anchor="lm")
    im = im.convert("RGBA"); im.alpha_composite(lay); return im.convert("RGB")


def trend_chart(im, t, start, label, v0=55, v1=93, prag=90, dur=2.2, y0=560, h=520, osa="Popunjenost diska %"):
    """Graf koji raste od v0 do v1; isprekidana crvena linija praga; preko praga linija postane crvena."""
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    x0, x1 = 120, W - 100
    d.rounded_rectangle([x0 - 40, y0 - 110, x1 + 40, y0 + h + 70], radius=30, fill=(16, 28, 44, 240), outline=(50, 70, 95, 255), width=3)
    d.text((x0, y0 - 60), label, font=f("Inter-SemiBold.otf", 38), fill=WH + (255,), anchor="lm")
    d.text((x0, y0 + h + 35), osa, font=f("Inter-Regular.otf", 28), fill=B + (255,), anchor="lm")
    def Y(v): return y0 + h - (v - 40) / 60 * h
    for v in (50, 70, 90):
        d.line([x0, Y(v), x1, Y(v)], fill=(34, 50, 70, 255), width=2)
        d.text((x0 - 12, Y(v)), str(v), font=f("Inter-Regular.otf", 26), fill=B + (255,), anchor="rm")
    for xx in range(int(x0), int(x1), 34):
        d.line([xx, Y(prag), xx + 18, Y(prag)], fill=RED + (255,), width=4)
    d.text(((x0 + x1) / 2, Y(prag) - 26), f"prag {prag} %", font=f("Inter-SemiBold.otf", 28), fill=RED + (255,), anchor="mm")
    p = max(0.0, min(1.0, (t - start) / dur)); n = 90; pts = []
    for i in range(int(n * p) + 1):
        u = i / n; v = v0 + (v1 - v0) * (u ** 1.6) + 1.2 * math.sin(u * 40)
        pts.append((x0 + (x1 - x0) * u, Y(v), v))
    for i in range(1, len(pts)):
        d.line([pts[i - 1][:2], pts[i][:2]], fill=(RED if pts[i][2] >= prag else A) + (255,), width=7)
    if pts and pts[-1][2] >= prag:
        cx, cy = pts[-1][:2]; r = 16 + 6 * math.sin(t * 12)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=RED + (255,), width=5)
    im = im.convert("RGBA"); im.alpha_composite(lay); return im.convert("RGB")


_scr = {}


def screen_card(im, t, d, path, box_a, box_b=None, y0=430, w=1000, h=None, mark=None, mark_from=0.6, label=None):
    """Snimak ekrana (npr. pravi Zabbix) u okviru monitora, sa pomjeranjem/zumom od box_a do box_b
    (koordinate u pikselima snimka). mark = (x0,y0,x1,y1) u koordinatama snimka: crveni okvir koji pulsira od mark_from s."""
    if path not in _scr:
        _scr[path] = Image.open(path).convert("RGB")
    src = _scr[path]; box_b = box_b or box_a
    u = ease(t / max(d, 0.01))
    bx = [a + (b - a) * u for a, b in zip(box_a, box_b)]
    bw, bh = bx[2] - bx[0], bx[3] - bx[1]
    h = h or int(w * bh / bw)
    x0 = (W - w) // 2
    crop = src.resize((w, h), Image.LANCZOS, box=tuple(bx))
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dr = ImageDraw.Draw(lay)
    dr.rounded_rectangle([x0 - 18, y0 - 18, x0 + w + 18, y0 + h + 18], radius=26, fill=(8, 12, 20, 255), outline=(60, 72, 90, 255), width=4)
    im = im.convert("RGBA"); im.alpha_composite(lay); im = im.convert("RGB")
    im.paste(crop, (x0, y0))
    if mark and t >= mark_from:
        sx, sy = w / bw, h / bh
        mx0, my0 = x0 + (mark[0] - bx[0]) * sx, y0 + (mark[1] - bx[1]) * sy
        mx1, my1 = x0 + (mark[2] - bx[0]) * sx, y0 + (mark[3] - bx[1]) * sy
        a = int(160 + 95 * (0.5 + 0.5 * math.sin((t - mark_from) * 8)))
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dr = ImageDraw.Draw(lay)
        dr.rounded_rectangle([max(x0, mx0 - 8), max(y0, my0 - 8), min(x0 + w, mx1 + 8), min(y0 + h, my1 + 8)], radius=10, outline=RED + (a,), width=6)
        im = im.convert("RGBA"); im.alpha_composite(lay); im = im.convert("RGB")
    if label:
        im = top_pill(im, t, 0.0, label[0], label[1] if len(label) > 1 else None, y=y0 - 230, size=72)
    return im


def screen_seq(paths, t, d):
    """Izabere snimak iz niza (npr. 18 snimaka grafa uživo) prema vremenu u sceni."""
    i = min(len(paths) - 1, int(len(paths) * t / max(d, 0.01)))
    return paths[i]
