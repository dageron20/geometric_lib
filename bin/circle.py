import math
'''Добавление библиотеки math. В контексте кода добавляет число Пи. (3.1415926...)'''
def area(r):
    if r < 0:
        return "Error: radius cannot be negative"
    return math.pi * r * r
    '''
    Возвращает площадь окружности.
        Параметры: 
            r (int): Радиус окружности.
        
        Возвращаемое значение: 
            (math.pi * r * r): Площадь окружности.
    '''

def perimeter(r):
    if r < 0:
        return "Error: radius cannot be negative"
    return 2 * math.pi * r
    '''
        Возвращает периметр окружности.
            Параметры: 
                r (int): Радиус окружности.

            Возвращаемое значение: 
                (2 * math.pi * r): Периметр окружности.
        '''


