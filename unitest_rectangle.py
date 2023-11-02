import unittest

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_zero_side(self):
        res = perimetr(10, 0)
        self.assertEqual(res, 0)

    def test_perimetr_low(self):
        res = perimetr(1, 1)
        self.assertEqual(res, 4)

def area(a, b):
    '''
    На вход поступает два числа:
                a (int): длина одной стороны
                b (int): длина другой стороны
        Функция возвращает значение равное произведению длины одной стороны на длину другой.
    '''
    return a * b

def perimetr(a, b):
    '''
    На вход поступает 2 числа:
                a (int): длина одной стороны
                b (int): длина другой стороны
        Функция возвращает значение равное удвоенному произведению длины одной стороны на длину другой.
    '''
    return (a + b) * 2