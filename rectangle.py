def area(a, b): 
    '''принимает числа a(длина) и b(ширина), возвращает площадь прямоугольника с длиной a и шириной b'''
    if not isinstance(a, int) and not isinstance(a, float):
        return "error"

    elif not isinstance(b, int) and not isinstance(b, float):
        return "error"

    elif a <= 0 or b <= 0:
        return "error"
        
    else:
        return a * b

def perimeter(a, b): 
     '''принимает числа a(длина) и b(ширина), возвращает периметр прямоугольника с длиной a и шириной b'''
     if not isinstance(a, int) and not isinstance(a, float):
        a = 0

    elif not isinstance(b, int) and not isinstance(b, float):
        b = 0

    elif a <= 0 or b <= 0:
        return "error"

    else:
        return 2 * (a + b) 
