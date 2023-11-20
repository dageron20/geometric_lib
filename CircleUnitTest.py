import unittest
import circle

class CircleTestCase (unittest.TestCase):
    def test_int_arg_area (self):
        res = circle.area(3) 
        self.assertEqual(res, 28.274333882308138)
    
    def test_zero_arg_area (self):
        res = circle.area(0)
        self.assertEqual(res, 0)
    
    def test_float_arg_area (self):
        res = circle.area(5.442)
        self.assertEqual(res, 93.03940997578762)
    
    def test_int_arg_perim (self):
        res = circle.perimeter(3)
        self.assertEqual(res, 18.84955592153876)
    
    def test_zero_arg_perim (self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)
    
    def test_float_arg_perim (self):
        res = circle.perimeter(5.442)
        self.assertEqual(res, 34.193094441671306)
    

