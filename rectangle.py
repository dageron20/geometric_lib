def area(a, b):
    """
    Функция area принимает на вход два параметра a и b (int/float) - длины смежных сторон прямоугольника.
    Возвращает площадь этого прямоугольника (int/float (в зависимости от типа входных данных)).
    """
    if all([a >= 0, b >= 0]):
        return a * b
    else:
        raise ValueError("Side length of rectangle can't be negative.")


def perimeter(a, b):
    """
    Функция perimeter принимает на вход два параметра a и b (int/float) - длины смежных сторон квадрата.
    Возвращает периметр этого прямоугольника (int/float (в зависимости от типа входных данных)).
    """
    if all([a >= 0, b >= 0]):
        return 2 * (a + b)
    else:
        raise ValueError("Side length of rectangle can't be negative.")
