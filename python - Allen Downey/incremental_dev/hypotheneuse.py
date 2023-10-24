import math

def find_hypotheneuse(base,height):
    bsquared = base**2
    hsquared = height**2
    print('base squared',bsquared)
    print('height squared', hsquared)

    bsquared_plus_hsquared = bsquared + hsquared
    print('base + height: ',bsquared_plus_hsquared)

    hypotheneuse = math.sqrt(bsquared_plus_hsquared)
    return hypotheneuse

print(find_hypotheneuse(3,4))