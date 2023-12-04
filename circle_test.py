import unittest
from circle import *


class СircleTestCase(unittest.TestCase):
    def test_basic_area(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)
        res = area(10.115)
        self.assertEqual(res, 321.4264760250796)

    def test_basic_area_float(self):
        res = area(10.5)
        self.assertEqual(res, 346.36059005827474)

    def test_negative_area(self):
        res = area(-5)
        self.assertIsNone(res)

    def test_zero_area(self):
        res = area(0)
        self.assertIsNone(res)

    def test_basic_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 31.41592653589793)

    def test_basic_perimeter_float(self):
        res = perimeter(8.5)
        self.assertEqual(res, 53.40707511102649)

    def test_negative_perimeter(self):
        res = area(-7)
        self.assertIsNone(res)

    def test_zero_perimeter(self):
        res = area(0)
        self.assertIsNone(res)
