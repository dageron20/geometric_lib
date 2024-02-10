import unittest
import rectanlge

class RectanlgeTestCase(unittest.TestCase):
    #area
    def test_area_default(self):
        result = rectanlge.area(3,4)
        self.assertEqual(result, 12)
    def test_area_float(self):
        result = rectanlge.area(2.5,3.5)
        self.assertEqual(result, 8.75)
    def test_area_zero(self):
        result = rectanlge.area(0,0)
        self.assertEqual(result, 0)
    #perimiter
    def test_perimeter_default(self):
        result = rectanlge.perimeter(4,6)
        self.assertEqual(result, 20)
    def test_perimeter_float(self):
        result = rectanlge.perimeter(1.5,2)
        self.assertEqual(result, 7)
    def test_perimeter_zero(self):
        result = rectanlge.perimeter(0,0)
        self.assertEqual(result, 0)