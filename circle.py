import math


def area(r):
    """ Возвращает площадь окружности.
           Параметр:
               r (int, float) : радиус окружности
           Возвращаемое значение:
               πr² (int, float) : значение площади окружности радиуса r"""
    if ((type(r) not in [float, int]) or r <= 0):
        return 'Не корректные входные данные'
    else:
        return math.pi * r * r


def perimeter(r):
    """ Возвращает периметр окружности.
               Параметр:
                   r (int, float) : радиус окружности
               Возвращаемое значение:
                   2πr (int, float) : значение периметра окружности радиуса r"""
    if ((type(r) not in [float, int]) or r <= 0):
        return 'Не корректные входные данные'
    else:
        return (2 * (math.pi * r))
