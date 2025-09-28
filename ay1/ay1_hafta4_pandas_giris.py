import pandas as pd
import numpy as np
#==================================================
#1. Veri Okuma ve İlk Keşif
#==================================================

#CSV dosyasını Pandas DataFrame'e okuma.
#Pandas, bu işlemi Python'daki satır satır okumadan çok daha hızlı yapar.

try:
    # Hata Düzeltmesi: Dosyanın sonundaki veya arasındaki boş satırları atlamak için parametre ekledik.
    df = pd.read_csv('ucus_verileri.csv', skip_blank_lines=True) 
    
    print("---1. Veri Okuma Başarılı---")
    print("İlk 5 satır (df.head()):")
    print(df.head())

    print("\nVeri Tipleri (df.dtypes):")
    #Gecikme ve fiyat sütunlarının henüz sayısal olmadığını göreceğiz(object/string)
    print(df.dtypes)

except FileNotFoundError:
    print("HATA: ucus_verileri.csv dosyası bulunamadı. Lütfen kontrol edin.")
    exit()

#==================================================
#2. Temizlik Öncesi Eksik Değer Kontrolü
#==================================================

print("\n---2. Eksik Değer Kontrolü (isnull().sum()) ---")
#Hangi sütunlarda kaç tane eksik/hatalı (NaN) değer olduğunu gösterir
print(df.isnull().sum())

#==================================================
#3. Veri Temizleme (Hafta3'teki try/except işini Pandas ile yapma)
#==================================================

print("\n---3. Veri Temizleme ve Dönüştürme---")
#Hata Yönetimi: Gecikme_dakika sütununu sayıya dönüştürürken hatalı değerleri (Örn: "Hata")
#otomatik olarak NaN (Not a Number) olarak ayarla. errors='coerce' bu işi yapar.

df['gecikme_dakika'] = pd.to_numeric(df['gecikme_dakika'], errors='coerce')
df['bilet_fiyati'] = pd.to_numeric(df['bilet_fiyati'], errors='coerce')

# Temizlik: Hatalı (NaN) olan satırları veri setinden tamamen çıkar. (drop)
df_temiz = df.dropna()

print("Temizlenmiş Veri Tipleri (Artık hepsi sayısal olmalı):")
print(df_temiz.dtypes)
print(f"Kayıp veri sonrası kalan satır sayısı: {len(df_temiz)} (Hatalı olanlar atıldı.)")

#==================================================
#4. Veri Filtreleme ve Analiz Pratiği
#==================================================

print("\n---4. Filtreleme Pratiği ---")

# a) Bilet fiyatı 5000TL'nin üzerindeki uçuşları filtreleme (Boş küme parantezleri ile yapılır)
premium_ucus_df = df_temiz[df_temiz['bilet_fiyati'] > 5000]
print(f"Premium Uçuş Sayısı (>5000 TL): {len(premium_ucus_df)}")
print("Premium Uçuşların İlk Satırı:")
print(premium_ucus_df.head(1))

# b) Sadece belirli sütunları seçme
secili_sutunlar_df = df_temiz[['ucus_no', 'gecikme_dakika']]
print("\nSeçili Sütunlar (ucus_no ve gecikme_dakika):")
print(secili_sutunlar_df.head())

# c) Ortalama Gecikmeyi Hesaplama (Pandas'ın dahili fonksiyonu)
ortalama = df_temiz['gecikme_dakika'].mean()
print(f"\nTemizlenmiş Uçuşların Ortalama Gecikmesi: {ortalama:.2f} dakika.")

"""
Bu hafta, Pandas kütüphanesine giriş yaptık ve Python'daki dosya işlemlerini profesyonel
veri bilimi araçlarıyla yapmayı öğrendik.

Temel Öğrenilenler ve Kullanılan Komutlar:

1. Kurulum ve İçeri Aktarma:
    - pip install pandas: Pandas kütüphanesini sanal ortama kurma.
    - import pandas as pd: Pandas'ı 'pd' kısaltmasıyla kodumuza dahil etme.

2. Veri Okuma:
    - pd.read_csv('dosya.csv'): CSV, Excel gibi dosyaları hızlıca okuyarak DataFrame oluşturma.
    - **skip_blank_lines=True**: CSV dosyasında boş satırları atlayarak parser hatalarını önleme (Yeni öğrenilen).

3. Veri Yapısı Keşfi:
    - df.head(): DataFrame'in ilk 5 satırını görüntüleme (Veriye ilk bakış).
    - df.dtypes: Her sütunun veri tipini (int, float, object vb.) kontrol etme.

4. Hata Yönetimi ve Temizlik (Hafta 3'e göre Pandas ile daha hızlı):
    - df.isnull().sum(): Her sütundaki eksik (NaN) değerlerin toplamını sayma.
    - pd.to_numeric(sütun, errors='coerce'): Sütunu sayısal tipe dönüştürmeye zorlama. Hata (metin) içeren değerleri otomatik olarak NaN'a dönüştürme.
    - df.dropna(): NaN (eksik/hatalı) değer içeren satırları veri setinden çıkarma (temizleme).

5. Filtreleme ve Analiz:
    - df[koşul]: Veri setini belirli bir koşula göre filtreleme (Örn: df[df['fiyat'] > 5000]).
    - df[['sütun1', 'sütun2']]: DataFrame'den sadece belirtilen sütunları seçme.
    - df['sütun'].mean(): Seçilen sütunun ortalamasını hızlıca hesaplama.
"""