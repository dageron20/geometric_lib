import unittest
from circle import *

class circleTestCase(unittest.TestCase):
    def test_right_area(self):
        res = area(5)
        self.assertEqual(res,78.53981633974483)

    def test_str_argument_area(self):
        res = area("5")
        self.assertEqual(res,78.53981633974483)

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res,0)

    def test_right_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res,31.41592653589793)

    def test_str_argument_perimeter(self):
        res = perimeter("5")
        self.assertEqual(res,31.41592653589793)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res,0)




