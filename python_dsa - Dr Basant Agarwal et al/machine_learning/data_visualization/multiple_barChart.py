import matplotlib.pyplot as plt
import numpy as np

data = [
    [8., 57., 22., 10.],
    [16., 7., 32., 40.]
]

x_values = np.arange(4)
plt.bar(x_values + 0.00, data[0], color='r', width=0.30)
plt.bar(x_values + 0.30, data[1], color='y', width=0.30)

plt.show()
