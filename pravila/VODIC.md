# Vodič: @pametnija.firma (od 20.11.2026)

Profil: Instagram @pametnija.firma i Facebook stranica "Pametnija firma" (isti nalozi kao bivši @video.nadzorkamere, preimenovani 20.11.2026; stare objave obrisane). Vlasnik: Igor. Plan i identitet: dokument "Pametnija firma: identitet i plan prve dvije sedmice" (claude.ai artefakt).

## Cilj i publika
- Publika (od 22.11.2026, Igorova odluka): ozbiljne firme koje imaju ozbiljne sisteme (ERP, serveri, više lokacija, magacin, finansije, mreža), bez obzira na broj zaposlenih: direktori, menadžeri, finansije, IT odgovorni. NE male radnje i "firmice". NIKAD ne spominjati broj zaposlenih ni veličinu firme (ne gađamo ničiji ego).
- Cilj: upiti firmi za automatizaciju (botovi, izvještaji, povezivanje programa), nadzor sistema (Zabbix, Grafana, upozorenje na telefon) i savjet za AI.

## Pravila sadržaja (Igorova)
1. NEMA čisto tekstualnih objava ni carousela od teksta. Svaka objava je animirani Reel: prave fotke (Gemini) ili snimak, animacija (alati/animacija.py), muzika, zvučni efekti i glas.
2. Glas: Gemini TTS, model gemini-3.8-flash-tts, glas "algieba" (Igor izabrao "glas B"), stil iz pravila/mediji.md. Glas se ne mijenja bez Igora.
3. Poziv na akciju:
   - objave koje nude uslugu firmama (automatizacija, nadzor, ponuda): "Pišite nam u poruke." NIKAD poziv na komentar ("napišite X u komentar");
   - opšte korisne objave (savjet za sve): poziv na komentar je u redu.
4. Obraćanje sa "vi". Korporativan, autoritativan ton: govorimo kao iskusan konsultant upravi firme. Kratko i konkretno, jezik posla (zastoj, trošak, rizik, proces, izvještaj, odgovornost), bez šala i bez "kafanskog" tona. Primjeri iz ozbiljnih firmi, ne iz male radnje.
5. Tvrdnje i brojke samo provjerene ili jasno označene kao "primjer računa". Bez cijena, izmišljenih rezultata i recenzija. AI fotke nikad kao Igorov urađeni posao.
6. U opisu svake objave: "Fotografije i glas su napravljeni AI alatom." i fajl ai.txt u folderu (objavi.py tada šalje i AI oznaku).
7. Najviše 5 hashtagova: #automatizacija #digitalizacija #bih + 1 do 2 tematska.
8. Bez lica, tablica, logotipa i brendova na fotkama. Nikad podaci, snimci ni ekrani iz Igorove službe.

## Izgled
Tamno plava #0E1A2B, tirkizna #22C3E6, bijeli tekst, font Inter (alati/fonts), znak "PF". Reel 1080x1920, 15 do 25 s. Fotke: moderne kancelarije, open space, sale za sastanke, server sale, proizvodne hale, magacini, ekrani sa grafovima. NE seoske kancelarije, stari namještaj ni male radnje.

## Raspored
3 Reela sedmično: ponedjeljak, srijeda, petak (objava od 17:43). Stubovi: automatizacija poslova, nadzor sistema, AI u poslu, sigurnost firme, studije slučaja (samo uz dozvolu klijenta, bez imena). Plan: pravila/plan_objava.csv. Priprema dvije sedmice unaprijed.

## Folder objave
objave/GGGG-MM-DD_tema/: video.mp4, cover.jpg (kadar iz prve 2-3 s, 1080x1920), opis.txt, alt.txt (jedna rečenica šta se vidi), ai.txt, scenarij.py (skripta po kojoj je video napravljen). Bez opis.txt GitHub neće objaviti.

## Zadržavanje pažnje (od 22.11.2026)
Prva 4 Reela (21.11.): prosječno gledanje 3,7 do 6,1 s od 26 do 38 s. Ljudi odlaze baš u trenutku kad se prvi put nešto promijeni (5-6 s), jer je prva scena mirna fotka sa dva okvira teksta. Zato:
1. Prva sekunda: pokret i jaka tvrdnja ili broj, ne pitanje tipa "imate li...?". Velik tekst (3-6 riječi) koji udari odmah u 0.0 s, glas počinje u 0.1 s, bez uvoda.
2. Promjena slike najmanje svakih 1.5-2 s (novi kadar, zum, tekst koji ulazi, grafikon, brojač). Nijedna scena duža od 3 s bez pokreta.
3. Prvih 3 s mora otvoriti "petlju": obećanje koje se ispuni tek na kraju (npr. "Treći razlog košta najviše").
4. Kraće: 15-25 s (najviše 28 s). Glas A je miran, zato poslije rezanja tišine: duge pauze unutar rečenice skrati (silenceremove stop_duration=0.28) i atempo=1.1. Tekst glasa: najviše 6 rečenica od 4 do 12 riječi.
7. Alati za brzi rez (alati/animacija.py): slam (tekst udari u 0.0 s), cflow (titl glasa po 2-4 riječi), line_chart, mail_card; uskladi(..., lead=0.1, pad=0.3); render(..., xf=4). Uzor: objave/2026-11-22_server-petak/scenarij.py.
5. Tekst na ekranu = ono što glas govori (titl u 2-4 riječi), jer većina gleda bez zvuka.
6. Bez kraja koji se razvlači: poziv i logo najviše 2 s.

## Nadzor sistema (Igorov zahtjev 22.11.2026)
Reelsi o nadzoru sistema vizuelno podsjećaju na Zabbix, ali ga ne potenciraju: lista problema (problem_table: vrijeme, ozbiljnost u boji Info/Upozorenje/Visoko/Kritično, server, opis, PROBLEM → RIJEŠENO), graf sa isprekidanim pragom (trend_chart), pregled servera sa zelenim/crvenim statusom (tiles). U videu se NE pojavljuju ime ni logotip Zabbix; u glasu i opisu se kaže "sistem za nadzor". U hashtagu smije #zabbix. Uzor: objave/2026-11-25_disk-nadzor.

## Pravljenje Reela
0. Prvo napiši prompt.md u folder objave, po uzoru na objave/2026-11-22_upiti-stanje-erp/prompt.md: za svaku scenu tačno vrijeme, slika, DOSLOVAN tekst na ekranu (pozicija, veličina, boja, kad ulazi), doslovna rečenica glasa, titlovi sa vremenima i zvuk. Ništa se ne izmišlja u toku pravljenja: scenarij.py radi tačno ono što piše u prompt.md.
1. Scenarij: 4 do 6 scena (problem, posljedica, rješenje, rezultat, kraj). Po sceni jedna kratka rečenica glasa i kratak tekst na ekranu.
2. Fotke: Gemini po pravila/mediji.md, u materijal/pf/ (ime AI_pf_...). Pogledaj svaku prije upotrebe.
3. Glas: po sceni jedan wav u materijal/pf/glas/<folder>_N.wav, odreži tišinu (ffmpeg silenceremove).
4. scenarij.py po uzoru na objave/2026-11-23_pozivi-na-stanju/scenarij.py: funkcije scena iz alati/animacija.py (photo_bg, top_pill, overlay_text, phone, tiles, big_center, end_card, grid_bg), trajanje scene = max(plan, glas + 0.7 s), render(..., voice=...).
5. Pogledaj kadrove (bar 4) prije objave: tekst ne smije izlaziti iz okvira ni prekrivati bitan dio.

## Objavljivanje (GitHub Actions)
- .github/workflows/objava.yml od 17:43 objavi dospjele foldere na Instagram (Reel + Story "Nova objava") i Facebook stranicu, upiše stanje/objavljeno.json. Ručno pokretanje: promijeni stanje/pokreni.txt.
- kljuc.yml obnavlja Instagram ključ 1. i 15. u mjesecu; provjera.yml ponedjeljkom provjerava ključeve.
- Komentari: alati/komentari.py, upiti -> GitHub issue (mail Igoru).

## Zakazani zadaci
- "Instagram – kontrolor" (oblak, 17:45): objava izašla? spremne objave ispravne? zaliha.
- "Instagram – nedjeljna priprema" (računar, nedjelja 18:32): fotke + glas preko Gemini-ja, Reelsi za dvije sedmice, na GitHub.
- "Instagram – dnevna objava i zajednica" (računar, 18:21): komentari, poruke (samo navede), Facebook grupe za preduzetnike.

## Posebne objave van rasporeda
Folder sa fajlom odmah.txt objavljuje se odmah kad se pokrene workflow (promjena stanje/pokreni.txt), i prije 17:43. Takve objave čekaju u cekaju/ (objavi.py ih ne vidi) i premještaju se u objave/ tek u trenutku objave. Prvi put 21.11.2026: 4 Reela, jedan svaka 2 sata (Igorov zahtjev, samo taj dan).
