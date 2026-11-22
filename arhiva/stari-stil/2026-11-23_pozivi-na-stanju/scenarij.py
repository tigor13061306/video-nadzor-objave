import sys; sys.path.insert(0, '../../alati')
from animacija import *
import os
FT = '../../materijal/pf/'
GRID = grid_bg()

def s1(t, d):
    im = photo_bg(FT + 'AI_pf_prodavnica_telefon.jpg', t, d, 1.0, 1.3, 0.35, 0.85, dark=0.5)
    im = top_pill(im, t, 0.1, '„Imate li ovo', None, y=230, size=84)
    im = top_pill(im, t, 0.25, 'na stanju?“', None, y=370, size=84)
    im = overlay_text(im, t, 0.8, 'Isto pitanje, 30 puta dnevno', 'Telefonom, na Viberu, u radnji.', y=1440)
    return handle_bar(im)

def s2(t, d):
    im = GRID.copy()
    im = big_center(im, t, 0.0, '30 upita × 2 min', size=96, y=560)
    n = int(60 * prog(t, 0.8, 1.6))
    im = big_center(im, t, 0.8, f'= {n} min', size=200, y=860, color=A)
    im = big_center(im, t, 2.0, 'svaki dan, oko 20 sati mjesečno', size=56, y=1120, color=B, font='Inter-SemiBold.otf')
    im = big_center(im, t, 2.6, 'primjer računa', size=40, y=1260, color=(120, 140, 160), font='Inter-Regular.otf')
    return handle_bar(im)

def s3(t, d):
    im = GRID.copy()
    im = top_pill(im, t, 0.0, '22:14', 'radnja zatvorena', y=210)
    b = [(0.5, 'l', 'Imate li bijeli silikon 280 ml na stanju?')]
    if 1.3 <= t < 2.5: b.append((1.3, 'r', '...'))
    if t >= 2.5: b.append((2.5, 'r', 'Da, 14 komada u radnji. Sutra radimo od 8 do 16h.'))
    if t >= 4.0: b.append((4.0, 'l', 'Super, hvala! 👍'.replace(' 👍', '')))
    im = phone(im, t, x0=110, y0=520, w=860, h=1260, header='Gvožđara · asistent', time='22:14', bubbles=b)
    return handle_bar(im)

def s4(t, d):
    im = photo_bg(FT + 'AI_pf_prodavnica_noc.jpg', t, d, 1.05, 1.2, 0.5, 0.5, dark=0.45)
    im = overlay_text(im, t, 0.2, 'Bot odgovara za par sekundi', 'I kad radnja ne radi. Program koji koristite ostaje isti.', y=1340, label='VIBER BOT')
    return handle_bar(im)

def s5(t, d):
    return end_card(t, 'Želite ovo za svoju firmu?', 'Pišite nam u poruke')

scenes = [(3.4, s1), (3.8, s2), (5.6, s3), (3.6, s4), (3.2, s5)]
sfx = [(0.15, 'ring'), (1.4, 'ring'), (3.4, 'whoosh'), (4.2, 'tick'), (4.6, 'tick'), (5.0, 'tick'), (5.4, 'tick'),
       (7.2, 'whoosh'), (7.7, 'pop'), (9.7, 'pop'), (11.2, 'pop'), (12.8, 'whoosh'), (16.4, 'ping')]
GL = '../../materijal/pf/glas/'
voice = []; t0 = 0.0; new = []
for i, (dur, fn) in enumerate(scenes):
    vp = GL + 'v23_%d.wav' % (i + 1)
    if os.path.exists(vp):
        L = wav_len(vp); dur = max(dur, L + 0.7); voice.append((t0 + 0.25, vp))
    new.append((dur, fn)); t0 += dur
# zvučne efekte pomjeri srazmjerno novim početcima scena
old_starts = [sum(s[0] for s in scenes[:i]) for i in range(len(scenes))]
new_starts = [sum(s[0] for s in new[:i]) for i in range(len(new))]
def remap(tt):
    i = max(k for k in range(len(old_starts)) if old_starts[k] <= tt)
    return new_starts[i] + (tt - old_starts[i])
sfx = [(remap(tt), k) for (tt, k) in sfx]
scenes = new
if len(sys.argv) > 1:  # probni kadrovi
    for (i, tt) in [(0, 2.0), (1, 3.0), (2, 4.8), (3, 2.0), (4, 2.0)]:
        scenes[i][1](tt, scenes[i][0]).save(f'/tmp/k23_{i}.jpg', quality=85)
else:
    render(scenes, 'video.mp4', sfx, voice=voice, seed='2026-11-23')
