def area(a):
    if a < 0:
        return "Error: side cannot be negative"
    return a * a
    '''
        Возвращает площадь квадрата.
            Параметры: 
                a(int): Сторона квадрата.

            Возвращаемое значение: 
                (a * a): Площадь квадрата.
    '''

def perimeter(a):
    if a < 0:
        return "Error: side cannot be negative"
    return 4 * a
    '''
        Возвращает периметр квадрата.
            Параметры: 
                a(int): Сторона квадрата.

            Возвращаемое значение: 
                (4 * a): Периметр квадрата.
    '''
