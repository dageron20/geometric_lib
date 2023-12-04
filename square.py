def area(a):
    '''
        Возвращает площадь квадрата, вычисленную по формуле:
        a * a, где a (int) - cторона квадрата
    '''
    if a <= 0:
        return None
    return a * a


def perimeter(a):
    '''
        Возвращает периметр квадрата, вычисленный по формуле:
        4 * a, где a (int) - cторона квадрата
    '''
    if a <= 0:
        return None
    return 4 * a
