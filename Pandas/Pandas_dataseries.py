import pandas as pd
print('Pandas program to create and display a one-dimensional array-like object containing an array of data')
pandas_array= pd.Series([1,2,3,4,5])
print(pandas_array)
print('type of array:'+str(type(pandas_array)))
print('convert into list')
print(pandas_array.tolist())
print(type(pandas_array.tolist()))
ds1=pd.Series([2, 4, 6, 8, 10])
ds2=pd.Series([1, 3, 5, 7, 9])
ds_add=ds1+ds2
print('addition:'+'\n'+str(ds_add))
ds_sub=ds1-ds2
print('substract:'+'\n'+str(ds_sub))
ds_mul=ds1*ds2
print('Multiple:'+'\n'+str(ds_mul))
ds_div=ds1/ds2
print('divide:'+'\n'+str(ds_div))
ds3=pd.Series([2, 4, 6, 8, 10])
ds4=pd.Series([1, 3, 5, 7, 10])
ds_comp=ds3==ds4
print(ds_comp)
fam = [1,2,3,4]
for index,height in enumerate(fam):
    print(str(index) + ":" +str(height))
