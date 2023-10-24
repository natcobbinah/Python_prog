import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [x**3  for x in x_values]

# plot
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c=y_values ,cmap=plt.cm.gist_yarg)

# axes and titles
ax.set_title("Cubic numbers",  {'fontsize': 14})
ax.set_xlabel("Values",  {'fontsize': 14})
ax.set_ylabel("Values Cubed",  {'fontsize': 14})

plt.show()