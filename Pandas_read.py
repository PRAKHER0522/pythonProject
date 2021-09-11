#reading file to pandas
import pandas as pd
data = pd.read_csv("indexData.csv")
print(data)
print('*****************')
print(data.info())


