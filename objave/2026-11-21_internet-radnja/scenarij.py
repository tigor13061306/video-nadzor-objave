import sys, os; sys.path.insert(0, '../../alati')
from animacija import *
from glas_tajming import uskladi
FT = '../../materijal/pf/'; GRID = grid_bg()
def s1(t, d):
    im = photo_bg(FT + 'AI_pf_radnja_kasa.jpg', t, d, 1.0, 1.25, 0.5, 0.7, dark=0.5)
    im = top_pill(im, t, 0.1, 'SUBOTA 10:15', 'nestalo interneta u radnji', y=230, size=86)
    return handle_bar(overlay_text(im, t, 1.0, 'Kartice ne prolaze', 'A kasa ne šalje račune.', y=1440))
def s2(t, d):
    im = GRID.copy()
    m = int(30 * prog(t, 0.3, 1.8))
    im = big_center(im, t, 0.2, f'{m} min', size=230, y=760, color=RED)
    im = big_center(im, t, 1.2, 'dok neko ne primijeti i ne nazove', size=56, y=1000, color=B, font='Inter-SemiBold.otf')
    im = big_center(im, t, 1.8, 'primjer', size=40, y=1120, color=(120, 140, 160), font='Inter-Regular.otf')
    return handle_bar(im)
def s3(t, d):
    im = GRID.copy()
    im = top_pill(im, t, 0.0, 'Sa nadzorom', 'upozorenje za minut', y=200, size=90)
    notes = [(0.6, RED, 'Internet ne radi · 10:16', 'Radnja Centar'), (3.0, GRN, 'Internet radi · 10:24', 'Radnja Centar')]
    im = phone(im, t, x0=110, y0=540, w=860, h=1240, time='10:16', notes=notes)
    return handle_bar(tiles(im, t, 3.6, [('Internet', t >= 3.0), ('Ruter', True), ('Kasa 1', True), ('Terminal', True)], x0=150, y0=1200))
def s4(t, d):
    im = photo_bg(FT + 'AI_pf_radnja_kasa.jpg', t, d, 1.2, 1.3, 0.6, 0.4, dark=0.55)
    return handle_bar(overlay_text(im, t, 0.3, 'Jedan pregled za sve radnje', 'Kase, terminali i internet veze na jednom mjestu.', y=1360, label='NADZOR SISTEMA'))
def s5(t, d):
    return end_card(t, 'Želite ovo u svojoj firmi?', 'Pišite nam u poruke')
scenes = [(3.6, s1), (3.4, s2), (5.5, s3), (3.6, s4), (3.4, s5)]
sfx = [(0.2, 'alarm'), (1.2, 'alarm'), (3.6, 'whoosh'), (3.9, 'tick'), (4.4, 'tick'), (4.9, 'tick'), (7.0, 'whoosh'), (7.6, 'ping'), (10.0, 'ping'), (12.5, 'whoosh'), (16.1, 'ping')]
scenes, sfx, voice = uskladi(scenes, sfx, '../../materijal/pf/glas/d21_c_')
if len(sys.argv) > 1:
    for i, (dur, fn) in enumerate(scenes): fn(dur * 0.8, dur).save(f'/tmp/k_c_{i}.jpg', quality=85)
else:
    render(scenes, 'video.mp4', sfx, voice=voice, seed='2026-11-21c')
