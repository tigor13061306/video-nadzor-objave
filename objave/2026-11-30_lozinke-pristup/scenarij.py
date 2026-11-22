import sys, os; sys.path.insert(0, '../../alati')
from animacija import *
from glas_tajming import uskladi
FT = '../../materijal/pf/'; GRID = grid_bg(); GL = '../../materijal/pf/glas/2026-11-30_lozinke-pristup_'
T = [l.strip() for l in open('glas.txt', encoding='utf-8') if l.strip()]
def s1(t, d):
    im = photo_bg(FT + 'AI_pf_finansije.jpg', t, d, 1.15, 1.35, 0.6, 0.6, dark=0.45)
    im = slam(im, t, 0.0, 'Lozinka za ERP:', size=110, y=480)
    im = slam(im, t, 0.5, 'ispod tastature.', size=110, y=650, color=RED)
    im = slam(im, t, 1.0, '3 koraka to rješavaju', size=58, y=830, color=A, font='Inter-SemiBold.otf')
    return handle_bar(cflow(im, t, d, T[0], hl={'tri', 'koraka'}))
def s2(t, d):
    im = GRID.copy()
    im = slam(im, t, 0.0, 'Rizik', size=120, y=400, color=RED, box=False)
    im = list_items(im, t, 0.2, ['Ko je vidi, ima pristup', 'U zapisu stoji vaše ime', 'Često ista i za mail'], y0=580, gap=170, every=0.4, num=False, colr=[RED, RED, RED])
    return handle_bar(cflow(im, t, d, T[1], y=1400, hl={'ime.'}))
def s3(t, d):
    im = photo_bg(FT + 'AI_pf_openspace.jpg', t, d, 1.2, 1.4, 0.4, 0.55, dark=0.5)
    im = slam(im, t, 0.0, '1  Menadžer lozinki', size=96, y=600, color=A)
    return handle_bar(cflow(im, t, d, T[2], hl={'menadžeru', 'lozinki,'}))
def s4(t, d):
    im = GRID.copy()
    im = top_pill(im, t, 0.0, '2  Prijava u dva koraka', 'ERP i mail', y=150, size=72)
    im = phone(im, t, x0=170, y0=430, w=740, h=880, time='08:41', notes=[(0.4, A, 'Potvrdite prijavu', 'ERP · novi uređaj · Odobri?')])
    return handle_bar(cflow(im, t, d, T[3], y=1500, hl={'dva', 'koraka'}))
def s5(t, d):
    im = GRID.copy()
    im = slam(im, t, 0.0, '3  Svako svoj nalog', size=90, y=400, color=A)
    im = steps(im, t, 0.3, ['Bez zajedničkih naloga', 'Odlazak = pristup ugašen'], y0=600, every=0.7)
    return handle_bar(cflow(im, t, d, T[4], y=1300, hl={'gasi.'}))
def s6(t, d):
    return end_card(t, 'Koliko zajedničkih naloga imate?', 'Napišite u komentar')
scenes = [(2.2, s1), (2.2, s2), (2.0, s3), (2.4, s4), (2.4, s5), (2.0, s6)]
sfx = [(0.0, 'whoosh'), (0.5, 'alarm'), (2.2, 'alarm'), (2.4, 'tick'), (2.8, 'tick'), (3.2, 'tick'), (4.4, 'whoosh'), (6.4, 'pop'), (6.8, 'ping'), (8.8, 'pop'), (9.6, 'tick'), (11.2, 'ping')]
scenes, sfx, voice = uskladi(scenes, sfx, GL, lead=0.1, pad=0.3)
if len(sys.argv) > 1:
    for i, (dur, fn) in enumerate(scenes):
        for j, u in enumerate((0.05, 0.6)): fn(dur * u, dur).save(f'{sys.argv[1]}/k_{i}{j}.jpg', quality=80)
else:
    render(scenes, 'video.mp4', sfx, voice=voice, seed='2026-11-30', xf=4)
