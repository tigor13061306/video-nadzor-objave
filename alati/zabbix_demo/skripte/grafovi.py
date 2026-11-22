"""Ponovljeni snimak grafova iz podataka koje je upisala rezija.py (chart.php, bez legende), sličica po sličica."""
import os, time, datetime as dt
from playwright.sync_api import sync_playwright
import requests
URL = os.environ.get("ZBX_URL", "http://zabbix-web:8080"); OUT = "/out/grafovi"; os.makedirs(OUT, exist_ok=True)
def api(m, p, tok=None):
    h = {"Content-Type": "application/json-rpc"}
    if tok: h["Authorization"] = "Bearer " + tok
    j = requests.post(URL + "/api_jsonrpc.php", json={"jsonrpc": "2.0", "method": m, "params": p, "id": 1}, headers=h, timeout=60).json()
    if "error" in j: raise RuntimeError(j["error"])
    return j["result"]
tok = api("user.login", {"username": "Admin", "password": "zabbix"})
def item(host, key): return api("item.get", {"host": host, "filter": {"key_": [key]}, "output": ["itemid"]}, tok)[0]["itemid"]
def first_clock(iid, minval, hist=0):
    h = api("history.get", {"itemids": iid, "history": hist, "sortfield": "clock", "sortorder": "DESC", "limit": 400, "output": "extend"}, tok)
    return sorted(int(x["clock"]) for x in h if float(x["value"]) >= minval)
disk = item("SQL-01", "disk.d.pused"); temp = item("Hladnjaca-2", "temp")
dc = first_clock(disk, 79)      # vrijednosti scenarija (rast preko praga)
t_start, t_end = dc[0] - 5, dc[-1] + 90
fmt = lambda t: dt.datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S")
with sync_playwright() as p:
    b = p.chromium.launch(); ctx = b.new_context(viewport={"width": 1400, "height": 700}, device_scale_factor=2, timezone_id="Europe/Sarajevo")
    pg = ctx.new_page()
    pg.goto(URL + "/index.php"); pg.fill("#name", "Admin"); pg.fill("#password", "zabbix"); pg.click("#enter"); pg.wait_for_load_state("networkidle")
    def chart(iid, frm, to, name, w=1200, h=420):
        url = f"{URL}/chart.php?itemids%5B0%5D={iid}&from={frm}&to={to}&width={w}&height={h}&legend=0&profileIdx=web.item.graph.filter"
        r = pg.request.get(url); open(f"{OUT}/{name}.png", "wb").write(r.body()); print("graf", name, r.status, len(r.body()), flush=True)
    # 1) graf diska: prozor od 1 h koji klizi, 24 sličice od početka rasta do kraja
    n = 24
    for i in range(n):
        to = t_start + (t_end - t_start) * i / (n - 1)
        chart(disk, fmt(to - 3600), fmt(to), f"disk_{i:02d}")
    # 2) cijeli događaj: 3 h, rast preko 90 % i pad poslije čišćenja
    chart(disk, fmt(t_end - 3 * 3600 + 600), fmt(t_end + 600), "disk_cijelo")
    # 3) hladnjača: zadnji sat
    chart(temp, fmt(t_end - 3000), fmt(t_end + 600), "hladnjaca")
    b.close()
print("GOTOVO", flush=True)
