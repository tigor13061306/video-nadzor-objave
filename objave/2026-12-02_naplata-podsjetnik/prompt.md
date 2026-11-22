# PROMPT: Reel 2026-12-02_naplata-podsjetnik (@pametnija.firma)

Na ekranu SAMO doslovni tekst iz ovog prompta. Bez dodatnog teksta, logotipa i lica.

## Zajedničko (kao objave/2026-11-22_upiti-stanje-erp/prompt.md)
- 1080x1920, 30 fps, prelaz 4 frejma; boje #0E1A2B / #22C3E6 / crvena #EB5757 / bijela; font Inter; oznaka @pametnija.firma gore lijevo (scene 1-5).
- Glas: gemini-3.8-flash-tts, glas algieba, stil A iz pravila/mediji.md; po sceni jedna rečenica iz glas.txt -> materijal/pf/glas/2026-12-02_naplata-podsjetnik_N.wav; obrada: rez tišine na početku/kraju, pa silenceremove=stop_periods=-1:stop_duration=0.28:stop_threshold=-42dB,atempo=1.1.
- Trajanje scene = max(plan, glas + 0.4 s) (uskladi lead=0.1, pad=0.3). Glas počinje 0.1 s poslije početka scene.
- Titl: cflow (2-4 riječi, bijelo na crnoj traci, označene riječi tirkizno).
- Udarni tekst (slam) ulazi u 0.0 s scene sa skalom 135 % -> 100 % za 0.18 s.
- Fotke: samo postojeće iz materijal/pf (bez novih generisanja za ovaj Reel).
- Cover: kadar iz 1. sekunde (scena 1, sav udarni tekst vidljiv).
- Muzika: alati/muzika.py (seed = datum), efekti iz animacija.sfx_sound.


## Scene

### Scena 1: Kuka (2.4 s)
- Slika: AI_pf_finansije.jpg, zum 100->120 %
- Tekst: „Dospjelo: 30 dana.“ bijelo 100 px y480 (0.0); „Niko nije podsjetio.“ crveno y650 (0.6); „A može samo od sebe“ tirkizno 58 px y830 (1.2)
- Glas: „Faktura je dospjela prije mjesec dana. Niko nije podsjetio kupca.“
- Zvuk: whoosh, alarm

### Scena 2: Posljedica (2.2 s)
- Slika: mreža
- Tekst: „Otvorene stavke“ 96 px; „primjer“ sivo 40 px; kartice „Faktura 1184 · 32 dana“, „Faktura 1201 · 18 dana“ (crveno), „Faktura 1215 · 9 dana“ (tirkizno)
- Glas: „Podsjećanje zavisi od nečijeg slobodnog vremena. A novac čeka.“
- Zvuk: pop + 3x tick

### Scena 3: Rješenje (1.8 s)
- Slika: AI_pf_openspace.jpg, zum 100->118 %
- Tekst: „Podaci su već u ERP-u“ 84 px y620
- Glas: „Sve što treba već piše u vašem ERP sistemu.“
- Zvuk: whoosh

### Scena 4: Pravila (2.4 s)
- Slika: mreža
- Tekst: „Vaša pravila“ tirkizno; koraci „+3 dana: ljubazan mail“, „+15 dana: drugi podsjetnik“, „+30 dana: komercijalista“
- Glas: „Sistem sam šalje podsjetnik, po pravilima koja vi odredite.“
- Zvuk: pop + 3x tick

### Scena 5: Dokaz (2.4 s)
- Slika: mreža + mail
- Tekst: Od: finansije@vasafirma.ba; predmet „Podsjetnik: faktura 1184 je dospjela“; tekst „Poštovani, u prilogu su faktura i pregled otvorenih stavki. Ako ste uplatu već izvršili, zanemarite ovu poruku.“
- Glas: „Ljubazno, tačno i na vrijeme. Vaš tim rješava samo izuzetke.“
- Zvuk: ping

### Scena 6: Kraj (2.0 s)
- Slika: end_card
- Tekst: „Želite ovo u svojoj firmi?“ / „Pišite nam u poruke“
- Glas: „Želite ovo u svojoj firmi? Pišite nam u poruke.“
- Zvuk: ping


## Opis i alt
Doslovno iz opis_nacrt.txt (postaje opis.txt kad je video sa glasom gotov) i alt.txt.
