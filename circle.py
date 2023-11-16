import math
import unittest

def area(r):
    return math.pi * r * r
def perimeter(r):
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):

    def test_circle_area(self):
        c_area = area(10)
        self.assertAlmostEqual(c_area, 314.2, delta=0.1)   

    
    def test_circle_perimeter(self):
        c_peri = perimeter(10)
        self.assertAlmostEqual(c_peri, 62.8, delta=0.1)   


