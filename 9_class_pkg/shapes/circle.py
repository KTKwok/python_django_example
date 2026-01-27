import math
from shapes.shape import Shape

class Circle(Shape):
    """Class for representing a circle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (self.radius ** 2) * math.pi

    def perimeter(self):
        return 2 * self.radius * math.pi

if __name__ == '__main__':
    """Test the class is working"""
    c = Circle(5)
    print(c.area())