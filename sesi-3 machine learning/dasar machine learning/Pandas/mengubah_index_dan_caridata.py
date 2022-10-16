import pandas as pd

tamu=[10,20,30,40]
dTamu = pd.Series(tamu, index=["jumat","sabtu","minggu","senin"])

#TAMPILKAN HARI TERTENTU
print(dTamu["minggu"])
#print(dTamu)