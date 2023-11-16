import math
import unittest
def area(r):

    '''
    Takes r - the radius of a circle, outputs the area of ​​the circle

    area (5)

    Output:78.5
    '''

    return math.pi * r * r

def perimeter(r):

    '''
    Takes r - the radius of the circle, outputs the perimeter of the circle

    area (5)

    Output:31.4
    '''

    return 2 * math.pi * r

class CircleTest(unittest.TestCase):
    '''
    testing functions for calculating the area and perimeter of a circle
    '''
    def test1(self):
        res = area(2)
        self.assertEqual(res, 4*math.pi)
        
    def test1_1(self):
        res = area(5)
        self.assertEqual(res, 25*math.pi)
        
    def test2(self):
        res = perimeter(3)
        self.assertEqual(res, 6*math.pi)
        
    def test2_1(self):
        res = perimeter(6)
        self.assertEqual(res, 12*math.pi)