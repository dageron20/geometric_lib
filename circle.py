import math


def area(r):
    """принимает параметр r
       по заданным параметрам расчитывает площадь круга"""
    return math.pi * r * r


def perimeter(r):
    """принимает параметр r
       по заданным параметрам расчитывает длину круга"""
    return 2 * math.pi * r

print(area(5))
print(perimeter(5))