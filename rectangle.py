def area(a, b):
    # Принимает на вход два целых числа a и b, возвращет произведение a b
    if not (type(a) is int) or not (type(b) is int):
        return "Incorrect input"
    elif b <= 0 or a <= 0:
        return "Incorrect input"
    return a * b


def perimeter(a, b):
    # Принимает на вход два целых числа a и b, возвращает удвоенную сумму a b
    if not (type(a) is int) or not (type(b) is int):
        return "Incorrect input"
    elif b <= 0 or a <= 0:
        return "Incorrect input"
    return 2 * (a + b)
