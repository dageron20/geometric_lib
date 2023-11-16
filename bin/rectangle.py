def area(a, b):
    if a < 0 or b < 0:
        return "Error: sides cannot be negative"
    return a * b
    '''
        Возвращает площадь прямоугольника.
            Параметры: 
                a, b (int): Две стороны прямоугольника.

            Возвращаемое значение: 
                (a * b): Площадь прямоугольника.
    '''

def perimeter(a, b):
    if a < 0 or b < 0:
        return "Error: sides cannot be negative"
    return (a + b) * 2
    '''
        Возвращает периметр прямоугольника.
            Параметры: 
                a, b (int): Две стороны прямоугольника.

            Возвращаемое значение: 
                ((a + b) * 2): Периметр прямоугольника.
    '''



