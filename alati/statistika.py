"""Statistika objava @pametnija.firma: Instagram Reel metrike + Facebook video metrike (sa krivom zadržavanja).
Rezultat ide u stanje/statistika.json. Pokreće .github/workflows/statistika.yml."""
import json, os, datetime as dt
import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IG_V = "https://graph.instagram.com/v23.0/"
FB_V = "https://graph.facebook.com/v23.0/"
IG_METRIKE = ["views", "reach", "likes", "comments", "shares", "saved", "total_interactions",
              "ig_reels_avg_watch_time", "ig_reels_video_view_total_time", "follows", "profile_visits"]
FB_METRIKE = ["total_video_views", "total_video_views_unique", "total_video_avg_time_watched",
              "total_video_complete_views", "total_video_impressions", "total_video_10s_views",
              "total_video_retention_graph", "total_video_view_total_time"]


def jedna(url, tok, metric):
    r = requests.get(url, params={"metric": metric, "access_token": tok}, timeout=30)
    j = r.json()
    if "error" in j:
        return {"greska": j["error"].get("message", "")[:150]}
    d = j.get("data", [])
    if not d:
        return None
    vals = d[0].get("values") or [{}]
    return d[0].get("total_value", {}).get("value", vals[0].get("value"))


def main():
    ig, fb, pid = (os.environ.get(k, "").strip() for k in ("IG_TOKEN", "FB_PAGE_TOKEN", "FB_PAGE_ID"))
    objave = json.load(open(os.path.join(ROOT, "stanje", "objavljeno.json"), encoding="utf-8"))
    out = {"vrijeme": dt.datetime.utcnow().isoformat(timespec="minutes") + "Z", "objave": {}}
    try:
        out["profil"] = requests.get(IG_V + "me", params={"fields": "username,followers_count,media_count",
                                                          "access_token": ig}, timeout=30).json()
    except Exception as e:
        out["profil"] = {"greska": str(e)}
    for ime, v in objave.items():
        o = {"link": v.get("link"), "objavljeno": v.get("vrijeme"), "ig": {}, "fb": {}}
        if v.get("id"):
            for m in IG_METRIKE:
                o["ig"][m] = jedna(IG_V + v["id"] + "/insights", ig, m)
        fbid = str(v.get("facebook", "")).replace("ok", "").strip()
        if fbid and fb:
            for m in FB_METRIKE:
                o["fb"][m] = jedna(FB_V + fbid + "/video_insights", fb, m)
            if all(isinstance(x, dict) and "greska" in x for x in o["fb"].values()):
                o["fb"]["post"] = requests.get(FB_V + fbid, params={"fields": "id,permalink_url,length,views",
                                                                    "access_token": fb}, timeout=30).json()
        out["objave"][ime] = o
        print(ime, json.dumps(o["ig"], ensure_ascii=False)[:300])
    json.dump(out, open(os.path.join(ROOT, "stanje", "statistika.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
