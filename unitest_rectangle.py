import unittest

class RectangleTestCase(unittest.TestCase):
    def test1_rectangle_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test2_rectangle_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test3_rectangle_area(self):
        res = area(-1, -1)
        self.assertEqual(res, 'error')

    def test1_rectangle_perimetr(self):
        res = perimetr(1, 1)
        self.assertEqual(res, 4)

    def test2_rectangle_perimetr(self):
        res = perimetr(10, 0)
        self.assertEqual(res, 0)

    def test3_rectangle_perimetr(self):
        res = perimetr(-1, -1)
        self.assertEqual(res, 'error')

def area(a, b):
    if a > 0 and b > 0:
        return a * b
    '''
    На вход поступает два числа:
                a (int): длина одной стороны
                b (int): длина другой стороны
        Функция возвращает значение равное произведению длины одной стороны на длину другой.
    '''
    if a < 0 or b < 0:
        return 'error'

    if a == 0 or b == 0:
        return 0



def perimetr(a, b):
    if a > 0 and b > 0:
        return (a + b) * 2
    '''
    На вход поступает 2 числа:
                a (int): длина одной стороны
                b (int): длина другой стороны
        Функция возвращает значение равное удвоенному произведению длины одной стороны на длину другой.
    '''

    if a < 0 or b < 0:
        return 'error'

    if a == 0 or b == 0:
        return 0