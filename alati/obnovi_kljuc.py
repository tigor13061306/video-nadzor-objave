"""Obnavlja Instagram ključ (važi 60 dana) i upisuje ga u GitHub Secret IG_TOKEN.

Okruženje: IG_TOKEN (trenutni ključ), GH_PAT (GitHub ključ sa dozvolom Secrets: Read and write).
Ključevi se nikad ne ispisuju.
"""
import base64, os
import requests
from nacl import encoding, public

REPO = "tigor13061306/video-nadzor-objave"


def main():
    t = os.environ["IG_TOKEN"].strip()
    # ključ ide u tijelo zahtjeva (POST), ne u adresu
    url = "https://graph.instagram.com/refresh_access_token"
    r = requests.post(url, data={"grant_type": "ig_refresh_token", "access_token": t}, timeout=60).json()
    if not r.get("access_token"):
        r = requests.get(url, params={"grant_type": "ig_refresh_token", "access_token": t}, timeout=60).json()
    novi = r.get("access_token")
    if not novi:
        raise SystemExit("Obnova ključa nije uspjela: %s" % r.get("error", {}).get("message", "nepoznato"))
    h = {"Authorization": "Bearer " + os.environ["GH_PAT"].strip(), "Accept": "application/vnd.github+json"}
    pk = requests.get(f"https://api.github.com/repos/{REPO}/actions/secrets/public-key", headers=h, timeout=60).json()
    box = public.SealedBox(public.PublicKey(pk["key"].encode(), encoding.Base64Encoder()))
    enc = base64.b64encode(box.encrypt(novi.encode())).decode()
    p = requests.put(f"https://api.github.com/repos/{REPO}/actions/secrets/IG_TOKEN", headers=h,
                     json={"encrypted_value": enc, "key_id": pk["key_id"]}, timeout=60)
    if p.status_code not in (201, 204):
        raise SystemExit("Upis ključa u GitHub nije uspio: %s" % p.status_code)
    print("Ključ obnovljen, važi još %d dana." % (r.get("expires_in", 0) // 86400))


if __name__ == "__main__":
    main()
