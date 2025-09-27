#1-Veri Yapıları: Uçuş Bilgileri Sözlüğü (Dictionary)
ucus_bilgileri = {
    "ucus_no": "TK190",
    "kalkis_yeri": "IST",
    "varis_yeri": "JFK",
    "bilet_fiyatlari_tl": 12500,
    "yolcu_sinifi": "Business",
    "bagaj_hakki_kg": 30
}

#2-Koşullu Yapı: Fiyat Kontrolü (if/elif/else)
#Bilet fiyatlarına göre yolcuya mesajı gösterelim
fiyat = ucus_bilgileri["bilet_fiyatlari_tl"]

if fiyat >= 10000:
    print(f"TK1980 uçuşu için fiyat (₺{fiyat}): Premium/Business segmentinde yer almaktadır.")
elif fiyat >=5000:
    print(f"TK1980 uçuşu için fiyat (₺{fiyat}): Standart Ekonomi sınıfıdır.")
else:
    print(f"TK1980 uçuşu için fiyat (₺{fiyat}): Promosyonel veya İndirimli Bilet.")

#3-Temel İşlem: Liste ve döngü ile ortalama hesaplama
gecikme_sureleri = [15, 5, 45, 0, 10]
toplam_gecikme = 0

for sure in gecikme_sureleri:
    toplam_gecikme += sure

#ortalama hesaplama
ortalama_gecikme = toplam_gecikme / len(gecikme_sureleri)
print(f"\nSon 5 uçuşun toplam gecikme süresi: {toplam_gecikme} dakika.")
print(f"Ortalama gecikme süresi: {ortalama_gecikme} dakika.")