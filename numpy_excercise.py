import numpy as np

#a. Create a null vector of size 10 but the fifth value which is 1
a = np.zeros(10)
a[4] = 1
print(a)

#b. Create a vector with values ranging from 10 to 49
a = np.arange(10,50)
print(a)

#c. Reverse a vector (first element becomes last)
a = a[::-1]
print(a)

#d. Create a 3x3 matrix with values ranging from 0 to 8
a = np.arange(9).reshape(3,3)
print(a)

#e. Find indices of non-zero elements from [1,2,0,0,4,0]
a = np.array([1,2,0,0,4,0])
b = a > 0
print(b)

#f. Create a random vector of size 30 and find the mean value
a = np.random.random(30)
b = np.mean(a)
print(b)

#g. Create a 2d array with 1 on the border and 0 inside
a = np.zeros((3,3))
a = np.pad(a, (1,1), 'constant', constant_values=(1,1))
print(a)

#h. Create a 8x8 matrix and fill it with a checkerboard pattern
a = np.zeros((8,8))
a[::2,1::2] = 1
a[1::2,::2] = 1
print(a)

#i. Create a checkerboard 8x8 matrix using the tile function
a = np.array([[0.,1.], [1.,0.]])
a = np.tile(a,(4,4))
print(a)

#j. Given a 1D array, negate all elements which are between 3 and 8, in place
Z = np.arange(11)
Z[3:9] = np.negative(Z[3:9])
print(Z)

#k. Create a random vector of size 10 and sort it
a = np.random.random(10)
a = np.sort(a)
print(a)

#l. Consider two random array A anb B, check if they are equal
A = np.random.random(10)
B = np.random.random(10)
equal = np.array_equal(A,B)
print(equal)

#m. How to convert an integer (32 bits) array into a float (32 bits) in place?
A = np.arange(10, dtype=np.int32)
print(A.dtype)
A = A.astype('float32')
print(A.dtype)

#n. How to get the diagonal of a dot product?
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diagonal(C)
print(D)


