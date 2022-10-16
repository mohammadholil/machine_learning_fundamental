import pandas as pd

data = pd.read_csv('datanilai.csv')
print(data.to_string())

#menampilkan data teratas
print(data.head(3))