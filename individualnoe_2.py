import sys


if __name__ == '__main__':
    a = float(input('Введите 1-ое вещественное число: '))
    b = float(input('Введите 2-ое вещественное число: '))
    c = float(input('Введите 3-е вещественное число: '))

    flag = False

    if abs(a) >= 4:
        print(f"Модуль {a} >= 4")
        flag = True

    if abs(b) >= 4:
        print(f"Модуль {b} >= 4")
        flag = True

    if abs(c) >= 4:
        print(f"Модуль {c} >= 4")
        flag = True

    if flag == False:
        print(f'Модули чисел {a}, {b}, {c} < 4', file = sys.stderr)
        exit(1)





        