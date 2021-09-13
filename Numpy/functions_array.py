import numpy as np
#creating zeros array
zeros_array= np.zeros((3,4),dtype=int)
print('*****zeros-array******')
print(zeros_array)
#creating ones array
ones_array = np.ones((3,4),dtype=int)
print('*****ones-array******')
print(ones_array)
#numpy arange function
numpy_arange= np.arange(10, 30, 5)
print('*****numpy_arange function******')
print(numpy_arange)
#numpy linspace function
print('*****numpy_linspace function******')
numpy_linspace=np.linspace(10, 30, 5)
print(numpy_linspace)
#type of array using numpy and arange function
print('*****1d array******')
a = np.arange(6)
print(a)
print('*****2d array******')
a=np.arange(12).reshape(3,4)
print(a)
print('*****3d array******')
a=np.arange(24).reshape(2,3,4)
print(a)