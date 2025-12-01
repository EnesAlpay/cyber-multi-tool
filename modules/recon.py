import requests
from core import log

def fingerprint(url):
    if not url.startswith("http"):
        url = "http://" + url

    print(f"\n[+] {url} için HTTP fingerprint başlatılıyor...\n")

    try:
        r = requests.get(url, timeout=5)
    except Exception as e:
        print(f"[!] Bağlantı hatası: {e}")
        return

    print("=== HTTP Headers ===")
    for k,v in r.headers.items():
        print(f"{k}: {v}")

    log("recon", {"url":url, "headers":dict(r.headers)})

    tech = []

    server = r.headers.get("Server")
    if server:
        tech.append(f"Sunucu: {server}")

    powered = r.headers.get("X-Powered-By")
    if powered:
        tech.append(f"Framework: {powered}")

    if "wordpress" in r.text.lower():
        tech.append("CMS: WordPress")

    if tech:
        print("\n=== Olası Teknolojiler ===")
        for t in tech:
            print(f"- {t}")

        log("recon", {"tech": tech})
    else:
        print("\nHiçbir teknoloji tespit edilemedi.")
