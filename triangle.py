def area(a, h): 
    # Принимает числа a и h, вовращает произведние этих чисел, деленное на два.
    # Если один из параметров меньше либо равен 0, возвращает 'Wrong arguments'
    if(isinstance(a, (int, float)) == False or isinstance(h, (int, float)) == False):
        return "Non-integer arguments"
    if(a <= 0 or h <= 0):
        return "Negative arguments"
    
    return a * h / 2 

def perimeter(a, b, c): 
    # Принимает числа a, b и c, вовращает сумму этих чисел.
    # Если один из параметров меньше либо равен 0, возвращает 'Wrong arguments'
    if(isinstance(a, (int, float)) == False or isinstance(b, (int, float)) == False or isinstance(c, (int, float)) == False):
        return "Non-integer arguments"
    if(a <= 0 or b <= 0 or c <= 0):
        return "Negative arguments"
    return a + b + c 