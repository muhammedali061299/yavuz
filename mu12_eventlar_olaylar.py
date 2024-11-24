from PyQt6.QtWidgets import *

class GirisEkrani(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Program Giriş Ekranı')
        # self.resize(300,50)
        self.setFixedSize(300,100)

        di6 = QVBoxLayout()
        yatayicerik = QHBoxLayout()

        dikeyicerik3 = QVBoxLayout()
        dikeyicerik3.addWidget(QLabel("Kullanıcı adı"))
        dikeyicerik3.addWidget(QLabel("Şifresi"))

        dikeyicerik4 = QVBoxLayout()
        self.kullanici_adi = QLineEdit()
        dikeyicerik4.addWidget(self.kullanici_adi)

        self.sifre = QLineEdit()
        dikeyicerik4.addWidget(self.sifre)
       
        yi5 = QHBoxLayout()
        dugme1 = QPushButton("Giriş yap")
        yi5.addWidget(dugme1)
        # dugme1.clicked.connect(self.xxx) # fonksiyon parantezi olmasın
        dugme1.clicked.connect(self.kontrol) # fonksiyon parantezi olmasın
        
        dugme2 = QPushButton("Vazgeç")
        yi5.addWidget(dugme2)
        dugme2.clicked.connect(self.vazgec)

        yatayicerik.addLayout(dikeyicerik3)
        yatayicerik.addLayout(dikeyicerik4)
        # yatayicerik.addLayout(yi5)

        di6.addLayout(yatayicerik)
        di6.addLayout(yi5)

        pencere = QWidget()
        pencere.setLayout(di6)
        self.setCentralWidget(pencere)

    def xxx(self,x):
        mesaj = "Giriş düğmesine tıklandı."
        print(mesaj)
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Dikkat")
        dlg.setText(mesaj)
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dlg.setIcon(QMessageBox.Icon.Question)
        dlg.exec()
        # sonuc = dlg.exec()
        # if sonuc == QMessageBox.Yes:
        #     print("Yes!")
        # else:
        #     print("No!")
        
    def kontrol(self):
        dka = "qqq"
        dsf = "11"

        # dosya = open("bilgiler.txt")
        # dka = dosya.readline()
        # dsf = dosya.readline()

        print("Doğru kullanıcı adı: ", dka)
        print("Doğru şifre: ", dsf)
        ka = self.kullanici_adi.text()
        sf = self.sifre.text()
        print(f"Giriş düğmesine tıklandı.\nGirilen kullanıcı adı:{ka}\nGirilen şifre:{sf}")
        if dka == ka and dsf == sf :
            print("Yetki var, ana ekrana yönlendiriliyorsunuz.")
            self.ana = AnaEkran()
            self.ana.show()
            self.close()
        else:
            print("Kullanım yetkisi yok.")

    def vazgec(self):
        print("vazgeç düğmesine tıklandı.")
        aaa = QMessageBox(self)
        aaa.setWindowTitle("Aman Dikkat")
        aaa.setText("Vazgeç düğmesine tıkladınız.")
        aaa.exec()

class AnaEkran(QMainWindow):
    def __init__(self):
        super().__init__()
   
        mainIcerik = QVBoxLayout()
        
        mainIcerik.addWidget(QLabel("REHBER ANA EKRANI"))
        mainIcerik.addWidget(QPushButton("Rehbere ekle"))
        mainIcerik.addWidget(QPushButton("Listele"))
        mainIcerik.addWidget(QPushButton("Düzelt"))
        mainIcerik.addWidget(QPushButton("..."))

        pencere = QWidget()
        pencere.setLayout(mainIcerik)
        self.setCentralWidget(pencere)

class EklemeEkrani(QMainWindow):
    def __init__(self):
        super().__init__()
   
        di6 = QVBoxLayout()
        yatayicerik = QHBoxLayout()

        dikeyicerik3 = QVBoxLayout()
        dikeyicerik3.addWidget(QLabel("Adı soyadı:"))
        dikeyicerik3.addWidget(QLabel("Telefon numarası:"))

        dikeyicerik4 = QVBoxLayout()
        dikeyicerik4.addWidget(QLineEdit())
        dikeyicerik4.addWidget(QLineEdit())
       
        baslikBolumu = QHBoxLayout()
        baslikBolumu.addWidget(QLabel("YENİ KAYIT EKLEME EKRANI"))
        
        yi5 = QHBoxLayout()
        yi5.addWidget(QPushButton("Giriş yap"))
        yi5.addWidget(QPushButton("Vazgeç"))

        yatayicerik.addLayout(dikeyicerik3)
        yatayicerik.addLayout(dikeyicerik4)
        # yatayicerik.addLayout(yi5)

        di6.addLayout(baslikBolumu)
        di6.addLayout(yatayicerik)
        di6.addLayout(yi5)

        pencere = QWidget()
        pencere.setLayout(di6)
        self.setCentralWidget(pencere)


aa = QApplication([])
pencere = GirisEkrani()
pencere.show()

# ana = AnaEkran()
# ana.show()
aa.exec()