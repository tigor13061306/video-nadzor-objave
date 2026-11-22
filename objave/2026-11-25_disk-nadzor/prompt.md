# PROMPT: Reel „Disk: 100 %. Server stao.“ (@pametnija.firma, 25.11.2026, nadzor sistema)

## OBAVEZNA PRAVILA (važe za cijeli video)
1. Na ekranu se pojavljuje SAMO tekst naveden u ovom promptu, DOSLOVNO: isto slovo, isti razmak, isti znak interpunkcije, ista velika i mala slova.
2. NE dodaji nikakav drugi tekst: bez naslova, natpisa, logotipa, vodenih žigova, brojeva, datuma, emojija i hashtagova. U AI video kadru nema nikakvog čitljivog teksta.
3. Ne prevodi, ne skraćuj, ne ispravljaj i ne „poboljšavaj“ tekst. Jezik je bosanski, ijekavica.
4. Ako neki element ne možeš napraviti tačno kako piše, izostavi ga. Ne izmišljaj zamjenu.
5. Bez ljudi, lica, ruku, tablica ni brendova. Ime i logotip bilo kog alata za nadzor (Zabbix i slični) se NE pojavljuju u videu; prikaz samo podsjeća na takav alat (lista problema, ozbiljnost u boji, PROBLEM / RIJEŠENO, graf sa pragom).
6. Video model (Gemini Omni) pravi SAMO pozadinski kadar bez teksta. Sav tekst, titlove, glas i muziku dodaje naš alat (alati/animacija.py).

## TEHNIČKI PODACI
- Format: vertikalno 1080 x 1920 px, 30 fps, trajanje 26,5 s.
- Boje: pozadina #0E1A2B, tirkizna #22C3E6, crvena #EB5757, zelena #4CC978, narandžasta (Visoko) #F08232, plava (Info) #508CDC, bijela #FFFFFF, svijetlo siva #C5D0DC.
- Font: Inter (naslovi Inter Display Bold, ostalo Inter SemiBold ili Regular).
- Prelaz između scena: pretapanje 0,13 s (4 frejma).
- Stalni element u scenama 1 do 5: gore lijevo (x 90, y 140) tirkizni kružić i „@pametnija.firma“, 36 px.
- Mreža (scene 2 do 5): tamna pozadina sa mrežom kvadrata 60 px (linije #16283C).

## VIDEO KADAR (Gemini Omni)
Model gemini-omni-1.2-flash, Interactions API, response_format: type "video", aspect_ratio "9:16", duration "4s", resolution "720p". Cijena oko 0,28 $.
Prompt doslovno:
"Vertical 9:16 cinematic shot, slow smooth dolly forward along a narrow aisle of a modern corporate server room, rows of black server racks with small blue and green status lights, cool dim lighting, raised floor tiles, cables neatly organized; at the end of the aisle one server shows a single blinking red warning light that slowly becomes the focus, shallow depth of field, realistic, premium, calm tension. No people, no faces, no hands, no text, no letters, no numbers, no logos, no brand names, no watermark, no screens with readable content. Quiet server fan hum only."
Fajl: materijal/pf/video/omni_serverska_disk.mp4. Zvuk iz kadra se NE koristi.

## GLAS
- Gemini TTS gemini-3.8-flash-tts, glas "algieba", stil A (pravila/mediji.md, doslovno):
"Confident, authoritative senior business consultant presenting to a company's management board. Calm, measured pace, firm and clear, assured emphasis on key words. Standard Bosnian literary pronunciation, ijekavica, Bosnian accent. Pronounce every word fully and exactly as written, every syllable, no colloquial shortening or swallowed vowels (say 'koliko', never 'kolko'). Human and natural, not a radio ad, not robotic."
- Obrada: silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=stop_periods=-1:stop_duration=0.28:stop_threshold=-42dB,atempo=1.1
- Glas počinje 0,1 s poslije početka svoje scene.

## TITL (scene 1 do 5)
Bijeli tekst Inter Display Bold 64 px, centriran, na crnoj zaobljenoj traci (67 %), centar na y 1560. [tirkizno] = tirkizna riječ. Titl se pojavi odmah i zamijeni ga sljedeći.

---

## SCENA 1 | 0,0 – 3,6 s
- Slika: VIDEO KADAR preko cijelog ekrana, razvučen na 3,6 s, zatamnjen 35 %.
- Tekst na ekranu:
  od 0,0 s, centrirano na y 520, crveno, 140 px, tamna podloga, ulazi smanjenjem 135 % → 100 % za 0,18 s: „Disk: 100 %“
  od 0,9 s, centrirano na y 700, bijelo, 100 px, isti ulazak: „Server stao.“
- Glas: „Disk se puni polako. A stane odjednom.“
- Titl:
  0,1 – 1,8 s: „Disk se puni polako.“
  1,8 – 3,3 s: „A stane [tirkizno]odjednom.“
- Zvuk: alarm na 0,0 s i na 0,9 s.

## SCENA 2 | 3,6 – 8,7 s
- Slika: mreža.
- Tekst na ekranu:
  od 3,6 s, centrirano na y 300, crveno, 110 px, bez podloge: „ERP ne radi“
  tri kartice sa crvenim okvirom (x 110 – 970), ulaze s lijeva svakih 0,5 s:
  od 4,0 s, y 500: „Fakture: ne mogu se izdati“
  od 4,5 s, y 670: „Magacin: nema otpreme“
  od 5,0 s, y 840: „Kasa: ne prima uplate“
- Glas: „Baza više ne može ništa upisati, i ERP staje usred radnog dana.“
- Titl:
  3,7 – 5,0 s: „Baza više ne može“
  5,0 – 6,1 s: „ništa upisati,“
  6,1 – 7,5 s: „i [tirkizno]ERP staje usred“
  7,5 – 8,4 s: „radnog dana.“
- Zvuk: whoosh na 3,6 s, alarm na 4,0 / 4,5 / 5,0 s.

## SCENA 3 | 8,7 – 13,7 s
- Slika: mreža.
- Tekst na ekranu:
  od 8,7 s, tamna podloga centrirana na y 150: „Nadzor sistema“ (bijelo, 84 px), ispod „svake minute, 0-24“ (tirkizno, 44 px)
  osam pločica sa zelenom tačkom i zelenim okvirom, dvije kolone (od x 110, od y 520, razmak redova 120 px), ulaze svakih 0,15 s od 9,0 s, redom:
  „ERP-SRV“, „SQL-01“, „FILE-SRV“, „MAIL“, „FW-01“, „SW-CORE“, „BACKUP“, „VPN“
- Glas: „Sistem za nadzor prati svaki server, disk i servis, svake minute.“
- Titl:
  8,8 – 10,4 s: „Sistem za nadzor prati“
  10,4 – 11,4 s: „svaki server,“
  11,4 – 12,5 s: „disk i servis,“
  12,5 – 13,4 s: „[tirkizno]svake [tirkizno]minute.“
- Zvuk: whoosh na 8,7 s, tick na 9,0 i 9,3 s.

## SCENA 4 | 13,7 – 18,7 s
- Slika: mreža.
- Graf (tamna kartica od x 80 do x 1020, od y 220 do y 830):
  naslov gore lijevo, bijelo, 38 px: „SQL-01: disk D:“
  osa lijevo, sivo, 26 px: „50“, „70“, „90“; ispod grafa, sivo, 28 px: „Popunjenost diska %“
  crvena isprekidana linija na 90, na sredini iznad nje crveno, 28 px: „prag 90 %“
  tirkizna linija se crta slijeva nadesno za 2,4 s (od 13,7 do 16,1 s), raste od 58 do 93; dio iznad 90 je crven; na kraju crveni krug koji pulsira.
- Tabela problema (od y 960, x 60 – 1020), od 16,1 s:
  zaglavlje, sivo, 30 px: „Vrijeme“, „Ozbiljnost“, „Server / problem“, „Status“
  red (od 16,2 s): „08:14“ | narandžasta oznaka „Visoko“ | tirkizno „SQL-01“, ispod bijelo „Disk D: popunjen više od 90 %“ | crveno „PROBLEM“
- Glas: „Na devedeset posto, IT dobije upozorenje. Danima prije zastoja.“
- Titl:
  13,8 – 15,3 s: „Na devedeset posto,“
  15,3 – 16,8 s: „IT dobije [tirkizno]upozorenje.“
  16,8 – 18,4 s: „Danima prije zastoja.“
- Zvuk: whoosh na 13,7 s, alarm na 16,1 s.

## SCENA 5 | 18,7 – 23,5 s
- Slika: mreža.
- Tekst na ekranu: od 18,7 s, centrirano na y 300, zeleno, 86 px, bez podloge: „Riješeno prije zastoja“
- Tabela problema (od y 470), od 18,9 s, tri reda:
  „08:14“ | „Visoko“ | „SQL-01“ / „Disk D: popunjen više od 90 %“ | „PROBLEM“ → od 20,1 s zelena oznaka „OK“ i zeleno „RIJEŠENO“
  „07:52“ | žuta „Upozorenje“ | „FILE-SRV“ / „Backup traje duže od 2 h“ | „PROBLEM“ → od 20,5 s „OK“ i „RIJEŠENO“
  „06:30“ | plava „Info“ | „FW-01“ / „Restart VPN servisa“ | „PROBLEM“ → od 20,9 s „OK“ i „RIJEŠENO“
- Glas: „Prostor se oslobodi, a problem dobije zeleni status: riješeno.“
- Titl:
  18,8 – 20,3 s: „Prostor se oslobodi,“
  20,3 – 21,9 s: „a problem dobije [tirkizno]zeleni“
  21,9 – 23,2 s: „status: [tirkizno]riješeno.“
- Zvuk: whoosh na 18,7 s, ping na 20,1 / 20,5 / 20,9 s.

## SCENA 6 (KRAJ) | 23,5 – 26,5 s
- Ravna tamna pozadina, bez mreže i bez oznake gore lijevo.
- Tirkizni krug 220 px (centar x 540, y 640) sa „PF“; ispod na y 820: „@pametnija.firma“
- od 23,8 s, y 1020, bijelo, 78 px: „Želite ovo u svojoj firmi?“
- od 24,1 s, y 1230, tirkizno, 48 px: „Pišite nam u poruke“
- Glas: „Želite ovo u svojoj firmi? Pišite nam u poruke.“
- Bez titla. Zvuk: ping na 23,8 s.

---

## MUZIKA I ZVUK
Mirna korporativna podloga (alati/muzika.py, sintetička), 55 %, ispod glasa 15 %. Efekti 60 %. Konačno oko −14 LUFS, AAC 160 kb/s.

## NASLOVNA SLIKA
Kadar iz 1. sekunde (scena 1 sa „Disk: 100 %“).

## OPIS OBJAVE (doslovno)
Disk se puni polako. A stane odjednom.

Kad se disk na serveru napuni, baza ne može ništa upisati i ERP staje usred radnog dana: nema faktura, nema otpreme. Sistem za nadzor prati svaki server, disk i servis svake minute i na 90 % šalje upozorenje IT-u, danima prije zastoja.

Želite ovo u svojoj firmi? Pišite nam u poruke.

Fotografije i glas su napravljeni AI alatom. Uvodni video kadar je takođe napravljen AI alatom.

#nadzorsistema #zabbix #digitalizacija #bih #it

## ALT TEKST (doslovno)
Animirani video: prolaz kroz server salu sa crvenim svjetlom upozorenja, zatim posljedice zastoja ERP-a, pregled servera sa zelenim statusom, graf popunjenosti diska koji prelazi prag od 90 % i lista problema u kojoj svi problemi dobiju status riješeno.
