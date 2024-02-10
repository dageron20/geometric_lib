import unittest
import triangle

class RectanlgeTestCase(unittest.TestCase):
    #area
    def test_area_default(self):
        result = triangle.area(1,2)
        self.assertEqual(result, 1)
    def test_area_float(self):
        result = triangle.area(1.5,3.5)
        self.assertEqual(result, 2.625)
    def test_area_zero(self):
        result = triangle.area(0, 0)
        self.assertEqual(result, 0)
    #perimiter
    def test_perimeter_default(self):
        result = triangle.perimeter(4, 6, 8)
        self.assertEqual(result, 18)
    def test_perimeter_float(self):
        result = triangle.perimeter(1.5, 2.5, 3.5)
        self.assertEqual(result, 7.5)
    def test_perimeter_zero(self):
        result = triangle.perimeter(0, 0, 0)
        self.assertEqual(result, 0)