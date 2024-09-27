import unittest
from triangle import *

class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5,3),7.5)

    def test_area_string(self):
        self.assertEqual(area("5","3"),7.5)

    def test_area_zero(self):
        with self.assertRaises(ValueError):
            res = area(0,5)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            res = area(-5, -10)

    def test_perimeter_right(self):
        self.assertEqual(perimeter(3,2,2), 7)

    def test_perimeter_string(self):
        self.assertEqual(perimeter("15","1","2"), 18)

    def test_perimeter_zero(self):
        with self.assertRaises(ValueError):
            res = res = perimeter(0,5,0)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            res = perimeter(1, -5, 3)
unittest.main()
