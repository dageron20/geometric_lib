import unittest
from triangle import *


class TriangleTest(unittest.TestCase):
    def test_area_1(self):
        self.assertEqual(area(3, 4), 6)
    def test_area_2(self):
        self.assertEqual(area(0, 3), 'Doesn`t exist')
    def test_area_3(self):
        self.assertEqual(area(-3, 4), 'Doesn`t exist')
    def test_area_4(self):
        self.assertEqual(area(True, 3), "Incorrect input")
    def test_area_5(self):
        self.assertEqual(area('ms', 4), "Incorrect input")

    def test_perimeter_1(self):
        self.assertEqual(perimeter(4, 4, 4), 12)
    def test_perimeter_2(self):
        self.assertEqual(perimeter(0, 4, 4), 'Doesn`t exist')
    def test_perimeter_3(self):
        self.assertEqual(perimeter(-3, 4, 4), 'Doesn`t exist')
    def test_perimeter_4(self):
        self.assertEqual(perimeter(True, 4, 4), "Incorrect input")
    def test_perimeter_5(self):
        self.assertEqual(perimeter("mw", 9, 7), "Incorrect input")


if __name__ == '__main__':
    unittest.main()
