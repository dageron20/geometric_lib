def area(a, b):
    '''
    Функция area принимает числa a,b (длины сторон прямоугольника),
    возвращает площадь данного прямоугольника.
    Пример вызова: area(5,10.5), area(15.5,3).
    '''
    if float(a) > 0 and float(b) > 0:
        return float(a) * float(b)
    else:
        raise ValueError("Error")

def perimeter(a, b):
    '''
    Функция perimeter принимает числa a,b (длины сторон прямоугольника),
    возвращает периметр данного прямоугольника.
    Пример вызова: perimeter(5,10.5), perimeter(15.5,3).
    '''
    if float(a) > 0 and float(b) > 0:
        return 2 * (float(a) + float(b))
    else:
        raise ValueError("Error")
