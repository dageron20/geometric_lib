import math
import unittest


def area(r):
    '''
    Функция area принимает параметр r (int/float) - длину радиуса этой окружности.
    Возвращает площадь искомой окружности. (float)
    '''
    if r >= 0:
        return math.pi * r * r
    else:
        raise ValueError("Radius can't be negative.")


def perimeter(r):
    '''
    Функция perimeter принимает параметр r (int/float) - длину радиуса этой окружности.
    Возвращает периметр искомой окружности (float)
    '''
    if r >= 0:
        return 2 * math.pi * r
    else:
        raise ValueError("Radius can't be negative.")
