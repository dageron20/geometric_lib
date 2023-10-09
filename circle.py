import math


def area(r: float) -> float:
    """
        Принимает параметр r (float : радиус окружности) и возвращает площадь окружности с данным радиусом по формуле:
            `math.pi * r * r` (float)
    """
    return math.pi * r * r


def perimeter(r: float) -> float:
    """
        Принимает параметр r (float : радиус окружности) и возвращает периметр окружности с данным радиусом по формуле:
            `2 * math.pi * r` (float)
    """
    return 2 * math.pi * r

