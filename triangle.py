def area(a, h):
    '''
    Функция area принимает на вход два параметра a и h (int/float) - длины стороны и высоты треугольника соответственно.
    Возвращает площадь этого треугольника (float).
    '''
    if all([a >= 0, h >= 0]):
        return a * h / 2
    else:
        raise ValueError("Side and/or height can't be negative.")
def perimeter(a, b, c):
    '''
    Функция perimeter принимает на вход три параметра: a, b и c (int/float) - длины сторон треугольника.
    Возвращает периметр этого треугольника (int/float (в зависимости от типа входных данных)).
    '''
    if all([a >= 0, b >= 0, c >= 0]):
        return a + b + c
    else:
        raise ValueError("Sides can't be negative.")
