def area(a, h):
    '''
    Принимает сторону (a) и высоту (h) треугольника 

    Возвращает площадь треугольника
    
    Пример: area(10, 5) вернёт 25 т.к. (10 * 5 / 2 = 25) 
    '''  
    if (a>0) and (h>0):
        return a * h / 2 
    else:
        return "wrong parameter(s)" 

def perimeter(a, b, c):
    '''
    Принимает стороны (a), (b), (c) треугольника 

    Возвращает периметр треугольника
    
    Пример: area(10, 5, 10) вернёт 25 т.к. (10 + 5 + 10 = 25) 
    '''
    if (a>0) and (b>0) and (c>0):
        return a + b + c  
    else:
        return "wrong parameter(s)"    
    
