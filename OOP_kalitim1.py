class Personel():
    sicilNo = "--"
    adiSoyadi = "tanımsız"

class Idareci(Personel):
    idariGorevi = "tanımlanmamış"

class katPersoneli(Personel):
    gorevliOlduguKat = 4

class Veli():
    ogrencisininAdi ="----"

class CokluYetkiliPersonel(Idareci, Veli): # çoklu miras alma. Multiple inheritence
    pass

personel1 = Idareci()
personel2 = CokluYetkiliPersonel()
personel2.idariGorevi = "Müdür yardımcısı"
personel2.ogrencisininAdi = "Ufuk ALTIN"

print(personel1.sicilNo)
# print(personel1.gorevliOlduguKat)


print("İdari görev:",personel2.idariGorevi, "\nÖğrenci adı:",personel2.ogrencisininAdi)

