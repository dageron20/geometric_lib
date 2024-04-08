import unittest
import triangle

class TriangleTestCase (unittest.TestCase):
    def test_int_arg_area (self):
        res = triangle.area(3, 4) 
        self.assertEqual(res, 6.0)
    
    def test_zero_arg_area (self):
        res = triangle.area(0, 0)
        self.assertEqual(res, 0.0)
    
    def test_float_arg_area (self):
        res = triangle.area(5.4, 4.8)
        self.assertEqual(res, 12.96)
    
    def test_int_arg_perim (self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)
    
    def test_zero_arg_perim (self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)
    
    def test_float_arg_perim (self):
        res = triangle.perimeter(5.4, 4.8, 6.7)
        self.assertEqual(res, 16.9)