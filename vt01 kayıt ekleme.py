#  python -m pip install mysql-connector-python
import mysql.connector
try:
  vts = mysql.connector.connect(host="localhost",user="root",password="1234",
  database="deneme1"
  ); print("Bağlantı tamam:")  
  
  vts1 = mysql.connector.connect(host="localhost",user="root",password="1234",
  database="deneme2"
  ); print("Bağlantı tamam:")  

  try:
    secilen = vts.cursor()
    # secilen.execute("CREATE TABLE ogrenciler (ad VARCHAR(50), telefon VARCHAR(30))")
    # secilen.execute("INSERT INTO ogrenciler (id,ad, telefon) VALUES (2,'Buse VAROL', '5336325412')")
    secilen.execute("INSERT INTO ogretmen (ad, tc) VALUES ('Sude KARA', '545214523')")
    vts.commit()

    print("kayıt eklendi.")
  except mysql.connector.Error as hata:
    print(f"Hata : {hata}")  

except: # veritabanı sistemine bağlanma sistem kurulu değilse veya herhangi bir eksik varsa hata verecektir.
  print("Veritabanına bağlanırken bir hata oluştu.")


