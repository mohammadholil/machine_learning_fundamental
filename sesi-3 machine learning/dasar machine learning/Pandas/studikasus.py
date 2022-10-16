#bayangkan anda adalah seorang admin penjualan di perusahaan 
#anda sering berinteraksi yang berisi nomor transaksi, tanggal, barang, terjual
#buatlah file csv yang memuat data diatas bermainlah dengan fungsi pandas!

import pandas as pd

#menampilkan data
dataPenjualan = pd.read_csv('datapenjualan.csv')
#menghapus data
dataPenjualan.drop(11, inplace=True)
print(dataPenjualan.to_string())

#menampilkan 5 data teratas
print(dataPenjualan.head(5))

#menampilkan 3 data terbawah
print(dataPenjualan.tail(3)) 


