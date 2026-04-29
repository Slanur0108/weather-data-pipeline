from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp

# 1. Spark Oturumunu Başlat (Veri işleme motorunu çalıştırıyoruz)
spark = SparkSession.builder \
    .appName("WeatherDataTransform") \
    .getOrCreate()

# 2. Extract adımında kaydettiğimiz JSON dosyasını okuma 
# indent=4 ile kaydettiğimiz için multiline özelliğini açıyoruz
raw_df = spark.read.option("multiline", "true").json("raw_weather.json")

print("Ham Veri Şeması (Nasıl göründüğüne dikkat et):")
raw_df.printSchema()

# 3. TRANSFORM: İç içe geçmiş (nested) verileri dışarı çıkarıp düzleştiriyoruz
clean_df = raw_df.select(
    col("name").alias("Sehir"),
    col("main.temp").alias("Sicaklik_C"),
    col("main.humidity").alias("Nem_Yuzde"),
    col("wind.speed").alias("Ruzgar_Hizi"),
    col("weather").getItem(0).getField("description").alias("Hava_Durumu")
)

# 4. Verinin işlendiği zamanı ekleme
clean_df = clean_df.withColumn("Islem_Zamani", current_timestamp())

# 5. Temizlenmiş veriyi ekranda göster
print("\n Temizlenmiş ve Dönüştürülmüş Tablo:")
clean_df.show(truncate=False)

import sqlite3
import pandas as pd

print("\nLoad (Yükleme) işlemi başlıyor...")

# 1. PySpark tablosunu, SQL'e daha rahat yazabilmek için Pandas tablosuna çeviriyoruz
pandas_df = clean_df.toPandas()

# 2. SQLite veritabanına bağlanıyoruz (Eğer 'weather_database.db' yoksa otomatik oluşturur)
conn = sqlite3.connect("weather_database.db")

# 3. Veriyi 'gunluk_hava_durumu' adında bir SQL tablosu olarak kaydediyoruz
# if_exists="append" demek: Kod her çalıştığında yeni veriyi eskisinin altına ekle
pandas_df.to_sql("gunluk_hava_durumu", conn, if_exists="append", index=False)

# Bağlantıyı kapat
conn.close()

print("✅ Veri başarıyla SQL veritabanına yüklendi!")