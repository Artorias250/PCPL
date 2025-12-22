from lab_python_oop.GeometricFigure import GeometricFigure
from lab_python_oop.FigureColor import FigureColor
from lab_python_oop.Square import Square
from lab_python_oop.Circle import Circle
from lab_python_oop.Rectangle import Rectangle
import unittest
import math
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'lab_python_oop'))

class TestRectangle(unittest.TestCase):

    def test_rectangle_creation(self):
        rect = Rectangle(5, 3, "синий")
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.color_parametr.color, "синий")
        self.assertEqual(rect.name, "прямоугольник")

    def test_rectangle_area(self):
        rect = Rectangle(4, 6, "красный")
        expected_area = 4 * 6
        self.assertEqual(rect.AreaCalculation(), expected_area)

class TestCurcle(unittest.TestCase):

    def test_curcle_creation(self):
        circle = Circle(5, "красный")
        self.assertEqual(circle.radius, 5)
        self.assertEqual(circle.color_parametr.color, "красный")
        self.assertEqual(circle.name, "круг")

    def test_curcle_area(self):
        circle = Circle(3, "зеленый")
        expected_area = math.pi * 9
        self.assertAlmostEqual(circle.AreaCalculation(),
                               expected_area, places=2)


class TestSquare(unittest.TestCase):

    def test_square_creation(self):
        square = Square(4, "зеленый")
        self.assertEqual(square.length, 4)
        self.assertEqual(square.color_parametr.color, "зеленый")
        self.assertEqual(square.name, "квадрат")
        self.assertEqual(square.height, 4)
        self.assertEqual(square.width, 4)

    def test_square_area(self):
        square = Square(5, "красный")
        expected_area = 25
        self.assertEqual(square.AreaCalculation(), expected_area)


if __name__ == '__main__':
    unittest.main(verbosity=2)
