import unittest
from circle import *

class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5),78.53981633974483)
        
    def test_area_string(self):
        self.assertEqual(area("5"),78.53981633974483)
        
    def test_area_zero(self):
        with self.assertRaises(ValueError):
            res = area(0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            res = area(-10)

    def test_perimeter(self):
        self.assertEqual(perimeter(5),31.41592653589793)
        
    def test_perimeter_string(self):
        self.assertEqual(perimeter("5"),31.41592653589793)
        
    def test_perimeter_zero(self):
        with self.assertRaises(ValueError):
            res = perimeter(0)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            res = perimeter(-10)
unittest.main()
