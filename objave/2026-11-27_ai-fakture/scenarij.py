import sys, os; sys.path.insert(0, '../../alati')
from animacija import *
from glas_tajming import uskladi
FT = '../../materijal/pf/'; GRID = grid_bg(); GL = '../../materijal/pf/glas/2026-11-27_ai-fakture_'
T = [l.strip() for l in open('glas.txt', encoding='utf-8') if l.strip()]
def s1(t, d):
    im = photo_bg(FT + 'AI_pf_fakture_stol.jpg', t, d, 1.0, 1.2, 0.5, 0.6, dark=0.45)
    im = slam(im, t, 0.0, '100 ulaznih faktura.', size=100, y=480)
    im = slam(im, t, 0.5, 'Sve ručno.', size=120, y=660, color=RED)
    im = slam(im, t, 1.0, 'A može za minut', size=58, y=850, color=A, font='Inter-SemiBold.otf')
    im = big_center(im, t, 1.0, 'primjer', size=40, y=990, color=B, font='Inter-Regular.otf')
    return handle_bar(cflow(im, t, d, T[0], hl={'stotinu'}))
def s2(t, d):
    im = GRID.copy()
    im = slam(im, t, 0.0, 'Rizik', size=120, y=400, color=RED, box=False)
    im = list_items(im, t, 0.2, ['Pogrešna cifra', 'PDV ne štima', 'Zaključak mjeseca kasni'], y0=580, gap=170, every=0.4, num=False, colr=[RED, RED, RED])
    return handle_bar(cflow(im, t, d, T[1], y=1400, hl={'ručno.', 'PDV'}))
def s3(t, d):
    im = GRID.copy()
    im = slam(im, t, 0.0, 'AI pročita PDF', size=96, y=400, color=A)
    im = list_items(im, t, 0.3, ['Dobavljač', 'Broj i datum', 'Iznos i PDV'], y0=580, gap=170, every=0.4, num=False, colr=[A, A, A])
    return handle_bar(cflow(im, t, d, T[2], y=1400, hl={'PDF:'}))
def s4(t, d):
    im = photo_bg(FT + 'AI_pf_finansije.jpg', t, d, 1.15, 1.35, 0.6, 0.6, dark=0.5)
    im = slam(im, t, 0.0, 'Stavka spremna', size=100, y=560, color=A)
    im = slam(im, t, 0.4, 'u vašem ERP-u', size=84, y=720)
    return handle_bar(cflow(im, t, d, T[3], hl={'ERP'}))
def s5(t, d):
    im = GRID.copy()
    im = slam(im, t, 0.0, 'Kontrola ostaje vaša', size=84, y=380, color=A)
    im = steps(im, t, 0.3, ['AI pročita fakturu', 'Knjigovođa provjeri', 'Potvrda u ERP-u'], y0=560, every=0.5)
    return handle_bar(cflow(im, t, d, T[4], y=1440, hl={'provjeri', 'crveno.'}))
def s6(t, d):
    return end_card(t, 'Želite ovo u svojoj firmi?', 'Pišite nam u poruke')
scenes = [(2.4, s1), (2.2, s2), (2.2, s3), (1.8, s4), (2.4, s5), (2.0, s6)]
sfx = [(0.0, 'whoosh'), (0.5, 'alarm'), (2.4, 'pop'), (2.6, 'tick'), (3.0, 'tick'), (3.4, 'tick'), (4.6, 'whoosh'), (4.9, 'tick'), (5.3, 'tick'), (5.7, 'tick'), (6.8, 'whoosh'), (8.6, 'pop'), (8.9, 'tick'), (9.4, 'tick'), (9.9, 'tick'), (11.0, 'ping')]
scenes, sfx, voice = uskladi(scenes, sfx, GL, lead=0.1, pad=0.3)
if len(sys.argv) > 1:
    for i, (dur, fn) in enumerate(scenes):
        for j, u in enumerate((0.05, 0.6)): fn(dur * u, dur).save(f'{sys.argv[1]}/k_{i}{j}.jpg', quality=80)
else:
    render(scenes, 'video.mp4', sfx, voice=voice, seed='2026-11-27', xf=4)
