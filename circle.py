import math
import unittest

def area(r):
    ''' Находит площадь круга по заданному радиусу r '''
    return math.pi * r * r


def perimeter(r):
    ''' Находит периметр круга по задданому радиусу r '''
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_one(self):
        res = area(1)
        self.assertEqual(res, math.pi)
    
    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_perimetr_one(self):
        res = perimeter(1)
        self.assertEqual(res, 2*math.pi)