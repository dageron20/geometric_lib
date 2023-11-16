import unittest
def area(a, h): 
    '''
    Takes a - the side of the triangle and h - the height of the triangle, outputs the area of ​​the triangle

    area(2, 3)

    Output:3
    '''

    return a*h/2 

def perimeter(a, b, c): 
    '''
    Takes a, b and c - sides of a triangle, outputs the perimeter of ​​the triangle

    perimeter(3, 4, 5)

    Output:12
    '''

    return a + b + c 
    
class triangleTest(unittest.TestCase):
    '''
    testing functions for calculating the area and perimeter of a triangle
    '''
    def test1(self):
        res = area(2,3)
        self.assertEqual(res, 3)
        
    def test1_1(self):
        res = area(5,6)
        self.assertEqual(res, 15)
        
    def test2(self):
        res = perimeter(3,4,5)
        self.assertEqual(res, 12)
        
    def test2_1(self):
        res = perimeter(6,5,4)
        self.assertEqual(res, 15)