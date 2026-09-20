# Komut rehberi

Sohbeti kaydırmadan bakmak için. Yeni komutlar öğrendikçe eklenir.

## Her seferinde başlarken
- `wsl -d Ubuntu`: (PowerShell'de) Linux'a girer
- `cd ~/lab/deprem-projesi`: proje klasörüne gider
- `source .venv/bin/activate`: Python ortamını açar, satırın başında (.venv) çıkar
- `sudo service docker start`: Docker'ı başlatır (her yeniden girişte gerekebilir)
- `exit`: Linux'tan çıkar

## Terminal
- `pwd`: hangi klasördeyim
- `ls` ve `ls -lh`: klasörde ne var (boyutlarıyla)
- `cd klasor`, `cd ~`, `cd ..`: klasöre gir, ev klasörüne git, bir üste çık
- `mkdir -p a/b`: klasör (ve ara klasörler) oluştur
- `touch dosya`: boş dosya oluştur
- `cat dosya`: dosyanın içini göster
- `head -n 5 dosya`: ilk 5 satırı göster
- `wc -l dosya`: satır say
- `grep "kelime" dosya`: içinde kelime geçen satırları bul
- `komut1 | komut2`: birinin çıktısını diğerine ver
- `echo "yazı" > dosya`: dosyayı sıfırdan yaz, `>>` sonuna ekler
- `curl -o hedef adres`: internetten dosya indir
- nano: Ctrl+O kaydet, Enter onay, Ctrl+X çık

## Git ve GitHub
- `git status`: hangi dosyalar değişti ya da takip edilmiyor
- `git add dosya` ya da `git add .`: değişiklikleri geçmişe eklemek üzere seç
- `git commit -m "mesaj"`: o anın fotoğrafını çek ve isim ver
- `git push`: GitHub'a gönder
- `gh auth login`: GitHub'a giriş
- `gh repo clone lab`: repoyu indir
- `.gitignore`: Git'in yok sayacağı dosya ve klasörler

## SQL (sqlite3)
- `sqlite3 veri/deprem.db`: veritabanını aç. İçinde: `.tables`, `.quit`
- Tek satırda: `sqlite3 veri/deprem.db "SELECT ...;"`
- Yazılış sırası (sabit, kullanmadığını atla): SELECT, FROM, WHERE, GROUP BY, ORDER BY, LIMIT
- WHERE: hangi satırları istiyorum (koşul). Örnek: `WHERE yer LIKE '%Hawaii%' AND buyukluk > 3`
- GROUP BY: hangi sütunla gruplayayım (sütun adı yazılır)
- ORDER BY: neye göre sıralayayım. `DESC` sadece burada durur
- `COUNT(*)`: sayar. Bir hesaptır, GROUP BY'a yazılmaz, SELECT ve ORDER BY'da kullanılır
- `ROUND(sütun)`: en yakın tam sayıya yuvarlar
- `CAST(sütun AS REAL)`: metni sayıya çevirir. Sadece ham CSV'den import edilen metin tablolarında gerekir, `depremler_temiz`'de gerekmez
- SQL yanlış sorguya da hata vermeden cevap verir: sonucun mantıklı olup olmadığına bak (örnek kontrol: `SELECT MAX(buyukluk) FROM depremler_temiz;`)

## Python
- `python3 dosya.py`: script çalıştır (basit dosyalar için ortam açmaya gerek yok)
- `python3 -m venv .venv`: izole ortam oluştur
- `pip install paket` ve `pip freeze > requirements.txt`: paket kur, listeyi kaydet
- Hata mesajının son satırı genelde sorunu söyler, önce onu oku
- Girinti kuralı: `:` ile biten satırdan sonra gelen satır 4 boşluk daha içeriden başlar
- Liste: `sayilar = [3, 8, 1]`, boş liste: `[]`, sona ekle: `liste.append(x)`
- Döngü: `for x in liste:`
- Koşul: `if x >= 50:`
- Sözlük: `d = {"yer": "Hawaii"}`, okuma: `d["yer"]`, ekleme: `d["zaman"] = "..."`
- Fonksiyon: `def isim(girdi):` ... `return sonuc`
- Toplama kalıbı: `toplam = 0`, döngüde `toplam = toplam + x`
- Süzme kalıbı: boş liste aç, döngüde `if` ile koşulu sağlayanı `append` et (SQL'deki WHERE gibi)
- Boş hücre: `float("")` hata verir, boşsa `None` kullan

## Docker
- `docker --version`, `docker run hello-world`: kurulum testi
- `docker images`: elindeki paketleri (image) listeler
- `docker build -t deprem-projesi .`: Dockerfile'dan paketi inşa eder
- `docker run --rm --user "$(id -u):$(id -g)" -v "$(pwd)/veri:/veri" deprem-projesi`: paketi çalıştırır
- `--rm`: bitince container'ı siler
- `--user ...`: dosyaları senin adına oluşturur
- `-v ...`: senin `veri` klasörünü container'ın `/veri` klasörüne bağlar
- Image paket/tarif, container onun çalışan hâli
- Dockerfile: FROM (temel imaj), WORKDIR, COPY, RUN, CMD

## Sorun çıkınca
- WSL "Çok zararlı hata": bilgisayarı yeniden başlat, sonra `wsl --update`
- Şifre unutuldu: PowerShell'de `wsl -d Ubuntu -u root`, sonra `passwd kullaniciadin`, sonra `exit`
- "Cannot connect to the Docker daemon": `sudo service docker start`
- Anlamadığın hata: yazıyı olduğu gibi kopyala, tahmin etme
