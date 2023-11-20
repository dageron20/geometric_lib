import unittest
from rectangle import *

class circleTestCase(unittest.TestCase):
    def test_right_area(self):
        res = area(5,3)
        self.assertEqual(res,15)

    def test_str_argument_area(self):
        res = area("5","3")
        self.assertEqual(res,15)

    def test_zero_area(self):
        res = area(0,0)
        self.assertEqual(res,0)

    def test_right_perimeter(self):
        res = perimeter(5,3)
        self.assertEqual(res,16)

    def test_str_argument_perimeter(self):
        res = perimeter("5","3")
        self.assertEqual(res,16)

    def test_zero_perimeter(self):
        res = perimeter(0,3)
        self.assertEqual(res,3)
