import math

def distance(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    print('dx is', dx)
    print('dy is', dy)
    
    dsquared = dx**2 + dy**2
    print('dsquared is:', dsquared)

    result = math.sqrt(dsquared)
    return result

print(distance(1,2,4,6))