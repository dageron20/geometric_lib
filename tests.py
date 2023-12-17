import unittest
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter

class RectangleTestCase(unittest.TestCase):

    def test_zero_value(self):
        res_area = rectangle_area(10, 0)
        self.assertEqual(res_area, 0)
        res_perimeter = rectangle_perimeter(0, 0)
        self.assertEqual(res_perimeter, 0)
        
    def test_square_values(self):
        res_area = rectangle_area(10, 10)
        self.assertEqual(res_area, 100)

    def test_different_values(self):
        res_area = rectangle_area(2, 5)
        self.assertEqual(res_area, 10)
        res_perimeter = rectangle_perimeter(2, 5)
        self.assertEqual(res_perimeter, 14)
    
    def test_float_values(self):
        res_area = rectangle_area(2.5, 4.5)
        self.assertEqual(res_area, 11.25)
        res_perimeter = rectangle_perimeter(2.5, 4.5)
        self.assertEqual(res_perimeter, 14)
    
    # def test_negative_value(self):
    #     with self.assertRaises(ValueError):
    #         rectangle_area(-2, 5)
    #         rectangle_perimeter(-2, 5)
    
    # def test_char_inputs(self):
    #     with self.assertRaises(TypeError):
    #         rectangle_area('a', 2)
    #         rectangle_perimeter('a', 2)
    
    # def test_bool_inputs(self):
    #     with self.assertRaises(TypeError):
    #         rectangle_area(True, False)
    #         rectangle_perimeter(True, False)
        
class CircleTestCase(unittest.TestCase):

    def test_zero_radius(self):
        res_area = circle_area(0)
        self.assertEqual(res_area, 0)
        res_perimeter = circle_perimeter(0)
        self.assertEqual(res_perimeter, 0)

    def test_natural_value(self):
        res_area = circle_area(10)
        self.assertEqual(res_area, 314.1592653589793)
        res_perimeter = circle_perimeter(10)
        self.assertEqual(res_perimeter, 62.83185307179586)

    # def test_negative_values(self):
    #     with self.assertRaises(ValueError):
    #         circle_area(-10)
    #         circle_perimeter(-10)
    
    def test_float_values(self):
        res_area = circle_area(2.2)
        self.assertAlmostEqual(res_area, 15.205308443374602)
        res_perimeter = circle_perimeter(3.3)
        self.assertAlmostEqual(res_perimeter, 20.734511513692635)
    
    # def test_char_inputs(self):
    #     with self.assertRaises(TypeError):
    #         circle_area('a')
    #         circle_perimeter('a')

    # def test_bool_inputs(self):
    #     with self.assertRaises(TypeError):
    #         circle_area(True)
    #         circle_perimeter(True)

class SquareTestCase(unittest.TestCase):

    def test_zero_value(self):
        res_area = square_area(0)
        self.assertEqual(res_area, 0)
        res_perimeter = square_perimeter(0)
        self.assertEqual(res_perimeter, 0)

    def test_natural_value(self):
        res_area = square_area(5)
        self.assertEqual(res_area, 25)
        res_perimeter = square_perimeter(5)
        self.assertEqual(res_perimeter, 20)

    # def test_negative_values(self):
    #     with self.assertRaises(ValueError):
    #         square_area(-5)
    #         square_perimeter(-5)
    
    def test_float_values(self):
        res_area = square_area(2.2)
        self.assertEqual(res_area, 4.840000000000001)
        res_perimeter = square_perimeter(3.3)
        self.assertEqual(res_perimeter, 13.2)

    # def test_char_inputs(self):
    #     with self.assertRaises(TypeError):
    #         square_area('a')
    #         square_perimeter('a')
    
    # def test_bool_inputs(self):
    #     with self.assertRaises(TypeError):
    #         square_area(True)
    #         square_perimeter(True)

class TriangleTestCase(unittest.TestCase):
    
    def test_zero_value(self):
        res_area = triangle_area(5, 0)
        self.assertEqual(res_area, 0)
        res_perimeter = triangle_perimeter(0, 0, 0)
        self.assertEqual(res_perimeter, 0)

    def test_different_values(self):
        res_area = triangle_area(5, 2)
        self.assertEqual(res_area, 5.0)
        res_perimeter = triangle_perimeter(5, 2, 3)
        self.assertEqual(res_perimeter, 10)

    # def test_negative_values(self):
    #     with self.assertRaises(ValueError):
    #         triangle_area(-5, 2)
    #         triangle_perimeter(-3, 2, 1)
    
    def test_float_values(self):
        res_area = triangle_area(3.3, 2.2)
        self.assertEqual(res_area, 3.63)
        res_perimeter = triangle_perimeter(1.1, 2.2, 3.3)
        self.assertEqual(res_perimeter, 6.6)
    
    # def test_char_inputs(self):
    #     with self.assertRaises(TypeError):
    #         triangle_area('a', 'b')
    #         triangle_perimeter('a', 'b', 'c')
    
    # def test_bool_inputs(self):
    #     with self.assertRaises(TypeError):
    #         triangle_area(True, False)
    #         triangle_perimeter(True, True, False)
