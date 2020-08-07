# Penggunaan API 'chinook'
## Pengantar

<i>Application Programming Interface </i> (API) ini digunakan untuk menampilkan beberapa data melalui web service. Data yang ditampilan dari database SQLLite. Berikut skema ERD database chinook.


**Daftar Tabel yang ada di Database Chinook:**
- `employees` menyimpan informasi pegawai
- `customers` menyimpan informasi customer (pelanggan)
- `invoices` menyimpan informasi invoice
- `invoices_items` menyimpan informasi rincian invoice
- `tracks` menyimpan informasi track lagu
- `playlists` menyimpan informasi playlist lagu
- `playlist_track` menyimpan informasi relasi antara table `tracks` dan `playlist` 
- `media_types` menyimpan informasi jenis media
- `genres` menyimpan informasi genre musik
- `albums` menyimpan informasi album lagu
- `artists` menyimpan informasi artis lagu

## Daftar Method

Dalam API sederhana ini, terdapat beberapa method yang telah disediakan untuk menampilkan data dari database chinook. Beberapa method tersebut antara lain:

**Daftar Method dalam API Chinook:**
- `customers` statis
- `billingcountry` statis
- `top_customer` dinamis
- `top_billingcountry` dinamis
- `market_by_day` dinamis
- `best_genres` dinamis

### Method `customers`

- Keterangan    = Menampilkan data nama dari tabel customers
- Jenis         = Statis
- Output        = JSON
- Parameter     = TIDAK ADA

**Contoh Penggunaan**

- `http://127.0.0.1:5000/chinook/customers`

### Method `billingcountry`

- Keterangan    = Menampilkan data billingcountry dari tabel invoices
- Jenis         = Statis
- Output        = JSON
- Parameter     = TIDAK ADA

**Contoh Penggunaan**

- `http://127.0.0.1:5000/chinook/billingcountry`

### Method `top_customer`

- Keterangan    = Menampilkan informasi customer yang paling banyak bertransaksi
- Jenis         = Dinamis
- Output        = JSON
- Parameter   
    - `get` (integer) berupa filter angka untuk menampilkan daftar teratas sesuai angka yang dimasukkan dalam parameter tersebut  

**Contoh Penggunaan**

- `http://127.0.0.1:5000/chinook/top_customer` menampilkan seluruh customer diurutkan dari yang paling banyak transaksi
- `http://127.0.0.1:5000/chinook/top_customer?get=5` hanya menampilkan lima terbanyak

### Method `top_billingcountry`

- Keterangan    = Menampilkan informasi negara yang paling banyak transaksi
- Jenis         = Dinamis
- Output        = JSON
- Parameter   
    - `get` (integer) berupa filter angka untuk menampilkan daftar teratas sesuai angka yang dimasukkan dalam parameter tersebut 

**Contoh Penggunaan**

- `http://127.0.0.1:5000/chinook/top_billingcountry` menampilkan seluruh negara diurutkan dari yang paling banyak transaksi
- `http://127.0.0.1:5000/chinook/top_billingcountry?get=3` hanya menampilkan tiga terbanyak

### Method `market_by_day`

- Keterangan    = Menampilkan data market berdasarkan negara dan hari
- Jenis         = Dinamis
- Output        = JSON
- Parameter   
    - `country` (string) untuk filter berdasarkan negara tertentu sesuai yang dimasukkan 
    - `day` (string) untuk filter berdasarkan hari

**Contoh Penggunaan**

- `http://127.0.0.1:5000/chinook/market_by_day` menampilkan seluruh data
- `http://127.0.0.1:5000/chinook/market_by_day?country=USA` hanya menampilkan data amerika
- `http://127.0.0.1:5000/chinook/market_by_day?day=Saturday` hanya menampilkan data hari Sabtu
- `http://127.0.0.1:5000/chinook/market_by_day?country=USA&day=Saturday` hanya menampilkan data Amerika di hari Sabtu


### Method `best_genres`

- Keterangan    = Menampilkan informasi genres dari setiap negara yang bertransaksi
- Jenis         = Dinamis
- Output        = JSON
- Parameter   
    - `country` (string) untuk filter berdasarkan negara tertentu sesuai yang dimasukkan 
    - `year` (integer)  untuk filter berdasarkan tahun transaksi

**Contoh Penggunaan**

- `http://127.0.0.1:5000/chinook/best_genres` menampilkan seluruh data
- `http://127.0.0.1:5000/chinook/best_genres?country=Denmark` hanya menampilkan data Denmark
- `http://127.0.0.1:5000/chinook/best_genres?year=2009` hanya menampilkan data tahun 2009
- `http://127.0.0.1:5000/chinook/best_genres?country=Denmark&year=2009` hanya menampilkan data Amerika di hari Sabtu

