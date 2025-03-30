import numpy as np
import matplotlib.pyplot as plt

Y = np.ones((10,10))
Y1 = np.ones((10,10))
Y_final = np.max(Y, axis=0)
Y1_final = np.max(Y1, axis=0)

plt.plot(Y_final)
plt.plot(Y1_final)

plt.show()