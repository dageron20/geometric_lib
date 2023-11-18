def area(a, b): 
    '''
    Принимает a, b (int) - длины сторон прямоугольника
    Возвращает площадь этого прямоугольника
    '''
    if a < 0 or b < 0:
        raise ValueError("Side of rectangle cannot be negative")
    elif a == 0 or b == 0:
        raise ValueError("Side of rectangle can`t be 0")
    return a * b

def perimeter(a, b): 
    '''
    Принимает a, b (int) - длины сторон прямоугольника
    Возвращает периметр этого прямоугольника (int)
    '''
    if a < 0 or b < 0:
        raise ValueError("Side of rectangle cannot be negative")
    elif a == 0 or b == 0:
        raise ValueError("Side of rectangle can`t be 0")
    return 2 * (a + b)
