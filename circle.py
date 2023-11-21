import math

def area(r):
    """ Принимает число r, возвращает площадь круга с радиусом r. """
    if not r.isdigit():
        return False
    return math.pi * r * r

def perimeter(r):
    """ Принимает число r, возвращает периметр круга с радиусом r. """
    if not r.isdigit():
        return False
    return 2 * math.pi * r
