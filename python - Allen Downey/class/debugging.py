from point_demo import Point

p = Point()
p.x = 3
p.y = 4
#print(p.z) # attribute error

# if you're not sure what type of object is, you can ask
print(type(p))

# you can also use isinstance to check whether an object is an instance
# of a class
print(isinstance(p,Point))

# if you're not sure, whether an object has a particular attribute, you
# can use hasattr
print(hasattr(p,'x'))
print(hasattr(p,'z'))

# or use the try fxn
try:
     x = p.x
except AttributeError:
     x = 0

print(x)
