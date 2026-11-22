"""Režija demo Zabbixa za Reelse @pametnija.firma.
1) napravi izmišljene servere, stavke i okidače (Zabbix API 7.0)
2) upiše 3 sata istorije (history.push)
3) odigra scenarij: disk raste preko 90 %, pa redom kamera, snimač, UPS, backup, hladnjača, ERP, VPN; zatim sve riješeno
4) za to vrijeme pravi oštre snimke ekrana (Playwright, 2x) u /out
Svi podaci su izmišljeni."""
import os, time, math, random, traceback
import requests
from playwright.sync_api import sync_playwright

URL = os.environ.get("ZBX_URL", "http://zabbix-web:8080"); API = URL + "/api_jsonrpc.php"; OUT = "/out"
os.makedirs(OUT, exist_ok=True)
LOGF = open(f"{OUT}/rezija.log", "a", encoding="utf-8")
def log(*a):
    s = time.strftime("%H:%M:%S") + " " + " ".join(map(str, a)); print(s, flush=True); LOGF.write(s + "\n"); LOGF.flush()

TOK = None
def api(method, params, auth=True):
    h = {"Content-Type": "application/json-rpc"}
    if auth: h["Authorization"] = "Bearer " + TOK
    j = requests.post(API, json={"jsonrpc": "2.0", "method": method, "params": params, "id": 1}, headers=h, timeout=60).json()
    if "error" in j: raise RuntimeError(f"{method}: {j['error']}")
    return j["result"]

def wait_login():
    global TOK
    for _ in range(180):
        try:
            TOK = api("user.login", {"username": "Admin", "password": "zabbix"}, auth=False); log("prijava OK"); return
        except Exception as e:
            log("čekam Zabbix...", str(e)[:90]); time.sleep(5)
    raise SystemExit("Zabbix ne odgovara")

GRUPA = "Pametnija firma demo"
# host, vidljivo ime, ključ, naziv stavke, jedinica, tip vrijednosti (0 float, 3 cijeli), okidač (izraz poslije last(...), naziv, prioritet)
STAVKE = [
    ("SQL-01", "SQL-01", "disk.d.pused", "Disk D: popunjenost", "%", 0, (">90", "Disk D: popunjen više od 90 %", 4)),
    ("ERP-SRV", "ERP-SRV", "erp.odziv", "ERP: vrijeme odziva", "s", 0, (">5", "ERP sporo odgovara (više od 5 s)", 2)),
    ("NVR-Magacin", "NVR-Magacin", "kamera.ulaz2", "Kamera Ulaz-2: slika", "", 3, ("=0", "Kamera Ulaz-2 nema slike", 3)),
    ("NVR-Magacin", "NVR-Magacin", "nvr.snimanje", "Snimanje aktivno", "", 3, ("=0", "Snimač ne snima: disk 2 u grešci", 4)),
    ("UPS-Server-sala", "UPS Server sala", "ups.baterija", "UPS na bateriji", "", 3, ("=1", "Nestanak struje: UPS radi na bateriji", 5)),
    ("UPS-Server-sala", "UPS Server sala", "ups.autonomija", "Preostalo vrijeme baterije", "min", 0, None),
    ("BACKUP-SRV", "BACKUP-SRV", "backup.starost", "Starost zadnjeg uspješnog backupa", "h", 0, (">24", "Zadnji uspješan backup stariji od 24 h", 2)),
    ("Hladnjaca-2", "Hladnjača 2", "temp", "Temperatura", "°C", 0, (">4", "Hladnjača 2: temperatura iznad +4 °C", 4)),
    ("FW-01", "FW-01", "vpn.magacin", "VPN Centrala–Magacin", "", 3, ("=0", "VPN tunel Centrala–Magacin ne radi", 4)),
    ("FILE-SRV", "FILE-SRV", "dostupnost", "Dostupnost", "", 3, None),
    ("MAIL", "MAIL", "dostupnost", "Dostupnost", "", 3, None),
    ("SW-CORE", "SW-CORE", "dostupnost", "Dostupnost", "", 3, None),
]
NORMALNO = {"disk.d.pused": 78, "erp.odziv": 0.9, "kamera.ulaz2": 1, "nvr.snimanje": 1, "ups.baterija": 0, "ups.autonomija": 45,
            "backup.starost": 8, "temp": 3.1, "vpn.magacin": 1, "dostupnost": 1}
IID = {}

def setup():
    g = api("hostgroup.get", {"filter": {"name": [GRUPA]}})
    gid = g[0]["groupid"] if g else api("hostgroup.create", {"name": GRUPA})["groupids"][0]
    for h in api("host.get", {"filter": {"host": ["Zabbix server"]}}):
        api("host.update", {"hostid": h["hostid"], "status": 1})      # bez šuma od demo servera
    api("user.update", {"userid": "1", "theme": "dark-theme", "refresh": "5s", "autologout": "0", "lang": "en_US", "rows_per_page": 50})
    hid = {}
    for host, ime, key, naziv, jed, vt, trig in STAVKE:
        if host not in hid:
            e = api("host.get", {"filter": {"host": [host]}})
            hid[host] = e[0]["hostid"] if e else api("host.create", {"host": host, "name": ime, "groups": [{"groupid": gid}]})["hostids"][0]
        e = api("item.get", {"hostids": hid[host], "filter": {"key_": [key]}})
        iid = e[0]["itemid"] if e else api("item.create", {"hostid": hid[host], "name": naziv, "key_": key, "type": 2, "value_type": vt,
                                                           "units": jed, "history": "7d", "trends": "30d"})["itemids"][0]
        IID[(host, key)] = iid
        if trig:
            izraz = f"last(/{host}/{key}){trig[0]}"
            if not api("trigger.get", {"hostids": hid[host], "filter": {"description": [trig[1]]}}):
                api("trigger.create", {"description": trig[1], "expression": izraz, "priority": trig[2]})
    log("postavka gotova:", len(hid), "servera,", len(IID), "stavki")
    return gid

def push(vals, clock=None):
    """vals: {(host,key): vrijednost}"""
    c = int(clock or time.time())
    data = [{"itemid": IID[k], "value": str(round(v, 2)), "clock": c, "ns": 0} for k, v in vals.items()]
    r = api("history.push", data)
    bad = [d for d in r.get("data", []) if d.get("error")]
    if bad: log("push greške:", bad[:3])

def backfill():
    now = int(time.time()); batch = []
    for k in range(180, 0, -1):
        c = now - k * 60; u = (180 - k) / 180
        for (host, key), iid in IID.items():
            v = NORMALNO[key]
            if key == "disk.d.pused": v = 55 + 23 * u + random.uniform(-0.6, 0.6)
            elif key == "erp.odziv": v = 0.8 + random.uniform(0, 0.4)
            elif key == "temp": v = 3.0 + 0.4 * math.sin(k / 9) + random.uniform(-0.1, 0.1)
            elif key == "backup.starost": v = 5 + 3 * u
            elif key == "ups.autonomija": v = 45 + random.uniform(-0.5, 0.5)
            batch.append({"itemid": iid, "value": str(round(v, 2)), "clock": c, "ns": 0})
    for i in range(0, len(batch), 500): api("history.push", batch[i:i + 500])
    log("istorija upisana:", len(batch), "vrijednosti")

def main():
    wait_login(); gid = setup()
    log("čekam da server učita stavke (25 s)"); time.sleep(25)
    backfill(); time.sleep(5)
    DASH = "/zabbix.php?action=dashboard.view"
    PROB = f"/zabbix.php?action=problem.view&filter_set=1&show=1&groupids%5B%5D={gid}"
    GRAF = lambda host, key: f"/history.php?action=showgraph&itemids%5B%5D={IID[(host, key)]}&from=now-3h&to=now"
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={"width": 1280, "height": 800}, device_scale_factor=2, timezone_id="Europe/Sarajevo", locale="en-US")
        pg = ctx.new_page()
        pg.goto(URL + "/index.php"); pg.fill("#name", "Admin"); pg.fill("#password", "zabbix"); pg.click("#enter")
        pg.wait_for_load_state("networkidle")
        def shot(name, path=None, wait=2.5):
            if path: pg.goto(URL + path, wait_until="networkidle")
            time.sleep(wait); pg.screenshot(path=f"{OUT}/{name}.png"); log("snimak", name)
        shot("01_dashboard_sve_ok", DASH, 6)
        shot("01_problemi_prazno", PROB)
        # 2) disk raste preko praga, graf uživo
        for i in range(18):
            push({("SQL-01", "disk.d.pused"): 79 + i * 0.85 + random.uniform(-0.2, 0.2)})
            time.sleep(3); shot(f"02_graf_disk_{i:02d}", GRAF("SQL-01", "disk.d.pused"), 1.5)
        # 3) problemi jedan po jedan
        redom = [None,
                 {("NVR-Magacin", "kamera.ulaz2"): 0},
                 {("NVR-Magacin", "nvr.snimanje"): 0},
                 {("Hladnjaca-2", "temp"): 9.1},
                 {("UPS-Server-sala", "ups.baterija"): 1, ("UPS-Server-sala", "ups.autonomija"): 12},
                 {("BACKUP-SRV", "backup.starost"): 216},
                 {("FW-01", "vpn.magacin"): 0},
                 {("ERP-SRV", "erp.odziv"): 8.2}]
        for i, v in enumerate(redom):
            if v: push(v)
            time.sleep(6); shot(f"03_problemi_{i:02d}", PROB)
        shot("04_dashboard_problemi", DASH, 6)
        shot("04_graf_hladnjaca", GRAF("Hladnjaca-2", "temp"))
        # 4) rješavanje: sve se vraća u normalu, statusi postaju RESOLVED (zeleno)
        rjes = [{("SQL-01", "disk.d.pused"): 61.3},
                {("NVR-Magacin", "kamera.ulaz2"): 1, ("NVR-Magacin", "nvr.snimanje"): 1},
                {("UPS-Server-sala", "ups.baterija"): 0, ("UPS-Server-sala", "ups.autonomija"): 45},
                {("Hladnjaca-2", "temp"): 3.2},
                {("BACKUP-SRV", "backup.starost"): 1, ("FW-01", "vpn.magacin"): 1, ("ERP-SRV", "erp.odziv"): 0.9}]
        for i, v in enumerate(rjes):
            push(v); time.sleep(6); shot(f"05_rijeseno_{i:02d}", PROB)
        shot("06_graf_disk_poslije", GRAF("SQL-01", "disk.d.pused"))
        shot("06_dashboard_poslije", DASH, 6)
        b.close()
    open(f"{OUT}/gotovo.txt", "w").write(time.strftime("%F %T") + " režija gotova\n"); log("GOTOVO")

try:
    main()
except Exception:
    log("GREŠKA", traceback.format_exc())
    raise
