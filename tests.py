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

class CircleTestCase(unittest.TestCase):

    def test_zero_radius(self):
        res_area = circle_area(0)
        self.assertEqual(res_area, 0)
        res_perimeter = circle_perimeter(0)
        self.assertEqual(res_perimeter, 0)

    def test_natural_value_test(self):
        res_area = circle_area(10)
        self.assertEqual(res_area, 314.1592653589793)
        res_perimeter = circle_perimeter(10)
        self.assertEqual(res_perimeter, 62.83185307179586)

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
