"""Pravi Story 1080x1920 "Nova objava" od prve slike objave.

Upotreba:
    python napravi_story.py putanja/do/01.jpg putanja/do/story.jpg
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps

W, H = 1080, 1920
GROUND = (14, 26, 43); ACCENT = (34, 195, 230); WHITE = (255, 255, 255)
M = 96
FONTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


def main(src, out):
    img = Image.new("RGB", (W, H), GROUND); d = ImageDraw.Draw(img)
    post = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    pw = W - 2 * M; ph = round(post.height * pw / post.width)
    post = post.resize((pw, ph), Image.LANCZOS)
    d.text((M, 300), "NOVA OBJAVA", font=font("Inter-SemiBold.otf", 44), fill=ACCENT)
    y0 = 390
    d.rounded_rectangle([M - 8, y0 - 8, M + pw + 8, y0 + ph + 8], radius=20, fill=ACCENT)
    img.paste(post, (M, y0))
    y = y0 + ph + 80
    d.text((M, y), "Pogledaj cijelu objavu", font=font("InterDisplay-Bold.otf", 60), fill=WHITE)
    d.text((M, y + 82), "na profilu  →", font=font("InterDisplay-Bold.otf", 60), fill=ACCENT)
    img.save(out, quality=92)
    print("snimljeno:", out)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__); sys.exit(1)
    main(sys.argv[1], sys.argv[2])
