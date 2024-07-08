# Web Scraping Wikipedia - Daftar Video Game Terbaik Sepanjang Masa

Proyek ini berfungsi untuk mengumpulkan data dari halaman Wikipedia yang memuat daftar video game yang dianggap terbaik sepanjang masa dan menyimpannya dalam file CSV. Proses ini dilakukan dengan menggunakan `BeautifulSoup` untuk scraping HTML dan `pandas` untuk manipulasi data.

## Prasyarat

Sebelum menjalankan kode ini, pastikan Anda telah menginstal paket-paket yang diperlukan. Anda dapat menginstalnya menggunakan pip:

```bash
pip install beautifulsoup4 requests pandas
```

## Cara Menjalankan Kode

Pastikan terminal berada di direktori yang berisi file `get_best_game_all_the_time.py`. Jalankan kode dengan perintah berikut:

```bash
python get_best_game_all_the_time.py
```

Setelah menjalankan perintah di atas, Anda akan menemukan file Best-Game-All-The-Time.csv di direktori yang sama dengan file kode
