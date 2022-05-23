import matplotlib.pyplot as plt
import numpy as np

# Generate n=100 random points in a unit square [0,1]x[0,1].
# Points are green if the distance from (0,0) is less then 1; they are red otherwise.
# The marker area of a point (x,y) should be proportional to x+y.

X = [np.random.rand() for i in range(100)]
Y = [np.random.rand() for i in range(100)]



dist = (((x - 0)**2 + (y - 0)**2)**0.5 for x, y in zip(X,Y))
colors = ['green' if i < 1 else 'red' for i in dist]
area = [x+y for x, y in zip(X,Y)]

plt.scatter(X, Y, s=area, c=colors)
plt.savefig('9_2.png')
