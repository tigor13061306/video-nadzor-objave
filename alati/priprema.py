"""Priprema Reelsa bez Igorovog računara (pokreće GitHub Actions, workflow priprema.yml).

Za svaki folder u objave/ koji ima ceka.txt i glas.txt:
1. fotke: ako folder ima fotke.json ({"AI_pf_ime.jpg": "opis fotke"}) i fotka ne postoji u materijal/pf/, napravi je (Gemini);
2. glas: za svaki red glas.txt koji nema materijal/pf/glas/<folder>_N.wav napravi glas (Gemini TTS, glas algieba, stil A),
   odreži tišinu, skrati pauze, atempo 1.1 (pravila/mediji.md, pravila/VODIC.md);
3. render: python3 scenarij.py u folderu objave, provjera videa (1080x1920, H.264 + AAC, 10 do 30 s);
4. cover.jpg (kadar iz 1. s), opis_nacrt.txt -> opis.txt (provjera AI rečenice i najviše 5 hashtagova),
   ceka.txt se premješta u _to_delete/, u planu status "spremno".
Greške idu u stanje/greske.log i kao GitHub issue (mail Igoru). Ključ se nikad ne ispisuje.
"""
import base64, csv, io, json, os, re, shutil, subprocess, sys, time, wave
from datetime import datetime, timedelta, timezone
import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEY = os.environ.get("GEMINI_API_KEY", "").strip()
GH = os.environ.get("GITHUB_TOKEN", "")
REPO = os.environ.get("GITHUB_REPOSITORY", "tigor13061306/video-nadzor-objave")
API = "https://generativelanguage.googleapis.com/v1beta/"
STIL = ("Confident, authoritative senior business consultant presenting to a company's management board. Calm, measured pace, "
        "firm and clear, assured emphasis on key words. Standard Bosnian literary pronunciation, ijekavica, Bosnian accent. "
        "Pronounce every word fully and exactly as written, every syllable, no colloquial shortening or swallowed vowels "
        "(say 'koliko', never 'kolko'). Human and natural, not a radio ad, not robotic.")
FOTO_STIL = ("Photorealistic, like a real phone photo. Modern serious company in Bosnia and Herzegovina. People in the background "
             "blurred by depth of field, logos on devices blurred. No text, no logos, no brands, no faces, no license plates.")
MAX_GLAS, MAX_FOTO = 25, 15  # budžet po pokretanju (pravila/mediji.md)
AI_RECENICA = "Fotografije i glas su napravljeni AI alatom."
AF = ("silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,"
      "silenceremove=stop_periods=-1:stop_duration=0.28:stop_threshold=-42dB,atempo=1.1")

greske, gotovo = [], []
brojac = {"glas": 0, "foto": 0}


def sad():
    return datetime.now(timezone(timedelta(hours=1))).strftime("%Y-%m-%d %H:%M")


def gemini(path, body, pokusaja=3):
    for i in range(pokusaja):
        r = requests.post(API + path, headers={"x-goog-api-key": KEY, "Content-Type": "application/json"},
                          data=json.dumps(body), timeout=300)
        if r.status_code in (429, 500, 503) and i < pokusaja - 1:
            time.sleep(90 * (i + 1)); continue
        j = r.json()
        if r.status_code != 200 or "error" in j:
            raise RuntimeError("Gemini %s: %s" % (r.status_code, json.dumps(j.get("error", j), ensure_ascii=False)[:300]))
        return j


def tts(tekst, izlaz):
    body = {"model": "gemini-3.8-flash-tts",
            "input": [{"type": "user_input", "content": [{"type": "text", "text": tekst,
                                                          "annotations": [{"type": "speech_metadata", "style": STIL}]}]}],
            "response_format": {"type": "audio"}, "generation_config": {"speech_config": [{"voice": "algieba"}]}}
    j = gemini("interactions", body)
    b = base64.b64decode(next(s for s in j["steps"] if s["type"] == "model_output")["content"][0]["data"])
    sirov = izlaz + ".sirov.wav"
    if b[:4] == b"RIFF":
        open(sirov, "wb").write(b)
    else:  # goli PCM 24 kHz, mono, 16 bit
        with wave.open(sirov, "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(24000); w.writeframes(b)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", sirov, "-af", AF, izlaz], check=True)
    os.remove(sirov)


def foto(opis, izlaz):
    body = {"contents": [{"role": "user", "parts": [{"text": opis + "\n\n" + FOTO_STIL}]}],
            "generationConfig": {"responseModalities": ["IMAGE"], "imageConfig": {"aspectRatio": "9:16"}}}
    j = gemini("models/gemini-3.1-flash-image:generateContent", body)
    p = next(p for p in j["candidates"][0]["content"]["parts"] if "inlineData" in p)
    from PIL import Image
    im = Image.open(io.BytesIO(base64.b64decode(p["inlineData"]["data"]))).convert("RGB")
    s = min(1.0, 1920 / max(im.size))
    im.resize((round(im.width * s), round(im.height * s))).save(izlaz, quality=90)


def probe(video):
    j = json.loads(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries",
                                            "stream=codec_type,codec_name,width,height:format=duration", "-of", "json", video]))
    v = [s for s in j["streams"] if s["codec_type"] == "video"]
    a = [s for s in j["streams"] if s["codec_type"] == "audio"]
    pr = []
    if not v or v[0]["codec_name"] != "h264" or (v[0]["width"], v[0]["height"]) != (1080, 1920):
        pr.append("video nije H.264 1080x1920")
    if not a or a[0]["codec_name"] != "aac":
        pr.append("nema AAC zvuka")
    d = float(j["format"]["duration"])
    if not 10 <= d <= 30:
        pr.append("trajanje %.1f s (treba 10 do 30)" % d)
    return d, pr


def plan_spremno(ime):
    p = os.path.join(ROOT, "pravila", "plan_objava.csv")
    redovi = list(csv.reader(open(p, encoding="utf-8"), delimiter=";"))
    for r in redovi[1:]:
        if len(r) > 6 and r[6] == ime and r[5] != "objavljeno":
            r[5] = "spremno"
    with open(p, "w", encoding="utf-8", newline="") as f:
        csv.writer(f, delimiter=";", lineterminator="\n").writerows(redovi)


def pripremi(ime):
    folder = os.path.join(ROOT, "objave", ime)
    recenice = [l.strip() for l in open(os.path.join(folder, "glas.txt"), encoding="utf-8") if l.strip()]
    # 1. fotke
    fj = os.path.join(folder, "fotke.json")
    if os.path.exists(fj):
        for naziv, opis in json.load(open(fj, encoding="utf-8")).items():
            cilj = os.path.join(ROOT, "materijal", "pf", naziv)
            if os.path.exists(cilj):
                continue
            if brojac["foto"] >= MAX_FOTO:
                raise RuntimeError("dostignut sedmični budžet fotki (%d)" % MAX_FOTO)
            foto(opis, cilj); brojac["foto"] += 1
    # 2. glas
    for i, tekst in enumerate(recenice, 1):
        cilj = os.path.join(ROOT, "materijal", "pf", "glas", "%s_%d.wav" % (ime, i))
        if os.path.exists(cilj):
            continue
        if brojac["glas"] >= MAX_GLAS:
            raise RuntimeError("dostignut budžet glasa po pokretanju (%d rečenica)" % MAX_GLAS)
        tts(tekst, cilj); brojac["glas"] += 1
    # 3. render
    subprocess.run([sys.executable, "scenarij.py"], cwd=folder, check=True)
    trajanje, pr = probe(os.path.join(folder, "video.mp4"))
    if pr:
        raise RuntimeError("video: " + ", ".join(pr))
    # 4. cover, opis, ceka.txt
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", "1", "-i", os.path.join(folder, "video.mp4"),
                    "-frames:v", "1", "-q:v", "2", os.path.join(folder, "cover.jpg")], check=True)
    nacrt = os.path.join(folder, "opis_nacrt.txt")
    opis = open(nacrt, encoding="utf-8").read().strip() if os.path.exists(nacrt) else ""
    if not opis:
        raise RuntimeError("nema opis_nacrt.txt")
    if AI_RECENICA not in opis:
        raise RuntimeError("opis nema rečenicu '%s'" % AI_RECENICA)
    if len(re.findall(r"#\w+", opis)) > 5:
        raise RuntimeError("opis ima više od 5 hashtagova")
    for f in ("alt.txt", "ai.txt"):
        if not os.path.exists(os.path.join(folder, f)):
            raise RuntimeError("nema " + f)
    open(os.path.join(folder, "opis.txt"), "w", encoding="utf-8").write(opis + "\n")
    kanta = os.path.join(ROOT, "_to_delete", "objave", ime)
    os.makedirs(kanta, exist_ok=True)
    shutil.move(os.path.join(folder, "ceka.txt"), os.path.join(kanta, "ceka.txt"))
    plan_spremno(ime)
    gotovo.append("%s (%.1f s)" % (ime, trajanje))


def javi(naslov, tekst):
    if not GH:
        return
    h = {"Authorization": "Bearer " + GH, "Accept": "application/vnd.github+json"}
    try:
        requests.post("https://api.github.com/repos/%s/issues" % REPO, headers=h, timeout=60,
                      json={"title": naslov, "body": tekst})
    except Exception:
        pass


def main():
    danas = datetime.now(timezone(timedelta(hours=1))).strftime("%Y-%m-%d")
    fol = [f for f in sorted(os.listdir(os.path.join(ROOT, "objave")))
           if f[:10] >= danas and os.path.exists(os.path.join(ROOT, "objave", f, "ceka.txt"))
           and os.path.exists(os.path.join(ROOT, "objave", f, "glas.txt"))]
    if not fol:
        print("Nema foldera koji čekaju."); return
    if not KEY:
        greske.append("GitHub Secret GEMINI_API_KEY nije postavljen (Settings > Secrets and variables > Actions).")
    else:
        for ime in fol:
            try:
                pripremi(ime)
            except Exception as e:
                greske.append("%s: %s" % (ime, str(e).replace(KEY, "***")[:400]))
    print("Gotovo:", gotovo); print("Greške:", greske)
    log = os.path.join(ROOT, "stanje", "greske.log")
    with open(log, "a", encoding="utf-8") as f:
        f.write("%s Priprema (GitHub): gotovo %s; glas %d, fotke %d; greške: %s\n" % (
            sad(), ", ".join(gotovo) or "ništa", brojac["glas"], brojac["foto"], " | ".join(greske) or "nema"))
    if greske:
        javi("Priprema Reelsa: greška " + sad(), "Spremno: %s\n\nGreške:\n- %s\n\nDetalji u stanje/greske.log."
             % (", ".join(gotovo) or "ništa", "\n- ".join(greske)))


if __name__ == "__main__":
    main()
