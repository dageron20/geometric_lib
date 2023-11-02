import unittest

def area(a):
    ''' Находит площадь квадрата по его стороне a '''
    return a * a


def perimeter(a):
    ''' Находит периметр квадрата по его стороне a '''
    return 4 * a


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_one(self):
        res = area(1)
        self.assertEqual(res, 1)
    
    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_perimetr_one(self):
        res = perimeter(1)
        self.assertEqual(res, 4)