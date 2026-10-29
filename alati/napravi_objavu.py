"""Pravi slajdove za Instagram po šablonima profila @video.nadzorkamere.

Upotreba:
    python napravi_objavu.py putanja/do/objava.json

objava.json opisuje slajdove; putanje do fotografija su relativne u odnosu na
folder u kojem je objava.json. Slike se snimaju u isti folder kao 01.png, 02.png...
Šabloni: naslovna, foto_traka, foto_kutija, tekst, dan_noc (vidi primjer_objava.json).
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter, ImageOps

W, H = 1080, 1350
GROUND = (14, 26, 43); RAISED = (19, 36, 58); ACCENT = (34, 195, 230)
WHITE = (255, 255, 255); BODY = (197, 208, 220); MUTED = (138, 155, 176)
HANDLE = "@video.nadzorkamere"
M = 96          # bočna margina
PH = 800        # visina fotografije u šablonima naslovna i foto_traka
FONTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
DISP, MED, REG, SEMI = "InterDisplay-Bold.otf", "Inter-Medium.otf", "Inter-Regular.otf", "Inter-SemiBold.otf"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


def crop(im, w, h, fx=0.5, fy=0.5):
    sc = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * sc), round(im.height * sc)), Image.LANCZOS)
    x = round((im.width - w) * fx); y = round((im.height - h) * fy)
    return im.crop((x, y, x + w, y + h))


def open_photo(base, rel):
    return ImageOps.exif_transpose(Image.open(os.path.join(base, rel))).convert("RGB")


def lens(d, cx, cy, r):
    for k, c in ((1, ACCENT), (0.78, GROUND), (0.5, ACCENT), (0.2, GROUND)):
        d.ellipse([cx - r * k, cy - r * k, cx + r * k, cy + r * k], fill=c)


def header(d, y, counter):
    lens(d, M + 20, y, 20)
    d.text((M + 56, y), HANDLE, font=font(MED, 30), fill=BODY, anchor="lm")
    if counter:
        d.text((W - M, y), counter, font=font(MED, 30), fill=MUTED, anchor="rm")


def wrap(d, text, f, maxw):
    out, cur = [], ""
    for w in text.split():
        c = (cur + " " + w).strip()
        if d.textlength(c, font=f) <= maxw:
            cur = c
        else:
            out.append(cur); cur = w
    return out + [cur] if cur else out


def block(d, text, f, y, fill, gap, x=M, maxw=W - 2 * M):
    for ln in wrap(d, text, f, maxw):
        d.text((x, y), ln, font=f, fill=fill); y += f.size + gap
    return y


def bar(d, y):
    d.rectangle([M, y, M + 120, y + 8], fill=ACCENT)


def s_naslovna(s, base, counter):
    img = Image.new("RGB", (W, H), GROUND)
    img.paste(crop(open_photo(base, s["foto"]), W, PH, *s.get("fokus", [0.5, 0.5])), (0, 0))
    d = ImageDraw.Draw(img)
    header(d, PH + 52, counter)
    ft = font(DISP, 76); y = PH + 112
    d.text((M, y), s["oznaka"], font=ft, fill=ACCENT); y += 86
    block(d, s["naslov"], ft, y, WHITE, 10)
    d.text((W - M, H - 62), "Prevuci  →", font=font(SEMI, 38), fill=ACCENT, anchor="rm")
    bar(d, H - 66)
    return img


def s_foto_traka(s, base, counter):
    img = Image.new("RGB", (W, H), GROUND)
    img.paste(crop(open_photo(base, s["foto"]), W, PH, *s.get("fokus", [0.5, 0.5])), (0, 0))
    d = ImageDraw.Draw(img)
    header(d, PH + 52, counter)
    ft = font(DISP, 64); y = PH + 112; x = M
    if s.get("broj"):
        d.text((M, y), s["broj"], font=ft, fill=ACCENT); x = M + d.textlength(s["broj"] + "  ", font=ft)
    for ln in wrap(d, s["naslov"], ft, W - M - x):
        d.text((x, y), ln, font=ft, fill=WHITE); y += 74
    if s.get("tekst"):
        block(d, s["tekst"], font(REG, 40), y + 18, BODY, 12)
    bar(d, H - 66)
    return img


def s_foto_kutija(s, base, counter):
    img = crop(open_photo(base, s["foto"]), W, H, *s.get("fokus", [0.5, 0.5]))
    d = ImageDraw.Draw(img)
    bx0, by0, bx1, by1 = M - 40, 1010, W - M + 40, 1270
    d.rounded_rectangle([bx0, by0, bx1, by1], radius=24, fill=RAISED, outline=ACCENT, width=4)
    header(d, by0 + 52, counter)
    d.text((bx0 + 40, by0 + 104), s["red1"], font=font(SEMI, 42), fill=WHITE)
    d.text((bx0 + 40, by0 + 162), s.get("red2", ""), font=font(REG, 34), fill=BODY)
    return img


def s_tekst(s, base, counter):
    img = Image.new("RGB", (W, H), GROUND); d = ImageDraw.Draw(img)
    header(d, 110, counter)
    y = 300
    if s.get("oznaka"):
        d.text((M, y), s["oznaka"], font=font(SEMI, 34), fill=ACCENT); y += 70
    y = block(d, s["naslov"], font(DISP, 88), y, WHITE, 14)
    if s.get("tekst"):
        y = block(d, s["tekst"], font(REG, 46), y + 44, BODY, 18)
    if s.get("stavke"):
        y += 40; fs = font(REG, 42)
        for t in s["stavke"]:
            d.ellipse([M, y + 17, M + 14, y + 31], fill=ACCENT)
            for j, ln in enumerate(wrap(d, t, fs, W - 2 * M - 36)):
                d.text((M + 36, y), ln, font=fs, fill=BODY); y += 54
            y += 18
    if s.get("poziv"):
        d.rounded_rectangle([M, 1000, W - M, 1160], radius=24, fill=RAISED, outline=ACCENT, width=4)
        d.text((M + 44, 1050), s["poziv"], font=font(SEMI, 42), fill=WHITE)
        d.text((M + 44, 1104), s.get("poziv2", ""), font=font(REG, 36), fill=BODY)
    bar(d, H - 120)
    return img


def s_dan_noc(s, base, counter):
    img = Image.new("RGB", (W, H), GROUND); d = ImageDraw.Draw(img)
    header(d, 100, counter)
    pw, ph = W - 2 * M, 466
    day = crop(open_photo(base, s["foto_dan"]), pw, ph)
    night = crop(open_photo(base, s["foto_noc"]), pw, ph)
    if s.get("noc_obrada", True):
        g = ImageOps.grayscale(night)
        g = ImageEnhance.Contrast(ImageEnhance.Brightness(g).enhance(0.62)).enhance(1.35)
        noise = Image.effect_noise((pw, ph), 18).filter(ImageFilter.GaussianBlur(0.4))
        night = Image.blend(g, noise, 0.06).convert("RGB")
    img.paste(day, (M, 160)); d.rectangle([M, 160 + ph, W - M, 168 + ph], fill=ACCENT); img.paste(night, (M, 168 + ph))
    for lbl, yy, col in ((s.get("oznaka_dan", "DAN"), 160, ACCENT), (s.get("oznaka_noc", "NOĆ · IC"), 168 + ph, WHITE)):
        fl = font(SEMI, 26); tw = d.textlength(lbl, font=fl)
        d.rounded_rectangle([M + 20, yy + 20, M + 56 + tw, yy + 70], radius=10, fill=GROUND)
        d.text((M + 38, yy + 45), lbl, font=fl, fill=col, anchor="lm")
    y = 168 + 2 * ph + 40
    d.text((M, y), s["naslov"], font=font(DISP, 60), fill=WHITE)
    if s.get("tekst"):
        d.text((M, y + 76), s["tekst"], font=font(REG, 38), fill=BODY)
    bar(d, H - 40)
    return img


PANEL = (236, 241, 246)


def s_proizvod(s, base, counter):
    """Zvanična slika proizvoda na svijetlom panelu, ispod brend, model i do 3 karakteristike."""
    img = Image.new("RGB", (W, H), GROUND); d = ImageDraw.Draw(img)
    header(d, 100, counter)
    px0, py0, px1, py1 = M, 160, W - M, 760
    d.rounded_rectangle([px0, py0, px1, py1], radius=24, fill=PANEL)
    ph = Image.open(os.path.join(base, s["foto"])).convert("RGBA")
    maxw, maxh = px1 - px0 - 80, py1 - py0 - 80
    sc = min(maxw / ph.width, maxh / ph.height); ph = ph.resize((round(ph.width * sc), round(ph.height * sc)), Image.LANCZOS)
    img.paste(ph, (px0 + (px1 - px0 - ph.width) // 2, py0 + (py1 - py0 - ph.height) // 2), ph)
    y = py1 + 50
    d.text((M, y), s["oznaka"].upper(), font=font(SEMI, 32), fill=ACCENT); y += 56
    for ln in wrap(d, s["naslov"], font(DISP, 60), W - 2 * M):
        d.text((M, y), ln, font=font(DISP, 60), fill=WHITE); y += 70
    y += 14
    for t in s.get("stavke", [])[:3]:
        d.ellipse([M, y + 16, M + 12, y + 28], fill=ACCENT)
        d.text((M + 30, y), t, font=font(REG, 38), fill=BODY); y += 54
    bar(d, H - 40)
    return img


SABLONI = {"proizvod": s_proizvod, "naslovna": s_naslovna, "foto_traka": s_foto_traka, "foto_kutija": s_foto_kutija,
           "tekst": s_tekst, "dan_noc": s_dan_noc}


def main(path):
    base = os.path.dirname(os.path.abspath(path))
    with open(path, encoding="utf-8") as f:
        spec = json.load(f)
    slides = spec["slajdovi"]
    n = len(slides)
    for i, s in enumerate(slides, start=1):
        counter = f"{i}/{n}" if n > 1 else None
        img = SABLONI[s["sablon"]](s, base, counter)
        out = os.path.join(base, f"{i:02d}.png")
        img.save(out)
        print("snimljeno:", out)
    if spec.get("opis"):
        with open(os.path.join(base, "opis.txt"), "w", encoding="utf-8") as f:
            f.write(spec["opis"].strip() + "\n")
        print("snimljeno:", os.path.join(base, "opis.txt"))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__); sys.exit(1)
    main(sys.argv[1])
