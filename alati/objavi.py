"""Dnevna objava na Instagram (@video.nadzorkamere), pokreće je GitHub Actions.

- Objavljuje svaki folder objave/GGGG-MM-DD_tema/ čiji je datum danas ili ranije,
  a nije upisan u stanje/objavljeno.json (tako se propuštene objave same nadoknade).
- Objava: video.mp4 = Reel; inače 01.jpg, 02.jpg… (jedna slika ili carousel).
- Opis iz opis.txt; red "[Pri objavi uključi AI info]" postaje AI napomena.
- Poslije objave Story "Nova objava" (story.jpg; ako ga nema, pravi se iz 01.jpg ili cover.jpg).
- Danas objavljuje tek od 17:40 po bosanskom vremenu.

Ključ: varijabla okruženja IG_TOKEN (GitHub Secret). Ključ nikad ne ide u adresu ni u log.
"""
import datetime as dt, json, os, re, subprocess, sys, time
from zoneinfo import ZoneInfo
import requests

IG = "17841415178280849"
V = "https://graph.instagram.com/v23.0/"
RAW = "https://raw.githubusercontent.com/tigor13061306/video-nadzor-objave/main/"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STANJE = os.path.join(ROOT, "stanje", "objavljeno.json")
AI_RED = "[Pri objavi uključi AI info]"
AI_TEKST = "Fotografije su ilustrativne, napravljene AI alatom."
NAJRANIJE = dt.time(17, 40)
MAX_NADOKNADA_DANA = 7


def log(*a):
    print(*a, flush=True)


class IGApi:
    def __init__(self, token):
        self.h = {"Authorization": "Bearer " + token}

    def get(self, path, **params):
        r = requests.get(V + path, headers=self.h, params=params, timeout=60)
        return r.json()

    def post(self, path, **data):
        r = requests.post(V + path, headers=self.h, data=data, timeout=120)
        return r.json()

    def cekaj(self, cid, maks=300):
        kraj = time.time() + maks
        while time.time() < kraj:
            st = self.get(cid, fields="status_code").get("status_code")
            if st in ("FINISHED", "ERROR", "EXPIRED"):
                return st
            time.sleep(5)
        return "TIMEOUT"


def git(*args):
    subprocess.run(["git", "-C", ROOT] + list(args), check=True)


def push(poruka):
    git("add", "-A", "stanje", "objave")
    if subprocess.run(["git", "-C", ROOT, "diff", "--cached", "--quiet"]).returncode == 0:
        return
    git("commit", "-q", "-m", poruka)
    for _ in range(3):
        if subprocess.run(["git", "-C", ROOT, "push", "-q"]).returncode == 0:
            return
        git("pull", "-q", "--rebase")
    raise SystemExit("git push nije uspio")


def cekaj_javno(url, maks=120):
    kraj = time.time() + maks
    while time.time() < kraj:
        if requests.head(url, timeout=30).status_code == 200:
            return True
        time.sleep(5)
    return False


def opis(folder):
    t = open(os.path.join(folder, "opis.txt"), encoding="utf-8").read().strip()
    t = t.replace(AI_RED, AI_TEKST)
    tagovi = re.findall(r"#\w+", t)
    if len(tagovi) > 5:  # Instagram pravilo: najviše 5
        for tag in tagovi[5:]:
            t = t.replace(" " + tag, "").replace(tag, "")
    return t


def objavi_folder(api, ime):
    folder = os.path.join(ROOT, "objave", ime)
    base = RAW + "objave/" + ime + "/"
    tekst = opis(folder)
    if os.path.exists(os.path.join(folder, "video.mp4")):
        params = {"media_type": "REELS", "video_url": base + "video.mp4", "caption": tekst, "share_to_feed": "true"}
        if os.path.exists(os.path.join(folder, "cover.jpg")):
            params["cover_url"] = base + "cover.jpg"
        c = api.post(IG + "/media", **params)
        vrsta, prva = "reel", "cover.jpg"
    else:
        slike = sorted(f for f in os.listdir(folder) if re.fullmatch(r"\d\d\.jpg", f))
        if not slike:
            raise RuntimeError("nema slika (01.jpg…)")
        if len(slike) == 1:
            c = api.post(IG + "/media", image_url=base + slike[0], caption=tekst)
        else:
            djeca = []
            for s in slike:
                d = api.post(IG + "/media", image_url=base + s, is_carousel_item="true")
                if "id" not in d:
                    raise RuntimeError("slika %s: %s" % (s, d.get("error", d)))
                djeca.append(d["id"])
            c = api.post(IG + "/media", media_type="CAROUSEL", children=",".join(djeca), caption=tekst)
        vrsta, prva = ("carousel" if len(slike) > 1 else "slika"), slike[0]
    if "id" not in c:
        raise RuntimeError("kontejner: %s" % c.get("error", c))
    st = api.cekaj(c["id"])
    if st != "FINISHED":
        raise RuntimeError("obrada: " + st)
    pub = api.post(IG + "/media_publish", creation_id=c["id"])
    if "id" not in pub:
        raise RuntimeError("objava: %s" % pub.get("error", pub))
    link = api.get(pub["id"], fields="permalink").get("permalink", "")
    log("objavljeno:", ime, vrsta, link)
    return {"id": pub["id"], "link": link, "vrsta": vrsta, "prva": prva}


def story(api, ime, prva):
    folder = os.path.join(ROOT, "objave", ime)
    sp = os.path.join(folder, "story.jpg")
    if not os.path.exists(sp):
        subprocess.run([sys.executable, os.path.join(ROOT, "alati", "napravi_story.py"),
                        os.path.join(folder, prva), sp], check=True)
        push("Story za " + ime)
    url = RAW + "objave/" + ime + "/story.jpg"
    if not cekaj_javno(url):
        return "story.jpg nije javno dostupan"
    c = api.post(IG + "/media", image_url=url, media_type="STORIES")
    if "id" not in c:
        return "story kontejner: %s" % c.get("error", c)
    if api.cekaj(c["id"], 120) != "FINISHED":
        return "story obrada nije završena"
    p = api.post(IG + "/media_publish", creation_id=c["id"])
    return "ok" if "id" in p else "story objava: %s" % p.get("error", p)


def main():
    token = os.environ.get("IG_TOKEN", "").strip()
    if not token:
        raise SystemExit("Nema IG_TOKEN")
    sada = dt.datetime.now(ZoneInfo("Europe/Sarajevo"))
    danas = sada.date()
    stanje = json.load(open(STANJE, encoding="utf-8")) if os.path.exists(STANJE) else {}
    kandidati = []
    for ime in sorted(os.listdir(os.path.join(ROOT, "objave"))):
        m = re.match(r"(\d{4}-\d{2}-\d{2})_", ime)
        if not m or ime in stanje or not os.path.exists(os.path.join(ROOT, "objave", ime, "opis.txt")):
            continue
        d = dt.date.fromisoformat(m.group(1))
        if d > danas or (d == danas and sada.time() < NAJRANIJE):
            continue
        if (danas - d).days > MAX_NADOKNADA_DANA:
            log("preskačem staru objavu (više od 7 dana):", ime)
            continue
        kandidati.append(ime)
    if not kandidati:
        log("nema objava za danas")
        return
    api = IGApi(token)
    nedavne = api.get(IG + "/media", fields="caption,permalink", limit=25).get("data", [])
    greske = []
    for ime in kandidati:
        # zaštita od duplog objavljivanja (npr. ako je objavu već objavio Claude sa računara)
        pocetak = opis(os.path.join(ROOT, "objave", ime))[:60]
        vec = next((m for m in nedavne if (m.get("caption") or "").startswith(pocetak)), None)
        if vec:
            log("već objavljeno, samo upisujem:", ime, vec.get("permalink"))
            stanje[ime] = {"link": vec.get("permalink", ""), "vrsta": "?", "story": "?", "naknadno": False, "napomena": "objavljeno van GitHuba"}
            os.makedirs(os.path.dirname(STANJE), exist_ok=True)
            json.dump(stanje, open(STANJE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
            push("Upisano: " + ime)
            continue
        try:
            r = objavi_folder(api, ime)
        except Exception as e:
            greske.append("%s: %s" % (ime, e))
            log("GREŠKA", ime, e)
            break  # ne nastavljaj sa ostalim; sljedeće pokretanje pokušava ponovo
        r["story"] = story(api, ime, r.pop("prva"))
        r["vrijeme"] = dt.datetime.now(ZoneInfo("Europe/Sarajevo")).isoformat(timespec="minutes")
        r["naknadno"] = not ime.startswith(danas.isoformat())
        stanje[ime] = r
        os.makedirs(os.path.dirname(STANJE), exist_ok=True)
        json.dump(stanje, open(STANJE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        push("Objavljeno: " + ime)
        log("story:", r["story"])
    if greske:
        raise SystemExit("Greške: " + "; ".join(greske))


if __name__ == "__main__":
    main()
