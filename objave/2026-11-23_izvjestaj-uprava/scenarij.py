import sys, os; sys.path.insert(0, '../../alati')
from animacija import *
from glas_tajming import uskladi
FT = '../../materijal/pf/'; GRID = grid_bg()
GL = ['Svake sedmice neko ručno slaže isti izvještaj za upravu.',
      'Izvoz iz sistema, kopiranje u Excel, grafikoni, pa mail.',
      'Jedna greška u kopiranju, i uprava odlučuje na pogrešnom broju.',
      'Automatski izvještaj sam uzima podatke direktno iz vašeg sistema.',
      'U ponedjeljak u sedam ujutro stiže svima kojima treba.']
def s1(t, d):
    im = video_bg(FT + 'video/omni_finansije_petak.mp4', t, d, dark=0.4)
    im = slam(im, t, 0.0, 'Izvještaj za upravu.', size=100, y=560)
    im = slam(im, t, 0.8, 'Opet ručno?', size=100, y=720, color=RED)
    return handle_bar(cflow(im, t, d, GL[0], hl={'ručno'}))
def s2(t, d):
    im = GRID.copy()
    im = slam(im, t, 0.0, 'Svake sedmice isto', size=84, y=260, box=False)
    im = list_items(im, t, 0.3, ['Izvoz iz ERP-a', 'Kopiranje u Excel', 'Grafikoni', 'Slanje mailom'], y0=440, gap=170, every=0.6)
    return handle_bar(cflow(im, t, d, GL[1]))
def s3(t, d):
    im = GRID.copy()
    im = slam(im, t, 0.0, 'Jedna greška u kopiranju', size=80, y=360, color=RED, box=False)
    im = big_center(im, t, 0.4, 'Tačno: 128.400 KM', size=68, y=620, color=GRN)
    im = big_center(im, t, 1.0, 'U izvještaju: 1.284.000 KM', size=64, y=760, color=RED)
    im = big_center(im, t, 1.4, 'primjer', size=40, y=880, color=B, font='Inter-Regular.otf')
    return handle_bar(cflow(im, t, d, GL[2], hl={'pogrešnom', 'broju.'}))
def s4(t, d):
    im = GRID.copy()
    im = slam(im, t, 0.0, 'Direktno iz sistema', size=96, y=380, color=A, box=False)
    im = tiles(im, t, 0.4, [('ERP', True), ('Naplata', True), ('Magacin', True), ('Prodaja', True)], x0=150, y0=620, w=780)
    im = big_center(im, t, 1.2, 'bez kopiranja, bez grešaka', size=56, y=980, color=WH, font='Inter-SemiBold.otf')
    return handle_bar(cflow(im, t, d, GL[3], hl={'automatski'}))
def s5(t, d):
    im = GRID.copy()
    im = slam(im, t, 0.0, 'Ponedjeljak 7:00', size=110, y=240)
    im = mail_card(im, t, 0.3, 'izvjestaji@firma.ba', 'Sedmični izvještaj: prodaja, naplata, zalihe', 'Izvještaj za prošlu sedmicu je u prilogu. Sve brojke su iz sistema, stanje u nedjelju u 23:59.', y0=420)
    return handle_bar(cflow(im, t, d, GL[4], y=1420, hl={'sedam'}))
def s6(t, d):
    return end_card(t, 'Želite ovo u svojoj firmi?', 'Pišite nam u poruke')
scenes = [(2.0, s1), (2.6, s2), (2.4, s3), (2.2, s4), (2.4, s5), (2.0, s6)]
sfx = [(0.0, 'whoosh'), (0.8, 'alarm'), (2.0, 'pop'), (2.3, 'tick'), (2.9, 'tick'), (3.5, 'tick'), (4.1, 'tick'), (4.6, 'alarm'), (5.6, 'alarm'), (7.0, 'whoosh'), (7.4, 'ping'), (9.2, 'whoosh'), (9.5, 'ping'), (11.6, 'ping')]
scenes, sfx, voice = uskladi(scenes, sfx, '../../materijal/pf/glas/d23i_', lead=0.1, pad=0.3)
if len(sys.argv) > 1:
    for i, (dur, fn) in enumerate(scenes):
        for j, u in enumerate((0.05, 0.6)): fn(dur * u, dur).save(f'/tmp/k23i_{i}{j}.jpg', quality=80)
else:
    render(scenes, 'video.mp4', sfx, voice=voice, seed='2026-11-23i', xf=4)
