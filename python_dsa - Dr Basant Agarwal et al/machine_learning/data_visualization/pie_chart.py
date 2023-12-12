import matplotlib.pyplot as plt 

data = [500, 200, 250]
labels = ["Agriculture", "Aide", "News"]

plt.pie(data, labels = labels, autopct='%1.1f%%')
plt.show()