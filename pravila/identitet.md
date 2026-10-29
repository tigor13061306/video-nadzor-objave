# Identitet profila @video.nadzorkamere

Boje: pozadina #0E1A2B, kutije #13243A, najtamnija #0A121E, akcent #22C3E6, tekst #FFFFFF, objašnjenja #C5D0DC, sitnice #8A9BB0.
Fontovi: Inter Display Bold za naslove, Inter za tekst (u alati/fonts).

Profil za ugradnju i servis video nadzora (Dahua i Hikvision) za kuće, radnje i firme. Korisničko ime je `@video.nadzorkamere`, ime na profilu `Video nadzor | kamere`. Profil prodaje povjerenje: uredan rad, jasan savjet i sliku na telefonu. Svaka objava ili pokazuje rezultat, ili rješava jedno konkretno pitanje.

**Lokacija:** na slikama, u videima i u opisima nikad ne piši "Doboj i do 100 km", "okolina do 100 km" ni sličan opis područja rada. Hashtag `#doboj` ostaje.

**Realna montaža:** na svakoj fotki kamere kablovi se ne vide (idu kroz zid, kamera na razvodnoj kutiji), a kamera za ulaz nikad nije iznad vrata ni nadstrešnice nego pored vrata na 2,5 do 3 m. Slika koja to ne poštuje ne ide u objavu.

**Cilj svake objave:** da potencijalni kupac kontaktira Igora ili ostavi broj telefona da ga Igor nazove, pa Igor izlazi na teren i pravi ponudu. Zato svaki opis završava pozivom tipa "Pošalji mi u DM broj telefona i mjesto, nazvaću te da se dogovorimo za izlazak na teren." Bez cijena u objavama.


## Ton i jezik

- Piši latinicom, ijekavicom, i obraćaj se čitaocu sa "ti".
- Piši u prvom licu jednine, bez ličnog imena: "ugrađujem", "pošalji mi", "na terenu vidim".
- Kratke rečenice, jedna misao po rečenici. Stručni izraz objasni odmah: "snimač (NVR)".
- Pokazuj rješenje, ne strah. Dobro: "Lice postaje crna silueta. Okreni kameru tako da svjetlo pada na osobu." Loše: "Lopovi samo čekaju da pogriješiš!"
- Bez emojija na grafikama. U opisu objave najviše jedan.
- Svaka objava završava jednim pozivom na akciju: "Piši u DM", "Pošalji fotku objekta u DM", "Sačuvaj za kasnije".
- Cijene pišu "od … KM" samo kad su stvarne. Nikad izmišljeni brojevi, recenzije ni statistike.

## Mješavina objava

Objave se smjenjuju tako da nikad dvije iste vrste ne idu jedna za drugom:

- **Foto objave (oko polovine):** kuće, kamere na fasadi, snimač u ormariću, slika na telefonu, dan i noć, prije i poslije.
- **Edukativni carousel:** savjeti na `ground`, kao "5 grešaka pri postavljanju kamera".
- **Reels:** kratki snimci sa terena ili ekrana, do 30 sekundi.

Tekstualni carousel nikad ne ide dva puta zaredom. Edukativni carousel može imati fotografiju na naslovnici ili na pojedinim slajdovima.

## Fotografije i video

- Glavni motivi: kuća ili objekat sa kamerama, kamera izbliza, snimač i uredni kablovi, telefon sa slikom kamere, snimak ekrana danju i noću, situacija (ulaz, dvorište, parking, kasa).
- Uglavnom fotografiši u sumrak ili oblačno: fasada je ravnomjerno osvijetljena, a kamera se vidi. Izbjegavaj sunce iza objekta.
- Ivice ravne, kamera ili kuća u sredini ili na trećini kadra. Bez filtera; samo malo osvijetli i izoštri.
- Vlastite fotografije sa privatnih poslova su prednost. Ilustrativne fotografije (Pexels, Unsplash, slike proizvođača) su dozvoljene za edukativne objave, ali nikad kao "moj urađeni rad".
- Slika napravljena vještačkom inteligencijom može ilustrovati savjet, ali je ne predstavljaj kao stvaran objekat. Fotorealističnu označi pri objavi kao AI sadržaj.
- Na fotografijama koje pokazuju rad nikad ne smije biti: prepoznatljiva adresa ili kućni broj, lica, tablice, šifre, korisnička imena i IP adrese na ekranu, raspored svih kamera jednog objekta.
- Snimke sa objekata na kojima radiš u službi nikad ne koristi.

## Šabloni objava

Sve grafike su 1080 × 1350 (4:5) za feed, a 1080 × 1920 za Reels naslovnicu i story. Bočna margina je uvijek `space-margin`. Zaglavlje (mali znak + `@video.nadzorkamere` u `meta`, `text-body`) stoji gore lijevo, a broj slajda u `meta`, `text-muted` gore desno. Pri dnu je kratka crta u `accent`.

1. **Naslovna carousela:** `ground`, mala oznaka teme u `label` i `accent` velikim slovima, naslov u `cover-title` sa ključnom riječju u `accent`, ostatak u `text`. Dole desno "Prevuci →" u `accent`.
2. **Slajd savjeta:** broj u `number` i `accent`, naslov u `slide-title` i `text`, objašnjenje u `body` i `text-body`.
3. **Foto + traka:** fotografija preko gornje dvije trećine, bez zatamnjenja i prelaza. Donja trećina je puna `ground` traka sa naslovom u `slide-title` i jednom rečenicom u `body`.
4. **Foto preko cijele:** fotografija na cijeloj površini, a pri dnu kutija `raised` sa `radius-box` i naslovom. Tekst nikad ne ide direktno preko fotografije.
5. **Prije / poslije i dan / noć:** dvije fotografije jedna iznad druge ili jedna pored druge, odvojene linijom od 8 px u `accent`, svaka sa malom oznakom u `label` ("PRIJE", "POSLIJE", "DAN", "NOĆ") na `ground` pločici.
6. **Poziv na akciju (zadnji slajd):** kutija `raised` sa obrubom od 4 px u `accent` i `radius-box`. Prvi red u `cta` i `text`, drugi red u `body` i `text-body`.

## Boje

- Pozadina je uvijek `ground`. Svijetlih objava nema; tamni profil se prepoznaje u feedu.
- `accent` je jedina boja: koristi je na jednom do dva elementa po slajdu. Nikad za dug tekst.
- Tekst na `accent` je uvijek `on-accent`. Bijeli tekst na `accent` ne prolazi kontrast.
- `text` za naslove, `text-body` za objašnjenja, `text-muted` samo za sitnice.
- Bez prelaza boja (gradijenata), sjenki i neonskih efekata.

## Tipografija

- Naslovi su u `display` porodici (Inter Display, podebljano), a tekst u `sans` (Inter).
- Naslov najviše 3 reda, objašnjenje najviše 3 do 4 reda. Ako ne stane, skrati tekst, a ne slova.
- Velika slova samo za kratke oznake u `label`.

## Logo

- Znak je objektiv kamere bez slova: prsten u `accent`, unutrašnjost u `raised` i `deep`, odsjaj u bijeloj.
- `profilna-1080.png` je profilna slika. Instagram je reže u krug, a znak je centriran.
- Na grafikama znak stoji samo u zaglavlju, visine oko 44 px, uz korisničko ime.
- Ne dodaji tekst u profilnu sliku, ne mijenjaj boje znaka i ne stavljaj ga na fotografiju bez `ground` podloge.

## Hashtagovi

Instagram dozvoljava najviše 5 hashtagova po objavi. Uvijek ide ovaj osnovni set od 4, plus jedan tematski:
`#videonadzor #kamere #doboj #bih` + jedan od `#ugradnjakamera #nocnisnimak #sigurnakuca #kamerezakucu #kamerezafirmu`
