class BankaKasasi():
    __KasadaKalanMiktar = 0 # __ ile kapsüllenmiş bilgi
    def kasadakiMiktar(self):
        return self.__KasadaKalanMiktar
    
    def kasayaParaEkle(self, miktar):
        self.__KasadaKalanMiktar += miktar

    def kasadanParaCikar(self,miktar):
        self.__KasadaKalanMiktar += miktar

class BankaMusterisi():

    adiSoyadi = "---"
    hesapNumarasi = "tanımlanmamış" # public yada global 
    __kalanParasi = 0 # __ ile kapsüllenmiş bilgi. Private özellik/propery.
    # private özellikler sınıf dışından değiştirilemez.
    # sınıf içerisindeki bir fonksiyon aracılığıyla değişir.
    def __init__(self,ad,no,para):
        self.adiSoyadi = ad
        self.hesapNumarasi = no
        # self.__kalanParasi = para
    def paraCek(self,cekilen):
        self.__kalanParasi -= cekilen
        # kasa1.__KasadaKalanMiktar -= cekilen
        kasa1.kasadanParaCikar(cekilen)
    
    def paraYatir(self,yatirilan):
        self.__kalanParasi += yatirilan
        # kasa1.__KasadaKalanMiktar += yatirilan
        kasa1.kasayaParaEkle(yatirilan)
    
    def kalanParaMiktariniGoster(self):
        return self.__kalanParasi

kasa1 = BankaKasasi()
kasa1.KasadaKalanMiktar = 50000

musteri1 = BankaMusterisi("Nurdan KARA","6325412",5000)

print(f"\n\nKasada kalan para miktarı : {kasa1.KasadaKalanMiktar}")

print(f"\n\nMüşteri Bilgileri\n\
    Adı: \t{musteri1.adiSoyadi}\n\
    Hesap No : \t{musteri1.hesapNumarasi}\n")

musteri1.adiSoyadi = "Ali AK"
# musteri1.__kalanParasi += 5000
musteri1.paraYatir(5000)

print(f"\n\nKasada kalan para miktarı : {kasa1.KasadaKalanMiktar}")

print(f"\n\nMüşteri Bilgileri\n\
    Adı: \t{musteri1.adiSoyadi}\n\
    Hesap No : \t{musteri1.hesapNumarasi}\n")

print("Müşteri1 kalan parası:", musteri1.kalanParaMiktariniGoster())
print("Kasadaki miktar:", kasa1.kasadakiMiktar())

musteri1.paraYatir(20)
print("Müşteri1 kalan parası:", musteri1.kalanParaMiktariniGoster())
print("Kasadaki miktar:", kasa1.kasadakiMiktar())

musteri2 = BankaMusterisi("Ebru SARICAOĞLU","524785",6000)
musteri2.paraYatir(1000)
print("Müşteri1 kalan parası:", musteri1.kalanParaMiktariniGoster())
print("Müşteri2 kalan parası:", musteri2.kalanParaMiktariniGoster())
print("Kasadaki miktar:", kasa1.kasadakiMiktar())

musteri2.paraYatir(3)
print("Müşteri1 kalan parası:", musteri1.kalanParaMiktariniGoster())
print("Müşteri2 kalan parası:", musteri2.kalanParaMiktariniGoster())
print("Kasadaki miktar:", kasa1.kasadakiMiktar())