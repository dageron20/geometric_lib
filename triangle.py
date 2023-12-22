def area(a,h):
    if isinstance(a, (bool, str)) or isinstance(h, (bool, str)):
        return "Invalid input"
    if a <= 0 or h <= 0:
        return "Invalid input"
    '''Принимает значение стороны a треугольника и
       прилежащей к ней высоте h, возвращает
       площадь треугольника'''
    return a*h/2

def perimeter(a,b,c):
    if isinstance(a, (bool, str)) or isinstance(b, (bool, str)) or isinstance(c, (bool, str)):
        return "Invalid input"
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid input"
    if a + b <= c or b + c <= a or a + c <= b:
        return "Nonexistent figure"
    '''Принимает значения сторон a,b и c треугольника,
       возвращает периметр треугольника'''
    return a+b+c
