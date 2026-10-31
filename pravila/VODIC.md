# Vođenje profila @video.nadzorkamere

Ovaj folder je centar profila. Sve objave, materijal, plan i statistika su ovdje, a Claude radi u njemu kad je računar upaljen i Claude desktop aplikacija otvorena.

## Struktura foldera

| Folder | Šta je unutra | Ko ga puni |
| --- | --- | --- |
| `01_identitet` | Pravila izgleda i tona, logo, šabloni odgovora na poruke | Claude, mijenja se rijetko |
| `02_materijal/ulaz` | Nove fotografije i video: tvoje, sa Pexelsa ili iz Geminija | Igor |
| `02_materijal/odobreno` | Materijal koji je pregledan i spreman za upotrebu | Claude |
| `03_plan` | `plan_objava.csv`, raspored objava za naredne sedmice | Claude predlaže, Igor potvrđuje |
| `04_u_pripremi` | Objave koje čekaju tvoj pregled, svaka u svom folderu | Claude |
| `05_spremno` | Odobrene objave, spremne za objavljivanje | Igor premješta |
| `06_objavljeno` | Arhiva objavljenog | Premješta se poslije objave |
| `07_statistika` | `statistika.csv`, brojke po mjesecima | Claude |
| `alati` | Alat za slajdove, fontovi, uputstvo za API, Instagram ključ (`instagram_kljuc.json`, tajno) | Claude |
| `prompti` | Opisi za Gemini, za nove fotografije | Claude |

Svaka objava ima svoj folder, nazvan `GGGG-MM-DD_tema` (npr. `2026-10-27_5-gresaka`). Unutra su slike po redu (`01.png`, `02.png`…), `opis.txt` sa tekstom za ispod objave i `objava.json` iz kojeg alat pravi slike.

## Sedmični ciklus

Sve radi samo, preko dva zakazana zadatka. Računar mora biti upaljen, a Claude desktop aplikacija otvorena u tim terminima.

**Nedjelja uveče (zakazani zadatak "Instagram – nedjeljna priprema"):**
1. Pogleda `03_plan/plan_objava.csv` i novi materijal u `02_materijal/ulaz`.
2. Napravi 7 objava za narednu sedmicu (ponedjeljak do nedjelje) u `05_spremno`, po sedmičnom rasporedu tema ispod, i postavi njihove slike na GitHub. Četvrtkom je Reel (`alati/napravi_reel.py`, uputstvo u `alati/objavljivanje_api.md`).
3. Obnovi Instagram ključ i, prve nedjelje u mjesecu, upiše statistiku.
4. Pošalje ti kratak izvještaj: šta ide te sedmice i šta fali.

**Svaki dan u 17:43 (zakazani zadatak "Instagram – dnevna objava"):**
1. Objavi objavu za taj dan preko Instagram API-ja (`alati/objavljivanje_api.md`), a odmah zatim i Story "Nova objava" (`alati/napravi_story.py`).
2. Folder objave premjesti u `06_objavljeno` i upiše link u plan.

Ako želiš izmijeniti objavu prije nego izađe, napiši šta u `napomene.txt` u njenom folderu u `05_spremno` ili javi Claudeu u razgovoru. Ako objavu želiš zaustaviti, premjesti njen folder u `04_u_pripremi`.

**Svaki dan (Igor, 5 minuta):** odgovori na poruke i komentare. Gotovi odgovori su u `01_identitet/odgovori.md`.

**Prva nedjelja u mjesecu (Claude):** upiše brojke prošlog mjeseca u `07_statistika/statistika.csv`, uporedi šta je radilo, i predloži plan za naredni mjesec.

## Sedmični raspored tema

| Dan | Tema |
| --- | --- |
| Ponedjeljak | Edukacija: kako se pravilno postavlja video nadzor (carousel) |
| Utorak | Rješenja: kako se nešto uradi uredno ili pametno (ormar, rack, bežični most…) |
| Srijeda | Oprema koju ugrađujem: jedan model, Hikvision i Dahua naizmjenično (šablon proizvod, bez AI napomene) |
| Četvrtak | Savjet, kao Reel |
| Petak | Česti problemi i kako se rješavaju |
| Subota | Lokacije sa kamerama, kao Reel (3 do 4 fotke, sa muzikom). Dok Igor ne počne snimati prave lokacije, ide AI fotografija sa naslovom "Primjer: …" i AI napomenom, nikad kao Igorov urađeni posao |
| Nedjelja | Objave za čuvanje: checkliste, tabele i podsjetnici koje ljudi sačuvaju ("Sačuvaj: …"), tekst na tamnoj pozadini + jedna fotka; poziv "Sačuvaj objavu" u opisu |

- Uz svaku objavu ide Story "Nova objava".
- Tvrdnje i brojke (dometi, dani snimanja, mitovi) samo provjerene, iz katalog_opreme.csv ili zvaničnih stranica proizvođača.
- Kad Igor ubaci prave fotke lokacija u `02_materijal/ulaz`, subota ide sa njima (zamutiti lica, tablice, kućne brojeve).

## Pravila za rast (od 31.10.2026)

Instagram danas nove ljude dovodi preko pretrage po ključnim riječima, Reelsa i dijeljenja u porukama. Zato:

- **Prvi red opisa** (do ~125 znakova, prije "više"): pitanje ili tvrdnja koja zaintrigira, sa riječima koje ljudi stvarno ukucaju u pretragu: "video nadzor", "kamere za kuću", "kamera za ulaz", "ugradnja kamera", "snimač", "kamera ne radi". Primjer: "Koliko megapiksela treba kameri za video nadzor?" Bez nabrajanja ključnih riječi jedne za drugom.
- **alt.txt** u svakom folderu objave sa slikama: jedna rečenica šta je stvarno na slici, sa ključnom riječi (npr. "Ugradni ormar u hodniku sa snimačem za video nadzor i UPS uređajem."). Mora odgovarati slici. GitHub ga šalje Instagramu kao alternativni tekst.
- **Dijeljenje:** prije svake objave odgovori sebi "ko će ovo poslati kome i zašto". Kod korisnih objava (checkliste, savjeti, česti problemi) prije poziva na kontakt ide jedan red tipa "Pošalji ovo nekome ko gradi kuću." ili "Pošalji je i nekome ko ima kamere kod kuće." Ne na svakoj objavi, samo kad sadržaj to zaslužuje.
- **Reels su glavni put do novih ljudi:** četvrtak i subota idu kao Reel sa muzikom (`alati/napravi_reel.py`). Prve 1 do 3 sekunde: tekst na ekranu koji odmah kaže o čemu je riječ, sa ključnom riječi; mora se razumjeti bez zvuka. Bez tuđih vodenih žigova.
- **Carousel:** naslovni slajd obećava šta se dobije prevlačenjem ("Prevuci →"), jedan slajd jedna misao, zadnji slajd sažetak i poziv.
- **Story** "Nova objava" na dnu ima poziv "Imaš pitanje o kamerama? Odgovori na ovu priču." Odgovori stižu Igoru u DM.
- **Mjerenje** (prva nedjelja u mjesecu): za svaku objavu upiši doseg, dijeljenja (shares), čuvanja (saved) i preglede; najbolji pokazatelj su dijeljenja i čuvanja u odnosu na doseg, ne lajkovi ni broj pratilaca. Teme koje se najviše dijele i čuvaju ponavljaj u novom obliku.

## Objavljivanje preko GitHuba (od 28.10.2026)

Objave na Instagram ne zavise od računara: GitHub Actions u repozitoriju `video-nadzor-objave` svaki dan u 17:43 objavi objavu i Story na Instagram i istu objavu na Facebook stranicu "Video nadzor kamere" (`alati/objavi.py`, `.github/workflows/objava.yml`), a propuštene nadoknadi sam (do 7 dana unazad). Šta je objavljeno piše u `stanje/objavljeno.json` na GitHubu.

- Objava mora biti u repozitoriju: `objave/GGGG-MM-DD_tema/` sa `opis.txt` i slikama `01.jpg…` (ili `video.mp4` + `cover.jpg` za Reel). Nedjeljna priprema zato postavlja i `opis.txt`.
- Priprema ide **dvije sedmice unaprijed**, da objave izlaze i kad računar nije upaljen.
- Kad je računar upaljen, Claude premješta objavljene foldere iz `05_spremno` u `06_objavljeno` po `stanje/objavljeno.json` i upisuje linkove u plan.
- Instagram ključ je u GitHub Secrets (`IG_TOKEN`), obnavlja se sam 1. i 15. u mjesecu (`kljuc.yml`). Facebook stranica: `FB_PAGE_TOKEN` (trajni ključ stranice) i `FB_PAGE_ID` = 1364094053457507. Ključeve svakog ponedjeljka provjerava `provjera.yml`; ako nešto ne valja, GitHub šalje mail.
- Komentari se bilježe u `stanje/komentari.json`; za nove se otvara GitHub issue (mail Igoru). Odgovaranje: `alati/zajednica.md`.

## Propuštena objava

Ako u 17:43 računar nije bio upaljen ili Claude aplikacija nije bila otvorena, objava tog dana ne izlazi i ostaje u `05_spremno` sa svojim datumom. Sistem tada zadatak "Instagram – dnevna objava" sam pauzira.

- Dnevni zadatak propuštene objave ne objavljuje sam. Samo ih navede u poruci Igoru.
- Kad Igor upali računar i napiše Claudeu **"objavi propuštenu objavu"**, Claude:
  1. nađe sve foldere u `05_spremno` sa datumom prije današnjeg (i koji nisu "objavljeno" u planu),
  2. objavi ih redom od najstarije, svaku sa Storyjem, tačno po `alati/objavljivanje_api.md`,
  3. premjesti ih u `06_objavljeno`, fotke u `02_materijal/iskoristeno`, upiše link u plan uz napomenu "objavljeno naknadno",
  4. provjeri da su zakazani zadaci "Instagram – dnevna objava" i "Instagram – nedjeljna priprema" uključeni i uključi ih ako su pauzirani,
  5. javi Igoru šta je objavljeno i linkove.
- Ako je današnja objava još u `05_spremno`, a 17:43 još nije prošlo, nju ne dira: izaći će redovno.

## Pravila prije svake objave

- [ ] Izgled po `01_identitet/identitet.md`: tamna pozadina, jedna boja akcenta, tekst nikad direktno preko fotografije.
- [ ] Nema lica, tablica, kućnih brojeva, adresa, šifri ni IP adresa na slici.
- [ ] Nikakvi snimci sa objekata na kojima radiš u službi.
- [ ] Ilustrativna ili AI fotografija nije predstavljena kao tvoj urađeni posao.
- [ ] AI slika: u opisu piše "Fotografije su ilustrativne, napravljene AI alatom." (API nema prekidač za AI oznaku).
- [ ] Opis završava jednim pozivom na akciju i ima osnovni set hashtagova.
- [ ] Dvije tekstualne objave ne idu jedna za drugom.
- [ ] Samo prave fotografije, bez nacrtanih ilustracija i tlocrta.
- [ ] Objava o opremi (šablon `proizvod`): samo zvanične slike iz `02_materijal/oprema`, karakteristike samo iz `katalog_opreme.csv` ili sa zvanične stranice proizvoda. Te slike nisu AI, pa opis ne dobija AI napomenu.
- [ ] Jednom sedmično ide objava "Oprema koju ugrađujem" (šablon `proizvod`, Hikvision i Dahua naizmjenično, model iz `katalog_opreme.csv`).

- [ ] Svaka fotografija se objavljuje samo jednom. Poslije objave ide iz `02_materijal/odobreno` u `02_materijal/iskoristeno`. Ako u `odobreno` ostane manje od 6 fotki, javi Igoru da napravi novu seriju u Geminiju (`prompti/gemini_prompti.md`).

## Novi materijal

- Tvoje fotografije: ubaci u `02_materijal/ulaz`, Claude ih pregleda i zamuti ono što ne smije biti vidljivo.
- Gemini: opisi su u `prompti/gemini_prompti.md`. Gotove slike ubaci u `02_materijal/ulaz`, sa `AI_` na početku imena fajla, da se zna koje treba označiti.

## Alat za objave

Claude pravi slike alatom `alati/napravi_objavu.py`. Ako želiš sam:

```
python alati\napravi_objavu.py 04_u_pripremi\2026-10-27_5-gresaka\objava.json
```

Potreban je Python sa paketom Pillow (`pip install pillow`). Šabloni koje alat zna: `naslovna`, `foto_traka`, `foto_kutija`, `tekst`, `dan_noc`, `proizvod`. Primjer je u `alati/primjer_objava.json`.
