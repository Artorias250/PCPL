from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square


def main():
    rectangle = Rectangle(4, 4, "синий")
    print(rectangle)
    square = Square(4, "зеленый")
    print(square)
    circle = Circle(4, "красный")
    print(circle)


if __name__ == "__main__":
    main()
