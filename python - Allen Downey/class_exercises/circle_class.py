from point_class import Point

import math

class Circle:
    """
    attributes: center, radius
    """

circle = Circle()
circle.radius = 75
circle.point = Point(150,100)

def distance_btwn_points(point1, point2):
    dx = point1.x - point2.x
    dy = point1.y - point2.y
    d = math.sqrt(dx**2 + dy**2)
    return d

def point_in_circle(circle,point):
    return distance_btwn_points(circle,point)

p = Point(120,80)
result = point_in_circle(circle.point, p)
print(result)
        
    

