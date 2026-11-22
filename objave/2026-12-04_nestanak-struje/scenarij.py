import sys, os; sys.path.insert(0, '../../alati')
from animacija import *
from glas_tajming import uskladi
FT = '../../materijal/pf/'; GRID = grid_bg(); GL = '../../materijal/pf/glas/2026-12-04_nestanak-struje_'
T = [l.strip() for l in open('glas.txt', encoding='utf-8') if l.strip()]
def s1(t, d):
    im = photo_bg(FT + 'AI_pf_serverska.jpg', t, d, 1.0, 1.22, 0.5, 0.55, dark=0.4)
    im = slam(im, t, 0.0, 'Nestala struja.', size=120, y=480, color=RED)
    im = slam(im, t, 0.4, 'Baterija: još 9 min', size=90, y=660)
    im = slam(im, t, 0.4, 'primjer', size=40, y=960, color=B, font='Inter-Regular.otf')
    im = slam(im, t, 1.2, 'A u desetoj minuti?', size=58, y=830, color=A, font='Inter-SemiBold.otf')
    return handle_bar(cflow(im, t, d, T[0], hl={'devet'}))
def s2(t, d):
    im = GRID.copy()
    im = line_chart(im, t, 0.0, 'Server baze podataka', crash_at=0.55, y0=480, h=420, dur=1.4)
    im = slam(im, t, 1.2, 'Rizik: oštećena baza', size=90, y=1080, color=RED)
    return handle_bar(cflow(im, t, d, T[1], y=1450, hl={'oštećena.'}))
def s3(t, d):
    im = photo_bg(FT + 'AI_pf_serverska.jpg', t, d, 1.35, 1.5, 0.65, 0.72, dark=0.45)
    im = slam(im, t, 0.0, '1  Uredno gašenje', size=100, y=560, color=A)
    return handle_bar(cflow(im, t, d, T[2], hl={'uredno'}))
def s4(t, d):
    im = GRID.copy()
    im = top_pill(im, t, 0.0, '2  Upozorenje', 'na telefon, odmah', y=150, size=80)
    im = phone(im, t, x0=170, y0=430, w=740, h=880, time='17:42', notes=[(0.3, RED, 'Nestanak napajanja', 'Server radi na bateriji'), (1.2, A, 'Gašenje počinje', 'Baza zatvorena uredno')])
    return handle_bar(cflow(im, t, d, T[3], y=1500, hl={'telefon'}))
def s5(t, d):
    im = GRID.copy()
    im = slam(im, t, 0.0, '3  Test 2x godišnje', size=90, y=400, color=A)
    im = steps(im, t, 0.3, ['Isključite napajanje', 'Server se ugasio sam?', 'Upozorenje stiglo?'], y0=580, every=0.5)
    return handle_bar(cflow(im, t, d, T[4], y=1440, hl={'zatreba.'}))
def s6(t, d):
    return end_card(t, 'Kada ste zadnji put testirali?', 'Napišite u komentar')
scenes = [(2.4, s1), (2.2, s2), (1.8, s3), (2.4, s4), (2.4, s5), (2.0, s6)]
sfx = [(0.0, 'alarm'), (0.4, 'tick'), (1.2, 'whoosh'), (2.4, 'pop'), (3.4, 'alarm'), (4.6, 'whoosh'), (6.4, 'pop'), (6.7, 'alarm'), (7.6, 'ping'), (8.8, 'pop'), (9.1, 'tick'), (9.6, 'tick'), (10.1, 'tick'), (11.2, 'ping')]
scenes, sfx, voice = uskladi(scenes, sfx, GL, lead=0.1, pad=0.3)
if len(sys.argv) > 1:
    for i, (dur, fn) in enumerate(scenes):
        for j, u in enumerate((0.05, 0.6)): fn(dur * u, dur).save(f'{sys.argv[1]}/k_{i}{j}.jpg', quality=80)
else:
    render(scenes, 'video.mp4', sfx, voice=voice, seed='2026-12-04', xf=4)
