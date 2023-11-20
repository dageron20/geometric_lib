import math


def area(r):
    '''Принимает радиус окружности r, возращает площадь круга радиуса r'''
    if (r>0):
        return math.pi * r * r
    else:
        return "wrong parameter"


def perimeter(r):
    '''Принимает радиус окружности r, возращает длину окружности радиуса r'''
    if (r>0):
        return 2 * math.pi * r
    else:
        return "wrong parameter"

