def area(a, b): 
    # Принимает числа a и b, возвращает их произведение.
    # Если один из параметров меньше либо равен 0, возвращает 'Wrong arguments'
    if(isinstance(a, (int, float)) == False or isinstance(b, (int, float)) == False):
        return "Non-integer arguments"
    if(a <= 0 or b <= 0):
        return "Negative arguments"
    return a * b 

def perimeter(a, b): 
    # Принимает числа a и b, возвращает их сумму, умноженую на 2.
    # Если один из параметров меньше либо равен 0, возвращает 'Wrong arguments'
    if(isinstance(a, (int, float)) == False or isinstance(b, (int, float)) == False):
        return "Non-integer arguments"
    if(a <= 0 or b <= 0):
        return "Negative arguments"
    return (a + b)*2
