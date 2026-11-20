# Vodič: @pametnija.firma (od 20.11.2026)

Profil: Instagram @pametnija.firma i Facebook stranica "Pametnija firma" (isti nalozi kao bivši @video.nadzorkamere, preimenovani 20.11.2026; stare objave obrisane). Vlasnik: Igor. Plan i identitet: dokument "Pametnija firma: identitet i plan prve dvije sedmice" (claude.ai artefakt).

## Cilj i publika
- Publika: vlasnici i menadžeri malih i srednjih firmi u BiH i regiji (trgovine, servisi, ugostiteljstvo, proizvodnja, računovodstva), firme bez svog IT odjela.
- Cilj: upiti firmi za automatizaciju (botovi, izvještaji, povezivanje programa), nadzor sistema (Zabbix, Grafana, upozorenje na telefon) i savjet za AI.

## Pravila sadržaja (Igorova)
1. NEMA čisto tekstualnih objava ni carousela od teksta. Svaka objava je animirani Reel: prave fotke (Gemini) ili snimak, animacija (alati/animacija.py), muzika, zvučni efekti i glas.
2. Glas: Gemini TTS, model gemini-3.8-flash-tts, glas "algieba" (Igor izabrao "glas B"), stil iz pravila/mediji.md. Glas se ne mijenja bez Igora.
3. Poziv na akciju:
   - objave koje nude uslugu firmama (automatizacija, nadzor, ponuda): "Pišite nam u poruke." NIKAD poziv na komentar ("napišite X u komentar");
   - opšte korisne objave (savjet za sve): poziv na komentar je u redu.
4. Obraćanje sa "vi". Kratko, konkretno, bez žargona, uvijek primjer iz naših firmi.
5. Tvrdnje i brojke samo provjerene ili jasno označene kao "primjer računa". Bez cijena, izmišljenih rezultata i recenzija. AI fotke nikad kao Igorov urađeni posao.
6. U opisu svake objave: "Fotografije i glas su napravljeni AI alatom." i fajl ai.txt u folderu (objavi.py tada šalje i AI oznaku).
7. Najviše 5 hashtagova: #automatizacija #malibiznis #bih + 1 do 2 tematska.
8. Bez lica, tablica, logotipa i brendova na fotkama. Nikad podaci, snimci ni ekrani iz Igorove službe.

## Izgled
Tamno plava #0E1A2B, tirkizna #22C3E6, bijeli tekst, font Inter (alati/fonts), znak "PF". Reel 1080x1920, 20 do 35 s. Prve 2 sekunde: slika problema + kratko pitanje.

## Raspored
3 Reela sedmično: ponedjeljak, srijeda, petak (objava od 17:43). Stubovi: automatizacija poslova, nadzor sistema, AI u poslu, sigurnost firme, studije slučaja (samo uz dozvolu klijenta, bez imena). Plan: pravila/plan_objava.csv. Priprema dvije sedmice unaprijed.

## Folder objave
objave/GGGG-MM-DD_tema/: video.mp4, cover.jpg (kadar iz prve 2-3 s, 1080x1920), opis.txt, alt.txt (jedna rečenica šta se vidi), ai.txt, scenarij.py (skripta po kojoj je video napravljen). Bez opis.txt GitHub neće objaviti.

## Pravljenje Reela
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
