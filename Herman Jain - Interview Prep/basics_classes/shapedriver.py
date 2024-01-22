from rectangle import Rectangle
from circle import Circle


class ShapeDemo:

    @classmethod
    def main(cls, args):
        width = 2
        length = 3
        radius = 10

        rectangle = Rectangle(width, length)
        print(f"Rectangle width {width}, and length {length}, area {
              rectangle.area()} perimeter {rectangle.perimeter()}")

        circle = Circle(radius)
        print(f"Circle radius {radius}, Area {
              circle.area()} perimeter {circle.perimeter()}")


if __name__ == "__main__":
    import sys
    ShapeDemo.main(sys.argv)
