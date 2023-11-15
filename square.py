def area(a):
    if isinstance(a, (bool, str, float, dict, list, set, tuple)) or isinstance(b, (bool, str, float, dict, list, set, tuple)) or isinstance((bool, str, float, dict, list, set, tuple), a) or isinstance((bool, str, float, dict, list, set, tuple), b) or (a == 0) or (b == 0) or (a < 0) or (b < 0):
        return "Invalid input"
    # На вход поступает число, равное длине стороны квадрата.
    # Функция выводит число, равное длине стороны квадрата во второй степени.
    # Что равно его прощади.

    return a * a


def perimeter(a):
    if isinstance(a, (bool, str, float, dict, list, set, tuple)) or isinstance(b, (bool, str, float, dict, list, set, tuple)) or isinstance((bool, str, float, dict, list, set, tuple), a) or isinstance((bool, str, float, dict, list, set, tuple), b) or (a == 0) or (b == 0) or (a < 0) or (b < 0):
        return "Invalid input"
    # На вход поступает число. равное длине стороны квадрата.
    # Функция выводит число, равное произведения 4 на длину стороны квадрата.
    # Что равно его периметру.

    return 4 * a
