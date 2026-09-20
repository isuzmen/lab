import sqlite3


def en_buyuk_depremler(db_yolu, adet):
    baglanti = sqlite3.connect(db_yolu)
    imlec = baglanti.cursor()
    imlec.execute(
        "SELECT zaman, buyukluk, yer FROM depremler_temiz ORDER BY buyukluk DESC LIMIT ?",
        (adet,),
    )
    sonuc = imlec.fetchall()
    baglanti.close()
    return sonuc


for zaman, buyukluk, yer in en_buyuk_depremler("veri/deprem.db", 5):
    print(buyukluk, yer, zaman)
