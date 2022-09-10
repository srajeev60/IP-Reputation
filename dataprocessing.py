
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as pydotplus

data_csv = pd.read_csv('ipdataset.csv', low_memory=False, nrows=20000)
print(data_csv)
