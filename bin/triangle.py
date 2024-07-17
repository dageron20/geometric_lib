def area(a, h): 
    '''
    Принимает длину стороны и высоты треугольника 
    Возвращает площадь этого треугольника
    '''
    if a < 0:
        raise ValueError("Error: side of triangle can`t be negative")
    elif h < 0:
        raise ValueError("Error: height of triangle can`t be negative")
    elif a == 0:
        raise ValueError("Error: side of triangle can`t be 0")
    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Принимает длины трёх сторон треугольника
    Возвращает периметр этого треугольника
    '''
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Error: side of triangle can`t be negative")
    elif a == 0 or b == 0 or c == 0:
        raise ValueError("Error: side of triangle can`t be 0")
    elif a >= b + c or b >= a + c or c >= a + b:
        raise ValueError("Error: wrong sides")
    return a + b + c
    