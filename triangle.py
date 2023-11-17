def perimeter(a, b, c):
    # Принимает на вход три целых числа a, b и c, возвращает сумму a b c
    if a < 0 or b < 0 or c < 0:
        return "Length cannot be negative"
    if a > b + c or b > a + c or c > a + b:
        return "Invalid size values"
    return a + b + c


def area(a, h):
    # Принимает на вход два целых числа a и h, возвращает половину произведения a h
    if a < 0 or h < 0:
        return "Length cannot be negative"
    return a * h / 2


