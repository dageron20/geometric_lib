import math


def area(r):
    '''
    Рассчитывает площадь круга.

            Пример вызова:
                    area(2)  # Возвращает площадь круга с радиусом 2.

            Параметры:
                    r (float): радиус круга.

            Возвращаемое значение:
                    math.pi * r * r (float): Площадь круга.
    '''
    if (type(r) != int and type(r) != float):
        return "Error: can't work with not integer or not float types"
    elif r < 0:
        return "Error: values can't be negative"
    else:
        return math.pi * r * r


def perimeter(r):
    '''
    Рассчитывает периметр круга.

            Пример вызова:
                    perimeter(2) # Возвращает периметр круга с радиусом 2.

            Параметры:
                    r (float): радиус

            Возвращаемое значение:
                    2 * math.pi * r (float): Периметр круга
    '''
    if (type(r) != int and type(r) != float):
        return "Error: can't work with not integer or not float types"
    elif r < 0:
        return "Error: values can't be negative"
    else:
        return 2 * math.pi * r

