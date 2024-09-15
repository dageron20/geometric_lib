import math


def area(r):
    '''
    Возвращает площадь круга с радиусом = r
        Параметры: r (int): заданный радиус
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает длинну окружности с радиусом = r
        Параметры: r (int): заданный радиус
    '''
    return 2 * math.pi * r

