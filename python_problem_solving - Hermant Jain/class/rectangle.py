from abstract_class_Shape import Shape

import math

class Rectangle(Shape):

    def __init__(self, width = 1, height = 1):
        super().__init__()
        self.width = width
        self.height = height
    
    def setWidth(self, width):
        self.width = width

    def setLength(self, height):
        self.height = height

    def area(self):
        return self.width * self.height # area = width * height
    
    def perimeter(self):
        return 2 * (self.width + self.height) # p = 2(w + h)