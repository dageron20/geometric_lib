import math


def area(r):
    '''
        Принимает радиус круга - r (int), площадь которого необходимо вычислить.
        Возвращает его площадь, вычисленную по формуле math.pi * r * r. 
        math.pi (float) - число пи
    '''
    if r <= 0:
        return None
    return math.pi * r * r


def perimeter(r):
    '''
        Принимает радиус круга - r (int) длину которой необходимо вычислить.
        Возвращает её длину, вычисленную по формуле 2 * math.pi * r.
        math.pi (float) - число пи
    '''
    if r <= 0:
        return None
    return 2 * math.pi * r

