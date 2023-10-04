import math


def area(r):
    '''
    Возвращает площадь круга

           Параметр:
                   r (int/float): радиус круга
                   
           Возвращаемое значение:
                   math.pi * r * r (int/float): площадь круга
                   
           Пример вызова функции:
                   area(1.5) = 7.068583
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает длину окружности

           Параметр:
                   r (int/float): радиус круга
                   
           Возвращаемое значение:
                   2 * math.pi * r (int/float): длина окружности
                   
           Пример вызова функции:
                   perimeter(1.5) = 9.424778
    '''
    return 2 * math.pi * r

