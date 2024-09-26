import unittest
from rectangle import *


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertIsNone(res)

    def test_negative_area(self):
        res = area(8, -5)
        self.assertIsNone(res)

    def test_basic_area(self):
        res = area(15, 15)
        self.assertEqual(res, 225)
        res = area(15, 15.115)
        self.assertEqual(res, 226.725)

    def test_negative_on_negative_area(self):
        res = area(-10, -8)
        self.assertIsNone(res)

    def test_zero_perimeter(self):
        res = perimeter(6, 0)
        self.assertIsNone(res)

    def test_negative_perimeter(self):
        res = perimeter(10, -5)
        self.assertIsNone(res)

    def test_basic_perimeter(self):
        res = perimeter(3, 10)
        self.assertEqual(res, 26)
        res = perimeter(3, 10.148)
        self.assertEqual(res, 26.296)
