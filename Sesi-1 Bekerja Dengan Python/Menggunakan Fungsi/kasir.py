jumlah=int(input("jumlah :"))
harga=int(input("harga :"))

def hitungTotal(a,b):
    return a*b
def hitungNet(c,d):
    return hitungTotal(c, d)-5000

if (hitungTotal(jumlah,harga)>=2000):
    print(hitungNet(jumlah,harga))
else :
    print(hitungTotal(jumlah,harga))