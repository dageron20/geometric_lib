import unittest
import circle

class CircleTestCase(unittest.TestCase):
    #area
    def test_area_default(self):
        result = circle.area(10)
        self.assertEqual(result, 314.1592653589793)
    def test_area_float(self):
        result = circle.area(1.5)
        self.assertEqual(result, 7.0685834705770345)
    def test_area_zero(self):
        result = circle.area(0)
        self.assertEqual(result, 0)
    #perimiter
    def test_perimeter_default(self):
        result = circle.perimeter(24)
        self.assertEqual(result, 150.79644737231007)
    def test_perimeter_float(self):
        result = circle.perimeter(61.3)
        self.assertEqual(result, 385.1592593301086)
    def test_perimeter_zero(self):
        result = circle.perimeter(0)
        self.assertEqual(result, 0)