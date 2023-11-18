def area(a, b):
    if (type(a) != int and type(a) != float) and (type(b) != int and type(b) != float):
        return "Error: function cannot work with not integer or float values"
    if a < 0 or b < 0:
        return "Error: sides cannot be negative"
    return round(a * b, 5)
    '''
        Возвращает площадь прямоугольника.
            Параметры: 
                a, b (int): Две стороны прямоугольника.

            Возвращаемое значение: 
                (a * b): Площадь прямоугольника.
    '''

def perimeter(a, b):
    if (type(a) != int and type(a) != float) and (type(b) != int and type(b) != float):
        return "Error: function cannot work with not integer or float values"
    if a < 0 or b < 0:
        return "Error: sides cannot be negative"
    return round((a + b) * 2, 5)
    '''
        Возвращает периметр прямоугольника.
            Параметры: 
                a, b (int): Две стороны прямоугольника.

            Возвращаемое значение: 
                ((a + b) * 2): Периметр прямоугольника.
    '''


