"""Jednokratno: trajno briše objave sa Instagram profila i Facebook stranice (Igorov zahtjev 20.11.2026, rebrend).
Instagram: sve objave koje API vrati za nalog. Facebook: samo objave iz stanje/objavljeno.json (slike profila i naslovne ostaju).
Upotreba: python obrisi_sve.py <limit>   (0 = sve)"""
import json, os, sys, requests
lim = int(sys.argv[1]) if len(sys.argv) > 1 else 1
IG = "https://graph.instagram.com/v24.0/"; FB = "https://graph.facebook.com/v24.0/"
h = {"Authorization": "Bearer " + os.environ["IG_TOKEN"].strip()}
fh = {"Authorization": "Bearer " + os.environ["FB_PAGE_TOKEN"].strip()}
log = []
ids, url, p = [], IG + "me/media", {"fields": "id,timestamp,media_type,permalink", "limit": 50}
while url:
    j = requests.get(url, headers=h, params=p, timeout=60).json(); p = None
    if "error" in j: log.append("IG lista: %s" % j["error"].get("message")); break
    ids += j.get("data", []); url = j.get("paging", {}).get("next")
ids.sort(key=lambda m: m["timestamp"])
log.append("IG objava na profilu: %d" % len(ids))
n = 0
for m in ids:
    if lim and n >= lim: break
    r = requests.delete(IG + m["id"], headers=h, timeout=60)
    log.append("IG %s %s %s -> %s %s" % (m["timestamp"][:10], m["media_type"], m.get("permalink", ""), r.status_code, r.text[:200]))
    n += 1
stanje = json.load(open("stanje/objavljeno.json"))
fbids = []
for ime, v in sorted(stanje.items()):
    f = str(v.get("facebook", ""))
    if f.startswith("ok "): fbids.append((ime, f.split()[1]))
log.append("FB objava iz objavljeno.json: %d" % len(fbids))
for k, (ime, fid) in enumerate(fbids):
    if lim and k >= lim: break
    r = requests.delete(FB + fid, headers=fh, timeout=60)
    log.append("FB %s %s -> %s %s" % (ime, fid, r.status_code, r.text[:200]))
os.makedirs("stanje", exist_ok=True)
open("stanje/brisanje_log.txt", "a").write("\n".join(log) + "\n---\n")
print("\n".join(log))
