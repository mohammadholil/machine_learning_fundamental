#fungsi reduce mengembalikan satu nilai hasil pengolahan sekelpmpok data 

#mencari bilangan terbesar
from functools import reduce

data=[1,2,3,4,5,6]

print(reduce(max, data,))