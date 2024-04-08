import unittest
import rectangle


class RectangleTestCase (unittest.TestCase):
    def test_int_arg_area (self):
        res = rectangle.area(3, 4) 
        self.assertEqual(res, 12)
    
    def test_zero_arg_area (self):
        res = rectangle.area(0, 0)
        self.assertEqual(res, 0)
    
    def test_float_arg_area (self):
        res = rectangle.area(5.4, 4.8)
        self.assertEqual(res, 25.92)
    
    def test_int_arg_perim (self):
        res = rectangle.perimeter(3, 4)
        self.assertEqual(res, 14)
    
    def test_zero_arg_perim (self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)
    
    def test_float_arg_perim (self):
        res = rectangle.perimeter(5.4, 4.8)
        self.assertEqual(res, 20.4)