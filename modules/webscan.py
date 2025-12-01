import requests
from core import log

admin_paths = [
    "/admin", "/admin/login", "/yonetim", "/wp-admin", "/cpanel", "/login", "/dashboard"
]

payloads = [
    "<script>alert(1)</script>",
    "' OR 1=1 --",
    "\" onmouseover=alert(1) x=\"",
]

def run(url):
    if not url.startswith("http"):
        url = "http://" + url

    print(f"\n[+] {url} üzerinde web taraması başlıyor...\n")

    print("=== Admin Panel Tarama ===")
    found_admins = []

    for path in admin_paths:
        full = url + path
        try:
            r = requests.get(full, timeout=4)
            if r.status_code in (200, 301, 302):
                print(f"[FOUND] {full}")
                found_admins.append(full)
        except:
            pass

    log("webscan", {"admins": found_admins})

    print("\n=== Input Fuzzing & XSS Test ===")
    test_params = ["q", "search", "id", "test"]

    for p in test_params:
        for payload in payloads:
            try:
                r = requests.get(url, params={p:payload}, timeout=4)
                if payload.lower() in r.text.lower():
                    print(f"[VULN?] {p} parametresinde yansıyan payload bulundu → {payload}")
                    log("webscan", {"xss_param": p, "payload": payload})
                    break
            except:
                continue

    print("\nTarama tamamlandı.")
