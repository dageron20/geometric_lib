def area(a, h): 
    '''принимает числа a(длина) и b(высота), возвращает площадь треугольника с длиной a и высотой h'''
    if not isinstance(a, int) and not isinstance(a, float):
        return "error"

    elif not isinstance(h, int) and not isinstance(h, float):
        return "error"

    elif a <= 0 or h <= 0:
        return "error"
        
    else:
        return a * h / 2

def perimeter(a, b, c): 
        '''принимает числа a, b и c(длины сторон треугольника), возвращает периметр треугольника с длинами a, b и c'''
    if not isinstance(a, int) and not isinstance(a, float):
        return "error"

    elif not isinstance(b, int) and not isinstance(b, float):
        return "error"

    elif not isinstance(c, int) and not isinstance(c, float):
        return "error"

    elif a <= 0 or b <= 0 or c <= 0:
        return "error"
        
    else:
        return a + b + c
