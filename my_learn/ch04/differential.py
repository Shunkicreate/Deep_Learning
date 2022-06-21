import numpy as np
import matplotlib.pyplot as plt


def function_1(x):
    return 0.01 * x * x + 0.1 * x

x = np.arange(0, 20, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y)
plt.show()