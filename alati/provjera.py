"""Provjera ključeva bez objavljivanja: Instagram i Facebook stranica."""
import os, requests
ig = requests.get("https://graph.instagram.com/v23.0/me", params={"fields": "username"},
                  headers={"Authorization": "Bearer " + os.environ["IG_TOKEN"].strip()}, timeout=30).json()
print("Instagram:", ig.get("username") or ig.get("error", {}).get("message"))
fb = requests.get("https://graph.facebook.com/v23.0/" + os.environ["FB_PAGE_ID"].strip(), params={"fields": "name,followers_count"},
                  headers={"Authorization": "Bearer " + os.environ["FB_PAGE_TOKEN"].strip()}, timeout=30).json()
print("Facebook:", fb.get("name") or fb.get("error", {}).get("message"))
if "error" in ig or "error" in fb:
    raise SystemExit(1)
