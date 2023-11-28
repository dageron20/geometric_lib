import math

def area(r):
    # Принимает число r, возвращает произведение числа pi и квадрата этого числа.
    # Если один из параметров меньше либо равен 0, возвращает 'Wrong arguments'
    if(isinstance(r, (int, float)) == False):
        return "Non-integer arguments"
    if(r <= 0):
        return "Negative arguments"
    return math.pi * r * r


def perimeter(r):
     # Принимает число r, возвращает произведение этого числа, числа pi и 2.
     # Если один из параметров меньше либо равен 0, возвращает 'Wrong arguments'
    if(isinstance(r, (int, float)) == False):
        return "Non-integer arguments"
    if(r <= 0):
        return "Negative arguments"
   
    return 2 * math.pi * r
