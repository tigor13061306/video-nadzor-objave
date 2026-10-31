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

- Stranica je članica grupa: Oglasi Teslić, Jelah, Tešanj, Doboj, Zenica, Banja Luka; Mali oglasi-DOBOJ; Doboj Oglasi; DOBOJSKI MEGA OGLASI; Doboj. ("Kupujem Prodajem Doboj" ne prima stranice.)
- Grupe za učlanjenje (nađene 31.10.2026), dnevni zadatak se kao stranica učlani u najviše 2 dnevno: prvo pročita pravila grupe, preskoči grupe koje ne primaju stranice ili zabranjuju poslovne objave, odgovori na pitanja za učlanjenje istinito (stranica za ugradnju video nadzora). Status upiše u `07_statistika/grupe.csv` (status "učlanjenje poslano"/"primljeno"/"ne prima stranice").
  - Oglasi Doboj, Tesanj, Teslić, Maglaj (35 hilj.)
  - Oglasi Gracanica, Doboj, Tesanj, Teslic, Maglaj (29 hilj.)
  - Grupa za prodaju Maglaj-Tesanj-Doboj. (16 hilj.)
  - Mali Oglasi Derventa Doboj Stanari Banja Luka Prnjavor (16 hilj.)
  - Oglasi Tešanj,Jelah,Doboj,Teslić,Maglaj i okolica (12 hilj.)
  - MAJSTORI I MAJSTORSKE USLUGE (12 hilj.)
  - Tesanj, Doboj, Modrica, Prnjavor, B.Luka OGLASI (10 hilj.)
  - Prnjavor, Tesanj, Doboj, Modrica OGLASI (8,6 hilj.)
  - Gradnja kuće savjeti i iskustva (9,5 hilj., privatna; tu samo korisni savjeti, bez oglasa)
  - Grupe prodavaca opreme za video nadzor se preskaču (to su konkurenti, ne kupci).
- Prije objave provjeri da je u gornjem desnom uglu Facebooka aktivan profil stranice (logo), ne Igorov.
- Jedna objava dnevno, u jednoj grupi; ista grupa najviše jednom sedmično. Evidencija: `07_statistika/grupe.csv` (datum;grupa;tema;status).
- Sadržaj: koristan savjet iz neke od naših objava (3 do 6 redova) + link https://www.instagram.com/video.nadzorkamere/ + "Za ugradnju ili savjet pošalji poruku sa brojem telefona i mjestom, javiću se." Bez cijena, bez "najbolji/najjeftiniji", bez područja rada.
- Pretraga grupa: ako neko traži majstora za kamere ili pita o video nadzoru, odgovori kratkim stručnim komentarom kao stranica i ponudi "Piši u poruke". Najviše 3 takva odgovora dnevno. Ne komentariši ništa drugo.
- Dan poslije svake objave u grupi pogledaj komentare na njoj i odgovori kratko i stručno kao stranica; objava ne smije ostati bez odgovora. Prvo korisno, pa tek onda poziv na kontakt.
- Ako administrator odbije ili ukloni objavu, tu grupu preskači 2 sedmice.
