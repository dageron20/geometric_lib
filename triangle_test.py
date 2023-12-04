import unittest
from triangle import *


class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertIsNone(res)

    def test_negative_area(self):
        res = area(8, -5)
        self.assertIsNone(res)

    def test_basic_area(self):
        res = area(15, 15)
        self.assertEqual(res, 112.5)
        res = perimeter(3, 148.4, 8)
        self.assertEqual(res, 159.4)

    def test_negative_on_negative_area(self):
        res = area(-10, -8)
        self.assertIsNone(res)

    def test_zero_perimeter(self):
        res = perimeter(6, 0, 4)
        self.assertIsNone(res)

    def test_negative_perimeter(self):
        res = perimeter(10, -5, 5)
        self.assertIsNone(res)

    def test_basic_perimeter(self):
        res = perimeter(3, 10, 8)
        self.assertEqual(res, 21)
        res = perimeter(3, 10, 8.4)
        self.assertEqual(res, 21.4)
