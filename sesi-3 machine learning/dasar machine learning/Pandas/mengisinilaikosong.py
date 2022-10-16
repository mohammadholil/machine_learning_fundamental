#mengisi nilai yang kosong
import pandas as pd

data = pd.read_csv('datanilai.csv')
data["GRADE"].fillna("C",inplace=True)
print(data.to_string())

