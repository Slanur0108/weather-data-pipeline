import requests
import json
import os
from dotenv import load_dotenv

# .env dosyasındaki gizli değişkenleri okumaya hazırlıyoruz
load_dotenv()

# Şifreyi koddan sildik! Artık bilgisayarındaki o gizli .env dosyasından çekecek
API_KEY = os.getenv("WEATHER_API_KEY")

# Verisini çekmek istediğimiz şehirler (BUNLAR KESİNLİKLE KALMALI)
cities = ["Istanbul", "Ankara", "Izmir", "Artvin"]

# Çektiğimiz verileri toplayacağımız boş bir liste (BU DA KALMALI)
weather_data_list = []

for city in cities:
    # API'ye istek atacağımız adres (URL)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    # Adrese gidip kapıyı çalıyoruz (GET isteği)
    response = requests.get(url)
    
    # Gelen cevabı JSON (sözlük) formatına çeviriyoruz
    if response.status_code == 200:
        data = response.json()
        weather_data_list.append(data)
        print(f"✅ {city} verisi başarıyla çekildi!")
    else:
        print(f"❌ {city} verisi çekilemedi. Hata Kodu: {response.status_code}")

# Veriyi JSON dosyasına kaydedelim
if len(weather_data_list) > 0:
    with open("raw_weather.json", "w", encoding="utf-8") as f:
        json.dump(weather_data_list, f, ensure_ascii=False, indent=4)
    print("\n💾 Tüm veriler 'raw_weather.json' dosyasına başarıyla kaydedildi!")
else:
    print("\n⚠️ Sepet boş! Hiçbir şehrin verisi çekilemedi.")