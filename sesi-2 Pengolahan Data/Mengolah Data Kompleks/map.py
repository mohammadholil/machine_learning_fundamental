#fungsi map untuk mengubah nilai sebuah list atau set 

#map sebuah data dengan fungsi kuadrat
data = [1,2,3,4,5]

def kuadrat(x):
    return x**2

hasil = map(kuadrat, data)
print(list(hasil))