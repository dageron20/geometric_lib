def area(a, h):
    """ Возвращает площадь треугольника.
                       Параметры:
                            a (int, float) : сторона треугольника
                            h (int, float) : высота треугольника, проведенная к стороне a
                       Возвращаемое значение:
                           (a*h)/2 (int, float) : значение площади треугольника"""
    if ((type(a) not in [float, int]) or type(h) not in [float, int] or
            a <= 0 or h <= 0):
        return 'Не корректные входные данные'
    else:
        return a * h / 2


def perimeter(a, b, c):
    """ Возвращает периметр треугольника.
                           Параметры:
                                a, b, c (int, float) : стороны треугольника
                           Возвращаемое значение:
                               a+b+c (int, float) : значение площади треугольника"""
    if ((type(a) not in [float, int]) or (type(b) not in [float, int]) or (
            type(c) not in [float, int]) or a <= 0 or b <= 0 or c <= 0):
        return 'Не корректные входные данные'
    else:
        return a + b + c
