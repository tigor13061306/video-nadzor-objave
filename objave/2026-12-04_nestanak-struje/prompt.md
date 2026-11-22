# PROMPT: Reel 2026-12-04_nestanak-struje (@pametnija.firma)

Na ekranu SAMO doslovni tekst iz ovog prompta. Bez dodatnog teksta, logotipa i lica.

## Zajedničko (kao objave/2026-11-22_upiti-stanje-erp/prompt.md)
- 1080x1920, 30 fps, prelaz 4 frejma; boje #0E1A2B / #22C3E6 / crvena #EB5757 / bijela; font Inter; oznaka @pametnija.firma gore lijevo (scene 1-5).
- Glas: gemini-3.8-flash-tts, glas algieba, stil A iz pravila/mediji.md; po sceni jedna rečenica iz glas.txt -> materijal/pf/glas/2026-12-04_nestanak-struje_N.wav; obrada: rez tišine na početku/kraju, pa silenceremove=stop_periods=-1:stop_duration=0.28:stop_threshold=-42dB,atempo=1.1.
- Trajanje scene = max(plan, glas + 0.4 s) (uskladi lead=0.1, pad=0.3). Glas počinje 0.1 s poslije početka scene.
- Titl: cflow (2-4 riječi, bijelo na crnoj traci, označene riječi tirkizno).
- Udarni tekst (slam) ulazi u 0.0 s scene sa skalom 135 % -> 100 % za 0.18 s.
- Fotke: samo postojeće iz materijal/pf (bez novih generisanja za ovaj Reel).
- Cover: kadar iz 1. sekunde (scena 1, sav udarni tekst vidljiv).
- Muzika: alati/muzika.py (seed = datum), efekti iz animacija.sfx_sound.


## Scene

### Scena 1: Kuka (2.4 s)
- Slika: AI_pf_serverska.jpg, zum 100->122 %, tamno 40 %
- Tekst: „Nestala struja.“ crveno 120 px y480 (0.0); „Baterija: još 9 min“ bijelo 90 px y660 (0.4); „A u desetoj minuti?“ tirkizno 58 px y830 (1.2); „primjer“ sivo 40 px y960
- Glas: „Nestala je struja. Baterija drži server još devet minuta.“
- Zvuk: alarm, tick, whoosh

### Scena 2: Posljedica (2.2 s)
- Slika: mreža + graf „Server baze podataka“ koji padne na 55 %
- Tekst: „Rizik: oštećena baza“ crveno 90 px y1080 (1.2)
- Glas: „Šta se desi u desetoj? Baza podataka može ostati oštećena.“
- Zvuk: pop, alarm

### Scena 3: Korak 1 (1.8 s)
- Slika: AI_pf_serverska.jpg, zum 135->150 % na crveno svjetlo
- Tekst: „1  Uredno gašenje“ tirkizno 100 px y560
- Glas: „Prvo: uređaj za rezervno napajanje mora uredno ugasiti server.“
- Zvuk: whoosh

### Scena 4: Korak 2 (2.4 s)
- Slika: mreža + telefon 17:42
- Tekst: gore „2  Upozorenje“ / „na telefon, odmah“; obavještenja „Nestanak napajanja“ / „Server radi na bateriji“ (crveno) i „Gašenje počinje“ / „Baza zatvorena uredno“ (tirkizno)
- Glas: „Drugo: upozorenje na telefon čim server pređe na bateriju.“
- Zvuk: pop, alarm, ping

### Scena 5: Korak 3 (2.4 s)
- Slika: mreža
- Tekst: „3  Test 2x godišnje“; koraci „Isključite napajanje“, „Server se ugasio sam?“, „Upozorenje stiglo?“
- Glas: „Treće: to testirajte dva puta godišnje, prije nego što zatreba.“
- Zvuk: pop + 3x tick

### Scena 6: Kraj (2.0 s)
- Slika: end_card
- Tekst: „Kada ste zadnji put testirali?“ / „Napišite u komentar“
- Glas: „Kada ste zadnji put testirali gašenje? Napišite u komentar.“
- Zvuk: ping


## Opis i alt
Doslovno iz opis_nacrt.txt (postaje opis.txt kad je video sa glasom gotov) i alt.txt.
