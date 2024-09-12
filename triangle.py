def area(a, h):
    '''
    Рассчитывает площадь треугольника.

            Пример вызова:
                    area(2, 3)  # Возвращает площадь треугольника с длинами основания 2 и высоты 3.


            Параметры:
                    a (float): длина основания треугольника.
                    h (float): длина высоты треугольника, опушенной к основанию.

            Возвращаемое значение:
                    a * h / 2 (float): Площадь треугольника.
    '''
    if (type(a) != int and type(a) != float) or (type(h) != int and type(h) != float):
        return "Error: can't work with not integer or not float types"
    elif a < 0 or h < 0:
        return "Error: values can't be negative"
    else:
        return a * h / 2

def perimeter(a, b, c):
    '''
    Рассчитывает периметр треугольника.

            Пример вызова:
                    area(2, 3, 4)  # Возвращает периметр треугольника со сторонами 2, 3, 4.

            Параметры:
                    a (float): длина первой стороны треугольника.
                    b (float): длина второй стороны треугольника.
                    c (float): длина третьей стороны треугольника.

            Возвращаемое значение:
                    a + b + c (float): Периметр треугольника.
    '''
    if (type(a) != int and type(a) != float) or (type(b) != int and type(b) != float) or (type(c) != int and type(c) != float):
        return "Error: can't work with not integer or not float types"
    elif a < 0 or b < 0 or c < 0:
        return "Error: values can't be negative"
    else:
        return a + b + c
