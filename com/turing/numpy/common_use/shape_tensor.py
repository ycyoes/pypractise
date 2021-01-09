import numpy as np

x = np.random.randn(10, 5)
print(x[:, None, :].shape) # This will add a new dimension

print(np.expand_dims(x, 1).shape)