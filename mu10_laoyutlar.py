from PyQt6.QtWidgets import *

class GirisEkrani(QMainWindow):
    def __init__(self):
        super().__init__()
   
        di6 = QVBoxLayout()
        yatayicerik = QHBoxLayout()

        dikeyicerik3 = QVBoxLayout()
        dikeyicerik3.addWidget(QLabel("Kullanoıcı adı"))
        dikeyicerik3.addWidget(QLabel("Şifresi"))

        dikeyicerik4 = QVBoxLayout()
        dikeyicerik4.addWidget(QLineEdit())
        dikeyicerik4.addWidget(QLineEdit())
       
        yi5 = QHBoxLayout()
        yi5.addWidget(QPushButton("Giriş yap"))
        yi5.addWidget(QPushButton("Vazgeç"))

        yatayicerik.addLayout(dikeyicerik3)
        yatayicerik.addLayout(dikeyicerik4)
        # yatayicerik.addLayout(yi5)

        di6.addLayout(yatayicerik)
        di6.addLayout(yi5)

        pencere = QWidget()
        pencere.setLayout(di6)
        self.setCentralWidget(pencere)

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

ana = AnaEkran()
ana.show()
aa.exec()