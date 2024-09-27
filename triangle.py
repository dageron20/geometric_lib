def area(a, h):
    '''
    Функция area принимает числа a,h (сторона и высота треугольника),
    возвращает площадь данного треугольника.
    Пример вызова: area(5,10), area(15.5,5.3).
    '''
    if float(a) > 0 and float(h) > 0:
        return float(a) * float(h) / 2
    else:
        raise ValueError("Error")

def perimeter(a, b, c):
    '''
    Функция perimeter принимает числа a,b,c (стороны треугольника),
    возвращает периметр данного треугольника.
    Пример вызова: perimeter(5,10,3), perimeter(15.5,5.3,3.3).
    '''
    if float(a) > 0 and float(b) > 0 and float(c) > 0:
        return float(a) + float(b) + float(c)
    else:
        raise ValueError("Error")
