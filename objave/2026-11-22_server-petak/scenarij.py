import sys, os; sys.path.insert(0, '../../alati')
from animacija import *
from glas_tajming import uskladi
FT = '../../materijal/pf/'; GRID = grid_bg()
def s1(t, d):
    im = photo_bg(FT + 'AI_pf_serverska.jpg', t, d, 1.0, 1.22, 0.5, 0.5, dark=0.35)
    im = slam(im, t, 0.0, 'PETAK 17:05', size=150, y=560, color=RED)
    return handle_bar(cflow(im, t, d, 'Petak popodne. Server je stao.', hl={'stao.'}))
def s2(t, d):
    im = GRID.copy(); n = int(63 * prog(t, 0.1, 2.2))
    im = slam(im, t, 0.0, f'{n} sati', size=190, y=620, color=RED, box=False)
    im = big_center(im, t, 0.4, 'bez sistema, a niko ne zna', size=58, y=820, color=WH, font='Inter-SemiBold.otf')
    im = list_items(im, t, 0.6, ['Petak 17:05', 'Subota', 'Nedjelja', 'Ponedjeljak 8:00'], y0=960, gap=140, every=0.35, num=False, colr=[RED, (120, 130, 145), (120, 130, 145), A])
    return handle_bar(cflow(im, t, d, 'Niko ne zna sve do ponedjeljka ujutro. Šezdeset i tri sata bez sistema.', y=1640))
def s3(t, d):
    im = photo_bg(FT + 'AI_pf_openspace.jpg', t, d, 1.0, 1.18, 0.5, 0.5, dark=0.45)
    im = slam(im, t, 0.0, 'Ponedjeljak 8:00', size=110, y=600)
    return handle_bar(cflow(im, t, d, 'Prvi kolega stigne na posao, i tek tada počinje panika.', hl={'panika.'}))
def s4(t, d):
    im = GRID.copy()
    im = top_pill(im, t, 0.0, 'Sa nadzorom', 'znate za minut', y=150, size=84)
    im = line_chart(im, t, 0.1, 'ERP server: rad', crash_at=0.62, y0=520, h=380, dur=1.4)
    im = phone(im, t, x0=170, y0=1040, w=740, h=520, time='17:06', notes=[(1.3, RED, 'ERP server ne odgovara', 'Petak 17:06 · poslano dežurnom')])
    return handle_bar(cflow(im, t, d, 'Uz nadzor sistema, poruka stiže za jedan minut. Vi znate prvi.', y=1680, hl={'minut.'}))
def s5(t, d):
    im = GRID.copy()
    im = slam(im, t, 0.0, 'Sve na jednom ekranu', size=96, y=430)
    im = tiles(im, t, 0.3, [('Serveri', True), ('Diskovi', True), ('Mreža', True), ('Backup', True), ('Internet', True), ('Štampači', True)], x0=110, y0=640, w=860)
    return handle_bar(cflow(im, t, d, 'Serveri, diskovi, mreža i backup, sve na jednom ekranu.', y=1500))
def s6(t, d):
    return end_card(t, 'Želite ovo u svojoj firmi?', 'Pišite nam u poruke')
scenes = [(1.8, s1), (2.6, s2), (1.8, s3), (3.0, s4), (2.2, s5), (2.0, s6)]
sfx = [(0.0, 'alarm'), (1.8, 'whoosh'), (2.4, 'tick'), (2.75, 'tick'), (3.1, 'tick'), (3.45, 'tick'), (4.4, 'whoosh'), (6.2, 'whoosh'), (7.5, 'alarm'), (9.2, 'pop'), (9.5, 'ping'), (11.4, 'ping')]
scenes, sfx, voice = uskladi(scenes, sfx, '../../materijal/pf/glas/d25_', lead=0.1, pad=0.3)
if len(sys.argv) > 1:
    for i, (dur, fn) in enumerate(scenes):
        for j, u in enumerate((0.05, 0.6)): fn(dur * u, dur).save(f'/tmp/k25_{i}{j}.jpg', quality=80)
else:
    render(scenes, 'video.mp4', sfx, voice=voice, seed='2026-11-25', xf=4)
