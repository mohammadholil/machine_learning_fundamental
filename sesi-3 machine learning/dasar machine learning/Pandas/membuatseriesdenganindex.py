#membuat series dengan custom index
import pandas as pd

tamu = {
    "jumat" : 30,
    "sabtu" : 50,
    "minggu" : 70,
}
dataTamu = pd.Series(tamu)

print(dataTamu)
