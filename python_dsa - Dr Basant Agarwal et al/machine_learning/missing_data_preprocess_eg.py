import numpy as np
import pandas as pd

data = pd.DataFrame([
    [4., 45., 984.],
    [np.NAN, np.NAN, 5.],
    [94., 23., 55.]
])

#as can be observed data[1][0] and data[1][1] have np.NAN values, representing that they 
#have no value

#If the np.NAN values are not desired in a given dataset, they can be set to a constant figure

# setting np.NAN to 0.1
print(data.fillna(0.1))

print()

# to apply the mean values instead, we do the ff
print(data.fillna(data.mean()))