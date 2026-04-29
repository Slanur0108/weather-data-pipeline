import subprocess
import time

print("🚀 Veri Boru Hattı (Data Pipeline) Başlatılıyor...\n")
print("-" * 50)

# 1. Adım: Extract (Çıkarma) işlemini çalıştır
print("Adım 1: API'den veriler çekiliyor (Extract)...")
extract_process = subprocess.run(["python", "extract.py"])

# Eğer ilk adımda hata olursa sistemi durdur
if extract_process.returncode != 0:
    print("❌ Extract adımında hata oluştu! Pipeline durduruldu.")
    exit()

# Sistemin dosyayı kaydetmesi için 2 saniye nefes payı 
time.sleep(2)
print("-" * 50)

# 2. Adım: Transform ve Load işlemlerini çalıştır
print("Adım 2: Veriler temizleniyor ve SQL'e yazılıyor (Transform & Load)...")
transform_process = subprocess.run(["python", "transform.py"])

if transform_process.returncode == 0:
    print("-" * 50)
    print("🎉 BÜYÜK BAŞARI: Tüm boru hattı (ETL) kusursuz bir şekilde çalıştı!")
else:
    print("❌ Transform adımında hata oluştu!")