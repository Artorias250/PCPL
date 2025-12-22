from lab_python_oop.Rectangle import Rectangle
from colorama import Fore, Style


class Square(Rectangle):
    name = "квадрат"

    def __init__(self, length, color):
        self.length = length
        super().__init__(self.length, self.length, color)

    def AreaCalculation(self):
        return pow(self.length, 2)

    def get_name(self):
        return self.name

    def __repr__(self):
        return "{} {} длиной {}, площадью {}".format(
            Fore.GREEN + self.color_parametr.color + Style.RESET_ALL,
            self.name,
            self.length,
            self.AreaCalculation())
