import unittest
from rectangle import *

class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5,5),25)

    def test_area_string(self):
        self.assertEqual(area("5","5"),25)

    def test_area_zero(self):
        with self.assertRaises(ValueError):
            res=area(0,0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            res = area(-5,50)

    def test_perimeter(self):
        self.assertEqual(perimeter(5,3),16)

    def test_perimeter_string(self):
        self.assertEqual(perimeter("5","3"),16)

    def test_perimeter_zero(self):
        with self.assertRaises(ValueError):
            res=perimeter(0,3)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            res = perimeter(-15, 3)
unittest.main()
