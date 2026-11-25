# PROMPT: Reel 2026-11-27_ai-zadatak (@pametnija.firma)

Na ekranu SAMO doslovni tekst iz ovog prompta. Bez dodatnog teksta, logotipa i lica.

## Zajedničko (kao objave/2026-11-22_upiti-stanje-erp/prompt.md)
- 1080x1920, 30 fps, prelaz 4 frejma; boje #0E1A2B / #22C3E6 / crvena #EB5757 / bijela; font Inter; oznaka @pametnija.firma gore lijevo (scene 1-5).
- Glas: gemini-3.8-flash-tts, glas algieba, stil A iz pravila/mediji.md; po sceni jedna rečenica iz glas.txt -> materijal/pf/glas/2026-11-27_ai-zadatak_N.wav; obrada: rez tišine na početku/kraju, pa silenceremove=stop_periods=-1:stop_duration=0.28:stop_threshold=-42dB,atempo=1.1.
- Trajanje scene = max(plan, glas + 0.4 s) (uskladi lead=0.1, pad=0.3). Glas počinje 0.1 s poslije početka scene.
- Titl: cflow (2-4 riječi, bijelo na crnoj traci, označene riječi tirkizno).
- Udarni tekst (slam) ulazi u 0.0 s scene sa skalom 135 % -> 100 % za 0.18 s.
- Fotke: samo postojeće iz materijal/pf (bez novih generisanja za ovaj Reel).
- Cover: kadar iz 1. sekunde (scena 1, sav udarni tekst vidljiv).
- Muzika: alati/muzika.py (seed = datum), efekti iz animacija.sfx_sound.


## Scene

### Scena 1: Kuka (plan 2.2 s)
- Slika: AI_pf_openspace.jpg, zum 100->120 %, tamno 45 %
- Tekst: „Izvještaj od AI-ja?“ bijelo 110 px y500 (0.0 s); „Opšte fraze.“ crveno 120 px y680 (0.5 s); „3 pravila to mijenjaju“ tirkizno 58 px y870 (0.9 s)
- Glas: „Pitali ste AI za izvještaj. Dobili ste opšte fraze.“
- Zvuk: whoosh 0.0, alarm 0.5

### Scena 2: Pravilo 1 (2.0 s)
- Slika: mreža
- Tekst: „1  Uloga i čitalac“ tirkizno 90 px y400; kartice „„Ti si finansijski analitičar.““ i „„Izvještaj čita uprava.““ (od 0.3 s, razmak 0.6 s)
- Glas: „Tri pravila to mijenjaju. Prvo: recite mu ulogu i za koga piše.“
- Zvuk: pop, 2x tick

### Scena 3: Pravilo 2 (2.0 s)
- Slika: AI_pf_finansije.jpg, zum 125->145 % na laptop
- Tekst: „2  Vaši podaci“ tirkizno 100 px y560; „+ primjer dobrog izvještaja“ 56 px y730 (0.4 s)
- Glas: „Drugo: priložite svoje podatke i primjer dobrog izvještaja.“
- Zvuk: whoosh

### Scena 4: Pravilo 3 (2.4 s)
- Slika: mreža
- Tekst: „3  Tačan format“ tirkizno 90 px y400; koraci „Najviše jedna strana“, „Tri ključna broja“, „Preporuka na kraju“ (svakih 0.55 s, zelena kvačica)
- Glas: „Treće: odredite format, dužinu i šta mora biti na kraju.“
- Zvuk: pop + 3x tick

### Scena 5: Rezultat (2.6 s)
- Slika: mreža + telefon „AI asistent“ 09:12
- Tekst: gore „Isti alat“ / „drugi rezultat“; poruka desno: „Ti si finansijski analitičar. Iz tabele napiši izvještaj za upravu: 1 strana, 3 broja, preporuka.“; lijevo: „Izvještaj za upravu: prodaja, marža, naplata. Preporuka: ...“
- Glas: „Isti alat, isti podaci. Izvještaj koji možete poslati upravi.“
- Zvuk: pop, ping, ping

### Scena 6: Kraj (2.0 s)
- Slika: end_card
- Tekst: „Koje pravilo već koristite?“ / „Napišite u komentar“
- Glas: „Koje pravilo vi već koristite? Napišite u komentar.“
- Zvuk: ping


## Opis i alt
Doslovno iz opis_nacrt.txt (postaje opis.txt kad je video sa glasom gotov) i alt.txt.
