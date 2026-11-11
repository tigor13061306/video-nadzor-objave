# Zajednica: komentari i Facebook grupe

Radi se kad je računar upaljen (zakazani zadatak "Instagram – dnevna objava i zajednica"). Ako je računar ugašen, taj dan se preskoči.

## Komentari na Instagramu (odobrio Igor 28.10.2026)

- Novi komentari: `stanje/komentari.json` u GitHub repozitoriju, ili preko API-ja: `GET <media_id>/comments?fields=id,text,username,timestamp,replies{username}`.
- Odgovor: `POST <comment_id>/replies` sa `message`, u ugrađenom pregledniku na https://graph.instagram.com/ (ključ samo u zaglavlju).
- Pravila:
  - kratko, stručno, kao profil, prvo lice i "ti", bez emotikona ili najviše jedan;
  - nikad cijene, rokovi, termini ni obećanja; kad neko pokaže interes (cijena, ponuda, ugradnja, termin), odgovori "Pošalji mi u DM broj telefona i mjesto, nazvaću te. Procjena je besplatna." i odmah javi Igoru (Claude ne šalje privatne poruke);
  - ako je neko ostavio broj telefona u komentaru, komentar sakrij (POST <comment_id> hide=true) da broj ne bude javan, odgovori "Hvala, javiću ti se." i odmah javi Igoru korisnika i broj;
  - na uvrede, spam i reklame ne odgovaraj, samo navedi Igoru;
  - na privatne poruke (DM) nikad ne odgovaraj, samo ih navedi Igoru.
- Poslije odgovora u `stanje/komentari.json` stavi `"odgovoreno": true`.

## Poziv "Napiši KAMERA" (odobrio Igor 31.10.2026)

- Na jednoj do dvije objave sedmično (najbolje Reels i korisne objave) poziv na kraju opisa glasi: "Napiši KAMERA u komentar i javiću ti se. Procjena je besplatna." Na ostalim objavama ostaje "Pošalji mi u DM broj telefona i mjesto…".
- Komentar sa riječju KAMERA odmah ide Igoru na mail (GitHub issue "UPIT"); Igor se javlja u DM.
- Claude na takav komentar odgovara javno samo kratko: "Hvala! Javljam ti se u poruke." Bez cijena i termina.

## Facebook grupe (kao stranica "Video nadzor kamere", nikad Igorov lični profil)

- Stranica je članica grupa: Oglasi Teslić, Jelah, Tešanj, Doboj, Zenica, Banja Luka; Mali oglasi-DOBOJ; Doboj Oglasi; DOBOJSKI MEGA OGLASI; Doboj. Od 31.10.2026 i: Oglasi Tešanj,Jelah,Doboj,Teslić,Maglaj i okolica; Grupa za prodaju Maglaj-Tesanj-Doboj. (samo kupovina/prodaja: tu ide oglas usluge, ne savjet); MAJSTORI I MAJSTORSKE USLUGE. ("Kupujem Prodajem Doboj" ne prima stranice; "Oglasi Doboj, Tesanj, Teslić, Maglaj" traži ime i prezime i cijenu - preskače se.)
- Grupe za učlanjenje (nađene 31.10.2026), dnevni zadatak se kao stranica učlani u najviše 2 dnevno: prvo pročita pravila grupe, preskoči grupe koje ne primaju stranice ili zabranjuju poslovne objave, odgovori na pitanja za učlanjenje istinito (stranica za ugradnju video nadzora). Status upiše u `07_statistika/grupe.csv` (status "učlanjenje poslano"/"primljeno"/"ne prima stranice").
  - Oglasi Doboj, Tesanj, Teslić, Maglaj (35 hilj.)
  - Oglasi Gracanica, Doboj, Tesanj, Teslic, Maglaj (29 hilj.)
  - Grupa za prodaju Maglaj-Tesanj-Doboj. (16 hilj.)
  - Mali Oglasi Derventa Doboj Stanari Banja Luka Prnjavor (16 hilj.)
  - Oglasi Tešanj,Jelah,Doboj,Teslić,Maglaj i okolica (12 hilj.)
  - MAJSTORI I MAJSTORSKE USLUGE (12 hilj.)
  - Tesanj, Doboj, Modrica, Prnjavor, B.Luka OGLASI (10 hilj.)
  - Prnjavor, Tesanj, Doboj, Modrica OGLASI (8,6 hilj.)
  - Gradnja kuće savjeti i iskustva (9,5 hilj., privatna) - ne prima stranice (4.11.2026)
  - Regija Doboj oglasi (12 hilj., privatna, facebook.com/groups/2390646654330477; nađena 4.11.2026, učlanjenje poslano)
  - Udruženje pčelara LIPA Doboj Jug (258 članova, facebook.com/groups/222300458233221; nađena 4.11.2026, grupa za signale: samo savjeti; primljeno 6.11.2026)
  - TESLIĆ I OKOLINA- RAZNI OGLASI(nekretnine,namještaj,posao...) (15 hilj., javna, facebook.com/groups/1042755206884573; nađena 6.11.2026, lokalni oglasi)
  - Oglasi Teslić 🛒 (12 hilj.), TESLIC Kupi Prodaj Mijenja OGLASI (11 hilj.), MALI OGLAS TESLIC (10 hilj.), Prodaj~Kupi Teslić i okolina. (9,7 hilj.), Oglasi Teslic (9,3 hilj.) - nađene 6.11.2026 pretragom, lokalni oglasi
  - TESLIĆ I OKOLINA- RAZNI OGLASI: primljeno 8.11.2026; MALI OGLAS TESLIC (facebook.com/groups/493781870831791): primljeno 8.11.2026
  - Oglasi Teslić 🛒 (facebook.com/groups/293437411520518): pravila zabranjuju reklamiranje bez dogovora sa adminom - preskače se (8.11.2026)
  - TESLIC Kupi Prodaj Mijenja OGLASI (facebook.com/groups/496312810494236) i Kupi prodaj zamijeni Jelah Tešanj Doboj Teslić Usora (19 hilj., facebook.com/groups/394025061412712): primljeno 11.11.2026; Regija Doboj oglasi: primljeno 10.11.2026
  - Još neprovjerene: Oglasi Teslic (facebook.com/groups/1595821597368110), Tražim / nudim posao - uslugu: DOBOJ - MODRIČA - ŠAMAC (nađena 11.11.2026 u pretrazi, lokalne usluge)
  - Grupe prodavaca opreme za video nadzor se preskaču (to su konkurenti, ne kupci).
- Oglasi i objave u grupama: bez "kablovi se ne vide" i sličnog (pravilo "Tekst bez nametanja" u identitet.md). U oglasnim grupama (kupovina/prodaja) ide oglas usluge bez linka, ne savjet sa linkom: savjeti sa linkom su uklonjeni u 4 grupe (31.10. do 3.11.).
- Prije objave provjeri da je u gornjem desnom uglu Facebooka aktivan profil stranice (logo), ne Igorov.
- **Od 10.11.2026: jedna objava SEDMIČNO, srijedom**, u jednoj grupi (ista grupa najviše jednom u 3 sedmice). Razlog: od 31.10. do 8.11. admini su uklonili 5 od desetak oglasa, a ostali nisu dobili nijedan komentar. Ostalim danima nema objava u grupama, samo odgovori na komentare, učlanjenje i traženje kupaca. Evidencija: `07_statistika/grupe.csv` (datum;grupa;tema;status).
- Sadržaj: koristan savjet iz neke od naših objava (3 do 6 redova) + link https://www.instagram.com/video.nadzorkamere/ + "Za ugradnju ili savjet pošalji poruku sa brojem telefona i mjestom, javiću se." Bez cijena, bez "najbolji/najjeftiniji", bez područja rada.
- Pretraga grupa: ako neko traži majstora za kamere ili pita o video nadzoru, odgovori kratkim stručnim komentarom kao stranica i ponudi "Piši u poruke". Najviše 3 takva odgovora dnevno. Ne komentariši ništa drugo.
- Dan poslije svake objave u grupi pogledaj komentare na njoj i odgovori kratko i stručno kao stranica; objava ne smije ostati bez odgovora. Prvo korisno, pa tek onda poziv na kontakt.
- Ako administrator odbije ili ukloni objavu, tu grupu preskači 2 sedmice.

## Svaki dan: traženje kupaca i posmatranje grupa (Igor, 31.10.2026; dio koraka 4 dnevnog zadatka)

**A) Traženje potencijalnih kupaca (svaki dan, kao stranica, samo čitanje):**
- U svakoj grupi u kojoj je stranica članica, i u Facebook pretrazi objava (https://www.facebook.com/search/posts/?q=..., filter "Nedavne objave"), traži objave iz zadnjih 7 dana sa riječima: kamere, video nadzor, kamera, snimač, alarm, majstor za kamere, ugradnja kamera, "treba mi kamera", "preporučite majstora". Upiti iz Doboja i okoline (Teslić, Tešanj, Maglaj, Modriča, Derventa, Gračanica, Stanari, Prnjavor) imaju prednost.
- Svaki pravi upit (neko traži ugradnju, popravku, savjet za kupovinu) upiši u `07_statistika/kupci.csv` (datum;grupa;link objave;šta traži;mjesto;status). Isti link se ne upisuje dvaput.
- Svaki dan kad je pretraga urađena, u repozitorij `video-nadzor-poslovi` pošalji `02_nalazi/GGGG-MM-DD_fb_grupe.json`, i kad nema nalaza (tada sadržaj `[]`), da zadatak "Poslovi – pretraga" vidi da je pretraga urađena.
- U grupama gdje je stranica članica može kratko i stručno odgovoriti kao stranica (najviše 3 dnevno, "Piši u poruke"), status "odgovoreno". Gdje stranica nije članica: ništa ne piše, status "za Igora".
- Igoru u poruci dnevnog zadatka: broj novih upita i linkovi (najviše 5), da im se javi sam.

**B) Posmatranje grupa o video nadzoru (za sada samo posmatranje, bez učlanjenja i objava):**
- 3.11.2026: "cctv ip ptz wifi video kamera nadzor security" (admin Milan Radovanović) i "Alarmi Kamere Gladijator" (agencija iz Subotice) su takođe grupe za reklamu administratora - preskaču se. Kad se nađe aktivna grupa o video nadzoru gdje pišu obični članovi, dodati je ovdje.
- Grupe u kojima objavljuje skoro samo administrator, za svoju reklamu (npr. "Alarm i Video Nadzor", admin Edin Kutić), se preskaču: ne posmatraju se, ne upisuju u statistiku i ne koriste za objave ili traženje kupaca (Igor, 3.11.2026).
- Grupe: VIDEO NADZOR - ALARMI PRODAJA (facebook.com/groups/152468741528682), plus lokalni majstori koji se pojave u pretrazi (npr. AVUR Technik Teslić).
- Svaki dan pregledaj nove objave (zadnja 24 h) i one sa najviše komentara; upiši u `07_statistika/grupe_teme.csv` (datum;grupa;link;tema;vrsta;komentara;reakcija). Vrsta: završen posao / pitanje / prodaja opreme / traži majstora / ostalo.
- Prve nedjelje u mjesecu nedjeljna priprema sabere `grupe_teme.csv` i `kupci.csv` u `07_statistika/statistika.csv` (koje teme i vrste objava imaju najviše komentara, koliko upita i odakle) i po tome dopuni plan objava.
