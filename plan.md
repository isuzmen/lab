# Plan

## Yöntem

### Merdiven (her konu için)
1. Oku ve çalıştır
2. Değiştir
3. Boşluk doldur
4. Boş dosyadan yaz (bakarak serbest)
5. Bakmadan yaz

Hedef seviye: S1 için 1-2, S2 için 4, S3 için 5. Alttaki basamağı takılmadan yapınca üste geçilir.

### Oturum türleri ve sıra
Yapım, yapım, yazma, tekrar, sonra başa. Yazma oturumu atlanarak yeni konuya geçilmez.
Yorgun günün asgari dozu: 15 dakikalık tekrar ya da tek commit.

### Tekrar takvimi
Bir şeyi bakmadan yazabildiğinde 2, 7, 21 gün sonra tekrar edilir. Yapılamazsa bir basamak aşağı inilir ve aralık baştan başlar. Tarihler tekrar.md'de.

### Takılma protokolü
20 dakika kendin dene, hata mesajının son satırını oku, dokümana bak. 40. dakikada Claude'a getir ve ne denediğini yaz. Aynı tür takılma ikinci kez gelirse sıradaki alıştırma konusu olur.

### Kapı kuralı
Aşama, kanıt görevlerinin hepsi geçilince kapanır. Liste dışı konular bekler.

## Aşama 1: kapalı liste
- Terminal: S2, ilk 10 komut bakmadan (S3)
- Git: S2, add/commit/push/pull/clone, branch ve pull request
- SQL: SELECT/WHERE/GROUP BY/ORDER BY/LIMIT bakmadan (S3), CREATE TABLE/INSERT/JOIN S2
- Python: değişken, if, for, liste, sözlük, fonksiyon, dosya okuma, try/except S3. requests ve sqlite3 S2. Sınıflar S1
- JSON ve API'den veri çekmek: S2
- Docker: S2, Dockerfile/build/run/volume/port/ortam değişkeni/Compose
- PostgreSQL: S2 (Compose ile ayağa kaldırıp script'ten yazmak)
- Gizli bilgiler: .env ve ortam değişkeni, şifre GitHub'a girmez (S2)
- Bash scripti: S2
- Ağ temeli: S1-S2 (HTTP, DNS, IP, port)
- VS Code + WSL: S2

## Kanıt görevleri (Aşama 1 kapısı)
1. ozet.py boş dosyadan, bakmadan
2. SQL'de 5 soru bakmadan (JOIN hariç)
3. Bir değişikliği branch ve pull request ile GitHub'a almak
4. Scripti Postgres'e yazacak şekilde Compose ile çalıştırmak (bakarak olur)
5. Repoyu başka klasöre clone edip README'deki tek komutla çalıştırmak, veriyi indirip satır sayısını yazan bir bash scripti yazmak (bakarak olur)

## Aşama 1'de yasak
Kubernetes, bulut, Terraform, FastAPI, pandas derinliği.

## Roadmap.sh kontrolü
Aşama 1 kapanırken Linux, Git and GitHub, SQL, PostgreSQL, Python, Docker haritalarıyla bu liste karşılaştırılacak. Eksik çıkan varsa listeye eklenecek, fazla olan "sonra" ya da "atla" diye işaretlenecek.

## Sonraki aşamalar
Aynı kalıp: aşama başında kapalı liste ve kanıt görevleri. Aşama 2 (bulut ve DevOps) listesi Aşama 1 kapanırken yazılacak.
