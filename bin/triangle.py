def area(a, h):
    if (type(a) != int and type(a) != float) and (type(h) != int and type(h) != float):
        return "Error: function cannot work with not integer or float values"
    if a < 0 or h < 0:
        return "Error: sides cannot be negative"
    return round(a * h / 2, 5)
    '''
        Возвращает площадь треугольника.
            Параметры: 
                a, h (int): Сторона и высота треугольника.

            Возвращаемое значение: 
                (a * h / 2): Площадь треугольника.
    '''


def perimeter(a, b, c):
    if (type(a) != int and type(a) != float) and (type(b) != int and type(b) != float) and (type(c) != int and type(c) != float):
        return "Error: function cannot work with not integer or float values"
    if a < 0 or b < 0 or c < 0:
        return "Error: sides cannot be negative"
    if (a + b > c) and (a + c > b) and (c + b > a):
        return round(a + b + c, 5)
    else:
        return "Error: triangle doesn't exist"

    '''
        Возвращает периметр треугольника.
            Параметры: 
                a, b, c (int): Стороны треугольника.

            Возвращаемое значение: 
                (a + b + c): Периметр треугольника.
    '''
