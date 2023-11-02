
def area(a):
    return a * a


def perimeter(a):
    return 4 * a

import unittest

class squareTestCase(unittest.TestCase):
   def test_zero_mul(self):
       res = area(10,10)
       self.assertEqual(res, 100)
       
   def test_square_mul(self):
       res = area(4, 10)
       self.assertEqual(res, 40)
