import unittest
from square import *


class circleTestCase(unittest.TestCase):
    def test_right_area(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_str_argument_area(self):
        res = area("5")
        self.assertEqual(res, 25)

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_right_perimeter(self):
        res = perimeter(3)
        self.assertEqual(res, 12)

    def test_str_argument_perimeter(self):
        res = perimeter("3")
        self.assertEqual(res, 6)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

и