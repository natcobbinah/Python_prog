from collections import namedtuple

space = namedtuple('volume','x y z')

s1 = [4,5,6]
print(space._make(s1))
#print(space._asdict(s1)) # returns an ordered dictionary
print(space._fields)
#print(space._field_defaults)
