def area(a, b):
    '''
        Возвращает площадь прямоугольника, вычисленную по формуле.

        Параметры:
            a (int): первая сторона прямоугольника в виде десятичного целого числа
            b (int): вторая сторона прямоугольника в виде десятичного целого числа
         
        Возвращаемое значение:
            a * b (int) - площадь прямоугольника
    '''
    if a <= 0 or b <= 0:
        return None
    return a * b


def perimeter(a, b):
    '''
        Возвращает периметр прямоугольника, вычисленный по формуле.

        Параметры:
            a (int): первая сторона прямоугольника в виде десятичного целого числа
            b (int): вторая сторона прямоугольника в виде десятичного целого числа

        Возвращаемое значение:
            2 * (a + b) (int) - периметр прямоугольника
    '''
    if a <= 0 or b <= 0:
        return None
    return 2 * (a + b)
