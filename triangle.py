def perimeter(a, b, c):
    # Принимает на вход три целых числа a, b и c, возвращает сумму a b c
    if not (type(a) is int) or not (type(b) is int) or not (type(c) is int):
        return "Incorrect input"
    elif b <= 0 or a <= 0 or c <= 0:
        return "Incorrect input"
    if a > b + c or b > a + c or c > a + b:
        return "Invalid size values"
    return a + b + c


def area(a, h):
    # Принимает на вход два целых числа a и h, возвращает половину произведения a h
    if not (type(a) is int) or not (type(h) is int):
        return "Incorrect input"
    elif h <= 0 or a <= 0:
        return "Incorrect input"
    return a * h / 2


