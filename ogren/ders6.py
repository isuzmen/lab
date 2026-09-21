import csv

with open("../deprem-projesi/data/deprem.csv") as f:
    satirlar = list(csv.DictReader(f))

print(len(satirlar))
print(satirlar[0]["place"])
print(satirlar[0]["mag"])
print(type(satirlar[0]["mag"]))

sayac = 0
for satir in satirlar:
    if satir ["mag"] != "":
        if float(satir["mag"]) >= 4:
            sayac += 1
print(f"4 ve üstü: {sayac}")


