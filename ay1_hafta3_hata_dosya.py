# ay1_hafta3_hata_dosya.py

# ====================================================================
# Hafta 2'den Gelen Fonksiyon: Fiyat Segmentini Belirleme
# ====================================================================

def fiyat_segmentini_belirle(fiyat: (int | float)) -> str:
    """Bilet fiyatına göre uçuşun ait olduğu segmenti belirler."""
    if fiyat >= 10000:
        return "Premium"
    elif fiyat >= 5000:
        return "Standart"
    else:
        return "Promosyonel"

# ====================================================================
# Ana İşlem: Dosya Okuma ve Hata Yönetimi
# ====================================================================

def verileri_isleyip_goster():
    """CSV dosyasını okur, hatalı satırları try-except ile atlar ve analiz yapar."""
    
    dosya_adi = 'ucus_verileri.csv'
    islenen_ucus_sayisi = 0
    toplam_gecikme = 0

    try:
        # 'with open' yapısı, dosyanın iş bitince otomatik kapanmasını sağlar.
        with open(dosya_adi, 'r', encoding='utf-8') as dosya:
            
            # İlk satırı (başlıkları) okuyup atla
            basliklar = next(dosya)
            print(f"Başlıklar: {basliklar.strip()}")
            print("-" * 30)
            
            for satir in dosya:
                # Satır sonu karakterini temizle ve virgülle ayır
                satir = satir.strip()
                sutunlar = satir.split(',')
                
                # Sütun sayısı kontrolü
                if len(sutunlar) != 3:
                    print(f"[UYARI] Satır atlandı: Eksik veri sütunu. Satır: {satir}")
                    continue

                ucus_no, gecikme_str, fiyat_str = sutunlar

                # Hata Yönetimi Başlangıcı: Veri dönüşüm hatalarını yakala
                try:
                    # Gecikme süresini tam sayıya dönüştürürken hata olabilir (Örn: "Hata" metni)
                    gecikme = int(gecikme_str)
                    
                    # Fiyatı ondalıklı sayıya dönüştürürken hata olabilir (Örn: "YOK" metni)
                    fiyat = float(fiyat_str)
                    
                    # Analiz yapma: Hafta 2 fonksiyonunu kullanma
                    segment = fiyat_segmentini_belirle(fiyat)

                    print(f"İşlendi: {ucus_no} -> Gecikme: {gecikme} dk, Segment: {segment}")
                    
                    toplam_gecikme += gecikme
                    islenen_ucus_sayisi += 1
                    
                except ValueError as e:
                    # Metinsel veya boş değerleri yakalar
                    print(f"[HATA YAKALANDI] {ucus_no} uçuşunda geçersiz veri tipi ({e}). Satır atlandı.")
                
                except Exception as e:
                    # Beklenmeyen diğer hataları yakalar
                    print(f"[BEKLENMEYEN HATA] {ucus_no} uçuşu işlenirken bir hata oluştu: {e}")

    except FileNotFoundError:
        print(f"[KRİTİK HATA] '{dosya_adi}' dosyası bulunamadı. Lütfen dosyanın klasörde olduğundan emin olun.")
        return # Dosya yoksa programı sonlandır

    print("-" * 30)
    print(f"ANALİZ SONUCU: Toplam {islenen_ucus_sayisi} uçuş işlendi.")
    if islenen_ucus_sayisi > 0:
        ortalama = toplam_gecikme / islenen_ucus_sayisi
        print(f"İşlenen uçuşlar için Ortalama Gecikme: {ortalama:.2f} dakika.")

# Ana fonksiyonu çalıştır
if __name__ == "__main__":
    verileri_isleyip_goster()