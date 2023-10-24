from collections import Counter 

count = Counter('parrot')

for val, freq in count.most_common(3):
    print(val,freq)