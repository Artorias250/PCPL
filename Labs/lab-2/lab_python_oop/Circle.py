from lab_python_oop.FigureColor import FigureColor
from colorama import Fore, Style
from lab_python_oop.GeometricFigure import GeometricFigure
import math


class Circle(GeometricFigure):
    name = "круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color_parametr = FigureColor(color)

    def AreaCalculation(self):
        return round(math.pi * pow(self.radius, 2), 2)

    def get_name(self):
        return self.name

    def __repr__(self):
        return "{} {} радиусом {}, площадью - {}".format(
            Fore.RED + self.color_parametr.color + Style.RESET_ALL,
            self.get_name(),
            self.radius,
            self.AreaCalculation())
