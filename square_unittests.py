import unittest
from square import *

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_str_area(self):
        res = area('2')
        self.assertEqual(res, "Error: can't work with not integer or not float types")

    def test_str_perimeter(self):
        res = perimeter('2')
        self.assertEqual(res, "Error: can't work with not integer or not float types")

    def test_negative_area(self):
        res = area(-7)
        self.assertEqual(res, "Error: values can't be negative")

    def test_negative_perimeter(self):
        res = perimeter(-14)
        self.assertEqual(res, "Error: values can't be negative")

    def test_right_area(self):
        res = area(7)
        self.assertEqual(res, 49)

    def test_right_perimeter(self):
        res = perimeter(2)
        self.assertEqual(res, 8)

if __name__ == '__main__':
    unittest.main()
