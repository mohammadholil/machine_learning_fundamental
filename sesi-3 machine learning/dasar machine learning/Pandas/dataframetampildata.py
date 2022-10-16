#dataframe menampilkan data
#studi kasus : pak budi memiliki data nilai ujian harian MTK dan ingin menampilkan dalam bentuk tabel
import pandas as pd

nilaiMTK = {
    'Nama' : ['ali','doni','salman'],
    'Nilai' : [60,80,100],
    'Grade' : ['C','B','A']
}

dataNilaiMTK = pd.DataFrame(nilaiMTK)


print(dataNilaiMTK)
