#fungsi lambda mempermudah untuk memberikan fungsi dalam map

#map kuadrat menggunakan lambda
data=[1,2,3,4,5]

hasil=map(lambda x : x**2 ,data)
print(list(hasil))