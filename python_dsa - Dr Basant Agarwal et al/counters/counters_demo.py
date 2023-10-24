from collections import Counter

c1 = Counter('anysequence')         # initializing with strings
c2 = Counter({'a':1, 'c':1, 'e':3}) # initializing with dictionary
c3 = Counter(a=1, c=1, e=3)         # initializing with tuple

print(c1)
print(c2)
print(c3)