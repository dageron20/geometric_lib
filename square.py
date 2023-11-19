
def area(a):
    '''
    Функция area принимает на вход параметр a (int/float) - длину стороны квадрата.
    Возвращает площадь этого квадрата (int/float (в зависимости от типа входных данных)).
    '''
    if a >= 0:
        return a * a
    else:
        raise ValueError("Side length of rectangle can't be negative.")


def perimeter(a):
    '''
    Функция perimeter принимает на вход параметр a (int/float) - длину стороны квадрата.
    Возвращает периметр этого квадрата (int/float (в зависимости от типа входных данных)).
    '''
    if a >= 0:
        return 4 * a
    else:
        raise ValueError("Side length of rectangle can't be negative.")
