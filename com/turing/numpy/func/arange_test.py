import numpy as np

array1 = np.array([[1,2,3],[4,5,6]])
print(array1)

array2 = np.random.randn(10, 2)
print(array2)
print(array2.shape)

array3 = np.arange(15).reshape(5, 3)
print(array3)

#generate n x n array with its main diagonal set to one, and all other elements 0.
identity_array = np.identity(10, dtype=np.float32)
print(identity_array)