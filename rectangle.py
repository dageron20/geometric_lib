def area(a, b):
    if isinstance(a,str) or isinstance(b,str):
        return "input can not contain characters"
    if a <= 0 or b <= 0:
        return "input must be greater than zero"
    '''
    Возвращает площадь прямоугольника со сторонами a и b.

        Параметры:
             a (int/float): ширина прямоугольника
             b (int/float): длина прямоугольника 

        Возвращаемое значение:
            a * b (int/float): площадь прямоугольника

        Пример вызова функции: 
            area(5,4)
            Output: 20
    '''
    return a * b 

def perimeter(a, b):
    if isinstance(a,str) or isinstance(b,str):
        return "input can not contain characters"
    if a <= 0 or b <= 0:
        return "input must be greater than zero"
    '''
    Возвращает периметр прямоугольника со сторонами a и b.

        Параметры:
             a (int/float): ширина прямоугольника
             b (int/float): длина прямоугольника 

        Возвращаемое значение:
            2*(a + b) (int/float): периметр прямоугольника

        Пример вызова функции: 
            perimeter(5,4)
            Output: 18
    '''
    return 2*(a + b)
