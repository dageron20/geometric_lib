def area(a):
    if isinstance(a, (bool, str, float)):
        return "Incorrect input"
    if a <= 0:
        return "Doesn't exist"
    else:
       return a*a
'''Принимает число n, возвращает квадрат числа n'''

def perimeter(a):
    if isinstance(a, (bool, str, float)):
        return "Incorrect input"
    if a <= 0:
        return "Doesn't exist"
    else:
        return 4*a
'''Приниимает число n, возвращает произведение четырех на n'''
