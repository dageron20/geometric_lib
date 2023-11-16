def area(a,b):
    if isinstance(a, (bool, str)) or isinstance(b, (bool, str)):
        return "Invalid input"
    if a <= 0 or b <= 0:
        return "Invalid input"
    '''Принимает значение сторон a и b прямоугольника,
       возвращает площадь прямоугольника'''
    return a*b

def perimeter(a,b):
    if isinstance(a, (bool, str)) or isinstance(b, (bool, str)):
        return "Invalid input"
    if a <= 0 or b <= 0:
        return "Invalid input"
    '''Принимает значение сторон a и b прямоугольника,
       возвращает периметр прямоугольника'''
    return 2*(a+b)
