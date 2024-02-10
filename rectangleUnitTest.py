import unittest
from rectangle import area
from rectangle import perimeter

class RectangleTest(unittest.TestCase):
    #test for area
    def test_for_area_first_integer(self):
        result = area(3, 9)
        self.assertEqual(result, 27)

    def test_for_area_second_integer(self):
        result = area(20, 700)
        self.assertEqual(result, 14000)

    def test_for_area_first_float(self):
        result = area(3.5, 7)
        self.assertEqual(result, 24.5)

    def test_for_area_second_float(self):
        result = area(6.31, 9.87)
        self.assertEqual(result, 62.27969999999999)

    def test_for_area_zero(self):
        result = area(0, 9)
        self.assertEqual(result, 0)

    #test for perimeter
    def test_for_perimeter_first_integer(self):
        result = perimeter(3, 9)
        self.assertEqual(result, 24)

    def test_for_perimeter_second_integer(self):
        result = perimeter(20, 700)
        self.assertEqual(result, 1440)

    def test_for_perimeter_first_float(self):
        result = perimeter(3.5, 7)
        self.assertEqual(result, 21)

    def test_for_perimeter_second_float(self):
        result = perimeter(6.31, 9.87)
        self.assertEqual(result, 32.36)

    def test_for_perimeter_zero(self):
        result = perimeter(0, 0)
        self.assertEqual(result, 0)