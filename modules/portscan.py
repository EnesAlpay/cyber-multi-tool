import socket, threading
from core import log

COMMON_PORTS = {22:"SSH",80:"HTTP",443:"HTTPS"}

def banner_grab(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        s.send(b"HEAD / HTTP/1.1\r\n\r\n")
        data = s.recv(200)
        return data.decode(errors="ignore").strip()
    except:
        return None

results = []

def scan_port(ip, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        if s.connect_ex((ip, port))==0:
            banner = banner_grab(ip, port)
            results.append((port,banner))
    except: pass
    finally: s.close()

def scan(ip):
    threads = []
    for port in COMMON_PORTS:
        t = threading.Thread(target=scan_port,args=(ip,port))
        threads.append(t)
        t.start()
    for t in threads: t.join()
    for port,banner in results:
        print(f"[OPEN] {port} | {banner}")
        log("portscan", {"port":port,"banner":banner})
