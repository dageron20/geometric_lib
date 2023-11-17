import math


def area(r):
    # Принимает на вход число r, возвращает квадрат r, умноженный на число Пи
    if r <= 0:
        return "Length cannot be negative"
    return (int)(math.pi * r * r)


def perimeter(r):
    # Принимает на вход число r, возвращает удвоенное число r, умноженное на число Пи
    if r <= 0:
        return "Length cannot be negative"
    return (int)(2 * math.pi * r)
