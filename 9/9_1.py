import matplotlib.pyplot as plt
import numpy as np


# Plot functions sin(x), cos(x), and exp(-x) in a range [0,10]. Colors are red, green, and blue, respectively.
# Lines are solid, dashed, and dotted, respectively. Add a legend.

x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(-x)

plt.plot(x, y1, color='red', linestyle='solid')
plt.plot(x, y2, color='green', linestyle='dashed')
plt.plot(x, y3, color='blue', linestyle='dotted')
plt.legend(['sin(x)', 'cos(x)', 'exp(-x)'], loc='best')
plt.show()
plt.savefig("plot1.png") 