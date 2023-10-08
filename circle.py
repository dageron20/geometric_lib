import math


def area(r):
    '''
    Функция area принимает параметр r (int/float) - длину радиуса этой окружности.
    Возвращает площадь искомой окружности. (float)
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Функция perimeter принимает параметр r (int/float) - длину радиуса этой окружности.
    Возвращает периметр искомой окружности (float)
    '''
    return 2 * math.pi * r
