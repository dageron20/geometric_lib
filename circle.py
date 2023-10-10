import math


def area(r):
    '''
    Расчитывает площадь круга.

        Параметры: 
            r (float): радиус круга

        Возвращаемое значение:
                    math.pi * r * r (float): площадь круга.
    '''
    return math.pi * r * r


def perimeter(r):
     '''
    Рассчитывает периметр круга.

            Параметры:
                    r (float): радиус

            Возвращаемое значение:
                    2 * math.pi * r (float): периметр круга
    '''
    return 2 * math.pi * r

