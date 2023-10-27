import timeit
import matplotlib.pyplot as plt

def nest(n):
    for i in range(n):
        for j in range(n):
            i + j

def test2(n):
    ls = []
    for n in range(n):
        t = timeit.timeit("nest (" + str(n) + ")", setup="from __main__ import nest", number=1)
        ls.append(t)
    return ls

n = 1000
plt.plot(test2(n))
plt.plot([x*x/10_000_000 for x in range(n)])
plt.show()