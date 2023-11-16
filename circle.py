import math
    

def area(r):
    '''принимает число r(радиус), возвращает площадь круга с радиусом r'''
    if not isinstance(r, int) and not isinstance(r, float):
        return "error"
    elif r <= 0:
        return "error"

    return math.pi * r * r


def perimeter(r):
    '''возвращает значение периметра круга с радиусом r

        параметры:
            r(int): целое десятичное число

        возвращаемое значение:
            perimeter(r): периметр круга с радиусом r
    '''
     if not isinstance(r, int) and not isinstance(r, float):
            return "error"
        elif r <= 0:
            return "error"
    
        return 2 * math.pi * r
