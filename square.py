import unittest

def area(a):
    '''
    Takes a and b - sides of a square, outputs the area of ​​the square

    area(3)

    Output:9
    '''

    return a * a


def perimeter(a):
    '''
    Takes a and b - sides of a square, outputs the perimeter of ​​the square

    perimeter(3)

    Output:12
    '''

    return 4 * a

class SquareTest(unittest.TestCase):
    '''
    testing functions for calculating the area and perimeter of a square
    '''
    def test1(self):
        res = area(2)
        self.assertEqual(res, 4)
        
    def test1_1(self):
        res = area(6)
        self.assertEqual(res, 36)
        
    def test2(self):
        res = perimeter(3)
        self.assertEqual(res, 12)
        
    def test2_1(self):
        res = perimeter(6)
        self.assertEqual(res, 24)