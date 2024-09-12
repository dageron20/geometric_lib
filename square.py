def area(a):
    '''
    Рассчитывает площадь квадрата.

            Пример вызова:
                    area(2)  # Возвращает площадь квадрата со стороной 2.

            Параметры:
                    a (float): длина стороны квадрата.

            Возвращаемое значение:
                    a * a (float): Площадь квадрата.
    '''
    if (type(a) != int and type(a) != float):
        return "Error: can't work with not integer or not float types"
    elif a < 0:
        return "Error: values can't be negative"
    else:
        return a * a


def perimeter(a):
    '''
    Рассчитывает периметр квадрата.

            Пример вызова:
                    area(2)  # Возвращает периметр квадрата со стороной 2.

            Параметры:
                    a (float): длина стороны квадрата.

            Возвращаемое значение:
                    4 * a (float): Периметр квадрата.
    '''
    if (type(a) != int and type(a) != float):
        return "Error: can't work with not integer or not float types"
    elif a < 0:
        return "Error: values can't be negative"
    else:
        return 4 * a
