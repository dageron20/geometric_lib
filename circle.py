import math


def area(r):
    # Принимает на вход число r, возвращает квадрат r, умноженный на число Пи
    if not (type(r) is int):
        return "Incorrect inputa"
    elif r <= 0:
        return "Incorrect input"
    return (int)(math.pi * r * r)


def perimeter(r):
    # Принимает на вход число r, возвращает удвоенное число r, умноженное на число Пи
    if not (type(r) is int):
        return "Incorrect input"
    elif r <= 0:
        return "Incorrect input"
    return (int)(2 * math.pi * r)
