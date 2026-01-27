from shapes.circle import Circle
from shapes.rectangle import Rectangle

def main():
    circle = Circle(5)
    rectangle = Rectangle(5, 5)
    print(circle.area())
    print(rectangle.area())

if __name__ == '__main__':
    main()