import math


def area(r: float) -> float | None:
    """
        Принимает параметр r (float : радиус окружности) и возвращает площадь окружности с данным радиусом по формуле:
            `math.pi * r * r` (float)
    """

    if r < 0:
        return None

    return math.pi * r * r


def perimeter(r: float) -> float | None:
    """
        Принимает параметр r (float : радиус окружности) и возвращает периметр окружности с данным радиусом по формуле:
            `2 * math.pi * r` (float)
    """

    if r < 0:
        return None

    return 2 * math.pi * r

