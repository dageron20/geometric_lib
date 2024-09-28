import math


def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r


import unittest

class circleTestCase(unittest.TestCase):
   def test_zero_mul(self):
       res = area(math.pi, 2)
       self.assertEqual(res, 2 math.pi)
       
   def test_square_mul(self):
       res = area(2, math.pi, 2)
       self.assertEqual(res, 4 math.pi)


