def area(a):
    '''
    Принимает a - длину стороны квадрата (int)
    Возвращает площадь этого квадрата (int)
    '''
    if a < 0:
        raise ValueError("Side of square can`t be negative")
    elif a == 0:
        raise ValueError("Side of square can`t be 0")
    return a * a


def perimeter(a):
    '''
    Принимает a - длину стороны квадрата (int)
    Возвращает периметр этого квадрата (int)
    '''
    if a < 0:
        raise ValueError("Side of square can`t be negative")
    elif a == 0:
        raise ValueError("Side of square can`t be 0")
    return 4 * a
