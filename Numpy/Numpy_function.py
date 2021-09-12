import numpy as np
#creating numpy array from list.
a = np.arange(15).reshape(3,5)
b = np.array([[0.0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19]])
print(a)
print(b)
#calculating dimension or axis of numpy array
print('Dimension of array a is: ' + str(a.ndim))
print('Dimension of array b is: ' + str(b.ndim))
#calculating shape of numpy array
print("shape of array a is" +str(a.shape))
print("shape of array b is" +str(b.shape))
# dtype of numpy array
print('Type of element in array a:'+str(a.dtype))
print('Type of element in array b:'+str(b.dtype))