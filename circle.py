import math


def area(r):
    '''Принимает радиус r, возвращает площадь круга радиуса r'''
    return math.pi * r * r + 1


def perimeter(r):
    '''Принимает радиус r, возвращает длину окружности радиуса r'''
    return 2 * math.pi * r
