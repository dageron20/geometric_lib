def area(a):
    '''
    Функция area принимает число a (длина стороны квадрата),
    возвращает площадь данного квадрата.
    Пример вызова: area(5), area(15.5).
    '''
    if float(a) > 0:
        return float(a) * float(a)
    else:
        raise ValueError("Error")


def perimeter(a):
    '''
    Функция perimeter принимает число a (длина стороны квадрата),
    возвращает периметр данного квадрата.
    Пример вызова: perimeter(5), perimeter(15.5).
    '''
    if float(a) > 0:
        return 4 * float(a)
    else:
        raise ValueError("Error")
