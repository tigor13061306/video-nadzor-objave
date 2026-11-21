import sys, os; sys.path.insert(0, '../../alati')
from animacija import *
from glas_tajming import uskladi
FT = '../../materijal/pf/'; GRID = grid_bg()
def s1(t, d):
    im = photo_bg(FT + 'AI_pf_kancelarija_papiri.jpg', t, d, 1.0, 1.2, 0.5, 0.6, dark=0.5)
    im = top_pill(im, t, 0.1, 'AI u maloj firmi', 'ne za 10 godina, danas', y=230, size=84)
    im = overlay_text(im, t, 0.9, 'Šta AI već danas radi?', 'Pet poslova koje možete predati od sutra.', y=1440)
    return handle_bar(im)
def s2(t, d):
    im = GRID.copy()
    im = top_pill(im, t, 0.0, '5 poslova za AI', None, y=230, size=84)
    return handle_bar(list_items(im, t, 0.5, ['Odgovor na mail kupca', 'Ponuda iz vaših bilješki', 'Sažetak dugog ugovora', 'Tabela iz gomile računa', 'Objava za vašu stranicu'], y0=520, gap=170, every=1.1))
def s3(t, d):
    im = GRID.copy()
    im = top_pill(im, t, 0.0, 'Običnim jezikom', 'prva verzija za par sekundi', y=180, size=80)
    b = [(0.4, 'r', 'Sažmi ovaj ugovor u 3 tačke.')]
    if 1.2 <= t < 2.2: b.append((1.2, 'l', '...'))
    if t >= 2.2: b.append((2.2, 'l', '1. Traje 12 mjeseci. 2. Otkaz 30 dana unaprijed. 3. Plaćanje do 15. u mjesecu.'))
    if t >= 3.6: b.append((3.6, 'r', 'Hvala, provjeriću.'))
    return handle_bar(phone(im, t, x0=110, y0=520, w=860, h=1260, header='AI asistent', time='10:42', bubbles=b))
def s4(t, d):
    im = GRID.copy()
    im = top_pill(im, t, 0.0, 'Nikad u AI', 'ovo ostaje kod vas', y=230, size=90, color=RED)
    return handle_bar(tiles(im, t, 0.6, [('Lozinke', False), ('Kartice', False), ('Podaci kupaca', False), ('Ugovori', False)], x0=150, y0=640, w=780))
def s5(t, d):
    return end_card(t, 'Koji posao biste prvi dali AI-ju?', 'Napišite u komentar')
scenes = [(3.6, s1), (6.5, s2), (5.5, s3), (4.0, s4), (3.4, s5)]
sfx = [(0.2, 'whoosh'), (3.6, 'whoosh'), (4.1, 'pop'), (5.2, 'pop'), (6.3, 'pop'), (7.4, 'pop'), (8.5, 'pop'), (10.1, 'whoosh'), (10.5, 'pop'), (12.3, 'pop'), (13.7, 'pop'), (15.6, 'alarm'), (19.6, 'ping')]
scenes, sfx, voice = uskladi(scenes, sfx, '../../materijal/pf/glas/d21_a_')
if len(sys.argv) > 1:
    for i, (dur, fn) in enumerate(scenes): fn(dur * 0.8, dur).save(f'/tmp/k_a_{i}.jpg', quality=85)
else:
    render(scenes, 'video.mp4', sfx, voice=voice, seed='2026-11-21a')
