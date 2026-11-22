# PROMPT: Reel „Izvještaj za upravu. Opet ručno?“ (@pametnija.firma, 23.11.2026)

## OBAVEZNA PRAVILA (važe za cijeli video)
1. Na ekranu se pojavljuje SAMO tekst naveden u ovom promptu, DOSLOVNO: isto slovo, isti razmak, isti znak interpunkcije, ista velika i mala slova.
2. NE dodaji nikakav drugi tekst: bez naslova, natpisa, logotipa, vodenih žigova, brojeva, datuma, emojija i hashtagova. U AI fotografijama i AI video kadrovima nema nikakvog čitljivog teksta.
3. Ne prevodi, ne skraćuj, ne ispravljaj i ne „poboljšavaj“ tekst. Jezik je bosanski, ijekavica.
4. Ako neki element ne možeš napraviti tačno kako piše, izostavi ga. Ne izmišljaj zamjenu.
5. Na fotografijama i u video kadrovima nema ljudi, lica, ruku, tablica ni brendova.
6. Video model (Gemini Omni) pravi SAMO pozadinski kadar bez teksta. Sav tekst, titlove, glas i muziku dodaje naš alat (alati/animacija.py).

## TEHNIČKI PODACI
- Format: vertikalno 1080 x 1920 px, 30 fps, trajanje 25,9 s.
- Boje: pozadina tamno plava #0E1A2B, naglasak tirkizna #22C3E6, problem crvena #EB5757, dobro zelena #4CC978, tekst bijela #FFFFFF, sporedni tekst svijetlo siva #C5D0DC.
- Font: Inter (naslovi Inter Display Bold, ostalo Inter SemiBold ili Regular).
- Prelaz između scena: pretapanje 0,13 s (4 frejma).
- Stalni element u scenama 1 do 5: gore lijevo (x 90, y 140) tirkizni kružić i bijeli tekst „@pametnija.firma“, 36 px.
- Mreža (scene 2 do 5): tamna pozadina #0E1A2B sa tankom mrežom kvadrata 60 px (linije #16283C).

## VIDEO KADAR (Gemini Omni, prije montaže)
Model: gemini-omni-1.2-flash, Interactions API, response_format: type "video", aspect_ratio "9:16", duration "4s", resolution "720p". Cijena oko 0,28 $.
Prompt doslovno:
"Vertical 9:16 cinematic shot, slow smooth dolly-in at eye level across a modern corporate finance office on a Friday late afternoon, warm low sun through large windows, empty desks with dark monitors, one desk in focus with a laptop showing an abstract soft blue glow and a neat stack of printed reports, dust particles floating in the light, shallow depth of field, realistic, calm, premium corporate look, modern European office in Bosnia and Herzegovina. No people, no faces, no hands, no text, no letters, no numbers, no logos, no watermark, no readable screen content. Silent ambient office sound only."
Fajl: materijal/pf/video/omni_finansije_petak.mp4. Zvuk iz kadra se NE koristi.

## GLAS
- Model: Gemini TTS gemini-3.8-flash-tts, glas "algieba", stil A (pravila/mediji.md, doslovno):
"Confident, authoritative senior business consultant presenting to a company's management board. Calm, measured pace, firm and clear, assured emphasis on key words. Standard Bosnian literary pronunciation, ijekavica, Bosnian accent. Pronounce every word fully and exactly as written, every syllable, no colloquial shortening or swallowed vowels (say 'koliko', never 'kolko'). Human and natural, not a radio ad, not robotic."
- Obrada svakog snimka: silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=stop_periods=-1:stop_duration=0.28:stop_threshold=-42dB,atempo=1.1
- Glas počinje 0,1 s poslije početka svoje scene.

## TITL (scene 1 do 5)
Bijeli tekst Inter Display Bold 64 px, centriran, na crnoj zaobljenoj traci (providnost 67 %). Centar trake na y 1560 (u sceni 5 na y 1420). Riječi označene [tirkizno] su tirkizne. Titl se pojavi odmah i zamijeni ga sljedeći.

---

## SCENA 1 | 0,0 – 4,1 s
- Slika: VIDEO KADAR preko cijelog ekrana (720x1280 povećan na 1080x1920), razvučen na 4,1 s, zatamnjen 40 % (jače pri dnu).
- Tekst na ekranu:
  od 0,0 s, centrirano na y 560, bijelo, 100 px, tamna podloga, ulazi smanjenjem 135 % → 100 % za 0,18 s: „Izvještaj za upravu.“
  od 0,8 s, centrirano na y 720, crveno, 100 px, isti ulazak: „Opet ručno?“
- Glas: „Svake sedmice neko ručno slaže isti izvještaj za upravu.“
- Titl:
  0,1 – 1,7 s: „Svake sedmice neko [tirkizno]ručno“
  1,7 – 3,8 s: „slaže isti izvještaj za upravu.“
- Zvuk: whoosh na 0,0 s, kratki alarm na 0,8 s.

## SCENA 2 | 4,1 – 8,6 s
- Slika: mreža.
- Tekst na ekranu:
  od 4,1 s, centrirano na y 260, bijelo, 84 px, bez podloge: „Svake sedmice isto“
  Četiri kartice sa brojem u tirkiznom krugu (širina x 110 – 970, tirkizni okvir), ulaze s lijeva svakih 0,6 s:
  od 4,4 s, y 440: „1“ „Izvoz iz ERP-a“
  od 5,0 s, y 610: „2“ „Kopiranje u Excel“
  od 5,6 s, y 780: „3“ „Grafikoni“
  od 6,2 s, y 950: „4“ „Slanje mailom“
- Glas: „Izvoz iz sistema, kopiranje u Excel, grafikoni, pa mail.“
- Titl:
  4,2 – 5,5 s: „Izvoz iz sistema,“
  5,5 – 6,9 s: „kopiranje u Excel,“
  6,9 – 7,7 s: „grafikoni,“
  7,7 – 8,3 s: „pa mail.“
- Zvuk: pop na 4,1 s, tick na 4,4 / 5,0 / 5,6 / 6,2 s.

## SCENA 3 | 8,6 – 13,3 s
- Slika: mreža.
- Tekst na ekranu:
  od 8,6 s, centrirano na y 360, crveno, 80 px, bez podloge: „Jedna greška u kopiranju“
  od 9,0 s, centrirano na y 620, zeleno, 68 px: „Tačno: 128.400 KM“
  od 9,6 s, centrirano na y 760, crveno, 64 px: „U izvještaju: 1.284.000 KM“
  od 10,0 s, centrirano na y 880, svijetlo sivo, 40 px: „primjer“
- Glas: „Jedna greška u kopiranju, i uprava odlučuje na pogrešnom broju.“
- Titl:
  8,7 – 10,4 s: „Jedna greška u kopiranju,“
  10,4 – 13,0 s: „i uprava odlučuje na [tirkizno]pogrešnom [tirkizno]broju.“
- Zvuk: alarm na 8,6 s i na 9,6 s.

## SCENA 4 | 13,3 – 19,0 s
- Slika: mreža.
- Tekst na ekranu:
  od 13,3 s, centrirano na y 380, tirkizno, 96 px, bez podloge: „Direktno iz sistema“
  četiri pločice sa zelenom tačkom (dvije kolone, od x 150, od y 620), ulaze svakih 0,15 s od 13,7 s: „ERP“, „Naplata“, „Magacin“, „Prodaja“
  od 14,5 s, centrirano na y 980, bijelo, 56 px: „bez kopiranja, bez grešaka“
- Glas: „Automatski izvještaj sam uzima podatke direktno iz vašeg sistema.“
- Titl:
  13,4 – 15,9 s: „[tirkizno]Automatski izvještaj sam uzima“
  15,9 – 18,7 s: „podatke direktno iz vašeg sistema.“
- Zvuk: whoosh na 13,3 s, ping na 13,7 s.

## SCENA 5 | 19,0 – 23,0 s
- Slika: mreža.
- Tekst na ekranu:
  od 19,0 s, centrirano na y 240, bijelo, 110 px, tamna podloga: „Ponedjeljak 7:00“
  od 19,3 s, mail (bijela kartica od x 90 do x 990, od y 420), ulazi odozdo:
    „Od:“ „izvjestaji@firma.ba“
    naslov: „Sedmični izvještaj: prodaja, naplata, zalihe“
    tekst: „Izvještaj za prošlu sedmicu je u prilogu. Sve brojke su iz sistema, stanje u nedjelju u 23:59.“
- Glas: „U ponedjeljak u sedam ujutro stiže svima kojima treba.“
- Titl (centar y 1420):
  19,1 – 20,5 s: „U ponedjeljak u [tirkizno]sedam“
  20,5 – 22,7 s: „ujutro stiže svima kojima treba.“
- Zvuk: whoosh na 19,0 s, ping na 19,3 s.

## SCENA 6 (KRAJ) | 23,0 – 25,9 s
- Slika: ravna tamna pozadina, bez mreže i bez oznake gore lijevo.
- Tirkizni krug 220 px (centar x 540, y 640) sa „PF“; ispod na y 820: „@pametnija.firma“
- od 23,3 s, y 1020, bijelo, 78 px: „Želite ovo u svojoj firmi?“
- od 23,6 s, y 1230, tirkizno, 48 px: „Pišite nam u poruke“
- Glas: „Želite ovo u svojoj firmi? Pišite nam u poruke.“
- Bez titla. Zvuk: ping na 23,3 s.

---

## MUZIKA I ZVUK
Mirna korporativna podloga oko 105 bpm (alati/muzika.py, sintetička), 55 %, ispod glasa 15 %. Efekti 60 %. Konačno oko −12 LUFS, AAC 160 kb/s.

## NASLOVNA SLIKA
Kadar iz 1. sekunde (scena 1 sa „Izvještaj za upravu.“).

## OPIS OBJAVE (doslovno)
Izvještaj za upravu. Svake sedmice opet ručno?

Izvoz iz sistema, kopiranje u Excel, grafikoni, pa mail. Jedna greška u kopiranju i uprava odlučuje na pogrešnom broju. Automatski izvještaj uzima podatke direktno iz vašeg sistema i u ponedjeljak u 7:00 stiže svima kojima treba.

Želite ovo u svojoj firmi? Pišite nam u poruke.

Fotografije i glas su napravljeni AI alatom. Uvodni video kadar je takođe napravljen AI alatom.

#automatizacija #digitalizacija #bih #izvjestaji #erp

## ALT TEKST (doslovno)
Animirani video: kamera prilazi stolu sa laptopom i izvještajima u kancelariji, pa četiri ručna koraka pravljenja izvještaja, primjer pogrešno prepisanog iznosa i mail sa automatskim sedmičnim izvještajem u ponedjeljak u 7:00.
