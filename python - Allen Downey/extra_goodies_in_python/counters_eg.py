from collections import Counter 
count = Counter('parrot') # behaves like a dictionary, but have  default value of 0
                          # if an un-existing index is accessed without throwing error
print(count)

print(count['d']) # not available, but doesn't throw error, its provides zero
