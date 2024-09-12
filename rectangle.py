def area(a, b):
    '''
        Рассчитывает площадь прямоугольника.

                Пример вызова:
                        area(2, 3)  # Возвращает площадь прямоугольника с длиной 2 и шириной 3.

                Параметры:
                        a (float): длина прямоугольника.
                        b (float): ширина прямоугольника.

                Возвращаемое значение:
                        a * b (float): Площадь прямоугольника.
    '''
    if (type(a) != int and type(a) != float) or (type(b) != int and type(b) != float):
        return "Error: can't work with not integer or not float types"
    elif a < 0 or b < 0:
        return "Error: values can't be negative"
    else:
        return a * b

def perimeter(a, b):
    '''
       Рассчитывает площадь прямоугольника.

               Пример вызова:
                       area(2, 3)  # Возвращает периметр прямоугольника с длиной 2 и шириной 3.

               Параметры:
                       a (float): длина прямоугольника.
                       b (float): ширина прямоугольника.

               Возвращаемое значение:
                       2 * (a + b) (float): Площадь периметр.
    '''
    if (type(a) != int and type(a) != float) or (type(b) != int and type(b) != float):
        return "Error: can't work with not integer or not float types"
    elif a < 0 or b < 0:
        return "Error: values can't be negative"
    else:
        return 2 * (a + b)


