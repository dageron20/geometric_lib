import unittest

class RectangleTestCase(unittest.TestCase):
    def test_square_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_perimetr(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

def area(a):
    '''
    На вход поступает число, равное длине стороны квадрата.
    Функция выводит число, равное длине стороны квадрата во второй степени.
    Что равно его прощади.
    '''
    return a * a


def perimeter(a):
    '''
    На вход поступает число. равное длине стороны квадрата.
    Функция выводит число, равное произведения 4 на длину стороны квадрата.
    Что равно его периметру.
    '''
    return 4 * a
