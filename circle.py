import math


def area(r):
    if isinstance(r,str):
        return "input can not contain characters"
    if r < 0:
        return "input must be greater than or equal to zero"
    '''
    Возвращает площадь круга

           Параметр:
                   r (int/float): радиус круга
                   
           Возвращаемое значение:
                   math.pi * r * r (int/float): площадь круга
                   
           Пример вызова функции:
                   area(1.5)
                   Output: 7.068583
    '''
    return math.pi * r * r


def perimeter(r):
    if isinstance(r,str):
        return "input can not contain characters"
    if r < 0:
        return "input must be greater than or equal to zero"

    '''
    Возвращает длину окружности

           Параметр:
                   r (int/float): радиус круга
                   
           Возвращаемое значение:
                   2 * math.pi * r (int/float): длина окружности
                   
           Пример вызова функции:
                   perimeter(1.5)
                   Output: 9.424778
    '''
    return 2 * math.pi * r

