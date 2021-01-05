import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)

print(np.__version__)

print(type(arr))

# Use a tuple to create a NumPy array:
arr1 = np.array((1,2,3,4,5))
print(arr1)

arr2 = np.array(42)
print(arr2)

arr3 = np.array([[1,2,3], [4,5,6]])
print(arr3)

# Check how many dimensions the arrays have:
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr4 = np.array([1, 2, 3, 4], ndmin=5)
print(arr4)
print("number of dimensions: ", arr.ndim)

print(arr4[0])

arr5 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print("2nd element on 1st dim: ", arr5[0,1])

print("5th element on 2nd dim: ", arr5[1, 4])

arr6 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr6[0, 1, 2])

#Use negative indexing to access an array from the end
#print the last element from the 2nd dim:
print('Last element from 2nd dim: ', arr6[1,-1])

# NumPy Array Slicing
print('from index 1 to index 5: ', arr[1:5])
print(arr[1:])
print(arr[:3])

#negative slicing
print(arr[-3:-1])

print(arr[1:5:2])

#return every other element from the entire array
print(arr[::2])

#Slicing 2-D Arrays
arr7 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#From the second element, slice elements from index 1 to index 4(not incluede)
print(arr7[1, 1:4])

#From both elements, return index 2
arr8 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr8[0:2, 2])

#From both elements, slice index 1 to index 4(not included), this will return a 2-D array
print(arr8[0:2, 1:4])






