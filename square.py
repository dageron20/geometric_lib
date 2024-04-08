
def area(a):
    """ Принимает число a. Возвращает площадь квадрата со стороной a. """
    if not type(a) is int:
        return False
    return a * a


def perimeter(a):
    """ Принимает число a. Возвращает периметр квадрата со стороной a. """
    if not type(a) is int:
        return False
    return 4 * a

