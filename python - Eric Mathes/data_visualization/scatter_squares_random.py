import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

# plot
fig, ax = plt.subplots()
#ax.scatter(x_values, y_values, s=10, c='red')
#ax.scatter(x_values, y_values, s=10, c=(0, 0.8, 0))
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Blues)

#set chart title and label axes
ax.set_title("Square numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

# set the range for each axis
ax.axis([0,1100,0,1100000])

plt.show()

# save plot
plt.savefig('squares_plot.png')