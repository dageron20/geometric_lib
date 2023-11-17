def area(ground: float, height: float) -> float:
    if not isinstance(ground, float):
        raise TypeError("Ground must be an float")
    if not isinstance(height, float):
        raise TypeError("Height must be an float")
    # Данная функция предназначенна для подсчета площади треугольника

    # Функция принимает два числа (float):
    #   height  :   значение высоты прилегающей к одной из сторон треугольника
    #   ground  :   значение основания треугольника, иначе сторона, к которой опущена высота

    # Возвращает площадь фигуры, а именно умножение ground на height деленное попалам
    #   * Возвращаемое значение area -> float

    # Пример вызова:
    # 1) height = 1.0, ground = 3.0 (входные данные)
    # 2) 1.0 * 3.0 / 2.0 = 1.5 (полученние возвращаемого значения функции)

    return ground * height / 2

def perimeter(a: float, b: float, c: float) -> float:
    if not isinstance(a, float):
        raise TypeError("First param must be an float")
    if not isinstance(b, float):
        raise TypeError("Second param must be an float")
    if not isinstance(c, float):
        raise TypeError("Third param must be an float")
    # Данная функция предназначенна для подсчета периметра треугольника

    # Функция принимает три числа (float):
    #   a  :   первая сторона треугольника
    #   b  :   вторая сторона треугольника
    #   c  :   третья сторона треугольника

    # Возвращает площадь фигуры, а именно сложение всех трех сторон
    #   * Возвращаемое значение perimeter -> float

    # Пример вызова:
    # 1) a = 2.0, b = 3.0, c = 4.0 (входные данные)
    # 2) 2.0 + 3.0 + 4.0 = 9.0 (полученние возвращаемого значения функции)
    return a + b + c




