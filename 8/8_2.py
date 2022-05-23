import numpy as np

# (a) Create an arbitrary one dimensional array called v1.

v1 = np.arange(0, 8)
print(v1)

# (b) Create a new array v2 which consists of the odd indices of v1.

v2 = np.array([v1[x] for x in range(len(v1)) if x % 2 != 0])
print(v2)

# (c) Create a new array v3 in backwards ordering from v1.

v3 = np.flip(v1)
print(v3)