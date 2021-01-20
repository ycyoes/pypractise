import numpy as np
arr = np.arange(10)
print(arr)

sum1 = np.einsum('i->', arr)
print(sum1)

arr2 = np.arange(20).reshape(4, 5)
print(arr2)

sum_col = np.einsum('ij->j', arr2)
print(sum_col)

sum_row = np.einsum("ab->a", arr2)
print(sum_row)

result = np.einsum('i...->...', arr2)
print(result)

A = np.array([[1,1,1],
              [2,2,2],
              [5,5,5]])
B = np.array([[0,1,0],
              [1,1,0],
              [1,1,1]])

#等价于result = np.dot(A, B)
result = A @ B
print(result)

result2 = np.einsum('ij,jk->ik', A, B)
print(result2)









