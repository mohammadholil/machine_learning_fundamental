#membuat 2 set 
merekmobil={"avanza","xenia","ertiga","jazz"}
mobilku={"avanza","jazz"}

#cek sebuah set adalah himpunan bagian
if mobilku.issubset(merekmobil):
    print("set mobilku adalah subset merek mobil")

#menambahkan elemen
merekmobil.add("mobilio")
print("setelah ditambahkan mobilio (add) :",merekmobil)

#menghapus elemen
merekmobil.remove("mobilio")
print("setelah dikurangi mobilio (remove) :",merekmobil)

#update elemen
merekmobil.update(["sigra","pickup"])
print("setelah diupdate sigra dan pickup (update) :",merekmobil)

#menghilangkan elemen yang sama
merekmobil.difference_update(mobilku)
print("diference update :",merekmobil)


