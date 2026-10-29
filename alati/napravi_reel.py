"""Pravi Reel 1080x1920 (MP4, H.264, 30 fps) od fotografija, u stilu profila.

Upotreba:
    python napravi_reel.py putanja/do/reel.json

reel.json (putanje do fotki relativne u odnosu na folder reel.json):
{
  "kadrovi": [
    {"foto": "../../02_materijal/odobreno/AI_x.jpg", "fokus": [0.5, 0.5],
     "tekst": "Kratak naslov kadra", "podtekst": "jedna rečenica ispod"},
    ...
  ],
  "trajanje_kadra": 3.5,
  "kraj": {"tekst": "Treba ti video nadzor?", "podtekst": "Piši u DM za ponudu"}
}
Izlaz: video.mp4 i cover.jpg u folderu reel.json.
"""
import json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageFont, ImageOps

W, H, FPS = 1080, 1920, 30
GROUND = (14, 26, 43); RAISED = (19, 36, 58); ACCENT = (34, 195, 230)
WHITE = (255, 255, 255); BODY = (197, 208, 220)
HANDLE = "@video.nadzorkamere"
M = 96
FONTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
FADE = 12  # broj frejmova prelaza


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


def wrap(d, text, f, maxw):
    out, cur = [], ""
    for w in text.split():
        c = (cur + " " + w).strip()
        if d.textlength(c, font=f) <= maxw:
            cur = c
        else:
            out.append(cur); cur = w
    return out + [cur] if cur else out


def lens(d, cx, cy, r):
    for k, c in ((1, ACCENT), (0.78, GROUND), (0.5, ACCENT), (0.2, GROUND)):
        d.ellipse([cx - r * k, cy - r * k, cx + r * k, cy + r * k], fill=c)


def cover_fill(im, w, h, fx, fy, zoom):
    sc = max(w / im.width, h / im.height) * zoom
    nw, nh = round(im.width * sc), round(im.height * sc)
    x = round((nw - w) * fx); y = round((nh - h) * fy)
    # izreži prvo u izvornoj rezoluciji pa smanji, brže je
    box = (x / sc, y / sc, (x + w) / sc, (y + h) / sc)
    return im.resize((w, h), Image.BILINEAR, box=box)


def overlay(k):
    """Providni sloj sa tekstom za jedan kadar (crta se jednom)."""
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    fT, fP = font("InterDisplay-Bold.otf", 64), font("Inter-Regular.otf", 40)
    tl = wrap(d, k.get("tekst", ""), fT, W - 2 * M - 80)
    pl = wrap(d, k.get("podtekst", ""), fP, W - 2 * M - 80) if k.get("podtekst") else []
    bh = 100 + len(tl) * 76 + (20 + len(pl) * 52 if pl else 0) + 40
    by1 = H - 330; by0 = by1 - bh
    d.rounded_rectangle([M - 40, by0, W - M + 40, by1], radius=28, fill=RAISED + (240,), outline=ACCENT, width=4)
    lens(d, M + 16, by0 + 54, 18)
    d.text((M + 50, by0 + 54), HANDLE, font=font("Inter-Medium.otf", 30), fill=BODY, anchor="lm")
    y = by0 + 100
    for ln in tl:
        d.text((M, y), ln, font=fT, fill=WHITE); y += 76
    y += 20
    for ln in pl:
        d.text((M, y), ln, font=fP, fill=BODY); y += 52
    return ov


def end_card(kraj):
    img = Image.new("RGB", (W, H), GROUND); d = ImageDraw.Draw(img)
    lens(d, W // 2, 640, 90)
    d.text((W // 2, 800), HANDLE, font=font("Inter-Medium.otf", 44), fill=BODY, anchor="mm")
    y = 960
    for ln in wrap(d, kraj.get("tekst", "Treba ti video nadzor?"), font("InterDisplay-Bold.otf", 76), W - 2 * M):
        d.text((W // 2, y), ln, font=font("InterDisplay-Bold.otf", 76), fill=WHITE, anchor="mm"); y += 90
    for ln in wrap(d, kraj.get("podtekst", "Piši u DM za ponudu"), font("Inter-Regular.otf", 42), W - 2 * M):
        d.text((W // 2, y + 20), ln, font=font("Inter-Regular.otf", 42), fill=ACCENT, anchor="mm"); y += 56
    d.rectangle([W // 2 - 60, y + 80, W // 2 + 60, y + 88], fill=ACCENT)
    return img


def main(path):
    base = os.path.dirname(os.path.abspath(path))
    spec = json.load(open(path, encoding="utf-8"))
    per = int(spec.get("trajanje_kadra", 3.5) * FPS)
    out = os.path.join(base, "video.mp4")
    total = len(spec["kadrovi"]) * per / FPS + 2.5
    if spec.get("muzika", True):
        import muzika
        wav = os.path.join(base, "muzika.wav")
        muzika.main(wav, total, os.path.basename(base))
        audio_in = ["-i", wav]
    else:
        audio_in = ["-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100"]
    cmd = ["ffmpeg", "-y", "-loglevel", "error",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-"] + audio_in + [
           "-shortest", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
           "-profile:v", "high", "-movflags", "+faststart", "-c:a", "aac", "-b:a", "128k", out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    prev_last = None
    for i, k in enumerate(spec["kadrovi"]):
        im = ImageOps.exif_transpose(Image.open(os.path.join(base, k["foto"]))).convert("RGB")
        fx, fy = k.get("fokus", [0.5, 0.5])
        ov = overlay(k)
        for f in range(per):
            z = 1.0 + 0.08 * f / per if i % 2 == 0 else 1.08 - 0.08 * f / per
            fr = cover_fill(im, W, H, fx, fy, z).convert("RGBA")
            fr.alpha_composite(ov); fr = fr.convert("RGB")
            if prev_last is not None and f < FADE:
                fr = Image.blend(prev_last, fr, (f + 1) / FADE)
            if i == 0 and f == per // 2:
                fr.save(os.path.join(base, "cover.jpg"), quality=92)
            p.stdin.write(fr.tobytes())
        prev_last = fr
    end = end_card(spec.get("kraj", {}))
    for f in range(int(2.5 * FPS)):
        fr = Image.blend(prev_last, end, (f + 1) / FADE) if f < FADE else end
        p.stdin.write(fr.tobytes())
    p.stdin.close(); p.wait()
    print("snimljeno:", out)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__); sys.exit(1)
    main(sys.argv[1])
