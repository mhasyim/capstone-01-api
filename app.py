from flask import Flask, request 
import pandas as pd
import sqlite3

app = Flask(__name__) 

@app.route('/')
def route():
    page_html = '''
                        <html>
    <head>
        <title>Read Me</title>
    </head>

    <body>

<h1>Penggunaan API 'chinook'</h1>
<h2>Pengantar</h2> 

<i>Application Programming Interface </i> (API) ini digunakan untuk menampilkan beberapa data melalui web service. Data yang ditampilan dari database SQLLite. Berikut skema ERD database chinook.


<strong>Daftar Tabel yang ada di Database Chinook: </strong>
<ul>
    <li>`employees` menyimpan informasi pegawai</li>
    <li>`customers` menyimpan informasi customer (pelanggan)</li>
    <li>`invoices` menyimpan informasi invoice</li>
    <li>`invoices_items` menyimpan informasi rincian invoice</li>
    <li>`tracks` menyimpan informasi track lagu</li>
    <li>`playlists` menyimpan informasi playlist lagu</li>
    <li>`playlist_track` menyimpan informasi relasi antara table `tracks` dan `playlist` </li>
    <li>`media_types` menyimpan informasi jenis media</li>
    <li>`genres` menyimpan informasi genre musik</li>
    <li>`albums` menyimpan informasi album lagu</li>
    <li>`artists` menyimpan informasi artis lagu</li>
</ul>

<h2> Daftar Method</h2>

Dalam API sederhana ini, terdapat beberapa method yang telah disediakan untuk menampilkan data dari database chinook. Beberapa method tersebut antara lain:

<strong>Daftar Method dalam API Chinook:</strong>
<ul>
    <li>`customers` statis</li>
    <li>`billingcountry` statis</li>
    <li>`top_customer` dinamis</li>
    <li>`top_billingcountry` dinamis</li>
    <li>`market_by_day` dinamis</li>
    <li>`best_genres` dinamis</li>
</ul>

<ol type="1">
    <li>


        <h3>Method `customers`</h3> 

        - Keterangan    = Menampilkan data nama dari tabel customers<br>
        - Jenis         = Statis<br>
        - Output        = JSON<br>
        - Parameter     = TIDAK ADA
        <br><br>
        <strong>Contoh Penggunaan</strong><br>
        <ul>
            <li>`http://127.0.0.1:5000/chinook/customers`</li>
        </ul>
        
        

    </li>

    <li>

        <h3>Method `billingcountry`</h3> 
        
        - Keterangan    = Menampilkan data billingcountry dari tabel invoices<br>
        - Jenis         = Statis<br>
        - Output        = JSON<br>
        - Parameter     = TIDAK ADA
        
        <br><br>
        <strong>Contoh Penggunaan </strong><br>
        <ul>
            <li>`http://127.0.0.1:5000/chinook/billingcountry`</li>
        </ul>

    </li>


    <li>

        
<h3>Method `top_customer`</h3>

- Keterangan    = Menampilkan informasi customer yang paling banyak bertransaksi<br>
- Jenis         = Dinamis<br>
- Output        = JSON<br>
- Parameter   <br>
    - `get` (integer) berupa filter angka untuk menampilkan daftar teratas sesuai angka yang dimasukkan dalam parameter tersebut  

    <br><br>
<strong>Contoh Penggunaan</strong><br>
<ul>
    <li>`http://127.0.0.1:5000/chinook/top_customer` menampilkan seluruh customer diurutkan dari yang paling banyak transaksi</li>
    <li>`http://127.0.0.1:5000/chinook/top_customer?get=5` hanya menampilkan lima terbanyak</li>
</ul>


    </li>
    <li>

        

<h3>Method `top_billingcountry`</h3>

- Keterangan    = Menampilkan informasi negara yang paling banyak transaksi<br>
- Jenis         = Dinamis<br>
- Output        = JSON<br>
- Parameter   <br>
    - `get` (integer) berupa filter angka untuk menampilkan daftar teratas sesuai angka yang dimasukkan dalam parameter tersebut 
    <br><br>
<strong>Contoh Penggunaan</strong><br>
<ul>
    <li>`http://127.0.0.1:5000/chinook/top_billingcountry` menampilkan seluruh negara diurutkan dari yang paling banyak transaksi</li>
    <li>`http://127.0.0.1:5000/chinook/top_billingcountry?get=3` hanya menampilkan tiga terbanyak</li>
</ul>



    </li>
    <li>




        <h3> Method `market_by_day`</h3>

        - Keterangan    = Menampilkan data market berdasarkan negara dan hari<br>
        - Jenis         = Dinamis<br>
        - Output        = JSON<br>
        - Parameter   <br>
            - `country` (string) untuk filter berdasarkan negara tertentu sesuai yang dimasukkan <br>
            - `day` (string) untuk filter berdasarkan hari
        
        <br><br><strong>Contoh Penggunaan</strong>
        <ul>
            <li>`http://127.0.0.1:5000/chinook/market_by_day` menampilkan seluruh data</li>
            <li>`http://127.0.0.1:5000/chinook/market_by_day?country=USA` hanya menampilkan data amerika</li>
            <li>`http://127.0.0.1:5000/chinook/market_by_day?day=Saturday` hanya menampilkan data hari Sabtu</li>
            <li>`http://127.0.0.1:5000/chinook/market_by_day?country=USA&day=Saturday` hanya menampilkan data Amerika di hari Sabtu</li>
        </ul>
        

    </li>
    <li>



        <h3>Method `best_genres`</h3> 

        - Keterangan    = Menampilkan informasi genres dari setiap negara yang bertransaksi<br>
        - Jenis         = Dinamis<br>
        - Output        = JSON<br>
        - Parameter   <br>
            - `country` (string) untuk filter berdasarkan negara tertentu sesuai yang dimasukkan <br>
            - `year` (integer)  untuk filter berdasarkan tahun transaksi<br><br>
        
        <strong>Contoh Penggunaan</strong>
        <ul>
            <li>`http://127.0.0.1:5000/chinook/best_genres` menampilkan seluruh data</li>
            <li>`http://127.0.0.1:5000/chinook/best_genres?country=Denmark` hanya menampilkan data Denmark</li>
            <li>`http://127.0.0.1:5000/chinook/best_genres?year=2009` hanya menampilkan data tahun 2009</li>
            <li>`http://127.0.0.1:5000/chinook/best_genres?country=Denmark&year=2009` hanya menampilkan data Amerika di hari Sabtu</li>
        </ul>
        


    </li>
    
</ol>




<br><br><br><br>
    </body>
</html>
                            '''

    return page_html

# =============================================================================================
# Nama Method   = customers
# Keterangan    = Menampilkan data nama dari tabel customers
# Jenis         = Statis
# Parameter     = TIDAK ADA
# =============================================================================================
@app.route('/chinook/customers') 
def customers(): 
    conn = sqlite3.connect("data/chinook.db")
    customers = pd.read_sql_query(
                        '''
                        SELECT Firstname, Lastname 
                        FROM customers
                        order by Firstname
                            ''', conn)

    return (customers.to_json())

# =============================================================================================
# Nama Method   = billingcountry
# Keterangan    = Menampilkan data billingcountry dari tabel invoices
# Jenis         = Statis
# Parameter     = TIDAK ADA
# =============================================================================================
@app.route('/chinook/billingcountry') 
def billingcountry(): 
    conn = sqlite3.connect("data/chinook.db")
    billing_country = pd.read_sql_query(
                       '''
                        SELECT a.FirstName, a.LastName, a.CustomerId, b.BillingCountry Country, b.InvoiceDate, sum(b.Total) as Total
                        FROM invoices b
                        LEFT JOIN customers a ON a.CustomerId = b.CustomerId
                        group by a.FirstName, a.LastName
                        order by Total desc
                            ''', conn, index_col='CustomerId')

    billing_country = billing_country.groupby(['Country']).agg({'Total': 'sum'}).sort_values('Total', ascending=False)

    return (billing_country.to_json())



# =============================================================================================
# Nama Method   = top_customer
# Keterangan    = Menampilkan informasi customer yang paling banyak bertransaksi
# Jenis         = Dinamis
# Parameter   
#   - GET (INTEGER)     = berupa filter angka untuk menampilkan daftar teratas sesuai 
#                         angka yang dimasukkan dalam parameter tersebut 
# =============================================================================================
@app.route('/chinook/top_customer') 
def top_customer(): 
    conn = sqlite3.connect("data/chinook.db")
    key = 'get'
    limit = ''
    get = request.args.get(key)
    query = '''
            SELECT a.FirstName, a.LastName, a.CustomerId, b.BillingCountry Country, sum(b.Total) as Total
            FROM invoices b
            LEFT JOIN customers a ON a.CustomerId = b.CustomerId
            group by a.FirstName, a.LastName
            order by Total desc
                '''
    if (get):
        limit = ' LIMIT '+get
    
    #append string
    query = query + limit
    top_customer = pd.read_sql_query(query, conn, index_col='CustomerId')

    #chek data is found
    if(top_customer['FirstName'].notna().sum() > 0):
            return (top_customer.to_json())
    
    return 'Data Not Found'


# =============================================================================================
# Nama Method   = top_billingcountry
# Keterangan    = Menampilkan informasi negara yang paling banyak transaksi
# Jenis         = Dinamis
# Parameter   
#   - GET (INTEGER)       = berupa filter angka untuk menampilkan daftar teratas sesuai 
#                           angka yang dimasukkan dalam parameter tersebut 
# =============================================================================================
@app.route('/chinook/top_billingcountry') 
def top_billingcountry(): 
    conn = sqlite3.connect("data/chinook.db")
    key = 'get'
    limit = ''
    get = request.args.get(key)
    query ='''
    SELECT InvoiceId, BillingCountry Country, sum(Total) as Total
    FROM invoices
    group by Country
    order by Total desc
        '''
    if (get):
        limit = ' LIMIT '+get
    
    #append string
    query = query + limit
    top_billingcountry = pd.read_sql_query(query, conn, index_col='InvoiceId')

    #chek data is found
    if(top_billingcountry['Country'].notna().sum() > 0):
            return (top_billingcountry.to_json())
    
    return 'Data Not Found'
    

# =============================================================================================
# Nama Method   = market_by_day
# Keterangan    = Menampilkan data market berdasarkan negara dan hari
# Jenis         = Dinamis
# Parameter
#   - COUNTRY (STRING)       = untuk filter berdasarkan negara tertentu sesuai yang dimasukkan 
#   - DAY (STRING)           = untuk filter berdasarkan hari
# =============================================================================================
@app.route('/chinook/market_by_day') 
def market_by_day(): 
    conn = sqlite3.connect("data/chinook.db")
    key1 = 'country'
    key2 = 'day'
    where = ''
    country = request.args.get(key1)
    day = request.args.get(key2)

    query = "SELECT * FROM invoices"
    
    if (country):
        where = " WHERE lower(BillingCountry) like '%"+country.lower()+"%' "
    else:
        where = ''
    
    query = query + where
    invoice = pd.read_sql_query(query, conn, parse_dates=['InvoiceDate'])

    #create new column with date function
    invoice['Invoice_dayname'] = invoice['InvoiceDate'].dt.day_name()
    
    # set day order
    dayorder = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # using categorical method
    invoice['Invoice_dayname'] = pd.Categorical(invoice['Invoice_dayname'], categories=dayorder, ordered=True)

    if (day):
        invoice = invoice[invoice['Invoice_dayname'].str.lower() == day.lower()]

    invoice = invoice.pivot_table(index='BillingCountry',
                                columns='Invoice_dayname',
                                values='Total',
                                aggfunc='sum')

 
    return (invoice.to_json())



# =============================================================================================
# Nama Method   = best_genres
# Keterangan    = Menampilkan informasi genres dari setiap negara yang bertransaksi
# Jenis         = Dinamis
# Parameter
#   - COUNTRY (STRING)       = untuk filter berdasarkan negara tertentu sesuai yang dimasukkan 
#   - YEAR (INTEGER)         = untuk filter berdasarkan tahun transaksi
# =============================================================================================
@app.route('/chinook/best_genres') 
def best_genres(): 
    conn = sqlite3.connect("data/chinook.db")
    key1 = 'country'
    key2 = 'year'
    where = ''
    country = request.args.get(key1)
    year = request.args.get(key2)
    query ='''
        SELECT 
            BillingCountry AS Country, d.Name AS Genre, strftime('%Y', a.invoiceDate) Year 
            FROM invoices a 
            LEFT JOIN invoice_items b ON a.InvoiceId = b.InvoiceId
            LEFT JOIN tracks c ON b.TrackId = c.TrackId 
            LEFT JOIN genres d ON c.GenreId = d.GenreId
            '''
    if (country and year):
        where = " WHERE lower(Country) like '%"+country.lower()+"%' and Year='"+year+"'"
    elif (country):
        where = " WHERE lower(Country) like '%"+country.lower()+"%'"
    elif (year):
        where = " WHERE Year='"+year+"'"
    else:
        where = ''
    
    #append string
    query = query + where
    best_genres = pd.read_sql_query(query, conn)

    #chek data is found
    if(best_genres['Country'].notna().sum() > 0):
            return (best_genres.to_json())
    
    return 'Data Not Found'




if __name__ == '__main__':
    app.run(debug=False, port=5000)
