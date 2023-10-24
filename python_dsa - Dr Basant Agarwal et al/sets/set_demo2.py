s1 = {'ab',3,4,(5,6)}
s2 = {'ab', 7, (7,6)}
#s3 = {[2,3], {1:4, 8:8}} set values cannot be mutable *unshahable type err

print(s1 - s2) # same as s1.difference(s2)
print(s1.intersection(s2))
print(s1.union(s2))

print('ab' in s1) # test for membership, True
print('ab' not in s1) # False

print()
# loop through elements in a set
for element in s1: 
    print(element)
