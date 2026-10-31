"""Provjerava nove komentare na objavama i upisuje ih u stanje/komentari.json.

- Komentar sa brojem telefona: sakrije se (da broj ne bude javan), označi kao UPIT i Igor dobije mail odmah.
- Komentar sa riječju KAMERA (poziv iz objave "Napiši KAMERA u komentar") ili koji pita za cijenu, ponudu, ugradnju ili izlazak: označi se kao UPIT (mail Igoru).
- Ostali novi komentari: GitHub issue "Novi komentari" (mail), a Claude odgovara kad je računar upaljen.
"""
import json, os, re, requests

IG = "17841415178280849"
V = "https://graph.instagram.com/v23.0/"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = os.path.join(ROOT, "stanje", "komentari.json")
REPO = "tigor13061306/video-nadzor-objave"
TELEFON = re.compile(r"(\+?387|\b0)\s*6\d[\s/.-]*\d{3}[\s/.-]*\d{3,4}")
UPIT = re.compile(r"\bkamer|cijen|cena|košt|kost|ponud|ugrad|postav|montir|izlaz|teren|kontakt|broj|nazov|pozov|zainteres|treba mi|trebam|koliko", re.I)


def issue(gh, naslov, oznaka, tijelo):
    otvoreni = requests.get(f"https://api.github.com/repos/{REPO}/issues", headers=gh,
                            params={"state": "open", "labels": oznaka}, timeout=60).json()
    if isinstance(otvoreni, list) and otvoreni:
        requests.post(otvoreni[0]["comments_url"], headers=gh, json={"body": tijelo}, timeout=60)
    else:
        requests.post(f"https://api.github.com/repos/{REPO}/issues", headers=gh, timeout=60,
                      json={"title": naslov, "body": tijelo, "labels": [oznaka]})


def main():
    h = {"Authorization": "Bearer " + os.environ["IG_TOKEN"].strip()}
    stanje = json.load(open(F, encoding="utf-8")) if os.path.exists(F) else {}
    mediji = requests.get(V + IG + "/media", headers=h, params={"fields": "id,permalink", "limit": 30}, timeout=60).json().get("data", [])
    novi, upiti = [], []
    for m in mediji:
        kom = requests.get(V + m["id"] + "/comments", headers=h,
                           params={"fields": "id,text,username,timestamp,replies{username}"}, timeout=60).json().get("data", [])
        for k in kom:
            if k["username"] == "video.nadzorkamere" or k["id"] in stanje:
                continue
            odgovoreno = any(r.get("username") == "video.nadzorkamere" for r in k.get("replies", {}).get("data", []))
            z = {"objava": m["permalink"], "media_id": m["id"], "korisnik": k["username"],
                 "tekst": k["text"], "vrijeme": k["timestamp"], "odgovoreno": odgovoreno}
            if TELEFON.search(k["text"]):
                r = requests.post(V + k["id"], headers=h, data={"hide": "true"}, timeout=60).json()
                z["upit"] = True
                z["sakriven"] = bool(r.get("success"))
            elif UPIT.search(k["text"]):
                z["upit"] = True
            stanje[k["id"]] = z
            if z.get("upit"):
                upiti.append(z)
            elif not odgovoreno:
                novi.append(z)
    os.makedirs(os.path.dirname(F), exist_ok=True)
    json.dump(stanje, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("novih komentara:", len(novi), "upita:", len(upiti))
    gt = os.environ.get("GITHUB_TOKEN")
    if not gt:
        return
    gh = {"Authorization": "Bearer " + gt, "Accept": "application/vnd.github+json"}
    if upiti:
        tijelo = "\n".join("- @%s: %s%s (%s)" % (u["korisnik"], u["tekst"][:300],
                                                 " — komentar sakriven jer ima broj telefona" if u.get("sakriven") else "",
                                                 u["objava"]) for u in upiti)
        issue(gh, "UPIT: neko želi ugradnju ili ponudu", "upit", "Nazovi ili odgovori u DM:\n" + tijelo)
    if novi:
        tijelo = "\n".join("- @%s: %s (%s)" % (n["korisnik"], n["tekst"][:200], n["objava"]) for n in novi)
        issue(gh, "Novi komentari na Instagramu", "komentari", tijelo)


if __name__ == "__main__":
    main()
