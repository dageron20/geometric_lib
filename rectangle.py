def area(side: int, ground: int) -> int:
    if not isinstance(side, int):
        raise TypeError("Side must be an integer")
    if not isinstance(ground, int):
        raise TypeError("Ground must be an integer")
    # Данная функция предназначенна для подсчета площади прямоугольника

    # Функция принимает два числа (int):
    #   side    :   значение боковой стороны прямоугольника
    #   ground  :   значение основания прямоугольника

    # Возвращает площадь фигуры, а именно умножение side на ground
    #   * Возвращаемое значение area -> int

    # Пример вызова:
    # 1. side = 1, ground = 3 (входные данные)
    # 2. 1 * 3 = 3 (умножение и полученние возвращаемого значения функции)
    return side * ground

def perimeter(side: int , ground: int) -> int:
    if not isinstance(side, int):
        raise TypeError("Side must be an integer")
    if not isinstance(ground, int):
        raise TypeError("Ground must be an integer")
    # Данная функция предназначенна для подсчета периметра прямоугольника

    # Функция принимает два числа (int):
    #   side    :   значение боковой стороны прямоугольника
    #   ground  :   значение основания прямоугольника

    # Возвращает периметр фигуры, а именно сложение оснований и боковых сторон
    #   * Возвращаемое значение perimeter -> int

    # Пример вызова:
    # 1. side = 2, ground = 4 (входные данные)
    # 2. 2 + 2 + 4 + 4 = 12 (сложение и полученние возвращаемого значения функции)
    return side + side + ground + ground
