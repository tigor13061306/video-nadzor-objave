"""Provjerava nove komentare na objavama i upisuje ih u stanje/komentari.json.

Ako ima novih komentara bez odgovora, otvara (ili dopunjava) GitHub issue "Novi komentari",
pa vlasnik repozitorija dobije mail. Claude ih čita i odgovara kad je računar upaljen.
"""
import json, os, requests

IG = "17841415178280849"
V = "https://graph.instagram.com/v23.0/"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = os.path.join(ROOT, "stanje", "komentari.json")
REPO = "tigor13061306/video-nadzor-objave"


def main():
    h = {"Authorization": "Bearer " + os.environ["IG_TOKEN"].strip()}
    stanje = json.load(open(F, encoding="utf-8")) if os.path.exists(F) else {}
    mediji = requests.get(V + IG + "/media", headers=h, params={"fields": "id,permalink", "limit": 30}, timeout=60).json().get("data", [])
    novi = []
    for m in mediji:
        kom = requests.get(V + m["id"] + "/comments", headers=h,
                           params={"fields": "id,text,username,timestamp,replies{username}"}, timeout=60).json().get("data", [])
        for k in kom:
            if k["username"] == "video.nadzorkamere" or k["id"] in stanje:
                continue
            odgovoreno = any(r.get("username") == "video.nadzorkamere" for r in k.get("replies", {}).get("data", []))
            stanje[k["id"]] = {"objava": m["permalink"], "media_id": m["id"], "korisnik": k["username"],
                               "tekst": k["text"], "vrijeme": k["timestamp"], "odgovoreno": odgovoreno}
            if not odgovoreno:
                novi.append(stanje[k["id"]])
    os.makedirs(os.path.dirname(F), exist_ok=True)
    json.dump(stanje, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("novih komentara:", len(novi))
    gt = os.environ.get("GITHUB_TOKEN")
    if novi and gt:
        gh = {"Authorization": "Bearer " + gt, "Accept": "application/vnd.github+json"}
        tijelo = "\n".join("- @%s: %s (%s)" % (n["korisnik"], n["tekst"][:200], n["objava"]) for n in novi)
        otvoreni = requests.get(f"https://api.github.com/repos/{REPO}/issues", headers=gh,
                                params={"state": "open", "labels": "komentari"}, timeout=60).json()
        if otvoreni:
            requests.post(otvoreni[0]["comments_url"], headers=gh, json={"body": tijelo}, timeout=60)
        else:
            requests.post(f"https://api.github.com/repos/{REPO}/issues", headers=gh, timeout=60,
                          json={"title": "Novi komentari na Instagramu", "body": tijelo, "labels": ["komentari"]})


if __name__ == "__main__":
    main()
