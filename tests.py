import unittest
from math import pi
from bin import circle
from bin import square
from bin import rectangle
from bin import triangle

class CircleTestCase(unittest.TestCase):
    def test_circle_area_regular(self):
        res = circle.area(2)
        self.assertEqual(res, 12.566)

    def test_circle_area_zero(self):
        self.assertRaises(ValueError, circle.area, 0)

    def test_circle_area_negative(self):
        self.assertRaises(ValueError, circle.area, -2)

    def test_circle_perimeter_regular(self):
        res = circle.perimeter(3)
        self.assertEqual(res, 18.850)

    def test_circle_perimeter_zero(self):
        self.assertRaises(ValueError, circle.perimeter, 0)

    def test_circle_perimeter_negative(self):
        self.assertRaises(ValueError, circle.perimeter, -3)


class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area_regular(self):
        res = rectangle.area(2, 3)
        self.assertEqual(res, 6)

    def test_rectangle_area_zero(self):
        self.assertRaises(ValueError, rectangle.area, 0, 32)

    def test_rectangle_area_negative(self):
        self.assertRaises(ValueError, rectangle.area, -2, 2)

    def test_rectangle_perimeter_regular(self):
        res = rectangle.perimeter(4, 5)
        self.assertEqual(res, 18)

    def test_rectangle_perimeter_zero(self):
        self.assertRaises(ValueError, rectangle.perimeter, 0, 5)

    def test_rectangle_perimeter_negative(self):
        self.assertRaises(ValueError, rectangle.perimeter, -1, 3)

class SquareTestCase(unittest.TestCase):
    def test_square_area_regular(self):
        res = square.area(4)
        self.assertEqual(res, 16)

    def test_square_area_zero(self):
        self.assertRaises(ValueError, square.area, 0)

    def test_square_area_negative(self):
        self.assertRaises(ValueError, square.area, -2)

    def test_square_perimeter_regular(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)

    def test_square_perimeter_zero(self):
        self.assertRaises(ValueError, square.perimeter, 0)

    def test_square_perimeter_negative(self):
        self.assertRaises(ValueError, square.perimeter, -1)

class TriangleTestCase(unittest.TestCase):
    def test_triangle_area_regular(self):
        res = triangle.area(3, 5)
        self.assertEqual(res, 7.5)

    def test_triangle_area_zero(self):
        self.assertRaises(ValueError, triangle.area, 0, 56)

    def test_triangle_area_negative(self):
        self.assertRaises(ValueError, triangle.area, -3, 9)

    def test_triangle_perimeter_regular(self):
        res = triangle.perimeter(6, 5, 8)
        self.assertEqual(res, 19)
    
    def test_triangle_perimeter_sides(self):
        self.assertRaises(ValueError, triangle.perimeter, 1, 4, 15)

    def test_triangle_perimeter_zero(self):
        self.assertRaises(ValueError, triangle.perimeter, 0, 4, 7)

    def test_triangle_perimeter_negative(self):
        self.assertRaises(ValueError, triangle.perimeter, -2, -5, 2)

if __name__ == '__main__':
    unittest.main()