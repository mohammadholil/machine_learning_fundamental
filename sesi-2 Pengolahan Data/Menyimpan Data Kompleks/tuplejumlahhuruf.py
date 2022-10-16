#mencari jumlah a pada rangkain kata berikut:
#satu dua tiga empat lima enam tujuh delapan

Data=("satu","dua","tiga","empat","lima","enam","tujuh","delapan")
print("Data Tuple :",Data)

i=0
hitungA=0
for x in Data:
    for y in Data[i]:
        if y=="u":
            hitungA=hitungA+1
    i=i+1
print("jumlah huruf 'u' ada :",hitungA)