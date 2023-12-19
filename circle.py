import math


def area(r):
    if r < 0:
        return "Negative number"
    return math.pi * r * r


def perimeter(r):
    if r < 0:
        return "Negative number"
    return 2 * math.pi * r

