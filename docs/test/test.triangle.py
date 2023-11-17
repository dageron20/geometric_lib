import unittest
from triangle import *

class RectangleTestCase(unittest.TestCase):
    def test_zero_mull_area(self):
        res = area(10, 0)
        self.assertEqual(res, "error")

    def test_area_mull_area(self):
        res = area(7, 4)
        self.assertEqual(res, 14)

    def test_str_mull_area(self):
        res = area("a", 4)
        self.assertEqual(res, "error")

    def test_negative_mull_area(self):
        res = area(-10, 4)
        self.assertEqual(res, "error")

    def test_float_mull_area(self):
        res = area(3.5, 10)
        self.assertEqual(res, 17.5)

    def test_area_mull_perimetr(self):
        res = area(7, 4, 9)
        self.assertEqual(res, 20)

    def test_str_mull_perimetr(self):
        res = area("a", 4, 8)
        self.assertEqual(res, "error")

    def test_negative_mull_perimetr(self):
        res = area(-10, 4, 8)
        self.assertEqual(res, "error")

    def test_float_mull_perimetr(self):
        res = area(3.5, 10, 4.5)
        self.assertEqual(res, 18)



