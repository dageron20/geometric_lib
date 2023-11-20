import unittest
import square


class SquareTestCase (unittest.TestCase):
    def test_int_arg_area (self):
        res = square.area(3) 
        self.assertEqual(res, 9)
    
    def test_zero_arg_area (self):
        res = square.area(0)
        self.assertEqual(res, 0.0)
    
    def test_float_arg_area (self):
        res = square.area(5.4)
        self.assertEqual(res, 29.160000000000004)
    
    def test_int_arg_perim (self):
        res = square.perimeter(3)
        self.assertEqual(res, 12)
    
    def test_zero_arg_perim (self):
        res = square.perimeter(0)
        self.assertEqual(res, 0.0)
    
    def test_float_arg_perim (self):
        res = square.perimeter(5.4)
        self.assertEqual(res, 21.6)