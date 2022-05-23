import numpy as np

# (a) Create a two dimensional array called m1, shape=(4,5).

m1 = np.zeros((4, 5))
m1[0][3] = 8
m1[1][2] = 5
m1[2][0] = 3
m1[3][1] = 4
print(m1)

# (b) Create a new array m2 from m1, in which the elements of each row are in reverse order.

m2 = np.fliplr(m1)
print(m2)

# (c) Create a new array m3 from m1, in which the elements of each column are in reverse order.
m3 = m1[::-1]
print(m3)

# (d) Cut of the first and last row and the first and last column of m1.
m4 = np.delete(m1, (0, 3), 0)
m4 = np.delete(m4, (0, 4), 1)
print(m4)