import unittest
from circle import *

class RectangleTestCase(unittest.TestCase):
    def test_zero_mull_area(self):
        res = area(0)
        self.assertEqual(res, "error")

    def test_area_mull_area(self):
        res = area(7)
        self.assertEqual(res, 153.68)

    def test_str_mull_area(self):
        res = area("a")
        self.assertEqual(res, "error")

    def test_negative_mull_area(self):
        res = area(-10)
        self.assertEqual(res, "error")

    def test_float_mull_area(self):
        res = area(3.5)
        self.assertEqual(res, 38.465)

    def test_zero_mull_perimetr(self):
        res = area(0)
        self.assertEqual(res, "error")

    def test_area_mull_perimetr(self):
        res = area(7)
        self.assertEqual(res, 43.96)

    def test_str_mull_perimetr(self):
        res = area("a")
        self.assertEqual(res, "error")

    def test_negative_mull_perimetr(self):
        res = area(-10)
        self.assertEqual(res, "error")

    def test_float_mull_perimetr(self):
        res = area(3.5)
        self.assertEqual(res, 21.98)
