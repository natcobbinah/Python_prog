from collections import Counter

ct = Counter(a=7, b=3, c=8)
print(ct)

# using other counter methods
print(ct.most_common(1))

ct.subtract({'a':2}) # printing counter now,shld have a = 5
print(ct)