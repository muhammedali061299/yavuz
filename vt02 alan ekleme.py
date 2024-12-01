#  python -m pip install mysql-connector-python
import mysql.connector
try:
  vts = mysql.connector.connect(host="localhost",user="root",password="1234",
  database="deneme1"
  ); print("Bağlantı tamam:")  

  secilen = vts.cursor()
#   secilen.execute("ALTER TABLE ogrenciler ADD COLUMN tc VARCHAR(11)")
#   secilen.execute("ALTER TABLE ogrenciler ADD COLUMN id int primary key AUTO_INCREMENT")
  secilen.execute("ALTER TABLE ogrenciler ADD COLUMN telefon VARCHAR(20)")
  print("alan eklendi.")
  

except: # veritabanı sistemine bağlanma sistem kurulu değilse veya herhangi bir eksik varsa hata verecektir.
  print("Veritabanına bağlanırken bir hata oluştu.")


