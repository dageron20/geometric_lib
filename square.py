def area(a):
    if isinstance(a, (bool, str)):
        return "Invalid input"
    if a <= 0:
        return "Invalid input"
    '''Принимает значение стороны a квадрата, возвращает
       площадь квадрата'''
    return a * a


def perimeter(a):
    if isinstance(a, (bool, str)):
        return "Invalid input"
    if a <= 0:
        return "Invalid input"
    '''Принимает значение стороны a квадрата, возвращает
       периметр квадрата'''
    return 4 * a
