def area(a, b):
    if isinstance(a, (bool, str, float, dict, list, set, tuple)) or isinstance(b, (bool, str, float, dict, list, set, tuple)) or isinstance((bool, str, float, dict, list, set, tuple), a) or isinstance((bool, str, float, dict, list, set, tuple), b) or (a == 0) or (b == 0) or (a < 0) or (b < 0):
        return "Invalid input"
    # На вход поступает два числа:
    #             a (int): длина одной стороны
    #             b (int): длина другой стороны
    #     Функция возвращает значение равное произведению длины одной стороны на длину другой.

    return a * b
def perimeter(a, b):
    if isinstance(a, (bool, str, float, dict, list, set, tuple)) or isinstance(b, (bool, str, float, dict, list, set, tuple)) or isinstance((bool, str, float, dict, list, set, tuple), a) or isinstance((bool, str, float, dict, list, set, tuple), b) or (a == 0) or (b == 0) or (a < 0) or (b < 0):
        return "Invalid input"

    # На вход поступает 2 числа:
    #             a (int): длина одной стороны
    #             b (int): длина другой стороны
    #     Функция возвращает значение равное удвоенному произведению длины одной стороны на длину другой.

    return (a + b) * 2
