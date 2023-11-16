import unittest
def area(a, b):
    '''
    Takes a and b - sides of a rectangle, outputs the area of ​​the rectangle

    area(2, 3)

    Output:6
    '''

    return a * b 

def perimeter(a, b): 
    '''
    Takes a and b - sides of a rectangle, outputs the perimeter of ​​the rectangle

    perimeter(2,3)

    Output:10
    '''

    return 2*a + 2*b 
    
class rectangleTest(unittest.TestCase):
    '''
    testing functions for calculating the area and perimeter of a rectangle
    '''
    def test1(self):
        res = area(2,3)
        self.assertEqual(res, 6)
        
    def test1_1(self):
        res = area(5,6)
        self.assertEqual(res, 30)
        
    def test2(self):
        res = perimeter(3,4)
        self.assertEqual(res, 14)
        
    def test2_1(self):
        res = perimeter(6,5)
        self.assertEqual(res, 22)