from point_demo import Point

p = Point(3,4)

# if you're not sure which attributes an object has use the vars fxn
print(vars(p))

# or a handy fxn such as this
def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))

print_attributes(p)