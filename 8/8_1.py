import numpy as np
# Create the following NumPy arrays:
# (a) float from 0.0 to 1.0 step 0.1, shape=(11,)

a = np.arange(0, 1.1, 0.1)
print(a)
print(a.shape)

# (b) int zeros (1 byte) with shape=(5,6)

b = np.zeros((5, 6), dtype = int)
print(b)

# (c) complex with shape=(9,), powers of x = complex(0, 1): 1, x, x**2, ..., x**8

c = np.array([0+1j**i for i in range(0,9)], dtype = complex)
print(c)
print(c.shape)

