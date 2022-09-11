
import pandas as pd

data_csv = pd.read_csv('ipdataset.csv', low_memory=False, nrows=20000)
print(data_csv.columns)

