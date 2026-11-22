# PROMPT: Reel „Disk: 100 %. Server stao.“ (@pametnija.firma, 25.11.2026, nadzor sistema)

## OBAVEZNA PRAVILA (važe za cijeli video)
1. Na ekranu se pojavljuje SAMO tekst naveden u ovom promptu, DOSLOVNO: isto slovo, isti razmak, isti znak interpunkcije, ista velika i mala slova.
2. NE dodaji nikakav drugi tekst: bez naslova, natpisa, logotipa, vodenih žigova, brojeva, datuma, emojija i hashtagova. U AI video kadru nema nikakvog čitljivog teksta.
3. Ne prevodi, ne skraćuj, ne ispravljaj i ne „poboljšavaj“ tekst. Jezik je bosanski, ijekavica.
4. Ako neki element ne možeš napraviti tačno kako piše, izostavi ga. Ne izmišljaj zamjenu.
5. Bez ljudi, lica, ruku, tablica ni brendova. Scene 4 i 5 su PRAVI snimci ekrana iz demo Zabbixa (izmišljeni serveri i podaci, oznaka „demo podaci“); logo i ime Zabbix nisu u kadru, u glasu se kaže „sistem za nadzor“.
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

## SCENA 4 | 13,7 – 18,7 s (PRAVI ZABBIX, demo podaci)
- Slika: mreža.
- 13,7 – 16,2 s:
  gore, tamna podloga centrirana na y 230: „SQL-01: disk D:“ (bijelo, 72 px), ispod „pravi sistem za nadzor, demo podaci“ (tirkizno, 44 px)
  okvir monitora (širina 1040 px, od y 560): PRAVI Zabbix graf materijal/pf/zabbix/zabbix_graf_disk.png (chart.php, 3 sata: disk raste polako od 57 % do 79 %, pa skoči na 93 % i poslije čišćenja padne na 61 %); preko grafa naša isprekidana crvena linija na 90 % i natpis „Okidač: disk > 90 %“ (tačno na Zabbix osi 90 %)
  kamera: od cijelog grafa (0,0 – 1316x546) zumira na desni dio (600,10 – 1316x307); od 14,9 s crveni okvir koji pulsira oko skoka preko 90 %
- 16,2 – 18,7 s:
  gore: „Upozorenje stiže odmah“ (bijelo, 72 px), ispod „lista problema, demo podaci“ (tirkizno, 44 px)
  okvir (širina 1040 px, od y 620): PRAVI Zabbix red iz liste problema, zbijen na kolone Severity | Status | Host | Problem: „High“ (narandžasto polje) | „PROBLEM“ (crveno) | „SQL-01“ | „Disk D: popunjen više od 90 %“; od 16,5 s crveni okvir oko reda
- Glas: „Na devedeset posto, IT dobije upozorenje. Danima prije zastoja.“
- Titl:
  13,8 – 15,3 s: „Na devedeset posto,“
  15,3 – 16,8 s: „IT dobije [tirkizno]upozorenje.“
  16,8 – 18,4 s: „Danima prije zastoja.“
- Zvuk: whoosh na 13,7 s, alarm na 16,2 s.

## SCENA 5 | 18,7 – 23,5 s (PRAVI ZABBIX, demo podaci)
- Slika: mreža.
- 18,7 – 20,7 s:
  gore: „Sve na jednom ekranu“ (bijelo, 72 px), ispod „serveri, kamere, UPS, backup“ (tirkizno, 44 px)
  okvir (širina 1040 px, od y 480): PRAVA Zabbix lista problema, zbijena na kolone Severity | Status | Host | Problem, 7 redova, svi „PROBLEM“ (crveno):
  Warning ERP-SRV „ERP sporo odgovara (više od 5 s)“; High FW-01 „VPN tunel Centrala–Magacin ne radi“; Warning BACKUP-SRV „Zadnji uspješan backup stariji od 24 h“; Disaster UPS Server sala „Nestanak struje: UPS radi na bateriji“; High Hladnjača 2 „Hladnjača 2: temperatura iznad +4 °C“; High NVR-Magacin „Snimač ne snima: disk 2 u grešci“; Average NVR-Magacin „Kamera Ulaz-2 nema slike“
- 20,7 – 23,5 s:
  gore, od 20,7 s, zeleno, 84 px, bez podloge, udari: „Riješeno prije zastoja“
  ista lista iz Zabbixa poslije rješavanja: svih 7 redova „RESOLVED“ (zeleno)
- Glas: „Prostor se oslobodi, a problem dobije zeleni status: riješeno.“
- Titl:
  18,8 – 20,3 s: „Prostor se oslobodi,“
  20,3 – 21,9 s: „a problem dobije [tirkizno]zeleni“
  21,9 – 23,2 s: „status: [tirkizno]riješeno.“
- Zvuk: whoosh na 18,7 s, ping na 20,7 / 21,1 / 21,5 s.

### Kako su nastali Zabbix snimci
Demo Zabbix 7 u Dockeru na Igorovom računaru (alati/zabbix_demo, kopija u C:\claude\video nadzor\Pametnija_firma\zabbix_demo): pokreni.bat podigne Zabbix i pokrene režiju (rezija.py), koja preko API-ja napravi izmišljene servere i okidače, upiše 3 sata istorije, odigra scenarij i napravi snimke ekrana (Playwright, 2560x1600); grafovi.bat napravi grafove iz istih podataka. Liste problema su zbijene na 4 kolone (Severity, Status, Host, Problem) da se čitaju na telefonu. Logo Zabbix nije u kadru. Svi serveri i podaci su izmišljeni.

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

U videu je pravi sistem za nadzor sa demo podacima (izmišljeni serveri).

Želite ovo u svojoj firmi? Pišite nam u poruke.

Fotografije i glas su napravljeni AI alatom. Uvodni video kadar je takođe napravljen AI alatom.

#nadzorsistema #zabbix #digitalizacija #bih #it

## ALT TEKST (doslovno)
Animirani video: prolaz kroz server salu sa crvenim svjetlom upozorenja, zatim posljedice zastoja ERP-a, pregled servera sa zelenim statusom, pravi graf popunjenosti diska iz sistema za nadzor koji prelazi prag od 90 % i prava lista problema u kojoj svi problemi dobiju status riješeno (demo podaci).
