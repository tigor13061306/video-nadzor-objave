import sys, os; sys.path.insert(0, '../../alati')
from animacija import *
from glas_tajming import uskladi
FT = '../../materijal/pf/'; GRID = grid_bg(); GL = '../../materijal/pf/glas/2026-11-27_ai-zadatak_'
T = [l.strip() for l in open('glas.txt', encoding='utf-8') if l.strip()]
def s1(t, d):
    im = photo_bg(FT + 'AI_pf_openspace.jpg', t, d, 1.0, 1.2, 0.5, 0.55, dark=0.45)
    im = slam(im, t, 0.0, 'Izvještaj od AI-ja?', size=110, y=500)
    im = slam(im, t, 0.5, 'Opšte fraze.', size=120, y=680, color=RED)
    im = slam(im, t, 0.9, '3 pravila to mijenjaju', size=58, y=870, color=A, font='Inter-SemiBold.otf')
    return handle_bar(cflow(im, t, d, T[0], hl={'opšte', 'fraze.'}))
def s2(t, d):
    im = GRID.copy()
    im = slam(im, t, 0.0, '1  Uloga i čitalac', size=90, y=400, color=A)
    im = list_items(im, t, 0.3, ['„Ti si finansijski analitičar.“', '„Izvještaj čita uprava.“'], y0=600, gap=190, every=0.6, num=False)
    return handle_bar(cflow(im, t, d, T[1], y=1400, hl={'ulogu'}))
def s3(t, d):
    im = photo_bg(FT + 'AI_pf_finansije.jpg', t, d, 1.25, 1.45, 0.62, 0.62, dark=0.5)
    im = slam(im, t, 0.0, '2  Vaši podaci', size=100, y=560, color=A)
    im = slam(im, t, 0.4, '+ primjer dobrog izvještaja', size=56, y=730, font='Inter-SemiBold.otf')
    return handle_bar(cflow(im, t, d, T[2], hl={'podatke'}))
def s4(t, d):
    im = GRID.copy()
    im = slam(im, t, 0.0, '3  Tačan format', size=90, y=400, color=A)
    im = steps(im, t, 0.3, ['Najviše jedna strana', 'Tri ključna broja', 'Preporuka na kraju'], y0=580, every=0.55)
    return handle_bar(cflow(im, t, d, T[3], y=1440, hl={'format,'}))
def s5(t, d):
    im = GRID.copy()
    im = top_pill(im, t, 0.0, 'Isti alat', 'drugi rezultat', y=150, size=80)
    b = [(0.2, 'r', 'Ti si finansijski analitičar. Iz tabele napiši izvještaj za upravu: 1 strana, 3 broja, preporuka.'), (1.0, 'l', 'Izvještaj za upravu: prodaja, marža, naplata. Preporuka: ...')]
    im = phone(im, t, x0=140, y0=420, w=800, h=980, header='AI asistent', time='09:12', bubbles=b)
    return handle_bar(cflow(im, t, d, T[4], y=1600, hl={'upravi.'}))
def s6(t, d):
    return end_card(t, 'Koje pravilo već koristite?', 'Napišite u komentar')
scenes = [(2.2, s1), (2.0, s2), (2.0, s3), (2.4, s4), (2.6, s5), (2.0, s6)]
sfx = [(0.0, 'whoosh'), (0.5, 'alarm'), (2.2, 'pop'), (2.5, 'tick'), (3.1, 'tick'), (4.2, 'whoosh'), (6.2, 'pop'), (6.5, 'tick'), (7.05, 'tick'), (7.6, 'tick'), (8.6, 'pop'), (8.8, 'ping'), (9.6, 'ping'), (11.2, 'ping')]
scenes, sfx, voice = uskladi(scenes, sfx, GL, lead=0.1, pad=0.3)
if len(sys.argv) > 1:
    for i, (dur, fn) in enumerate(scenes):
        for j, u in enumerate((0.05, 0.6)): fn(dur * u, dur).save(f'{sys.argv[1]}/k_{i}{j}.jpg', quality=80)
else:
    render(scenes, 'video.mp4', sfx, voice=voice, seed='2026-11-27', xf=4)
