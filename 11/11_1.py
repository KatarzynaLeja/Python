# Solve the 1D heat equation with initial and bondary conditions not used during the classes.
# Send the script and the figure.

import math
import numpy as np
import matplotlib.pyplot as plt

D, Nx, Nt, L, T = 1.0, 15, 205, 1.0, 0.2

t = np.linspace(0, T, num=Nt+1, dtype=float)
x = np.linspace(0, L, num=Nx+1, dtype=float)

dx = x[1] - x[0]
dt = t[1] - t[0]
r = D*dt/(dx*dx)

print(f'r = {r}')
assert r < 0.5

u = np.empty((Nx+1, Nt+1), dtype=float)

# initial condition, t = 0
u[:,0] = 5.3 * x * (1-x)

# boundary condition, x = 0 and x = L = 1
u[0,:] = 0.8
u[Nx,:] = 0.9

for j in range(Nt):
    u[1:-1,j+1] = r*u[:-2,j] + (1-2*r) * u[1:-1,j] + r*u[2:,j]


print(u)
plt.title('1D heat equation')
plt.xlabel('time')
plt.ylabel('x')
plt.imshow(u, cmap='hot', interpolation='hamming')

plt.colorbar()
plt.show()
plt.savefig("plot1.png") 
