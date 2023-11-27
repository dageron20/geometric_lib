def area(a: int, h: int) -> float | None:
    """
        Возвращает площадь треугольника.

        Параметры:
            a (int) : основание треугольника
            h (int) : высота треугольника

        Возвращаемое значение:
            `a * h / 2` (float) : площадь треугольника
    """
    if a < 0 or h < 0:
        return None

    return a * h / 2


def perimeter(a: int, b: int, c: int) -> int | None:
    """
        Возвращает периметр треугольника.

        Параметры:
            a (int) : первая сторона треугольника
            b (int) : вторая сторона треугольника
            c (int) : третья сторона треугольника

        Возвращаемое значение:
           `a + b + c` (int) : периметр треугольника
    """
    result_perimeter = a + b + c

    if result_perimeter < 0:
        return None

    return result_perimeter
