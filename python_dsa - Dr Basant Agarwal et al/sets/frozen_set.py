s1 = {'ab', 3, 4, (5, 6)}
s2 = frozenset({'ab', 7, (7, 6)})

s1.add(s2)
print(s1)

print()
# we can use frozen set as a key to a dictionary since it is immutable
fs1 = frozenset(s1)
user_dict = {fs1: 'fs1', s2: 'fs2'}
print(user_dict)