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

zero_array = np.zeros((10, 3), dtype=np.float32)
print(zero_array)

one_array = np.ones((10, 3))
print(one_array)

similar = np.ones_like(identity_array)
print(similar)

'''
Array Indexing and Reshaping
    The default behavior for array indexing is the same as python slicing.
'''
array = np.random.randn(100,10,20,3)
print(array[:, 0, 0, 0])

print(array[:, :, 0, 0])

print(array[:10:3, 0, 0, 0])

print(array[:-2, 0, 0, 0])

# Pay attention to the following code! Slicing does not create a copy!
x = np.random.randn(10, 10)
print(x)

y = x[:, 0]
y[:] = 1
print(x) # x is changed as well










