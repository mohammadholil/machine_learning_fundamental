#menghapus data
import pandas as pd

data = pd.read_csv('datanilai.csv')
data.drop(10, inplace=True)
print(data.to_string())