import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-2, 2, 100)
y = x ** 2
z = 5/x

plt.plot(x, y, z)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Sine Wave")
plt.show()