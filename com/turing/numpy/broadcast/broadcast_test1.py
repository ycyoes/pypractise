import numpy as np
a = np.array([1., 2., 3.])
b = np.array([2., 2., 2.])
print(a*b)

c = 2.
print(a * c)

x = np.random.randn(64, 10, 5)
y = np.random.randn(5, 10)
print(x @ y)
print(y @ x)
print((y@x).shape)

print('------einsum----------')
I, J, K, H = 10, 15, 20, 25
x = np.random.randn(I, J, K)
y = np.random.randn(J, K, H)
z = np.einsum('ijk, jkh -> ijh', x, y)
print(z)
