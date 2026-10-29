# Pravljenje fotografija preko Gemini API-ja

Ključevi (tajno, nikad na GitHub ni u poruke): `alati/gemini_kljuc.txt` i `alati/github_kljuc.txt` (GitHub ključ može pisati samo u repozitorij `video-nadzor-objave`).

## Zašto preko preglednika

Mreža iz Claude okruženja ne dopušta pozive na Google. Zato se slika pravi u ugrađenom pregledniku Claude desktop aplikacije, na stranici `https://generativelanguage.googleapis.com/`, a odmah se šalje na GitHub u `materijal/ulaz/`. Odatle se preuzima u `02_materijal/odobreno` sa `https://raw.githubusercontent.com/tigor13061306/video-nadzor-objave/main/materijal/ulaz/<ime>.jpg`.

## Pravila

- Model: `gemini-3.1-flash-image`. Format 4:5 za objave, 16:9 za prikaze kamere.
- Opisi na engleskom, po uzoru na `prompti/gemini_prompti.md`: fotorealistično, Balkan, bez teksta, logotipa, lica, tablica i kućnih brojeva.
- Ime fajla uvijek počinje sa `AI_`.
- Najviše 20 slika sedmično (budžet je 5 dolara mjesečno). Oprema srijedom koristi zvanične slike, ne Gemini. Ako slika ne valja, najviše jedan novi pokušaj.
- Svaku sliku pogledaj prije upotrebe; ako ima tekst, čudne ruke, američke utičnice ili nešto što ne liči na naše krajeve, ne koristi je.
- Oprema mora biti realna za video nadzor: za snimač i mrežu uski 10-inčni zidni rack (oko 30 cm, 6U), kablovi kroz kanalicu, evropske utičnice. Nikad veliki 19-inčni serverski ormari ni američke utičnice.
- Montaža kamere mora izgledati kao pravi profesionalni posao (Igorovo pravilo):
  - kablovi se nikad ne vide: kabl ide kroz zid, a kamera sjedi na razvodnoj kutiji iste boje; nikakvi kablovi po fasadi, strehi ni zidu;
  - kamera nikad iznad vrata ni na/iznad nadstrešnice; za ulaz ide na zid pored vrata, oko 2,5 do 3 m, okrenuta prema mjestu gdje stoji osoba, da se vidi lice;
  - u opis za Gemini uvijek dodaj: "mounted on a matching junction box, no cables visible anywhere, cable hidden inside the wall, not above the door canopy".
  - Ako na gotovoj slici vidiš kabl ili kameru iznad vrata/nadstrešnice, ne koristi je.
- Par dan/noć: drugu sliku pravi u istom razgovoru (pošalji prethodni odgovor kao historiju), da kadar ostane isti.
- Svaki poziv neka bude kratak: pokreni posao u pozadini, rezultat čuvaj u `window.LOG`, pa ga provjeri drugim pozivom (alat ima ograničenje od 45 sekundi).

## JavaScript (na stranici https://generativelanguage.googleapis.com/)

```js
window.GK = '<iz gemini_kljuc.txt>';
window.GH = '<iz github_kljuc.txt>';
window.REPO = 'https://api.github.com/repos/tigor13061306/video-nadzor-objave/contents/';
window.gen = async (prompt, aspect, history) => {
  const contents = (history || []).concat([{role: 'user', parts: [{text: prompt}]}]);
  const r = await fetch('https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image:generateContent', {method: 'POST', headers: {'x-goog-api-key': window.GK, 'Content-Type': 'application/json'}, body: JSON.stringify({contents, generationConfig: {responseModalities: ['IMAGE'], imageConfig: {aspectRatio: aspect}}})});
  const j = await r.json(); if (j.error) throw new Error(j.error.message.slice(0, 200));
  const c = j.candidates[0].content; const p = c.parts.find(p => p.inlineData);
  return {b64: p.inlineData.data, mime: p.inlineData.mimeType, history: contents.concat([c])};
};
window.shrink = async (b64, mime) => {
  const img = new Image(); img.src = 'data:' + mime + ';base64,' + b64; await img.decode();
  const s = Math.min(1, 1600 / Math.max(img.width, img.height)); const cv = document.createElement('canvas');
  cv.width = Math.round(img.width * s); cv.height = Math.round(img.height * s);
  cv.getContext('2d').drawImage(img, 0, 0, cv.width, cv.height); return cv.toDataURL('image/jpeg', 0.86).split(',')[1];
};
window.push = async (path, b64, msg) => {
  const h = {Authorization: 'Bearer ' + window.GH, Accept: 'application/vnd.github+json'};
  let sha; const g = await fetch(window.REPO + path, {headers: h}); if (g.ok) sha = (await g.json()).sha;
  const r = await fetch(window.REPO + path, {method: 'PUT', headers: h, body: JSON.stringify({message: msg || ('Materijal ' + path), content: b64, sha})});
  const j = await r.json(); return r.ok ? j.content.path : 'ERR ' + r.status + ' ' + (j.message || '');
};
// primjer, pa provjera window.LOG u sljedećem pozivu:
window.LOG = [];
(async () => { try {
  const d = await window.gen('<opis>', '4:5');
  window.LOG.push(await window.push('materijal/ulaz/AI_<ime>.jpg', await window.shrink(d.b64, d.mime)));
} catch (e) { window.LOG.push('ERR ' + e.message); } })();
```
