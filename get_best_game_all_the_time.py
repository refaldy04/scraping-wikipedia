from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL halaman Wikipedia yang akan di-scrape
url = 'https://en.wikipedia.org/wiki/List_of_video_games_considered_the_best'

# Mengirim permintaan GET ke halaman Wikipedia
page = requests.get(url)

# Mem-parse konten halaman dengan BeautifulSoup
soup = BeautifulSoup(page.text, 'html')

# Menemukan tabel kedua di halaman (tabel dengan data yang diinginkan)
table = soup.find_all('table')[1]

# Mendapatkan baris header dari tabel
header_row = table.find_all('tr')[0]

# Mengambil semua judul kolom dari header tabel
world_titles = header_row.find_all('th')

# Membersihkan teks dari judul kolom dan menyimpannya dalam daftar
world_table_titles = [title.text.strip() for title in world_titles]

# Membuat DataFrame dengan judul kolom yang diambil
df = pd.DataFrame(columns = world_table_titles)

# Mengambil semua baris data dari tabel
column_data = table.find_all('tr')

# Variabel untuk menyimpan header terakhir yang ditemukan (digunakan untuk menangani rowspan)
last_header = None

# Memproses setiap baris data dalam tabel (dimulai dari baris kedua)
for row in column_data[1:]:
    # Mengambil header dari baris (jika ada)
    header = row.find('th')
    # Mengambil semua data sel dari baris
    row_data = row.find_all('td')
    
    # Jika baris memiliki header
    if header:
        # Mendapatkan teks header
        header_text = header.get_text(strip=True)
        # Periksa apakah header memiliki atribut rowspan
        if header.has_attr('rowspan'):
            # Simpan header sebagai last_header jika memiliki rowspan
            last_header = header_text
        else:
            # Jika tidak, reset last_header
            last_header = None
    else:
        # Jika tidak ada header, gunakan last_header
        header_text = last_header

    # Jika header_text tersedia, gabungkan dengan data sel
    if header_text:
        individual_row_data = [header_text] + [data.text.strip() for data in row_data]

    # Menambahkan data baris ke DataFrame
    length = len(df)
    df.loc[length] = individual_row_data

# Menyimpan DataFrame ke file CSV
df.to_csv(r'D:\work\tech-celup\scraping\Best-Game-All-The-Time.csv', index = False)
