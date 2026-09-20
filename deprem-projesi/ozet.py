import sqlite3

baglanti = sqlite3.connect("veri/deprem.db")
imlec = baglanti.cursor()

imlec.execute("SELECT COUNT(*) FROM depremler_temiz")
toplam = imlec.fetchone()[0]
print(f"Toplam: {toplam}")

imlec.execute("SELECT MAX(buyukluk) FROM depremler_temiz")
enbuyuk= imlec.fetchone()[0]
print(f"En büyük: {enbuyuk}")

imlec.execute("SELECT COUNT(*) FROM depremler_temiz WHERE buyukluk > 4")
dorttenbuyuk = imlec.fetchone()[0]
print(f"4'ten büyük : {dorttenbuyuk}")

baglanti.close()
