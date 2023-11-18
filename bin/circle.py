import math
'''Добавление библиотеки math. В контексте кода добавляет число Пи. (3.1415926...)'''
def area(r):
    if type(r) != int and type(r) != float:
        return "Error: function cannot work with not integer or float values"
    if r < 0:
        return "Error: radius cannot be negative"
    return round(math.pi * r * r, 5)
    '''
    Возвращает площадь окружности.
        Параметры: 
            r (int): Радиус окружности.
        
        Возвращаемое значение: 
            (math.pi * r * r): Площадь окружности.
    '''

def perimeter(r):
    if type(r) != int and type(r) != float:
        return "Error: function cannot work with not integer or float values"
    if r < 0:
        return "Error: radius cannot be negative"
    return round(2 * math.pi * r, 5)
    '''
        Возвращает периметр окружности.
            Параметры: 
                r (int): Радиус окружности.

            Возвращаемое значение: 
                (2 * math.pi * r): Периметр окружности.
        '''


