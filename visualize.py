import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

def create_visuals():
    # Veritabanı yolunu bul
    db_path = os.path.join(os.path.dirname(__file__), "weather_database.db")
    conn = sqlite3.connect(db_path)
    
    # Senin transform.py dosmandaki tablo ve sütun isimlerine göre sorgu
    query = "SELECT Sehir, Sicaklik_C, Nem_Yuzde FROM gunluk_hava_durumu"
    
    try:
        df = pd.read_sql_query(query, conn)
        conn.close()

        if df.empty:
            print("⚠️ Veritabanında veri bulunamadı!")
            return

        # Grafik oluşturma
        plt.figure(figsize=(10, 6))
        # Şehir bazlı sıcaklık grafiği
        plt.bar(df['Sehir'], df['Sicaklik_C'], color='skyblue', edgecolor='navy')
        
        plt.title('Şehirlerin Güncel Sıcaklık Durumu', fontsize=15)
        plt.xlabel('Şehirler', fontsize=12)
        plt.ylabel('Sıcaklık (°C)', fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # Değerleri sütunların üzerine yaz
        for i, val in enumerate(df['Sicaklik_C']):
            plt.text(i, val + 0.5, f"{val}°C", ha='center', fontweight='bold')

        plt.savefig('temperature_report.png')
        print("✅ Grafik 'temperature_report.png' olarak başarıyla kaydedildi!")
        plt.show()

    except Exception as e:
        print(f"❌ Bir hata oluştu: {e}")
        conn.close()

if __name__ == "__main__":
    create_visuals()