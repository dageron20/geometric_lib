
def area(a):
    # Принимает на вход число a, возвращает квадрат a
    if not (type(a) is int):
        return "Incorrect input"
    elif a <= 0:
        return "Incorrect input"
    return a * a


def perimeter(a):
    # Принимает на вход число a, возвращает a, умноженное на 4
    if not (type(a) is int):
        return "Incorrect input"
    elif a <= 0:
        return "Incorrect input"
    return 4 * a;