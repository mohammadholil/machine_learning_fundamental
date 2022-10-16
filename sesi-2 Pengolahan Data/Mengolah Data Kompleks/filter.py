#fungsi filter mengembalikan data sesuai kriteria

#proses map dan filter untuk bilangan tidak sama dengan 4 :
data=[1,2,3,4,5]

hasil=map(lambda x : x !=4, data)
hasil=filter(lambda x : x !=4, data)
print(list(hasil))