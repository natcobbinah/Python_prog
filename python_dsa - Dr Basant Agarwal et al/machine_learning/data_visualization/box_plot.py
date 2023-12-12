import numpy as np
import matplotlib.pyplot as plt 

data = np.random.randn(50)

plt.boxplot(data)
plt.show()