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
ZB = FT + 'zabbix/'
K0 = (0, 0, W0 := 1067, 132)          # jedan red: SQL-01 High PROBLEM
KT = (0, 0, 1072, 488)                # zbijena tabela: Severity, Status, Host, Problem (zaglavlje + 7 redova)
def s4(t, d):
    im = GRID.copy(); half = d * 0.5
    if t < half:   # pravi graf iz sistema za nadzor: disk se puni 3 sata, pa preko praga
        im = top_pill(im, t, 0.0, 'SQL-01: disk D:', 'pravi sistem za nadzor, demo podaci', y=230, size=72)
        im = screen_card(im, t, half, ZB + 'zabbix_graf_disk.png', (0, 0, 1316, 546), (600, 10, 1316, 307), y0=560, w=1040, mark=(1180, 70, 1250, 150), mark_from=half * 0.6)
    else:          # u listi problema se pojavi: SQL-01, High, PROBLEM
        tt = t - half
        im = top_pill(im, tt, 0.0, 'Upozorenje stiže odmah', 'lista problema, demo podaci', y=230, size=72)
        im = screen_card(im, tt, d - half, ZB + 'zabbix_03_problemi_00_kompakt.png', K0, K0, y0=620, w=1040, mark=(12, 66, W0 - 12, 128), mark_from=0.3)
    return handle_bar(cflow(im, t, d, GL[3], y=1560, hl={'upozorenje.'}))
def s5(t, d):
    im = GRID.copy(); half = d * 0.42
    if t < half:   # svi problemi crveni
        im = top_pill(im, t, 0.0, 'Sve na jednom ekranu', 'serveri, kamere, UPS, backup', y=230, size=72)
        im = screen_card(im, t, half, ZB + 'zabbix_03_problemi_07_kompakt.png', KT, KT, y0=480, w=1040)
    else:          # isti problemi: RESOLVED, zeleno
        tt = t - half
        im = slam(im, tt, 0.0, 'Riješeno prije zastoja', size=84, y=300, color=GRN, box=False)
        im = screen_card(im, tt, d - half, ZB + 'zabbix_05_rijeseno_04_kompakt.png', KT, KT, y0=480, w=1040)
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
