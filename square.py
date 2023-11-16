def area(a):
    if isinstance(a,str):
        return "input can not contain characters"
    if a <= 0:
        return "input must be greater than zero"
    '''
    Возвращает площадь квадрата со сторонами длины а.

        Параметры:
             a (int/float): длина стороны квадрата

        Возвращаемое значение:
            a * a (int/float): площадь квадрата

        Пример вызова функции: 
            area(5)
            Output: 25
    '''
    return a * a


def perimeter(a):
    if isinstance(a,str):
        return "input can not contain characters"
    if a <= 0:
        return "input must be greater than zero"
    '''
    Возвращает периметр квадрата со сторонами длины а.

        Параметры:
             a (int/float): длина стороны квадрата

        Возвращаемое значение:
            4 * a (int/float): периметр квадрата

        Пример вызова функции: 
            perimeter(5)
            Output: 20
    '''
    return 4 * a
