import math
def area(r):
    if isinstance(r, (bool, str, float)):
        return 'Incorrect input'
    if r <= 0:
        return 'Doesn`t exist'
    else:
       return math.pi * r * r


def perimeter(r):

    if isinstance(r, (bool, str, float)):
        return 'Incorrect input'
    if r <= 0:
        return 'Doesn`t exist'
    else:
        return 2 * math.pi * r



