import sys, os; sys.path.insert(0, '../../alati')
from animacija import *
from glas_tajming import uskladi
FT = '../../materijal/pf/'; GRID = grid_bg()
def s1(t, d):
    im = photo_bg(FT + 'AI_pf_excel_stol.jpg', t, d, 1.0, 1.25, 0.5, 0.5, dark=0.5)
    im = top_pill(im, t, 0.1, '10 minuta', 'za jednu ponudu?', y=230, size=96)
    return handle_bar(overlay_text(im, t, 1.0, 'Kopirate, prepravljate, sređujete', 'Svaka ponuda ručno iz Excela.', y=1440))
def s2(t, d):
    im = GRID.copy()
    im = big_center(im, t, 0.0, '8 ponuda × 10 min', size=96, y=560)
    n = int(80 * prog(t, 0.8, 1.6))
    im = big_center(im, t, 0.8, f'= {n} min', size=200, y=850, color=A)
    im = big_center(im, t, 2.0, 'svaki dan', size=60, y=1100, color=B, font='Inter-SemiBold.otf')
    im = big_center(im, t, 2.5, 'primjer računa', size=40, y=1220, color=(120, 140, 160), font='Inter-Regular.otf')
    return handle_bar(im)
def s3(t, d):
    im = GRID.copy()
    im = top_pill(im, t, 0.0, 'A može i ovako', 'ponuda za 10 sekundi', y=200, size=86)
    return handle_bar(steps(im, t, 0.6, ['Odaberete kupca', 'Odaberete artikle', 'PDF ponuda je gotova'], y0=600, every=1.6))
def s4(t, d):
    im = photo_bg(FT + 'AI_pf_excel_stol.jpg', t, d, 1.2, 1.3, 0.4, 0.6, dark=0.55)
    return handle_bar(overlay_text(im, t, 0.3, 'Bez novog programa', 'Radi iz tabela koje već koristite.', y=1400, label='AUTOMATIZACIJA'))
def s5(t, d):
    return end_card(t, 'Želite ovo za svoju firmu?', 'Pišite nam u poruke')
scenes = [(3.6, s1), (3.6, s2), (6.0, s3), (3.4, s4), (3.4, s5)]
sfx = [(0.2, 'whoosh'), (3.6, 'whoosh'), (4.4, 'tick'), (4.8, 'tick'), (5.2, 'tick'), (7.2, 'whoosh'), (7.8, 'pop'), (8.3, 'ping'), (9.4, 'pop'), (9.9, 'ping'), (11.0, 'pop'), (11.5, 'ping'), (13.2, 'whoosh'), (16.6, 'ping')]
scenes, sfx, voice = uskladi(scenes, sfx, '../../materijal/pf/glas/d21_d_')
if len(sys.argv) > 1:
    for i, (dur, fn) in enumerate(scenes): fn(dur * 0.8, dur).save(f'/tmp/k_d_{i}.jpg', quality=85)
else:
    render(scenes, 'video.mp4', sfx, voice=voice, seed='2026-11-21d')
