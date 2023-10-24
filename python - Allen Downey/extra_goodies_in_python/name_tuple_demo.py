from collections import namedtuple

Point = namedtuple('Point',['x','y']) # a faster way to prototype a class

print(Point)

p = Point(1,2)
print(p.x,p.y)

#but it can also be treated as a tuple
print(p[0],p[1])

x,y = p
print(x,y)

# to extends the functionalities of the class you could extend it with eg:
class Pointier(Point):
    """define extra methods and attributes"""