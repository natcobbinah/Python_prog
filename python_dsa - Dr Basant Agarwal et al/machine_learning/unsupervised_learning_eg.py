import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans

original_set = -2 * np.random.rand(100,2)
second_set = 1 + 2 * np.random.rand(50,2)
original_set[50:100, :] = second_set

# Clustering the two groups of data
kmean = KMeans(n_clusters=2)
kmean.fit(original_set)
print(kmean.cluster_centers_)
print(kmean.labels_)

#charting the points of each group
for i in set(kmean.labels_):
    index = kmean.labels_ == i 
    plt.plot(original_set[index,0], original_set[index,1], 'o')

plt.plot(kmean.cluster_centers_[0][0], kmean.cluster_centers_[0][1],
         '*', c='r',ms=10)
plt.plot(kmean.cluster_centers_[1][0], kmean.cluster_centers_[1][1],
         '*', c='r',ms=10)

plt.show()

# with the two clusters that we have obtained, now we can predict where new set of 
# data points will fall in the cluster
sample = np.array([
    [-1.4, -1.4]
])
print(kmean.predict(sample))

another_sample = np.array([
    [2.5,2.5]
])
print(kmean.predict(another_sample))