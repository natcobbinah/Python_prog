from collections import defaultdict

dd = defaultdict(int)

words = str.split('red blue green red yellow blue red green green red')

for word in words:
    dd[word] += 1

print(dd)