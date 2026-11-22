# PROMPT: Reel „Imate li na stanju?“ (@pametnija.firma)

## OBAVEZNA PRAVILA (važe za cijeli video)
1. Na ekranu se pojavljuje SAMO tekst naveden u ovom promptu, DOSLOVNO: isto slovo, isti razmak, isti znak interpunkcije, ista velika i mala slova. Navodnici „ “ u tekstu su dio teksta.
2. NE dodaji nikakav drugi tekst: bez naslova, natpisa, logotipa, vodenih žigova, brojeva, datuma, emojija, hashtagova i tekstova na ekranima, papirima ili zidovima u fotografijama.
3. Ne prevodi, ne skraćuji, ne ispravljaj i ne „poboljšavaj“ tekst. Jezik je bosanski, ijekavica.
4. Ako neki element ne možeš napraviti tačno kako piše, izostavi ga. Ne izmišljaj zamjenu.
5. Na fotografijama nema prepoznatljivih lica, ljudi, tablica ni brendova.

## TEHNIČKI PODACI
- Format: vertikalno 1080 x 1920 px, 30 fps, trajanje tačno 26,5 s.
- Boje: pozadina tamno plava #0E1A2B, naglasak tirkizna #22C3E6, problem crvena #EB5757, tekst bijela #FFFFFF, sporedni tekst svijetlo siva #C5D0DC.
- Font: Inter (naslovi Inter Display Bold, ostalo Inter SemiBold ili Regular).
- Prelaz između scena: kratko pretapanje 0,13 s (4 frejma).
- Stalni element u svim scenama 1 do 5: gore lijevo (x 90, y 140) tirkizni kružić i bijeli tekst „@pametnija.firma“, veličina 36 px.

## FOTOGRAFIJE (napraviti prije videa)
Model: Gemini gemini-3.1-flash-image, format 9:16.

FOTKA A „prodaja“, prompt doslovno:
"Modern sales department open-space office: a clean desk in the foreground with a desk phone, a closed modern laptop and a smartphone lying face down, more desks and glass partitions softly blurred behind. Photorealistic vertical photo, looks like a real high-quality phone photo, natural light, modern European company in Bosnia and Herzegovina. Serious, professional, contemporary corporate look. No people, no faces, no readable text, no logos, no brand names, no license plates."
Obrada: zamutiti pozadinu između 34 % i 57 % visine slike, mekom maskom (zamućenje 9 px, ivica maske 40 px), kao plitka dubina polja.

FOTKA B „magacin“, prompt doslovno:
"Large modern distribution warehouse interior, tall pallet racks full of boxed goods, wide aisle, bright LED lighting, polished concrete floor, a forklift parked far in the background. Photorealistic vertical photo, looks like a real high-quality phone photo, natural light, modern European company in Bosnia and Herzegovina. Serious, professional, contemporary corporate look. No people, no faces, no readable text, no logos, no brand names, no license plates."

## GLAS
- Model: Gemini TTS gemini-3.8-flash-tts, glas "algieba".
- Stil, doslovno:
"Confident, authoritative senior business consultant presenting to a company's management board. Calm, measured pace, firm and clear, assured emphasis on key words. Standard Bosnian literary pronunciation, ijekavica, Bosnian accent. Pronounce every word fully and exactly as written, every syllable, no colloquial shortening or swallowed vowels (say 'koliko', never 'kolko'). Human and natural, not a radio ad, not robotic."
- Svaka rečenica je poseban snimak (tačan tekst je u scenama ispod).
- Obrada svakog snimka (ffmpeg, ovim redom):
  1) silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse
  2) silenceremove=stop_periods=-1:stop_duration=0.28:stop_threshold=-42dB,atempo=1.1
- Glas počinje 0,1 s poslije početka svoje scene.

## TITL (isti izgled u scenama 1 do 5)
Bijeli tekst Inter Display Bold 64 px, centriran, na crnoj zaobljenoj traci (providnost 67 %, zaobljenje 24 px). Centar trake na y 1560 (u sceni 4 na y 1620). Riječi označene kao [tirkizno] pišu se tirkiznom bojom, ostale bijelom. Svaki titl se pojavi odmah, bez animacije, i zamijeni ga sljedeći.

---

## SCENA 1 | 0,0 – 4,0 s
- Slika: FOTKA A preko cijelog ekrana, zatamnjena 45 % (jače pri dnu). Kamera: polagano zumiranje sa 100 % na 120 %, centar kadra na 50 % širine i 60 % visine.
- Tekst na ekranu, od 0,0 s, centriran na y 640: „Imate li na stanju?“
  (bijelo, Inter Display Bold 104 px, na tamnoj zaobljenoj podlozi #0E1A2B 85 %; ulazi tako što se za 0,18 s smanji sa 135 % na 100 %)
- Glas: „Ovo pitanje vašu prodaju svaki dan košta sate.“
- Titl:
  0,1 – 2,0 s: „Ovo pitanje vašu prodaju“
  2,0 – 3,7 s: „svaki dan košta [tirkizno]sate.“
- Zvuk: kratki „whoosh“ na 0,0 s.

## SCENA 2 | 4,0 – 9,5 s
- Slika: tamna pozadina #0E1A2B sa tankom mrežom kvadrata 60 px (linije #16283C). Bez fotografije.
- Tekst na ekranu:
  - Od 4,0 s, centrirano na y 430, crveno, Inter Display Bold 150 px, bez podloge: brojač koji za 1,8 s raste od „0 upita“ do „47 upita“ (cijeli brojevi).
  - Od 4,3 s, centrirano na y 560, svijetlo sivo, Inter Regular 40 px: „jedan dan, primjer“
  - Tri kartice (tamno plava #13243A, tirkizni okvir, bijeli tekst Inter SemiBold 50 px, širina od x 110 do x 970), ulaze s lijeva jedna za drugom:
    od 4,2 s, y 700: „Mail: stanje za šifru 10452?“
    od 4,55 s, y 870: „Telefon: cijena za paletu?“
    od 4,9 s, y 1040: „Viber: imate li na stanju?“
- Glas: „Isto pitanje, desetine puta dnevno. Mailom, telefonom, preko Vibera.“
- Titl:
  4,1 – 5,1 s: „Isto pitanje,“
  5,1 – 6,8 s: „[tirkizno]desetine puta dnevno.“
  6,8 – 7,4 s: „Mailom,“
  7,4 – 8,2 s: „telefonom,“
  8,2 – 9,2 s: „preko Vibera.“
- Zvuk: „pop“ na 4,0 s; tri tiha „ticka“ na 4,2 s, 4,55 s i 4,9 s.

## SCENA 3 | 9,5 – 13,2 s
- Slika: FOTKA A, drugi kadar: zumirano 130 % do 145 %, centar kadra na 30 % širine i 40 % visine, zatamnjeno 55 %.
- Tekst na ekranu, od 9,5 s, centriran na y 700: „Odgovor već postoji“
  (isti izgled i ulazak kao u sceni 1)
- Glas: „A odgovor već postoji. U vašem ERP sistemu.“
- Titl:
  9,6 – 11,3 s: „A odgovor već postoji.“
  11,3 – 12,9 s: „U vašem [tirkizno]ERP sistemu.“
- Zvuk: „whoosh“ na 9,5 s.

## SCENA 4 | 13,2 – 19,5 s
- Slika: ista tamna pozadina sa mrežom kao u sceni 2.
- Tekst na ekranu gore, od 13,2 s, tamna zaobljena podloga centrirana na y 150:
  „Bot iz ERP-a“ (bijelo, Inter Display Bold 80 px)
  ispod: „odgovara 0-24“ (tirkizno, Inter SemiBold 44 px)
- Telefon (crni, zaobljen, od x 140 do x 940, od y 430 do y 1450). Gore lijevo u telefonu sat „23:58“. Traka razgovora sa tirkiznim kružićem i naslovom „Narudžbe“.
  Poruke (sive = partner, lijevo; tirkizno-plave = bot, desno), svaka uđe za 0,3 s:
  od 13,4 s, lijevo: „Stanje za šifru 10452?“
  od 14,1 s, desno: „Na stanju: 120 kom. Isporuka sutra.“
  od 15,4 s, lijevo: „Odlično, šaljem narudžbu.“
- Glas: „Bot čita stanje i cijenu iz sistema i odgovara partneru za nekoliko sekundi. I u ponoć.“
- Titl (centar trake na y 1620):
  13,3 – 15,0 s: „Bot čita stanje i cijenu“
  15,0 – 16,5 s: „iz sistema i odgovara“
  16,5 – 18,5 s: „partneru za nekoliko [tirkizno]sekundi.“
  18,5 – 19,2 s: „I u [tirkizno]ponoć.“
- Zvuk: „pop“ na 13,4 s, „ping“ na 14,1 s i na 15,4 s.

## SCENA 5 | 19,5 – 23,1 s
- Slika: FOTKA B preko cijelog ekrana, zatamnjena 45 %, zumiranje sa 100 % na 120 %, centar kadra na sredini.
- Tekst na ekranu, od 19,5 s, centriran na y 640: „Prodaju. Ne prepisuju stanje.“
  (bijelo, Inter Display Bold 96 px, ista podloga i ulazak kao u sceni 1)
- Glas: „Vaši komercijalisti prodaju, umjesto da prepisuju stanje.“
- Titl:
  19,6 – 21,2 s: „Vaši komercijalisti [tirkizno]prodaju,“
  21,2 – 22,8 s: „umjesto da prepisuju stanje.“
- Zvuk: „whoosh“ na 19,5 s.

## SCENA 6 (KRAJ) | 23,1 – 26,5 s
- Slika: ravna tamna pozadina #0E1A2B, bez mreže, bez fotografije, bez oznake gore lijevo.
- Tirkizni krug prečnika 220 px, centar x 540, y 640, u njemu tamnoplavim slovima „PF“ (Inter Display Bold 120 px). Krug ulazi rastući sa 70 % na 100 % za 0,5 s.
- Ispod kruga, centrirano na y 820, svijetlo sivo, Inter Medium 44 px: „@pametnija.firma“
- Od 23,4 s, centrirano na y 1020, bijelo, Inter Display Bold 78 px: „Želite ovo u svojoj firmi?“
- Od 23,7 s, centrirano na y 1230, tirkizno, Inter SemiBold 48 px: „Pišite nam u poruke“
- Glas: „Želite ovo u svojoj firmi? Pišite nam u poruke.“
- Bez titla.
- Zvuk: „ping“ na 23,4 s.

---

## MUZIKA I ZVUK
- Mirna korporativna instrumentalna podloga, oko 105 bpm, bez vokala, autorska ili sa licencom za komercijalnu upotrebu.
- Muzika je na 55 % jačine. Dok glas govori, spušta se na 15 %.
- Efekti (whoosh, pop, tick, ping) su kratki, čisti i sintetički, na 60 % jačine.
- Konačna glasnoća: oko −13 LUFS. Zvuk AAC 160 kb/s.

## NASLOVNA SLIKA (COVER)
Kadar iz 1. sekunde videa (scena 1 sa tekstom „Imate li na stanju?“), 1080 x 1920.

## OPIS OBJAVE (doslovno)
„Imate li ovo na stanju?“ Isto pitanje, desetine puta dnevno: mailom, telefonom, preko Vibera.

Odgovor već postoji u vašem ERP sistemu. Bot čita stanje i cijenu iz sistema i odgovara partneru za nekoliko sekundi, i van radnog vremena. Partner vidi samo ono što vi dozvolite, a vaši komercijalisti imaju vremena za prodaju.

Želite ovo u svojoj firmi? Pišite nam u poruke.

Fotografije i glas su napravljeni AI alatom.

#automatizacija #digitalizacija #bih #erp #prodaja

## ALT TEKST (doslovno)
Animirani video: prodajna kancelarija, brojač upita koji raste, pa razgovor na telefonu u kojem bot iz ERP sistema odgovara partneru o stanju robe, i na kraju veliki magacin.
