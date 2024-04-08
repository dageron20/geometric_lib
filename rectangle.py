def area(a, b):
    """ 
    Принимает числа a и b. 
    Возвращает площадь прямоугольника с данными сторонами. 
    """
    if not (type(a) is int and type(b) is int):
        return False
    return a * b

def perimeter(a, b):
    """ 
    Принимает числа a и b. 
    Возвращает периметр прямоугольника с данными сторонами. 
    """
    if not (type(a) is int and type(b) is int):
        return False
    return (a + b) * 2
