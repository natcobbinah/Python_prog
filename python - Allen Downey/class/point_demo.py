class Point:
    """A demo of illustrating a class"""

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def distance_btwn_points(self):
        return self.x - self.y
    
    def add_points(self,point):
        sum_x = self.x + point.x
        sum_y = self.y + point.y
        return Point(sum_x, sum_y)
    
    def add_points_tuple(self,tuple_point):
        sum_x = tuple_point[0] + self.x 
        sum_y = tuple_point[1] + self.y
        return Point(sum_x,sum_y)
    
    def __add__(self,point):
        if(isinstance(point, Point)):
            return self.add_points(point)
        else:
            return self.add_points_tuple(point)
    
    def __str__(self):
        return '%d, %d' % (self.x, self.y)


blank = Point(4,5)
blank2 = Point(7,9)
t = (7,9)
print(blank)
print(blank.distance_btwn_points())
print(blank + blank2) # + operator overloaded to use correct dispatch args
print(blank + t)