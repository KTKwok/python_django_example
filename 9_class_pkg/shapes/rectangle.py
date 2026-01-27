from shapes.shape import Shape

class Rectangle(Shape):
    """Class representing a rectangle"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height

if __name__ == '__main__':
    """Test area and perimeter function work correctly"""

    t = Rectangle(100, 100)
    assert(t.area() == 10000)
    assert(t.perimeter() == 400)