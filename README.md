# 🌤️ End-to-End Weather Data ETL Pipeline

Bu proje, Python ve PySpark kullanılarak sıfırdan inşa edilmiş uçtan uca bir ETL (Extract, Transform, Load) veri boru hattıdır. Sistem, OpenWeatherMap API'sinden anlık hava durumu verilerini çeker, büyük veri araçlarıyla temizler ve yerel bir SQL veritabanına depolar.

## 🏗️ Proje Mimarisi

Proje, 3 ana aşamadan ve bunları yöneten bir orkestrasyon dosyasından oluşmaktadır:

1. **Extract (`extract.py`):** `requests` kütüphanesi kullanılarak OpenWeather API'den İstanbul, Ankara, İzmir ve Artvin illerinin anlık hava durumu verileri JSON formatında çekilir.
2. **Transform (`transform.py`):** Çekilen karmaşık (nested) JSON verisi, **Apache Spark (PySpark)** kullanılarak düzleştirilir (flatten). Sadece ilgili kolonlar seçilir ve veriye sistem işlem zamanı (timestamp) eklenir.
3. **Load (`transform.py`):** Temizlenen DataFrame, Pandas üzerinden geçirilerek **SQLite** veritabanına (`weather_database.db`) kalıcı olarak yazılır. Sistem her çalıştığında veriler eski verilerin altına eklenir (append), böylece tarihsel bir veri seti oluşur.
4. **Orchestration (`pipeline.py`):** Tüm bu süreçleri sırasıyla ve hata kontrolü yaparak otomatize eden ana kontrol dosyasıdır.

## 🛠️ Kullanılan Teknolojiler

* **Dil:** Python
* **Veri Çekme:** Requests, OpenWeatherMap API
* **Büyük Veri İşleme:** Apache Spark (PySpark)
* **Veritabanı:** SQLite, Pandas

## 📂 Proje Dosyaları

* `pipeline.py` : ETL boru hattını başlatan ana orkestrasyon kodu.
* `extract.py` : API'den veri çekip `raw_weather.json` dosyasını oluşturan kod.
* `transform.py`: JSON'u okuyan, PySpark ile temizleyen ve veritabanına yazan kod.
* `weather_database.db`: İşlenmiş verilerin saklandığı SQL veritabanı.

## 🚀 Nasıl Çalıştırılır?

Projenin bağımlılıklarını yüklemek için terminalde aşağıdaki komutu çalıştırın:
```bash
pip install requests pyspark pandas