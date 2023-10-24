# set uses userset = {a,b,c} but cannot be declard as userset ={} bcos then it bcomes
# a dictionary

# or one can use userset = set()
# and the immuatable version of the set, eg: userset = frozenset()

s1 = set()
s1.add(1)
s1.add(2)
s1.add(3)
s1.add(4)

print(s1)

s1.remove(4)
print(s1)

s1.discard(3)
print(s1)

s1.clear()
print(s1)