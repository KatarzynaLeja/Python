# Approximate the value of pi using a Monte Carlo method.
# Try different numbers of input points (10, 10^2, 10^3, 10^4, 10^5, 10^6).
# Try to get faster code with Numba (remember that the first run is slower).

import numpy as np
import random
import math
from numba import jit
import time

n = 100000000

x = np.empty(n, dtype=np.float64)
y = np.empty(n, dtype=np.float64)

c = 0

@jit(nopython=True)
def random_pair():
    while True:
        s1 = random.uniform(-1, 1)
        s2 = random.uniform(-1, 1)
        if s1 ** 2 + s2 ** 2 < 1:
            break
    return s1, s2

start = time.time()

for i in range(1, n):
    dx, dy = random_pair()
    r = math.sqrt(dx ** 2 + dy ** 2) * 10
    x[i] = (x[i-1] + dx / r + 1) % 1
    y[i] = (y[i-1] + dy / r + 1) % 1
    if x[i] ** 2 + y[i] ** 2 <= 1.0:
        c += 1

pi = (c/n) * 4

end = time.time()
t = end - start

print(f'Przybliżenie liczby pi wynosi: {pi}. Czas wyniósł: {t}')
