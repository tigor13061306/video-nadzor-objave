import sys, os; sys.path.insert(0, '../../alati')
from animacija import *
from glas_tajming import uskladi
FT = '../../materijal/pf/'; GRID = grid_bg()
def s1(t, d):
    im = photo_bg(FT + 'AI_pf_finansije.jpg', t, d, 1.0, 1.2, 0.5, 0.55, dark=0.45)
    im = slam(im, t, 0.0, 'Faktura je prava.', size=110, y=520)
    im = slam(im, t, 1.2, 'Broj računa nije.', size=110, y=700, color=RED)
    return handle_bar(cflow(im, t, d, 'Faktura je prava. Broj računa nije. Tri provjere to sprečavaju.', hl={'tri', 'provjere'}))
def s2(t, d):
    im = GRID.copy()
    im = mail_card(im, t, 0.0, 'prodaja@firrna.ba', 'Obavještenje: promjena bankovnog računa', 'Poštovani, od danas uplate vršite na novi račun. Stari račun se gasi.', mark='novi račun', y0=360)
    return handle_bar(cflow(im, t, d, 'Stiže mail, kao od vašeg dobavljača: od danas uplate idu na novi račun.', y=1400))
def s3(t, d):
    im = GRID.copy()
    im = slam(im, t, 0.0, '1  Adresa pošiljaoca', size=84, y=420, color=A)
    im = big_center(im, t, 0.3, 'prodaja@firma.ba', size=78, y=760, color=GRN)
    im = big_center(im, t, 0.7, 'prodaja@firrna.ba', size=78, y=900, color=RED)
    im = big_center(im, t, 1.1, '„rn“ izgleda kao „m“', size=52, y=1040, color=B, font='Inter-SemiBold.otf')
    return handle_bar(cflow(im, t, d, 'Prvo: provjerite adresu pošiljaoca. Često je drugačije samo jedno slovo.', y=1400, hl={'slovo.'}))
def s4(t, d):
    im = photo_bg(FT + 'AI_pf_finansije.jpg', t, d, 1.35, 1.5, 0.7, 0.35, dark=0.55)
    im = slam(im, t, 0.0, '2  Pozovite telefonom', size=96, y=560, color=A)
    return handle_bar(cflow(im, t, d, 'Drugo: promjenu računa potvrdite telefonom, na broj koji već imate.', hl={'već', 'imate,'}))
def s5(t, d):
    im = GRID.copy()
    im = slam(im, t, 0.0, '3  Dva odobrenja', size=96, y=420, color=A)
    im = steps(im, t, 0.4, ['Unosi: finansije', 'Odobrava: direktor'], y0=640, every=0.7)
    return handle_bar(cflow(im, t, d, 'Treće: svaku promjenu računa odobravaju dvije osobe.', y=1300))
def s6(t, d):
    return end_card(t, 'Pošaljite ovo svom računovodstvu', 'Sačuvajte za kasnije')
scenes = [(2.2, s1), (2.6, s2), (2.4, s3), (2.0, s4), (2.2, s5), (2.0, s6)]
sfx = [(0.0, 'whoosh'), (0.9, 'alarm'), (2.2, 'ping'), (3.2, 'alarm'), (4.8, 'whoosh'), (5.5, 'tick'), (5.9, 'alarm'), (7.2, 'whoosh'), (9.2, 'whoosh'), (9.6, 'pop'), (10.3, 'pop'), (11.4, 'ping')]
scenes, sfx, voice = uskladi(scenes, sfx, '../../materijal/pf/glas/d27_', lead=0.1, pad=0.3)
if len(sys.argv) > 1:
    for i, (dur, fn) in enumerate(scenes):
        for j, u in enumerate((0.05, 0.6)): fn(dur * u, dur).save(f'/tmp/k27_{i}{j}.jpg', quality=80)
else:
    render(scenes, 'video.mp4', sfx, voice=voice, seed='2026-11-27', xf=4)
