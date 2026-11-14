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

## Sedmični ciklus (stanje od 10.11.2026)

Objavljivanje ne zavisi od računara. Računar treba samo za nove fotke (Gemini) i za Facebook grupe.

| Kad | Ko | Šta radi |
| --- | --- | --- |
| Svaki dan od 17:43 | GitHub Actions (`objava.yml`) | Objavi današnju objavu na Instagram (sa Storyjem) i na Facebook stranicu; propuštene nadoknadi do 7 dana unazad. Više pokušaja do 21:30. |
| Svaki dan 17:45 | Zakazani zadatak "Instagram – kontrolor" (oblak) | Provjeri da je objava izašla i pokrene je ako nije; provjeri spremne objave za 7 dana; ako zaliha pokriva manje od 4 dana, napravi objave od slobodnih fotki ili tekstualne. |
| Svaki dan 18:21 | "Instagram – dnevna objava i zajednica" (računar) | Rezerva za objavu, sinhronizacija foldera sa GitHubom, komentari, Facebook grupe (vidi `alati/zajednica.md`). Kad je računar ugašen, preskače se. |
| Nedjelja 18:32 | "Instagram – nedjeljna priprema" (računar) | Nove fotke preko Gemini-ja i objave za naredne dvije sedmice, postavljene na GitHub; obnova ključa; prve nedjelje u mjesecu statistika. |
| Ponedjeljak 9:05 | GitHub (`provjera.yml`) | Provjera ključeva; ako nešto ne valja, mail. |
| 1. i 15. u mjesecu | GitHub (`kljuc.yml`) | Obnova Instagram ključa u GitHub Secrets. |

Ako želiš izmijeniti objavu prije nego izađe, napiši šta u `napomene.txt` u njenom folderu u `05_spremno` ili javi Claudeu u razgovoru. Ako objavu želiš zaustaviti, javi Claudeu (mora se skloniti i sa GitHuba, iz `objave/`).

**Svaki dan (Igor, 5 minuta):** odgovori na poruke. Gotovi odgovori su u `01_identitet/odgovori.md`.

**Prva nedjelja u mjesecu (Claude):** upiše brojke prošlog mjeseca u `07_statistika/statistika.csv`, uporedi šta je radilo, i predloži plan za naredni mjesec.

## Sedmični raspored tema

| Dan | Tema |
| --- | --- |
| Ponedjeljak | Edukacija: kako se pravilno postavlja video nadzor, kao Reel (3 fotke, sa muzikom) |
| Utorak | Rješenja: kako se nešto uradi uredno ili pametno (ormar, rack, bežični most…) |
| Srijeda | Oprema koju ugrađujem: jedan model, Hikvision i Dahua naizmjenično (šablon proizvod, bez AI napomene) |
| Četvrtak | Savjet, kao Reel |
| Petak | Česti problemi i kako se rješavaju, kao Reel (3 fotke, sa muzikom) |
| Subota | Završen objekat, kao Reel po pravilu "Format završen objekat" ispod: više kamera na različitim pozicijama iste kuće (fotke) pa kratak video. Dok Igor ne snimi pravi posao, AI materijal sa naslovom "Primjer" i AI napomenom, nikad kao Igorov urađeni posao |
| Nedjelja | Objave za čuvanje: checkliste, tabele i podsjetnici koje ljudi sačuvaju ("Sačuvaj: …"), tekst na tamnoj pozadini + jedna fotka; poziv "Sačuvaj objavu" u opisu |

- Uz svaku objavu ide Story "Nova objava".
- Tvrdnje i brojke (dometi, dani snimanja, mitovi) samo provjerene, iz katalog_opreme.csv ili zvaničnih stranica proizvođača.
- Kad Igor ubaci prave fotke lokacija u `02_materijal/ulaz`, subota ide sa njima (zamutiti lica, tablice, kućne brojeve).

## Pravila za rast (od 31.10.2026)

Instagram danas nove ljude dovodi preko pretrage po ključnim riječima, Reelsa i dijeljenja u porukama. Zato:

- **Prvi red opisa** (do ~125 znakova, prije "više"): pitanje ili tvrdnja koja zaintrigira, sa riječima koje ljudi stvarno ukucaju u pretragu: "video nadzor", "kamere za kuću", "kamera za ulaz", "ugradnja kamera", "snimač", "kamera ne radi". Primjer: "Koliko megapiksela treba kameri za video nadzor?" Bez nabrajanja ključnih riječi jedne za drugom.
- **alt.txt** u svakom folderu objave sa slikama: jedna rečenica šta je stvarno na slici, sa ključnom riječi (npr. "Ugradni ormar u hodniku sa snimačem za video nadzor i UPS uređajem."). Mora odgovarati slici. GitHub ga šalje Instagramu kao alternativni tekst.
- **Dijeljenje:** prije svake objave odgovori sebi "ko će ovo poslati kome i zašto". Kod korisnih objava (checkliste, savjeti, česti problemi) prije poziva na kontakt ide jedan red tipa "Pošalji ovo nekome ko gradi kuću." ili "Pošalji je i nekome ko ima kamere kod kuće." Ne na svakoj objavi, samo kad sadržaj to zaslužuje.
- **Reels su glavni put do novih ljudi:** u oktobru je jedan Reel imao doseg 131, a slike i carouseli 1 do 3. Zato od 10.11.2026 ponedjeljak, četvrtak, petak i subota idu kao Reel sa muzikom (`alati/napravi_reel.py`), 3 fotke po Reelu. Slika ostaje utorkom, oprema srijedom (zvanične slike), a carousel samo nedjeljom ("Sačuvaj"). Gemini tako treba oko 13 do 15 fotki sedmično, u okviru limita od 20. Prve 1 do 3 sekunde: tekst na ekranu koji odmah kaže o čemu je riječ, sa ključnom riječi; mora se razumjeti bez zvuka. Bez tuđih vodenih žigova.
- **Carousel:** naslovni slajd obećava šta se dobije prevlačenjem ("Prevuci →"), jedan slajd jedna misao, zadnji slajd sažetak i poziv.
- **Poziv "Napiši KAMERA u komentar i javiću ti se."** na jednoj do dvije objave sedmično umjesto poziva na DM (pravila u `alati/zajednica.md`). Komentari podižu doseg, a Igor odmah dobija mail.
- **Story** "Nova objava" na dnu ima poziv "Imaš pitanje o kamerama? Odgovori na ovu priču." Odgovori stižu Igoru u DM.
- **Mjerenje** (prva nedjelja u mjesecu): za svaku objavu upiši doseg, dijeljenja (shares), čuvanja (saved) i preglede; najbolji pokazatelj su dijeljenja i čuvanja u odnosu na doseg, ne lajkovi ni broj pratilaca. Teme koje se najviše dijele i čuvaju ponavljaj u novom obliku.

## Format "Završen objekat" (od 14.11.2026)

Igorovo pravilo: video sadržaj se usmjerava na snimke završenog objekta. Ne jedna kamera i ne "prije/poslije", nego VIŠE kamera postavljenih na različitim pozicijama iste kuće, pa malo videa.

**Sastav Reela** (oko 15 do 20 sekundi, `alati/napravi_reel.py`, primjer `alati/primjer_zavrsen_objekat.json`, muzika obavezna):

1. **Prve 2 sekunde:** šira fotka kuće na kojoj se vide bar dvije kamere, sa tekstom koji odmah kaže o čemu je riječ (npr. "Video nadzor na kući: 4 kamere"). Dok je materijal AI, podtekst je "Primjer, AI prikaz".
2. **3 do 5 fotki iste kuće**, svaka druga pozicija kamere: ulaz (na zidu pored vrata), ugao prema dvorištu i parkingu, kapija i ulica, zadnja strana ili garaža. Oko 1,8 s po fotki, mala oznaka pozicije gore lijevo (`"oznaka": "Ulaz"`, `"Parking"`, `"Kapija"`, `"Zadnja strana"`).
3. **1 do 2 kratka video kadra** (4 do 6 s): telefon u ruci prolazi oko kuće i u kadru se vidi više kamera (`"video": "obilazak.mp4"`).
4. **Kraj:** poziv, npr. "Napiši KAMERA u komentar i javiću ti se."

**AI materijal (dok nema pravih snimaka):**

- Kamere na AI fotkama: bijele turret (eyeball) kamere "mounted flush directly on the facade wall … no arm, no bracket, no separate box, no pipe, away from downpipes". Sa bullet kamerom i razvodnom kutijom Gemini skoro uvijek docrta krak ili cijev do kutije (provjereno 14.11.2026).
- Fotke: Gemini slike 9:16, SVE u istom razgovoru (prethodni odgovori idu kao historija), da kuća ostane ista: prvo šira fotka kuće sa kamerama, pa "same house, now a closer view of the camera at …" za svaku poziciju.
- Video kadar: model `gemini-omni-1.2-flash` preko `POST https://generativelanguage.googleapis.com/v1beta/interactions` (Veo nije dostupan na ovom ključu), tijelo `{"model":"gemini-omni-1.2-flash","input":"<opis>","response_format":{"type":"video","duration":"6s","resolution":"720p","aspect_ratio":"9:16"}}`; video je base64 u koraku `model_output`. Traje oko 1 do 1,5 minut, pa ga pokreni u pozadini i provjeravaj. Cijena oko 0,07 $ po sekundi. Da kuća bude ista kao na fotkama, pošalji široku fotku kao referencu: `"input": [{"type":"image","mime_type":"image/jpeg","data":"<base64>"}, {"type":"text","text":"Use the attached photo as the reference … <opis>"}]` (radi, provjereno 14.11.2026).
- Prenos na računar: preko GitHuba u `materijal/video_test/`, pa sa raw adrese u `02_materijal`. Raw adresa sa `main` zna dati staru verziju istog fajla (keš), zato skidaj preko SHA commita: `raw.githubusercontent.com/<vlasnik>/<repo>/<sha>/<putanja>`. Video od 10 MB se šalje oko minut.
- Opis za video uvijek: handheld smartphone video, amateur real-life footage, not cinematic; several security cameras visible at different positions; no tools, no drill, no hands, no faces, no text, no logos, no license plates; real ambient sound only, no music.
- Trošak jednog Reela oko 0,5 do 1 $. Pazi na budžet od 5 $ mjesečno.

**Pravila montaže** (važe za svaki kadar):

- Kabl se ne vidi, ili samo kratko odozgo, iz strehe pravo u razvodnu kutiju. Nikad kanalica ili kabl preko fasade.
- Kamera nikad iznad vrata ni na/iznad nadstrešnice.
- Bez bušilice, odvijača i ruku na snimku: zavrtanje izgleda nerealno.
- Bez lica, tablica i kućnih brojeva.
- Svaki kadar pregledaj prije upotrebe; ako pravilo nije ispoštovano, kadar ne ide.

**Kad Igor radi pravi posao:** telefonom snimi gotov objekat: svaku kameru posebno, jednu širu fotku na kojoj se vidi više kamera, i kratak obilazak (10 do 20 s). Ubaci u `02_materijal/ulaz`; takvi snimci imaju prednost pred AI i tada objava smije reći da je njegov posao.

## Objavljivanje preko GitHuba (od 28.10.2026)

Objave na Instagram ne zavise od računara: GitHub Actions u repozitoriju `video-nadzor-objave` svaki dan u 17:43 objavi objavu i Story na Instagram i istu objavu na Facebook stranicu "Video nadzor kamere" (`alati/objavi.py`, `.github/workflows/objava.yml`), a propuštene nadoknadi sam (do 7 dana unazad). Šta je objavljeno piše u `stanje/objavljeno.json` na GitHubu.

- Objava mora biti u repozitoriju: `objave/GGGG-MM-DD_tema/` sa `opis.txt` i slikama `01.jpg…` (ili `video.mp4` + `cover.jpg` za Reel). Nedjeljna priprema zato postavlja i `opis.txt`.
- Priprema ide **dvije sedmice unaprijed**, da objave izlaze i kad računar nije upaljen.
- Kad je računar upaljen, Claude premješta objavljene foldere iz `05_spremno` u `06_objavljeno` po `stanje/objavljeno.json` i upisuje linkove u plan.
- Instagram ključ je u GitHub Secrets (`IG_TOKEN`), obnavlja se sam 1. i 15. u mjesecu (`kljuc.yml`). Facebook stranica: `FB_PAGE_TOKEN` (trajni ključ stranice) i `FB_PAGE_ID` = 1364094053457507. Ključeve svakog ponedjeljka provjerava `provjera.yml`; ako nešto ne valja, GitHub šalje mail.
- Komentari se bilježe u `stanje/komentari.json`; za nove se otvara GitHub issue (mail Igoru). Odgovaranje: `alati/zajednica.md`.

## Propuštena objava

GitHub sam nadoknadi propuštene objave do 7 dana unazad, a kontrolor u 17:45 provjeri i pokrene ga ako treba. Igor ne mora ništa raditi.

- Ako objava ni tada ne izađe, kontrolor javi grešku. Tada Igor može napisati Claudeu **"objavi propuštenu objavu"**: Claude provjeri `stanje/objavljeno.json` na GitHubu, pokrene objavljivanje promjenom `stanje/pokreni.txt`, a tek ako ni to ne prođe, objavi sam po `alati/objavljivanje_api.md` (prije toga provjeri zadnjih 10 objava da ista nije već izašla).
- Zakazani zadaci na računaru se sami pauziraju kad je računar ugašen u terminu; kontrolor ih svaki dan ponovo uključi.

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
