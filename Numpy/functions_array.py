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
#apply operation along axis
print('*****operation along axis by mention axis******')
b =np.arange(12).reshape(3,4)
print(b)
print('*****operation along column axis by mention axis= 0 ******')
print(b.sum(axis=0))
print('*****operation along row axis by mention axis= 1 ******')
print(b.sum(axis=1))
c =np.arange(24).reshape(2,3,4)
print('*****operation along column axis by mention axis= 2 ******')
print(c)
print(c.sum(axis=2))
print('*****cumulative sum along axis 1 ******')
print(b.cumsum(axis =1))
print('*****universal function provide by numpy(sin,cos,exp ******')
uni_array= np.arange(5)
print(uni_array)
print('*****universal function exp(e^2) ******')
print(np.exp(uni_array))
print('*****universal function sin ******')
print(np.sin(uni_array))
print('*****test a array element wise for finiteness ******')
elem = np.array([1,2,3,np.NaN,np.inf])
print(np.isfinite(elem))
print('*****#Test element-wise for positive or negative infinity. ******')
print(np.isinf(elem))
print('*****# test element-wise for NaN of a given array ******')
print(np.isnan(elem))
print('*****# test element-wise for complex number, real number of a given array ******')
print(np.iscomplex(elem))
elem1 = np.array([1+1j,2+0j])
print('*****# test element-wise for complex number ******')
print(np.iscomplex(elem1))
print('*****# test element-wise for real number of a given array ******')
print(np.isreal(elem1))