import unittest
from square import *

class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5),25)

    def test_area_string(self):
        self.assertEqual(area("5"),25)

    def test_area_zero(self):
        with self.assertRaises(ValueError):
            res=area(0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            res = area(-5)

    def test_perimeter(self):
        self.assertEqual(perimeter(5),20)

    def test_perimeter_string(self):
        self.assertEqual(perimeter("5"),20)

    def test_perimeter_zero(self):
        with self.assertRaises(ValueError):
            res=perimeter(0)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            res = perimeter(-15)
unittest.main()
