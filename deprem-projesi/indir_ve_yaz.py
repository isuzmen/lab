
import csv
import io
import sqlite3
import requests

URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.csv"
DB_YOLU = "deprem.db"


def indir(url):
    yanit = requests.get(url)
    yanit.raise_for_status()
    return yanit.text


def satirlara_cevir(metin):
    okuyucu = csv.DictReader(io.StringIO(metin))
    return list(okuyucu)


def sayiya_cevir(deger):
    # CSV'de boş kalan hücreler olabiliyor, float("") hata verir
    if deger is None or deger == "":
        return None
    return float(deger)


def veritabanina_yaz(satirlar, db_yolu):
    baglanti = sqlite3.connect(db_yolu)
    imlec = baglanti.cursor()

    imlec.execute("""
        CREATE TABLE IF NOT EXISTS depremler_temiz (
            id TEXT PRIMARY KEY,
            zaman TEXT,
            enlem REAL,
            boylam REAL,
            derinlik REAL,
            buyukluk REAL,
            yer TEXT
        )
    """)

    kayitlar = []
    for satir in satirlar:
        kayitlar.append((
            satir["id"],
            satir["time"],
            sayiya_cevir(satir["latitude"]),
            sayiya_cevir(satir["longitude"]),
            sayiya_cevir(satir["depth"]),
            sayiya_cevir(satir["mag"]),
            satir["place"],
        ))

    imlec.executemany(
        "INSERT OR REPLACE INTO depremler_temiz VALUES (?, ?, ?, ?, ?, ?, ?)",
        kayitlar,
    )
    baglanti.commit()
    baglanti.close()


def main():
    metin = indir(URL)
    satirlar = satirlara_cevir(metin)
    veritabanina_yaz(satirlar, DB_YOLU)
    print(f"Toplam {len(satirlar)} deprem kaydı işlendi")


if __name__ == "__main__":
    main()
