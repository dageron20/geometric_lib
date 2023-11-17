def area(a, b):
    # Принимает на вход два целых числа a и b, возвращет произведение a b
    if a <= 0 or b <= 0:
        return "Length cannot be negative"
    return a * b


def perimeter(a, b):
    if a <= 0 or b <= 0:
        # Принимает на вход два целых числа a и b, возвращает удвоенную сумму a b
        return "Length cannot be negative"
    return 2 * (a + b)
