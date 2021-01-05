import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

newarr = arr.reshape(2, 3, 2)
print(newarr)
print(newarr.dtype)
print(newarr.ndim)

newarr = arr.reshape(3, 2, 2)
print(newarr)


newarr = arr.reshape(2, 2, 3)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)

newarr = arr.reshape(2, 2, -1)

print(newarr)


#Flattening the arrays
#Flattening array means converting a multidimensional array into a 1D array
#We can use reshape(-1) to do this
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)




