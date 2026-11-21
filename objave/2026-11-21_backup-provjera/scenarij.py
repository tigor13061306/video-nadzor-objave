import sys, os; sys.path.insert(0, '../../alati')
from animacija import *
from glas_tajming import uskladi
FT = '../../materijal/pf/'; GRID = grid_bg()
def s1(t, d):
    im = photo_bg(FT + 'AI_pf_backup_disk.jpg', t, d, 1.0, 1.25, 0.6, 0.6, dark=0.5)
    im = top_pill(im, t, 0.1, 'Imate backup?', 'a kad ste ga zadnji put probali?', y=230, size=90)
    return handle_bar(overlay_text(im, t, 1.0, 'Backup koji niko nije provjerio', 'Radi sve dok ne zatreba.', y=1440))
def s2(t, d):
    im = GRID.copy()
    im = big_center(im, t, 0.2, 'Kad zatreba:', size=80, y=520, color=B, font='Inter-SemiBold.otf')
    im = big_center(im, t, 1.0, 'disk prazan', size=120, y=720, color=RED)
    im = big_center(im, t, 2.2, 'ili kopija stara pola godine', size=64, y=930, color=WH, font='Inter-SemiBold.otf')
    return handle_bar(im)
def s3(t, d):
    im = GRID.copy()
    im = top_pill(im, t, 0.0, '3 pitanja za vašu firmu', None, y=230, size=76)
    return handle_bar(list_items(im, t, 0.6, ['Gdje je kopija? Van tog računara?', 'Koliko je stara? Pogledajte datum.', 'Jeste li iz nje vratili bar jedan fajl?'], y0=560, gap=230, every=2.2))
def s4(t, d):
    im = photo_bg(FT + 'AI_pf_backup_disk.jpg', t, d, 1.25, 1.35, 0.7, 0.7, dark=0.55)
    return handle_bar(overlay_text(im, t, 0.3, 'Jednom mjesečno vratite jedan fajl', 'Pet minuta, a znate da backup stvarno radi.', y=1360, label='SAVJET'))
def s5(t, d):
    return end_card(t, 'Kad ste zadnji put provjerili backup?', 'Napišite u komentar')
scenes = [(3.6, s1), (4.0, s2), (7.5, s3), (3.8, s4), (3.4, s5)]
sfx = [(0.2, 'whoosh'), (3.6, 'whoosh'), (4.6, 'alarm'), (7.6, 'whoosh'), (8.2, 'pop'), (10.4, 'pop'), (12.6, 'pop'), (15.1, 'whoosh'), (18.9, 'ping')]
scenes, sfx, voice = uskladi(scenes, sfx, '../../materijal/pf/glas/d21_b_')
if len(sys.argv) > 1:
    for i, (dur, fn) in enumerate(scenes): fn(dur * 0.8, dur).save(f'/tmp/k_b_{i}.jpg', quality=85)
else:
    render(scenes, 'video.mp4', sfx, voice=voice, seed='2026-11-21b')
