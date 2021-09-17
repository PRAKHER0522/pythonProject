import pandas as pd
print('Pandas program to create and display a one-dimensional array-like object containing an array of data')
pandas_array= pd.Series([1,2,3,4,5])
print(pandas_array)
print('type of array:'+str(type(pandas_array)))
print('convert into list')
print(pandas_array.tolist())
print(type(pandas_array.tolist()))
