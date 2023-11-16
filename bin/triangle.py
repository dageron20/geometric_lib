def area(a, h):
    if a < 0 or h < 0:
        return "Error: sides cannot be negative"
    return a * h / 2
    '''
        Возвращает площадь треугольника.
            Параметры: 
                a, h (int): Сторона и высота треугольника.

            Возвращаемое значение: 
                (a * h / 2): Площадь треугольника.
    '''

def perimeter(a, b, c):
    if a < 0 or b < 0 or c < 0:
        return "Error: sides cannot be negative"
    if (a + b > c) and (a + c > b) and (c + b > a):
        return a + b + c
    else:
        return "Error: triangle doesn't exist"

    '''
        Возвращает периметр треугольника.
            Параметры: 
                a, b, c (int): Стороны треугольника.

            Возвращаемое значение: 
                (a + b + c): Периметр треугольника.
    '''
