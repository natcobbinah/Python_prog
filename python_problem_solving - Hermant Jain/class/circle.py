from abstract_class_Shape import Shape

import math

class Circle(Shape):

    def __init__(self, radius = 1):
        super().__init__()
        self.radius = radius 

    def setRadius(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * math.pow(self.radius, 2)

    def perimeter(self):
        return 2 * math.pi * self.radius