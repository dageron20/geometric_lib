import unittest
from square import *


class SquareTestCase(unittest.TestCase):
    def test_basic_area(self):
        res = area(10)
        self.assertEqual(res, 100)
        res = area(10.5)
        self.assertEqual(res, 110.25)

    def test_negative_area(self):
        res = area(-5)
        self.assertIsNone(res)

    def test_zero_area(self):
        res = area(0)
        self.assertIsNone(res)

    def test_basic_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 20)
        res = perimeter(8.5)
        self.assertEqual(res, 34.0)

    def test_negative_perimeter(self):
        res = area(-7)
        self.assertIsNone(res)

    def test_zero_perimeter(self):
        res = area(0)
        self.assertIsNone(res)
