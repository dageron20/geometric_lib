def area(a, b):
    if isinstance(a, (bool, str, float, dict, list, set, tuple)) or isinstance(b, (bool, str, float, dict, list, set, tuple)) or isinstance((bool, str, float, dict, list, set, tuple), a) or isinstance((bool, str, float, dict, list, set, tuple), b) or (a == 0) or (b == 0) or (a < 0) or (b < 0):
        return "Invalid input"

    # Фунция расчитывает площадь треугольника.
    # На вход поступает 2 значения:
    #                 a (int): целое число, равное длине одной стороны треугольника
    #                 b (int): целое число, равное длине другой стороны треугольника
    #         Функция выводит произведение 2 чисел делённое на 2.

    return a * b / 2

def perimeter(a, b, c):
    if (a, (bool, str, float, dict, list, set, tuple)) or isinstance(b, (bool, str, float, dict, list, set, tuple)) or isinstance((bool, str, float, dict, list, set, tuple), a) or isinstance((bool, str, float, dict, list, set, tuple), b) or (a == 0) or (b == 0) or (a < 0) or (b < 0):
        return "Invalid input"

    # Фунция расчитывает периметр треугольника.
    # На вход поступает 2 значения:
    #                 a (int): целое число, равное длине одной стороны треугольника
    #                 b (int): целое число, равное длине другой стороны треугольника
    #                 c (int): целое число, равное длине третьей стороны треугольника
    #         Функция выводит сумму 3 чисел: a + b + c.

    return a + b + c