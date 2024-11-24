import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)
masa = QMainWindow()

tepsi1 = QVBoxLayout() # vertical
# tepsi1 = QHBoxLayout() # horizontal

tepsi1.addWidget(QLabel("Kullanıcı adı:"))
tepsi1.addWidget(QLineEdit())

tepsi1.addWidget(QLabel("şifre:"))
tepsi1.addWidget(QLineEdit())

tepsi1.addWidget(QPushButton("Giriş"))
tepsi1.addWidget(QCheckBox("Beni hatıla"))


sunumtepsisi = QWidget()
sunumtepsisi.setLayout(tepsi1)

masa.setCentralWidget(sunumtepsisi)

masa.show()
app.exec()
