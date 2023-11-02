import unittest

def area(a, b):
    ''' Находит площадь прямоугольника по его двум сторонам (a, b) ''' 
    return a * b 

def perimeter(a, b):
    ''' Находит периметр прямоугольника по его двум сторонам (a, b) '''
    return 2*(a + b)


class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area_square(self):
        res = area(1, 1)
        self.assertEqual(res, 1)
    
    def test_perimeter_square(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
    
    def test_perimetr_default(self):
        res = perimeter(100, 50)
        self.assertEqual(res, 300)