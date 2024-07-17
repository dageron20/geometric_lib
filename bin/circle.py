import math


def area(r):
    '''
    Принимает r - длину радиуса окружности (int)
    Возвращает площадь этой окружности (int)
    '''
    if r < 0:
        raise ValueError("radius cannot be negative")
    elif r == 0:
        raise ValueError("Error: radius can`t be 0")
    return round(math.pi * r * r, 3)


def perimeter(r):
    '''
    Принимает длину радиуса окружности
    Возвращает периметр этой окружности
    '''
    if r < 0:
        raise ValueError("radius cannot be negative")
    elif r == 0:
        raise ValueError("Error: radius can`t be 0")
    
    return round(2 * math.pi * r, 3)
