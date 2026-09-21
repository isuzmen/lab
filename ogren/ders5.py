depremler = [
    {"yer":"Hawaii","buyukluk":4.1},
    {"yer":"Alaska","buyukluk":6.5},
    {"yer":"Utah","buyukluk":2.3},
]

def siniflandir(buyukluk):
    if buyukluk >= 6:
        return "Çok büyük"
    elif buyukluk >= 4:
        return "Büyük"
    else:
        return "Küçük"

for d in depremler:
    yer = d["yer"]
    buyukluk = d["buyukluk"]
    sinif = siniflandir(buyukluk)
    d["sinif"] = sinif
    print(f"{yer} : {buyukluk} ({sinif})")

print(depremler[0])
print(depremler[1]["yer"])


