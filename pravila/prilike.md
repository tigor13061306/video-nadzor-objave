# Prilike za savjet: prijedlozi komentara uz Igorovo odobrenje (od 20.11.2026)

Igorovo pravilo: u grupama i tuđim objavama NIŠTA se ne komentariše bez njegovog odobrenja. Claude samo pronađe priliku i predloži komentar.

## Šta je prilika
Objava ili oglas iz BiH i regije (zadnjih 7 dana) gdje vlasnik firme ili čovjek iz firme pita ili se žali na nešto iz naše oblasti:
Excel i tabele, poslovni programi (Pantheon, kase, fakturisanje), automatizacija i botovi (Viber, WhatsApp), AI za posao, internet i mreža u firmi (WiFi, ruter, pristup izvana), backup i gubitak podataka, nadzor sistema (server, internet, kase), lažni mailovi i sigurnost, IT podrška za malu firmu.
Ne: konkurencija koja nudi usluge, politika, privatne svađe, objave o tuđoj nesreći ili provali (tu se ne komentariše), objave starije od 7 dana.

## Izvori
- Facebook grupe za preduzetnike, mali biznis, računovođe, trgovce, ugostitelje i IT pomoć (računar, ugrađeni preglednik, kao stranica "Pametnija firma"); i facebook.com/search/posts, Nedavne objave.
- Javni web iz oblaka: OLX (oglasi u kojima neko TRAŽI: IT podršku, programera, Excel, održavanje računara, mrežu, kase), lokalni portali i forumi.

## Prijedlog komentara
- Koristan savjet na samo pitanje, 2 do 4 rečenice, sa "vi", bez reklame, bez linka, bez cijena i obećanja. Na kraju najviše: "Ako treba, pišite nam u poruke." (samo ako je jasno da firma traži rješenje).
- Za OLX i slično gdje se ne komentariše: prijedlog kratke prve poruke u ime stranice.
- Nikad lični podaci (brojevi telefona, adrese) u prijedlogu ni u poruci Igoru; samo link, grupa, kratak citat (do 200 znakova).

## Tok odobravanja
1. Prilike idu u stanje/prilike.json na GitHubu: {"id": "P-GGGGMMDD-N", "datum", "izvor", "grupa", "link", "citat", "prijedlog", "status": "čeka", "napomena"}.
2. Claude pošalje Igoru poruku: za svaku priliku broj (id), gdje je, šta pita, link i predloženi komentar. Najviše 5 dnevno, najbolje prve.
3. Igor u razgovoru sa Claudeom kaže npr. "odobri P-20261121-1 i -3, odbij -2" ili ispravi tekst. Claude tada upiše status "odobreno" (sa Igorovim tekstom ako ga je mijenjao) ili "odbijeno". Ako je računar upaljen, Claude odobreni komentar odmah objavi kao stranica i upiše "objavljeno" sa datumom.
4. Dnevni zadatak (računar, 18:21) objavi sve sa statusom "odobreno" koje još nisu objavljene i upiše "objavljeno".
5. Prilika bez odgovora 4 dana postaje "isteklo". Igorove odluke Claude koristi da bolje bira (šta odbija, šta prihvata).
