def area(a, b):
    '''
    параметры:
    a (float, int): первая сторона (число)
    b (float, int): вторая сторона (число)

    возвращаемое значение:
    площадь прямоугольника по формуле через две стороны

    при вводе отрицательных чисел выводит ошибку
    '''
    if isinstance (a, str) or isinstance (b, str):
        return 'Вы ввели строку'
    if a < 0 or b < 0:
        return 'Сторона прямоугольника не может быть отрицательной'
    return a * b

def perimeter(a, b):
    '''
    параметры:
    a (float, int): первая сторона (число)
    b (float, int): вторая стороны (число)

    возвращаемое значение:
    периметр прямоугольника по формуле через две стороны

    при вводе отрицательных чисел выводит ошибку
    '''
    if isinstance (a, str) or isinstance (b, str):
        return 'Вы ввели строку'
    if a < 0 or b < 0:
        return 'Сторона прямоугольника не может быть отрицательной'
    return (a + b) * 2
