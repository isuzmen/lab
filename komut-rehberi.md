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
- `git add .`: değişiklikleri geçmişe eklemek üzere seç
- `git commit -m "mesaj"`: o anın fotoğrafını çek ve isim ver
- `git push`: GitHub'a gönder
- `gh auth login`: GitHub'a giriş
- `gh repo clone lab`: repoyu indir
- `.gitignore`: Git'in yok sayacağı dosya ve klasörler

## SQL (sqlite3)
- `sqlite3 deprem.db`: veritabanını aç. İçinde: `.tables`, `.mode csv`, `.import dosya tablo`, `.quit`
- `SELECT sütunlar FROM tablo WHERE koşul ORDER BY sütun DESC LIMIT n;`
- WHERE satırları eler, ORDER BY sıralar (karıştırma)
- `GROUP BY sütun` ile `COUNT(*)`: gruplayıp say
- `CAST(sütun AS REAL)`: metni sayıya çevir (CSV'den her şey metin gelir)
- Tek satırda: `sqlite3 deprem.db "SELECT ...;"`

## Python
- `python3 -m venv .venv`: izole ortam oluştur
- `pip install paket` ve `pip freeze > requirements.txt`: paket kur, listeyi kaydet
- `python dosya.py`: script çalıştır
- Fonksiyon: `def isim(girdi):` ile başlar, `return sonuc` ile sonucu verir. Girinti (4 boşluk) önemli
- Boş hücre: `float("")` hata verir, boşsa `None` kullan

## Docker
- `docker --version` ve `docker run hello-world`
- build ve run komutları Adım 8'den sonra eklenecek

## Sorun çıkınca
- WSL "Çok zararlı hata": bilgisayarı yeniden başlat, sonra `wsl --update`
- Şifre unutuldu: PowerShell'de `wsl -d Ubuntu -u root`, sonra `passwd kullaniciadin`, sonra `exit`
- "Cannot connect to the Docker daemon": `sudo service docker start`
- Anlamadığın hata: yazıyı olduğu gibi kopyala, tahmin etme

## Docker (devamı)
- `docker build -t isim .`: Dockerfile'dan paket (image) inşa eder
- `docker run --rm -v "$(pwd)/veri:/veri" isim`: paketi çalıştırır (container), `veri` klasörünü içeri bağlar
- `--rm`: bitince container'ı siler. `--user "$(id -u):$(id -g)"`: dosyaları senin adına oluşturur
- Image paket/tarif, container onun çalışan hâli
- Dockerfile: FROM (temel imaj), WORKDIR, COPY, RUN, CMD

## SQL yazılış sırası
SELECT, FROM, WHERE, GROUP BY, ORDER BY, LIMIT (sıra sabit, kullanmadığını atla)
