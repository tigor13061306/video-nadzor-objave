import sys, os; sys.path.insert(0, '../../alati')
from animacija import *
from glas_tajming import uskladi
FT = '../../materijal/pf/'; GRID = grid_bg()
GL = ['Disk se puni polako. A stane odjednom.',
      'Baza više ne može ništa upisati, i ERP staje usred radnog dana.',
      'Sistem za nadzor prati svaki server, disk i servis, svake minute.',
      'Na devedeset posto, IT dobije upozorenje. Danima prije zastoja.',
      'Prostor se oslobodi, a problem dobije zeleni status: riješeno.']
KADAR = FT + 'video/omni_serverska_disk.mp4'
def s1(t, d):
    im = video_bg(KADAR, t, d, dark=0.35) if os.path.exists(KADAR) else photo_bg(FT + 'AI_pf_serverska.jpg', t, d, 1.0, 1.22, 0.5, 0.5, dark=0.35)
    im = slam(im, t, 0.0, 'Disk: 100 %', size=140, y=520, color=RED)
    im = slam(im, t, 0.9, 'Server stao.', size=100, y=700)
    return handle_bar(cflow(im, t, d, GL[0], hl={'odjednom.'}))
def s2(t, d):
    im = GRID.copy()
    im = slam(im, t, 0.0, 'ERP ne radi', size=110, y=300, color=RED, box=False)
    im = list_items(im, t, 0.4, ['Fakture: ne mogu se izdati', 'Magacin: nema otpreme', 'Kasa: ne prima uplate'], y0=500, gap=170, every=0.5, num=False, colr=[RED, RED, RED])
    return handle_bar(cflow(im, t, d, GL[1], hl={'ERP'}))
def s3(t, d):
    im = GRID.copy()
    im = top_pill(im, t, 0.0, 'Nadzor sistema', 'svake minute, 0-24', y=150, size=84)
    im = tiles(im, t, 0.3, [('ERP-SRV', True), ('SQL-01', True), ('FILE-SRV', True), ('MAIL', True), ('FW-01', True), ('SW-CORE', True), ('BACKUP', True), ('VPN', True)], x0=110, y0=520, w=860)
    return handle_bar(cflow(im, t, d, GL[2], hl={'svake', 'minute.'}))
def s4(t, d):
    im = GRID.copy()
    im = trend_chart(im, t, 0.0, 'SQL-01: disk D:', v0=58, v1=93, prag=90, dur=min(2.4, d * 0.55), y0=330, h=430)
    im = problem_table(im, t, min(2.4, d * 0.55), [(0.1, '08:14', 'visoko', 'SQL-01', 'Disk D: popunjen više od 90 %', None)], y0=960)
    return handle_bar(cflow(im, t, d, GL[3], y=1560, hl={'upozorenje.'}))
def s5(t, d):
    im = GRID.copy()
    im = slam(im, t, 0.0, 'Riješeno prije zastoja', size=86, y=300, color=GRN, box=False)
    im = problem_table(im, t, 0.2, [(0.0, '08:14', 'visoko', 'SQL-01', 'Disk D: popunjen više od 90 %', 1.2),
                                     (0.2, '07:52', 'upoz', 'FILE-SRV', 'Backup traje duže od 2 h', 1.6),
                                     (0.4, '06:30', 'info', 'FW-01', 'Restart VPN servisa', 2.0)], y0=470)
    return handle_bar(cflow(im, t, d, GL[4], y=1560, hl={'riješeno.', 'zeleni'}))
def s6(t, d):
    return end_card(t, 'Želite ovo u svojoj firmi?', 'Pišite nam u poruke')
scenes = [(2.0, s1), (2.4, s2), (2.4, s3), (3.0, s4), (2.6, s5), (2.0, s6)]
sfx = [(0.0, 'alarm'), (0.9, 'alarm'), (2.0, 'whoosh'), (2.4, 'alarm'), (2.9, 'alarm'), (3.4, 'alarm'), (4.4, 'whoosh'), (4.7, 'tick'), (5.0, 'tick'), (6.8, 'whoosh'), (8.6, 'alarm'), (9.8, 'whoosh'), (11.0, 'ping'), (11.4, 'ping'), (11.8, 'ping'), (12.4, 'ping')]
scenes, sfx, voice = uskladi(scenes, sfx, '../../materijal/pf/glas/d25d_', lead=0.1, pad=0.3)
if len(sys.argv) > 1:
    for i, (dur, fn) in enumerate(scenes):
        for j, u in enumerate((0.05, 0.75)): fn(dur * u, dur).save(f'/tmp/k25d_{i}{j}.jpg', quality=80)
else:
    render(scenes, 'video.mp4', sfx, voice=voice, seed='2026-11-25d', xf=4)
