from collections import namedtuple

space = namedtuple('volume','x y z')

v1 = space(x=2, y=4, z= 10)
print(v1.x * v1.y * v1.z) # calculate the volume
