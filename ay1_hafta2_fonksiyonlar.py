# ay1_hafta2_fonksiyonlar.py

# ----------------------------------------------------------------------
# 1. Fonksiyon: Gecikme Ortalamasını Hesaplama
# ----------------------------------------------------------------------

def gecikme_ortalama_hesapla(sureler: list) -> tuple:
    """
    Verilen uçuş gecikme süreleri listesinin toplamını ve ortalamasını hesaplar.
    
    Bu fonksiyon, veri analizinde temel istatistikleri hızlıca çekmek için kullanılır.

    Args:
        sureler (list): Dakika cinsinden gecikme sürelerini içeren bir liste.
        
    Returns:
        tuple: (Toplam gecikme süresi, Ortalama gecikme süresi) içeren bir tuple döndürür.
    """
    # Liste boşsa hata vermemek için kontrol
    if not sureler:
        return 0, 0
    
    toplam_gecikme = sum(sureler)
    ortalama_gecikme = toplam_gecikme / len(sureler)
    
    return toplam_gecikme, ortalama_gecikme

# ----------------------------------------------------------------------
# 2. Fonksiyon: Bilet Fiyatı Segmentini Belirleme
# ----------------------------------------------------------------------

def fiyat_segmentini_belirle(fiyat: (int | float)) -> str:
    """
    Bilet fiyatına göre uçuşun ait olduğu segmenti belirler.
    
    Kurum için dinamik fiyatlandırma analizlerinde kullanılır.

    Args:
        fiyat (int | float): Biletin Türk Lirası cinsinden fiyatı.
        
    Returns:
        str: Biletin ait olduğu segment adı ('Premium', 'Standart' veya 'Promosyonel').
    """
    if fiyat >= 10000:
        return "Premium"
    elif fiyat >= 5000:
        return "Standart"
    else:
        return "Promosyonel"

# ----------------------------------------------------------------------
# Kodu çalıştırma (Fonksiyonları Kullanma)
# ----------------------------------------------------------------------

# Hafta 1'deki verileri fonksiyonlara gönderiyoruz
gecikme_sureleri = [15, 5, 45, 0, 10]
bilet_fiyati = 12500

# Fonksiyonları çağırıp çıktılarını değişkenlere atıyoruz
toplam, ortalama = gecikme_ortalama_hesapla(gecikme_sureleri)
segment = fiyat_segmentini_belirle(bilet_fiyati)


# Sonuçları ekrana yazdırma
print(f"--- Uçuş Analizi Raporu ---")
print(f"Gecikme Süreleri: {gecikme_sureleri}")
print(f"Toplam Gecikme: {toplam} dakika")
print(f"Ortalama Gecikme: {ortalama} dakika")
print(f"Bilet Fiyatı: ₺{bilet_fiyati}")
print(f"Belirlenen Segment: {segment}")
print(f"--------------------------")