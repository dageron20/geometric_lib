import unittest
from rectangle import *

class RectangleTestCase(unittest.TestCase):
    def test_zero_mull_area(self):
        res = area(10, 0)
        self.assertEqual(res, "error")

    def test_square_mull_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_mull_area(self):
        res = area(7, 4)
        self.assertEqual(res, 28)

    def test_str_mull_area(self):
        res = area("a", 4)
        self.assertEqual(res, "error")

    def test_negative_mull_area(self):
        res = area(-10, 4)
        self.assertEqual(res, "error")

    def test_float_mull_area(self):
        res = area(3.5, 10)
        self.assertEqual(res, 35)

    def test_zero_mull_perimetr(self):
        res = area(10, 0)
        self.assertEqual(res, "error")

    def test_square_mull_perimetr(self):
        res = area(10, 10)
        self.assertEqual(res, 40)

    def test_area_mull_perimetr(self):
        res = area(7, 4)
        self.assertEqual(res, 22)

    def test_str_mull_perimetr(self):
        res = area("a", 4)
        self.assertEqual(res, "error")

    def test_negative_mull_perimetr(self):
        res = area(-10, 4)
        self.assertEqual(res, "error")

    def test_float_mull_perimetr(self):
        res = area(3.5, 10)
        self.assertEqual(res, 27)
