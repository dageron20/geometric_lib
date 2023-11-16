import unittest

def area(a, h): 
        ''' Принимает числа a и h, возвращает площадь треугольника длин a и h. '''
        return a * h / 2

    def perimeter(a, b, c): 
            ''' Принимает число a,b,c, возвращает сумму'''
            return a+b+c

class TriangleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(3, 4) , 6)
    
    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
