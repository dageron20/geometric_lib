def area(a, h):
    """
      Вычисляет площадь треугольника

      Параметр a - Сторона треугольника
      Параметр h - Высота треугольника к стороне a

      Возвравщает площадь треугольника
    """
    if type(a) == str or type(h) == str:
        return "тип дынных передонных в функцию не подлежит вычеслениям"
    elif a < 0 or h < 0:
        return "нельзя вычеслить для отрицательных входных значний"
    else:
        return a * h / 2

def perimeter(a, b, c):
    """
      Вычисляет периметр треугольника

      Параметр a - сторона 1 треугольника
      Параметр b - сторона 2 треугольника
      Параметр c - сторона 3 треугольника

      Возвравщает периметр треугольника
    """
    if type(a) == str or type(b) == str or type(c) == str:
        return "тип дынных передонных в функцию не подлежит вычеслениям"
    elif a < 0 or b < 0 or c < 0:
        return "нельзя вычеслить для отрицательных входных значний"
    else:
        return a + b + c