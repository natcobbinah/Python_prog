from point_demo import Point 

import copy

p1 = Point()
p1.x = 3
p1.y = 5

p2 = copy.copy(p1)

print(p1.x, p1.y)
print(p2.x, p2.y)

print(p1 is p2)
print(p1 == p2)