from circle import Circle
from rectangle import Rectangle

class ShapeDemo:

    @classmethod
    def main(cls, args):
        width = 2
        height = 3
        radius = 10

        rectangle = Rectangle(width, height)
        print(f"rectangle area {rectangle.area()}")
        print(f"rectangle perimeter {rectangle.perimeter()}")

        circle = Circle(radius)
        print(f"circle area {circle.area()}")
        print(f"circle perimeter {circle.perimeter()}")

if __name__ == '__main__': 
    import sys
    ShapeDemo.main(sys.argv)
