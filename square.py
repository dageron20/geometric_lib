def area(a):
    '''
    параметры:
    a (float, int): сторона квадрата (число)
    возвращаемое значение:
    площадь квадрата по формуле через сторону

    при вводе отрицательного числа выдает ошибку
    '''
    if isinstance (a, str):
        return 'Вы ввели строку'
    if a < 0:
        return 'Сторона квадрата не может быть отрицательным числом'
    return a * a


def perimeter(a):
    '''
    параметры:
    a (float, int): сторона квадрата (число)
    возвращаемое значение:
    периметр квадрата по формуле через сторону

    при вводе отрицательного числа выдает ошибку
    '''
    if isinstance (a, str):
        return 'Вы ввели строку'
    if a < 0:
        return 'Сторона квадрата не может быть отрицательным числом'
    return 4 * a
