
def area(a: int) -> int | None:
    """
        Принимает параметр a (int : сторона квадрата) и возвращает площадь квадрата с данной стороной по формуле:
            `a * a` (int)
    """

    if a < 0:
        return None

    return a * a


def perimeter(a: int) -> int | None:
    """
        Принимает параметр a (int : сторона квадрата) и возвращает периметр квадрата с данной стороной по формуле:
            `4 * a` (int)
    """

    if a < 0:
        return None

    return 4 * a
