# PROMPT: Reel 2026-11-30_lozinke-pristup (@pametnija.firma)

Na ekranu SAMO doslovni tekst iz ovog prompta. Bez dodatnog teksta, logotipa i lica.

## Zajedničko (kao objave/2026-11-22_upiti-stanje-erp/prompt.md)
- 1080x1920, 30 fps, prelaz 4 frejma; boje #0E1A2B / #22C3E6 / crvena #EB5757 / bijela; font Inter; oznaka @pametnija.firma gore lijevo (scene 1-5).
- Glas: gemini-3.8-flash-tts, glas algieba, stil A iz pravila/mediji.md; po sceni jedna rečenica iz glas.txt -> materijal/pf/glas/2026-11-30_lozinke-pristup_N.wav; obrada: rez tišine na početku/kraju, pa silenceremove=stop_periods=-1:stop_duration=0.28:stop_threshold=-42dB,atempo=1.1.
- Trajanje scene = max(plan, glas + 0.4 s) (uskladi lead=0.1, pad=0.3). Glas počinje 0.1 s poslije početka scene.
- Titl: cflow (2-4 riječi, bijelo na crnoj traci, označene riječi tirkizno).
- Udarni tekst (slam) ulazi u 0.0 s scene sa skalom 135 % -> 100 % za 0.18 s.
- Fotke: samo postojeće iz materijal/pf (bez novih generisanja za ovaj Reel).
- Cover: kadar iz 1. sekunde (scena 1, sav udarni tekst vidljiv).
- Muzika: alati/muzika.py (seed = datum), efekti iz animacija.sfx_sound.


## Scene

### Scena 1: Kuka (2.2 s)
- Slika: AI_pf_finansije.jpg, zum 115->135 % na tastaturu
- Tekst: „Lozinka za ERP:“ bijelo 110 px y480 (0.0); „ispod tastature.“ crveno y650 (0.5); „3 koraka to rješavaju“ tirkizno 58 px y830 (1.0)
- Glas: „Lozinka za ERP stoji ispod tastature. Tri koraka to rješavaju.“
- Zvuk: whoosh, alarm

### Scena 2: Rizik (2.2 s)
- Slika: mreža
- Tekst: „Rizik“ crveno 120 px; crvene kartice „Ko je vidi, ima pristup“, „U zapisu stoji vaše ime“, „Često ista i za mail“ (svakih 0.4 s)
- Glas: „Ko je vidi, ulazi u sistem. A u zapisu stoji vaše ime.“
- Zvuk: alarm + 3x tick

### Scena 3: Korak 1 (2.0 s)
- Slika: AI_pf_openspace.jpg, zum 120->140 %
- Tekst: „1  Menadžer lozinki“ tirkizno 96 px y600
- Glas: „Prvo: lozinke čuvajte u menadžeru lozinki, ne na papiru.“
- Zvuk: whoosh

### Scena 4: Korak 2 (2.4 s)
- Slika: mreža + telefon 08:41
- Tekst: gore „2  Prijava u dva koraka“ / „ERP i mail“; obavještenje „Potvrdite prijavu“ / „ERP · novi uređaj · Odobri?“ (0.4 s)
- Glas: „Drugo: uključite prijavu u dva koraka za ERP i mail.“
- Zvuk: pop, ping

### Scena 5: Korak 3 (2.4 s)
- Slika: mreža
- Tekst: „3  Svako svoj nalog“; koraci „Bez zajedničkih naloga“, „Odlazak = pristup ugašen“
- Glas: „Treće: svako svoj nalog, a pri odlasku pristup se gasi.“
- Zvuk: pop, tick

### Scena 6: Kraj (2.0 s)
- Slika: end_card
- Tekst: „Koliko zajedničkih naloga imate?“ / „Napišite u komentar“
- Glas: „Koliko zajedničkih naloga ima vaša firma? Napišite u komentar.“
- Zvuk: ping


## Opis i alt
Doslovno iz opis_nacrt.txt (postaje opis.txt kad je video sa glasom gotov) i alt.txt.
