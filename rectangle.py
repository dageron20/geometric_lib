def area(a, b):
    """ 
    Принимает числа a и b. 
    Возвращает площадь прямоугольника с данными сторонами. 
    """
    if not (a.isdigit() and b.isdigit()):
        return false
    return a * b

def perimeter(a, b):
    """ 
    Принимает числа a и b. 
    Возвращает периметр прямоугольника с данными сторонами. 
    """
    if not (a.isdigit() and b.isdigit()):
        return false
    return (a + b) * 2
