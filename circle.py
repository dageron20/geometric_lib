import unittest
import math

class MyTestCase(unittest.TestCase):
   
    def test_zero_area(self):
       res = area(0)
       self.assertEqual(res, "Figure isn't circle")
    
    def test_zero_perimeter(self):
       res = perimeter(0)
       self.assertEqual(res, "Figure isn't circle")
    
    def test_area(self):
       res = area(5)
       self.assertEqual(res, 78.53981633974483)
    
    def test_perimeter_str(self):
       res = area("abcd")
       self.assertEqual(res, "Invalid input")

    def test_area_str(self):
       res = area("qwerty")
       self.assertEqual(res, "Invalid input")

    def test_perimeter(self):
       res = perimeter(10)
       self.assertEqual(res, 62.83185307179586)
    
    def test_perimeter_bool(self):
       res = perimeter(True)
       self.assertEqual(res, "Invalid input")
    
    def test_area_bool(self):
       res = area(False)
       self.assertEqual(res, "Invalid input")

    def test_area_minus(self):
       res = area(-51)
       self.assertEqual(res, "Invalid input")
    
    def test_perimeter_minus(self):
       res = perimeter(-28)
       self.assertEqual(res, "Invalid input")

def area(r):
    '''
    Принимает на вход радиус круга r
    возвращает площадь круга Pi*r*r
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает на вход радиус круга r
    возвращает периметр круга 2*Pi*r
    '''
    return 2 * math.pi * r

