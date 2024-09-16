
def area(a):
    # Принимает число a, возвращает квадрат этого числа.
    # Если один из параметров меньше либо равен 0, возвращает 'Wrong arguments'
    if(isinstance(a, (int, float)) == False):
        return "Non-integer arguments"
    if(a <= 0):
        return "Negative arguments"
    return a * a


def perimeter(a):
    # Принимает число a, возвращает это число, умноженое на 4.
    # Если один из параметров меньше либо равен 0, возвращает 'Wrong arguments'
    if(isinstance(a, (int, float)) == False):
        return "Non-integer arguments"
    if(a <= 0):
        return "Negative arguments"
    return 4 * a
