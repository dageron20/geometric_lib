import math


def area(r):
    '''
    Функция area принимает число r (радиус окружности),
    возвращает площадь данной окружности.
    Пример вызова: area(5), area(15.5).
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Функция perimeter принимает число r (радиус окружности),
    возвращает периметр данной окружности.
    Пример вызова: perimeter(5), perimeter(15.5).
    '''
    return 2 * math.pi * r

