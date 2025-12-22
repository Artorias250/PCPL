from lab_python_oop.FigureColor import FigureColor
from colorama import Fore, Style
from lab_python_oop.GeometricFigure import GeometricFigure


class Rectangle(GeometricFigure):
    name = "прямоугольник"

    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color_parametr = FigureColor(color)

    def AreaCalculation(self):
        return self.height * self.width

    def get_name(self):
        return self.name

    def __repr__(self):
        return '{} {} шириной {} и высотой,  {} площадью {}.'.format(
            Fore.BLUE + self.color_parametr.color + Style.RESET_ALL,
            self.get_name(),
            self.width,
            self.height,
            self.AreaCalculation()
        )
