def area(a, h):
    if isinstance(a, str) or isinstance(h, str):
        return "input can not contain characters"
    if a <= 0 or h <= 0:
        return "input must be greater than zero"
    '''
    Возвращает площадь треугольника с основанием длины а и высотой длины h.

        Параметры:
             a (int/float): длина основания треугольника
             h (int/float): длина высоты треугольника

        Возвращаемое значение:
            a * h / 2 (int/float): площадь треугольника

        Пример вызова функции:
            area(5,4)
            Output: 10
    '''
    return a * h / 2 

def perimeter(a, b, c):
    if isinstance(a, str) or isinstance(b, str) or isinstance(c, str):
        return "input can not contain characters"
    if a <= 0 or b <= 0 or c <= 0:
        return "input must be greater than zero"
    '''
    Возвращает периметр треугольника со сторонами длины a,b,c.

        Параметры:
             a (int/float): длина стороны треугольника
             b (int/float): длина стороны треугольника
             c (int/float): длина стороны треугольника

        Возвращаемое значение:
            a + b + c (int/float): периметр треугольника
            
        Пример вызова функции:
            perimeter(5,4,3)
            Output: 12
    '''
    return a + b + c 
