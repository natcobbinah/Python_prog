list = [1,2,3,4]

for item in map(lambda n: n * 2, list):
    print(item)

print()

for item in filter(lambda n: n < 4, list):
    print(item)