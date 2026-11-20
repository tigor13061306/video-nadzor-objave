import sys; sys.path.insert(0, '../../alati')
from animacija import *
import os
FT = '../../materijal/pf/'
GRID = grid_bg()

def s1(t, d):
    im = photo_bg(FT + 'AI_pf_kancelarija_server.jpg', t, d, 1.0, 1.35, 0.75, 0.2, dark=0.45)
    im = top_pill(im, t, 0.1, 'PETAK 17:00', 'svi su otišli kući', y=230, size=90)
    im = overlay_text(im, t, 1.0, 'Server je stao', 'Crvena lampica. Niko je ne vidi.', y=1440)
    return handle_bar(im)

def s2(t, d):
    im = GRID.copy()
    dani = ['SUBOTA', 'NEDJELJA']
    i = 0 if t < d / 2 else 1
    h = int((t * 9) % 24)
    im = big_center(im, 0.6, 0, dani[i], size=70, y=640, color=A, font='Inter-SemiBold.otf')
    im = big_center(im, 0.6, 0, f'{h:02d}:00', size=230, y=860)
    im = big_center(im, t, 0.4, 'Niko ne zna da sistem ne radi.', size=56, y=1160, color=B, font='Inter-SemiBold.otf')
    return handle_bar(im)

def s3(t, d):
    im = photo_bg(FT + 'AI_pf_kancelarija_jutro.jpg', t, d, 1.1, 1.3, 0.55, 0.85, dark=0.4)
    im = top_pill(im, t, 0.1, 'PONEDJELJAK 08:00', None, y=230, size=80)
    im = overlay_text(im, t, 0.7, 'Saznali ste od kupca', 'Dva dana bez sistema, a da niko nije znao.', y=1440)
    return handle_bar(im)

def s4(t, d):
    im = GRID.copy()
    im = top_pill(im, t, 0.0, 'Sa nadzorom', 'isti petak, 17:02', y=200, size=90)
    notes = [(0.6, RED, 'Upozorenje · 17:02', 'Server ne odgovara'), (2.8, GRN, 'Riješeno · 17:25', 'Server ponovo radi')]
    im = phone(im, t, x0=110, y0=540, w=860, h=1240, time='17:02', notes=notes)
    ok = t >= 2.8
    im = tiles(im, t, 3.4, [('Server', ok), ('Internet', True), ('Kasa 1', True), ('Kasa 2', True), ('Disk', True), ('UPS', True)], x0=150, y0=1200)
    return handle_bar(im)

def s5(t, d):
    im = photo_bg(FT + 'AI_pf_kancelarija_server.jpg', t, d, 1.15, 1.25, 0.7, 0.25, dark=0.55)
    im = overlay_text(im, t, 0.2, 'Upozorenje za par minuta, ne za dva dana', 'Server, internet, kase, disk i UPS, sve na jednom mjestu.', y=1300, label='NADZOR SISTEMA')
    return handle_bar(im)

def s6(t, d):
    return end_card(t, 'Želite nadzor u svojoj firmi?', 'Pišite nam u poruke')

scenes = [(3.4, s1), (2.8, s2), (3.2, s3), (5.0, s4), (3.4, s5), (3.2, s6)]
sfx = [(0.15, 'alarm'), (1.1, 'alarm'), (3.4, 'whoosh'), (3.8, 'tick'), (4.4, 'tick'), (5.0, 'tick'), (5.6, 'tick'),
       (6.2, 'ring'), (7.4, 'ring'), (9.4, 'whoosh'), (10.0, 'ping'), (12.2, 'ping'), (14.4, 'whoosh'), (17.8, 'ping')]
GL = '../../materijal/pf/glas/'
voice = []; t0 = 0.0; new = []
for i, (dur, fn) in enumerate(scenes):
    vp = GL + 'v25_%d.wav' % (i + 1)
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
if len(sys.argv) > 1:
    for (i, tt) in [(0, 2.0), (1, 2.0), (2, 2.0), (3, 4.0), (4, 2.0), (5, 2.0)]:
        scenes[i][1](tt, scenes[i][0]).save(f'/tmp/k25_{i}.jpg', quality=85)
else:
    render(scenes, 'video.mp4', sfx, voice=voice, seed='2026-11-25')
