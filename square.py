
def area(a):
    '''
    Принимает сторону квадрата a

    Возвращает площадь квадрата
    
    Пример: area(10) вернёт 100 т.к. 10*10=100 
    ''' 
    if (a>0):
        return a * a
    else:
        return "wrong parameter"


def perimeter(a):
    '''
    Принимает сторону квадрата a

    Возвращает периметр квадрата
    
    Пример: area(10) вернёт 40 т.к. 4*10=400 
    ''' 
    if (a>0):
        return 4 * a
    else:
        return "wrong parameter"