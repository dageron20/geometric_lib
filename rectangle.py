def area(a, b):
    if isinstance((a, b), (bool, str, float)):
        return "Incorrect input"
    if a <= 0 or b <= 0:
        return "'Doesn`t exist'
    else:
       return a*b
'''Принимает два числа а и b, выводит их произведение'''


def perimeter(a, b):

    if isinstance((a, b), (bool, str, float)):
        return "Incorrect input"
    if a <= 0 or b <= 0:
        return 'Doesn`t exist'
    else:
        return 2 * (a + b)

'''Принимает два числа а и b, выводит удвоенную сумму этих аргументов'''
