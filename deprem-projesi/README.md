# Deprem verisi

USGS'in son bir haftalık deprem verisini indirip yerel bir SQLite veritabanına yazan küçük bir veri hattı. Docker içinde çalışır.

## Ne yapar
1. USGS'in herkese açık deprem CSV dosyasını indirir.
2. Satırları ayırır ve sayı sütunlarını gerçek sayıya çevirir (boş hücreler `None` olur).
3. `depremler_temiz` tablosuna yazar. Her depremin `id`'si benzersiz olduğu için scripti tekrar çalıştırmak aynı depremi ikinci kez eklemez.

Tablo sütunları: `id, zaman, enlem, boylam, derinlik, buyukluk, yer`

## Nasıl çalıştırılır
Gereksinim: Docker.

~~~
docker build -t deprem-projesi .
mkdir -p veri
docker run --rm --user "$(id -u):$(id -g)" -v "$(pwd)/veri:/veri" deprem-projesi
~~~

Sonuç `veri/deprem.db` dosyasına yazılır. `veri/` klasörü Git'e girmez.

## Sonuca bakmak
Python ile (ek paket gerekmez):

~~~
python3 ozet.py
python3 en_buyuk.py
~~~

`ozet.py` toplam deprem sayısını, en büyük büyüklüğü ve büyüklüğü 4'ten büyük depremlerin sayısını yazar. `en_buyuk.py` en büyük 5 depremi listeler.

SQLite ile:

~~~
sqlite3 veri/deprem.db "SELECT COUNT(*) FROM depremler_temiz;"
~~~

## Dosyalar
- `indir_ve_yaz.py`: indirir ve veritabanına yazar
- `Dockerfile`, `requirements.txt`, `.dockerignore`: Docker paketi
- `ozet.py`, `en_buyuk.py`: veritabanından okuyan küçük sorgu scriptleri

## Veri kaynağı
USGS Earthquake Hazards Program, son 7 gün:
https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.csv

USGS her seferinde sadece son bir haftayı verir. Eski kayıtlar bu pencereden düşse bile veritabanında kalır, çünkü script kayıt silmez, sadece ekler ya da günceller.

## Bilinen sınırlar
- `yer` sütunu "16 km NE of Milford, Utah" gibi ham metin. Bölgeye göre saymak için önce temizlenmesi gerekir.
- Çalıştırma şu an üç komut. Tek komuta indirmek sonraki adım.

## Sonraki adımlar
PostgreSQL ve Docker Compose ile gerçek bir veritabanı sunucusuna geçmek.
