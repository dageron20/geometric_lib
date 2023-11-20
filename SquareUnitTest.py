import unittest
import square

class SquareTestCase(unittest.TestCase):
    #area
    def test_area_default(self):
        result = square.area(8)
        self.assertEqual(result, 64)
    def test_area_float(self):
        result = square.area(1.5)
        self.assertEqual(result, 2.25)
    def test_area_string(self):
        result = square.area("2")
        self.assertEqual(result, 4)
    def test_area_zero(self):
        result = square.area(0)
        self.assertEqual(result, 0)
    #perimiter
    def test_perimeter_default(self):
        result = square.perimeter(5)
        self.assertEqual(result, 20)
    def test_perimeter_float(self):
        result = square.perimeter(3.8)
        self.assertEqual(result, 15.2)
    def test_perimeter_string(self):
        result = square.perimeter("11")
        self.assertEqual(result, 44)
    def test_perimeter_zero(self):
        result = square.perimeter(0)
        self.assertEqual(result,0)
         