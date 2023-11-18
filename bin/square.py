def area(a):
    if type(a) == int or type(a) == float:
        if a < 0:
            return "Error: side cannot be negative"
        return round(a * a, 5)
    return "Error: function cannot work with not integer or float values"

    '''
        Возвращает площадь квадрата.
            Параметры: 
                a(int): Сторона квадрата.

            Возвращаемое значение: 
                (a * a): Площадь квадрата.
    '''


def perimeter(a):
    if type(a) == int or type(a) == float:
        if a < 0:
            return "Error: side cannot be negative"
        return round(a * 4, 5)
    return "Error: function cannot work with not integer or float values"
    '''
        Возвращает периметр квадрата.
            Параметры: 
                a(int): Сторона квадрата.

            Возвращаемое значение: 
                (4 * a): Периметр квадрата.
    '''

