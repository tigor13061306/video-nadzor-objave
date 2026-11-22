import sys, os; sys.path.insert(0, '../../alati')
from animacija import *
from glas_tajming import uskladi
FT = '../../materijal/pf/'; GRID = grid_bg()
def s1(t, d):
    im = photo_bg(FT + 'AI_pf_prodaja.jpg', t, d, 1.0, 1.2, 0.5, 0.6, dark=0.45)
    im = slam(im, t, 0.0, '„Imate li na stanju?“', size=104, y=640)
    return handle_bar(cflow(im, t, d, 'Ovo pitanje vašu prodaju svaki dan košta sate.', hl={'sate'}))
def s2(t, d):
    im = GRID.copy(); n = int(47 * prog(t, 0.0, 1.8))
    im = slam(im, t, 0.0, f'{n} upita', size=150, y=430, color=RED, box=False)
    im = big_center(im, t, 0.3, 'jedan dan, primjer', size=40, y=560, color=B, font='Inter-Regular.otf')
    im = list_items(im, t, 0.2, ['Mail: stanje za šifru 10452?', 'Telefon: cijena za paletu?', 'Viber: imate li na stanju?'], y0=700, gap=170, every=0.35, num=False)
    return handle_bar(cflow(im, t, d, 'Isto pitanje, desetine puta dnevno. Mailom, telefonom, preko Vibera.', hl={'desetine'}))
def s3(t, d):
    im = photo_bg(FT + 'AI_pf_prodaja.jpg', t, d, 1.3, 1.45, 0.3, 0.4, dark=0.55)
    im = slam(im, t, 0.0, 'Odgovor već postoji', size=104, y=700)
    return handle_bar(cflow(im, t, d, 'A odgovor već postoji. U vašem ERP sistemu.', hl={'erp'}))
def s4(t, d):
    im = GRID.copy()
    im = top_pill(im, t, 0.0, 'Bot iz ERP-a', 'odgovara 0-24', y=150, size=80)
    b = [(0.2, 'l', 'Stanje za šifru 10452?'), (0.9, 'r', 'Na stanju: 120 kom. Isporuka sutra.'), (2.2, 'l', 'Odlično, šaljem narudžbu.')]
    im = phone(im, t, x0=140, y0=430, w=800, h=1020, header='Narudžbe', time='23:58', bubbles=b)
    return handle_bar(cflow(im, t, d, 'Bot čita stanje i cijenu iz sistema i odgovara partneru za nekoliko sekundi. I u ponoć.', y=1620, hl={'sekundi.', 'ponoć'}))
def s5(t, d):
    im = photo_bg(FT + 'AI_pf_magacin.jpg', t, d, 1.0, 1.2, 0.5, 0.5, dark=0.45)
    im = slam(im, t, 0.0, 'Prodaju. Ne prepisuju stanje.', size=96, y=640)
    return handle_bar(cflow(im, t, d, 'Vaši komercijalisti prodaju, umjesto da prepisuju stanje.', hl={'prodaju.'}))
def s6(t, d):
    return end_card(t, 'Želite ovo u svojoj firmi?', 'Pišite nam u poruke')
scenes = [(1.8, s1), (2.0, s2), (1.6, s3), (3.2, s4), (1.8, s5), (2.0, s6)]
sfx = [(0.0, 'whoosh'), (1.8, 'pop'), (2.0, 'tick'), (2.35, 'tick'), (2.7, 'tick'), (3.8, 'whoosh'), (5.4, 'pop'), (5.6, 'ping'), (6.3, 'ping'), (8.6, 'whoosh'), (10.4, 'ping')]
scenes, sfx, voice = uskladi(scenes, sfx, '../../materijal/pf/glas/d23_', lead=0.1, pad=0.3)
if len(sys.argv) > 1:
    for i, (dur, fn) in enumerate(scenes):
        for j, u in enumerate((0.05, 0.6)): fn(dur * u, dur).save(f'/tmp/k23_{i}{j}.jpg', quality=80)
else:
    render(scenes, 'video.mp4', sfx, voice=voice, seed='2026-11-23', xf=4)
