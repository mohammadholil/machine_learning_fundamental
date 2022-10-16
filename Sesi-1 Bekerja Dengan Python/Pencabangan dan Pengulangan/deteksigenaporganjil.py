bil = int(input("masukkan bilangan : "))
if (bil <0) :
    print("masukkan bilangan positif")
else :
    if (bil % 2) == 0 :
        print(("{0} adalah bilangan genap".format(bil)))
    else :
        print("{0} adalahb bilangan ganjil".format(bil))