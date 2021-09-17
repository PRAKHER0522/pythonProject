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
print('***NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two gy =np iven arrays***')
x = np.array([4,2,6])
y = np.array([3,5,6])
print(np.greater(x,y))
print(np.greater_equal(x,y))
print(np.less(x,y))
print(np.less_equal(x,y))
print('***** NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied by the array****')
arr = np.array([1,7,13,105])
print(type(arr))
print("%d bytes" % (arr.size ))
print("%d bytes" % (arr.itemsize ))
print("%d bytes" % (arr.size * arr.itemsize))
zeros_arr = np.zeros(10).reshape(5,2)
print(zeros_arr)
ones_arr = np.ones(10,dtype=int)
print(ones_arr)
fives_arr = np.ones(10,dtype=int)*5
print(fives_arr)
#array of all the even integers from 30 to 70.
arr_30_70 = np.arange(30,71,2)
print(arr_30_70)
print('3*3 martrix')
arr_identity = np.identity(3)
print(arr_identity)
print('random number 0 and 1')
rand_num  = np.random.normal(0,1,1)
print(rand_num)
print('random number 15')
rand_num_15  = np.random.normal(0,1,15)
print(rand_num_15)
print("####vector is a numpy array 1D#####")
print("Horizonal vector")
horz_vector = np.arange(3)
print(horz_vector)
print("Vertical vector")
vert_vector = np.array([[3],[2],[1]])
print(vert_vector)
print('*** vector with values ranging from 15 to 55 and print all valuesexcept the first and last**')
vector1 = np.arange(15,56)
vector2 = vector1[1:-1]
print('vector1 :' +str(vector1))
print('vector2 :' +str(vector2))
print('vector 3*4')
array3 = np.arange(12).reshape(3,4)
print(array3)
print("each element of array!!!")
for x in np.nditer(array3):
    print(x,end=" ")
print("\n")
print("vector of length 10 with values evenly distributed between 5 and 50.")
vector3=np.linspace(6,50,5,dtype=int)
print(vector3)
vector4 = np.arange(21)
print(vector4)
print("change sign  between 9 and 15")
for x in np.nditer(vector4):
    if x >=9 and x <=15:
        print(-x,end=" ")
    else:
        print(x,end=" ")
print("\n")
vector5 = np.random.randint(0,10,5)
print(vector5)
print("Multiplication of 2 vector!!!")
vector6 = np.arange(3,dtype="int32")
vector7 = np.array([3,4,5],dtype="int32")
print("vector6"+str(vector6))
print("vector7"+str(vector7))
vector_mul=vector6*vector7
print("vector_mul "+str(vector_mul))




