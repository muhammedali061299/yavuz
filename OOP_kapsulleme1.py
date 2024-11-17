class BankaKasasi():
     KasadaKalanMiktar = 0
class BankaMusterisi():
    adiSoyadi = "---"
    hesapNumarasi = "tanımlanmamış"
    kalanParasi = 0

kasa1 = BankaKasasi()
kasa1.KasadaKalanMiktar = 50000

musteri1 = BankaMusterisi()
musteri1.adiSoyadi = "Nurdan KARA"
musteri1.hesapNumarasi = "6325412"
musteri1.kalanParasi = 5000

print(f"\n\nKasada kalan para miktarı : {kasa1.KasadaKalanMiktar}")

print(f"\n\nMüşteri Bilgileri\n\
    Adı: \t{musteri1.adiSoyadi}\n\
    Hesap No : \t{musteri1.hesapNumarasi}\n\
    Kalan Parası : \t{musteri1.kalanParasi}")

musteri1.kalanParasi += 5000

print(f"\n\nKasada kalan para miktarı : {kasa1.KasadaKalanMiktar}")

print(f"\n\nMüşteri Bilgileri\n\
    Adı: \t{musteri1.adiSoyadi}\n\
    Hesap No : \t{musteri1.hesapNumarasi}\n\
    Kalan Parası : \t{musteri1.kalanParasi}")