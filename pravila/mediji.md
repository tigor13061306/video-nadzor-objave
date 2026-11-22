# Fotke i glas preko Gemini API-ja (@pametnija.firma)

Ključevi (tajno, nikad na GitHub ni u poruke): na Igorovom računaru `C:\claude\video nadzor\Instagram_video_nadzor\alati\gemini_kljuc.txt` i `github_kljuc.txt`. Igor je dao trajno odobrenje da se čitaju.

Mreža iz Claude okruženja ne doseže Google, zato se sve radi u UGRAĐENOM PREGLEDNIKU Claude aplikacije na stranici `https://generativelanguage.googleapis.com/` (javascript), a rezultat se odmah šalje na GitHub (`materijal/pf/...`) i odatle preuzima (`gh api ... -H "Accept: application/vnd.github.raw"` ili raw adresa sa SHA commita).

Budžet: Google AI Studio projekat ima upozorenje na 5 $ mjesečno. Sedmično najviše 15 fotki i 25 rečenica glasa. Ako fotka ne valja, najviše jedan novi pokušaj.

## Fotke
- Model `gemini-3.1-flash-image`, format 9:16 za Reel.
- Fotorealistično, mali grad u BiH, evropski izgled, kao prava fotka telefonom. Bez teksta, logotipa, brendova, lica i tablica.
- Više kadrova istog mjesta: u istom razgovoru (prethodni odgovor kao historija).
- Svaku fotku pogledaj prije upotrebe; natpise i brendove ne koristi ili ih isjeci zumom.

## Glas
- Model `gemini-3.8-flash-tts` preko `POST /v1beta/interactions`, glas `algieba` (Igorov izbor), WAV 24 kHz.
- Stil (od 22.11.2026, autoritativniji i korporativni; Igor bira između uzoraka A/B/C u materijal/pf/glas/uzorak_korp_*.wav, dok ne izabere koristi se A): "Confident, authoritative senior business consultant presenting to a company's management board. Calm, measured pace, firm and clear, assured emphasis on key words. Standard Bosnian literary pronunciation, ijekavica, Bosnian accent. Pronounce every word fully and exactly as written, every syllable, no colloquial shortening or swallowed vowels (say 'koliko', never 'kolko'). Human and natural, not a radio ad, not robotic."
- Stari stil (do 21.11., "kafanski", gutao slova, npr. "kolko"): više se ne koristi.
- Tekst glasa: ijekavica, kratke rečenice, riječi koje se izgovaraju (brojevi slovima ako treba, bez VELIKIH slova).
- Poslije preuzimanja odreži tišinu: `ffmpeg -i in.wav -af "silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse" out.wav`

## JavaScript (na stranici https://generativelanguage.googleapis.com/)
Poziv alata traje najviše ~45 s: posao pokreni u pozadini, rezultat čuvaj u `window.LOG`, provjeri drugim pozivom.
```js
window.GK = '<gemini_kljuc.txt>'; window.GH = '<github_kljuc.txt>';
window.REPO = 'https://api.github.com/repos/tigor13061306/video-nadzor-objave/contents/';
window.gen = async (prompt, aspect, history) => {
  const contents = (history || []).concat([{role: 'user', parts: [{text: prompt}]}]);
  const r = await fetch('https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image:generateContent', {method: 'POST', headers: {'x-goog-api-key': window.GK, 'Content-Type': 'application/json'}, body: JSON.stringify({contents, generationConfig: {responseModalities: ['IMAGE'], imageConfig: {aspectRatio: aspect}}})});
  const j = await r.json(); if (j.error) throw new Error(r.status + ' ' + j.error.message.slice(0, 200));
  const c = j.candidates[0].content; const p = c.parts.find(p => p.inlineData);
  return {b64: p.inlineData.data, mime: p.inlineData.mimeType, history: contents.concat([c])};
};
window.tts = async (text, voice, style) => {
  const body = {model: 'gemini-3.8-flash-tts', input: [{type: 'user_input', content: [{type: 'text', text, annotations: [{type: 'speech_metadata', style}]}]}], response_format: {type: 'audio'}, generation_config: {speech_config: [{voice}]}};
  const r = await fetch('https://generativelanguage.googleapis.com/v1beta/interactions', {method: 'POST', headers: {'x-goog-api-key': window.GK, 'Content-Type': 'application/json'}, body: JSON.stringify(body)});
  const j = await r.json(); if (j.error) throw new Error(r.status + ' ' + JSON.stringify(j.error).slice(0, 300));
  return j.steps.find(s => s.type === 'model_output').content[0].data;  // base64 WAV
};
window.shrink = async (b64, mime) => { const img = new Image(); img.src = 'data:' + mime + ';base64,' + b64; await img.decode();
  const s = Math.min(1, 1920 / Math.max(img.width, img.height)); const cv = document.createElement('canvas');
  cv.width = Math.round(img.width * s); cv.height = Math.round(img.height * s);
  cv.getContext('2d').drawImage(img, 0, 0, cv.width, cv.height); return cv.toDataURL('image/jpeg', 0.9).split(',')[1]; };
window.push = async (path, b64, msg) => { const h = {Authorization: 'Bearer ' + window.GH, Accept: 'application/vnd.github+json'};
  let sha; const g = await fetch(window.REPO + path, {headers: h}); if (g.ok) sha = (await g.json()).sha;
  const r = await fetch(window.REPO + path, {method: 'PUT', headers: h, body: JSON.stringify({message: msg || ('Materijal ' + path), content: b64, sha})});
  const j = await r.json(); return r.ok ? j.content.path : 'ERR ' + r.status + ' ' + (j.message || ''); };
window.Q = Promise.resolve(); window.qpush = (p, b, m) => { const x = window.Q.then(() => window.push(p, b, m)); window.Q = x.catch(() => {}); return x; };
// fotka: const d = await gen(opis, '9:16'); await qpush('materijal/pf/AI_pf_ime.jpg', await shrink(d.b64, d.mime));
// glas:  await qpush('materijal/pf/glas/<folder>_1.wav', await tts('Rečenica.', 'algieba', STIL));
```
Push-evi idu jedan za drugim (`qpush`), inače GitHub vraća 409.

## Kad Gemini ne radi
Tačnu grešku (status i poruku, bez ključa) upiši u stanje/greske.log i javi Igoru. Ne pravi tekstualne objave kao zamjenu; ako nema materijala, objava tog dana izostaje i Igor dobija poruku.
