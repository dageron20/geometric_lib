import unittest

def area(a, h): 
    ''' Находит площадь треугольника по его основанию a и высоте h '''
    return a * h / 2 

def perimeter(a, b, c):
    ''' Находит периметр треугольника по его трем сторонам (a, b, c) ''' 
    return a + b + c


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_area_one(self):
        res = area(1, 1)
        self.assertEqual(res, 0.5)
    
    def test_perimeter_zero(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)
    
    def test_perimetr_one(self):
        res = perimeter(1, 2, 1)
        self.assertEqual(res, 4)