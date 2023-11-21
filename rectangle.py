def area(a, b):
    """
      Вычисляет площадь прямоугольник

      Параметр a - Сторона прямоугольника 1
      Параметр b - Сторона прямоугольника 1

      Возвращает площадь прямоугольника
    """
    if a < 0 or b < 0:
        return "нельзя вычеслить для отрицательных входных значний"
    elif type(a) == str or type(b) == str:
        return "тип дынных передонных в функцию не подлежит вычеслениям"
    else:
        return a * b

def perimeter(a, b):
    """
      Вычисляет периметр прямоугольник

      Параметр a - Сторона прямоугольника 1
      Параметр b - Сторона прямоугольника 1

      Возвращает периметр прямоугольника
    """
    if a < 0 or b < 0:
        return "нельзя вычеслить для отрицательных входных значний"
    elif type(a) == str or type(b) == str:
        return "тип дынных передонных в функцию не подлежит вычеслениям"
    else:
        return (a + b) * 2

