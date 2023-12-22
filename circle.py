import math

def area(r):
    if isinstance(r, (bool, str)):
        return "Invalid input"
    if r <= 0:
        return "Invalid input"
    '''Принимает число r, возвращает площадь круга с радиусом r'''
    return math.pi * r * r


def perimeter(r):
    if isinstance(r, (bool, str)):
        return "Invalid input"
    if r <= 0:
        return "Invalid input"
    '''Принимает число r, возвращает длину окружности с радиусом r'''
    return 2 * math.pi * r
