import sys, os; sys.path.insert(0, '../../alati')
from animacija import *
from glas_tajming import uskladi
FT = '../../materijal/pf/'; GRID = grid_bg(); GL = '../../materijal/pf/glas/2026-12-02_naplata-podsjetnik_'
T = [l.strip() for l in open('glas.txt', encoding='utf-8') if l.strip()]
def s1(t, d):
    im = photo_bg(FT + 'AI_pf_finansije.jpg', t, d, 1.0, 1.2, 0.5, 0.7, dark=0.45)
    im = slam(im, t, 0.0, 'Dospjelo: 30 dana.', size=100, y=480)
    im = slam(im, t, 0.6, 'Niko nije podsjetio.', size=100, y=650, color=RED)
    im = slam(im, t, 1.2, 'A može samo od sebe', size=58, y=830, color=A, font='Inter-SemiBold.otf')
    return handle_bar(cflow(im, t, d, T[0], hl={'niko'}))
def s2(t, d):
    im = GRID.copy()
    im = slam(im, t, 0.0, 'Otvorene stavke', size=96, y=380, color=WH, box=False)
    im = big_center(im, t, 0.2, 'primjer', size=40, y=480, color=B, font='Inter-Regular.otf')
    im = list_items(im, t, 0.2, ['Faktura 1184 · 32 dana', 'Faktura 1201 · 18 dana', 'Faktura 1215 · 9 dana'], y0=580, gap=170, every=0.35, num=False, colr=[RED, RED, A])
    return handle_bar(cflow(im, t, d, T[1], y=1400, hl={'novac'}))
def s3(t, d):
    im = photo_bg(FT + 'AI_pf_openspace.jpg', t, d, 1.0, 1.18, 0.6, 0.5, dark=0.5)
    im = slam(im, t, 0.0, 'Podaci su već u ERP-u', size=84, y=620)
    return handle_bar(cflow(im, t, d, T[2], hl={'erp'}))
def s4(t, d):
    im = GRID.copy()
    im = slam(im, t, 0.0, 'Vaša pravila', size=96, y=380, color=A)
    im = steps(im, t, 0.3, ['+3 dana: ljubazan mail', '+15 dana: drugi podsjetnik', '+30 dana: komercijalista'], y0=560, every=0.5)
    return handle_bar(cflow(im, t, d, T[3], y=1440, hl={'sam'}))
def s5(t, d):
    im = GRID.copy()
    im = mail_card(im, t, 0.0, 'finansije@vasafirma.ba', 'Podsjetnik: faktura 1184 je dospjela', 'Poštovani, u prilogu su faktura i pregled otvorenih stavki. Ako ste uplatu već izvršili, zanemarite ovu poruku.', y0=340)
    return handle_bar(cflow(im, t, d, T[4], y=1400, hl={'izuzetke.'}))
def s6(t, d):
    return end_card(t, 'Želite ovo u svojoj firmi?', 'Pišite nam u poruke')
scenes = [(2.4, s1), (2.2, s2), (1.8, s3), (2.4, s4), (2.4, s5), (2.0, s6)]
sfx = [(0.0, 'whoosh'), (0.6, 'alarm'), (2.4, 'pop'), (2.6, 'tick'), (2.95, 'tick'), (3.3, 'tick'), (4.6, 'whoosh'), (6.4, 'pop'), (6.7, 'tick'), (7.2, 'tick'), (7.7, 'tick'), (8.8, 'ping'), (11.2, 'ping')]
scenes, sfx, voice = uskladi(scenes, sfx, GL, lead=0.1, pad=0.3)
if len(sys.argv) > 1:
    for i, (dur, fn) in enumerate(scenes):
        for j, u in enumerate((0.05, 0.6)): fn(dur * u, dur).save(f'{sys.argv[1]}/k_{i}{j}.jpg', quality=80)
else:
    render(scenes, 'video.mp4', sfx, voice=voice, seed='2026-12-02', xf=4)
