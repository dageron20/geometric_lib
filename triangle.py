def area(a, h):
    if isinstance(a, (bool, str, float)) or isinstance(h, (bool, str, float)):
        return "Incorrect input"
    if a <= 0 or h <= 0:
        return 'Doesn`t exist'
    else:
        return a * h / 2
'''Принимает два значения, выводит половину их  произведения'''
def perimeter(a, b, c):
    if isinstance(a, (bool, str, float)) or isinstance(b, (bool, str, float)) or isinstance(c, (bool, str, float)):
        return "Incorrect input"
    if a <= 0 or b <= 0 or c <= 0:
        return 'Doesn`t exist'
    else:
        return a + b + c
'''Принимает три значения, выводит их сумму'''
