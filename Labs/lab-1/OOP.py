from typing import Callable
import sys
import math


class Equation:
    def __init__(self, a=1.0, b=1.0, c=1.0):
        self.a = a
        self.b = b
        self.c = c
        self.roots = []

    def coef_info(self):
        print(self.a, self.b, self.c)

    def roots_info(self):
        len_roots = len(self.roots)
        if len_roots == 0:
            print("Нет корней")
        elif len_roots == 1:
            print("Один корень: " + str(self.roots[0]))
        elif len_roots == 2:
            print("Два корня: " +
                  str(self.roots[0]) + " и " + str(self.roots[1]))

    def get_coef(self):
        if len(sys.argv) == 4:
            try:
                self.a = float(sys.argv[1])
                self.b = float(sys.argv[2])
                self.c = float(sys.argv[3])
            except ValueError:
                print("Ошибка ввода командной строки")
                sys.exit(0)

        elif len(sys.argv) == 1:
            while True:
                try:
                    print("Укажите коэффициенты уравнения")
                    self.a = float(input("Коэффициент A: "))
                    self.b = float(input("Коэффициент B: "))
                    self.c = float(input("Коэффициент C: "))
                    break
                except ValueError:
                    print("Ошибка ввода. Попробуйте еще раз.")

        elif (len(sys.argv) != 1 and len(sys.argv) != 4):
            print("Ошибка ввода командной строки")
            sys.exit(0)

    def get_roots(self):
        D = self.b**2 - 4*self.a*self.c
        if (D == 0):
            root = -self.b / (2.0*self.a)
            self.roots.append(root)
        elif (D > 0):
            sqD = math.sqrt(D)
            root1 = (-self.b + sqD) / (2.0*self.a)
            root2 = (-self.b - sqD) / (2.0*self.a)
            self.roots.append(round(root1, 2))
            self.roots.append(round(root2, 2))


def main():
    eq = Equation()

    eq.get_coef()
    eq.coef_info()
    eq.get_roots()
    eq.roots_info()


if __name__ == "__main__":
    main()


def x(a: Callable[[int, int], int], b: int):
    pass
