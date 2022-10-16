#menghapus data duplikat
import pandas as pd

data = pd.read_csv('datanilai.csv')
data.drop_duplicates(inplace=True)
print(data.to_string())

