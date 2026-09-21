import csv

with open("../deprem-projesi/data/deprem.csv") as f:
    satirlar = list(csv.DictReader(f))
satirsayisi = len(satirlar)
print(f"Toplam: {satirsayisi}")

en_buyuk = 0
en_buyuk_yer = ""

for satir in satirlar:
    if satir["mag"] != "":
        buyukluk = float(satir["mag"])
        if buyukluk > en_buyuk:
            en_buyuk = buyukluk
            en_buyuk_yer = satir["place"]

print(f"En büyük: {en_buyuk} ({en_buyuk_yer})")

sayac = 0
for satir in satirlar:
    if satir["mag"] != "":
        if float(satir["mag"]) >= 4:
            sayac += 1

print(f"4 ve üstü: {sayac}")
