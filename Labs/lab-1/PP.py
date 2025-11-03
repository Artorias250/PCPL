import math
import sys

def get_coef():
    list = []
    if (len(sys.argv) == 1):
        print ("Ввод коэффициентов биквадратного уравнения")
        for i in range(3):
            while True:
                try:
                    coef = float(input("Введите " + str(i + 1) + "й коэффициент: "))
                    break
                except ValueError:
                    print("Ошибка ввода. Попробуйте снова.")
            list.append(coef)

    elif (len(sys.argv) == 4):
        for i in range(3):
            try:
                coef = float(sys.argv[i + 1])
            except ValueError:
                print("Ошибка ввода командной строки")
                sys.exit(0)
            list.append(coef)
    elif (len(sys.argv) != 1 and len(sys.argv) != 4):
        print("Ошибка ввода командной строки")
        sys.exit(0)
    return list


def get_roots(list):
    a = list[0]
    b = list[1]
    c = list[2]
    result = []
    D = b**2 - 4*a*c
    if (D == 0):
        root = -b / (2.0*a)
        result.append(root)
    elif (D > 0):
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        result.append(round(root1, 2))
        result.append(round(root2, 2))
    return result


def print_roots(roots):
    len_roots = len(roots)
    if len_roots == 0:
        print("Нет корней")
    elif len_roots == 1:
        print("Один корень: " + str(roots[0]))
    elif len_roots == 2:
        print("Два корня: " + str(roots[0]) + " и " + str(roots[1]))


def main():
    list_coef = get_coef()
    roots = get_roots(list_coef)
    print_roots(roots)

if __name__ == "__main__":
    main()
