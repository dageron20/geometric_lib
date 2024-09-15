def area(a, b):
    '''
    Принимает стороны прямоугольника:

    a : 1-я сторона
    b : 2-я сторона

    Возвращает площадь прямоугольника
    ''' 
    if (a>0) and (b>0):
        return a * b
    else:
        return "wrong parameter(s)" 

def perimeter(a, b):
    '''
    Принимает стороны прямоугольника:

    a : 1-я сторона
    b : 2-я сторона

    Возвращает периметр прямоугольника
    '''  
    if (a>0) and (b>0):
        return (a + b)*2
    else:
        return "wrong parameter(s)"