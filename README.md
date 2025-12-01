# CyberSecurity Automation Toolkit


## Açıklama
Modüler ve legal kullanım odaklı siber güvenlik analiz aracı.  
Python ile geliştirilmiş CLI tabanlı framework, port tarama, servis analizi, passive recon, web panel keşfi ve lab ortamında SSH testleri içerir.

Tüm modüller **eğitim ve lab amaçlıdır**, gerçek sistemlerde saldırı amacıyla kullanılmamalıdır.

## Özellikler
- Thread’li hızlı port tarama ve banner grabbing
- HTTP header & web teknoloji fingerprinting (Wappalyzer-lite)
- Admin panel ve input fuzzing
- SSH brute-force (lab/testing amaçlı)
- Modüler plugin yapısı, kolay genişletilebilir
- JSON loglama ve renkli CLI arayüzü

## Kurulum

git clone https://github.com/EnesAlpay/CyberToolkit.git

cd CyberToolkit

pip install -r requirements.txt

Kullanım

python toolkit.py


CLI menüsünden modüller seçilebilir.

Gereksinimler

Python 3.9+

requests

paramiko
