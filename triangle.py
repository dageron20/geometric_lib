def area(a, h):
    """ 
    Принимает числа a и h.
    Возвращает площадь треугольника со стороной a и высотой h. 
    Высота, длина которой h должна падать на сторону a!
    """
    if not (type(a) is int and type(h) is int):
        return False
    return a * h / 2

def perimeter(a, b, c):
    """ 
    Принимает числа a, b и c.
    Возвращает периметр треугольника со сторонами a, b, c. 
    """
    if not (type(a) is int and type(b) is int and type(c) is int):
        return False
    return a + b + c
