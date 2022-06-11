# Solve the 1D wave equation with initial and bondary conditions not used during the classes.
# Send the script and the figure.

import math
import numpy as np
import matplotlib.pyplot as plt

Nx, Nt, L, T, c = 30, 300, 2.0, 3.0, 2.0

t = np.linspace(0, T, num=Nt+1, dtype=float)
x = np.linspace(0, L, num=Nx+1, dtype=float)

dx = x[1] - x[0]
dt = t[1] - t[0]
r = (c*dt/dx)**2

print(f'r = {r}')
assert r < 1

u = np.empty((Nx+1, Nt+1), dtype=float)

# initial condition, t = 0, j = 0
# initial shape of the string
u[:,0] = np.sin((x+1) * np.pi)


assert abs(u[0,0]) < 1e-6 and abs(u[Nx, 0]) < 1e-6

# boundary condition, x = 0 and x = L = 1
u[0,:] = 0.0
u[Nx,:] = 0.0

for j in range(1, Nt):
    u[1:-1,j+1] = -u[1:-1,j-1] + 2*u[1:-1,j] + r*(u[:-2,j] -2*u[1:-1,j] + u[2:,j])


print(u)
plt.title('1D wave equation')
plt.xlabel('time')
plt.ylabel('x')
plt.imshow(u, cmap='hot', interpolation='hamming')

plt.colorbar()
plt.show()
plt.savefig("11_2.png") 
