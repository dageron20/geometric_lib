
def area(a):
    '''принимает число a(длина), возвращает площадь квадрата с длиной a'''
    if not isinstance(a, int) and not isinstance(a, float):
        return "error"
    elif a <= 0:
        return "error"
    else:
        return a * a


def perimeter(a):
    '''принимает число a(длина), возвращает периметр квадрата с длиной a'''
    if not isinstance(a, int) and not isinstance(a, float):
        return "error"
    elif a <= 0:
        return "error"
    else:
        return 4 * a
