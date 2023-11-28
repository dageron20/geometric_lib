import unittest
import square
import circle
import triangle
import trapeze

class SquareTestCase(unittest.TestCase):
    def test_square_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)
    def test_square_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)
    def test_square_mul_digit_area(self):
        res = square.area(253)
        self.assertEqual(res, 64009)
    def test_square_mul_digit_perimeter(self):
        res = square.perimeter(253)
        self.assertEqual(res, 1012)
    def test_square_single_digit_area(self):
        res = square.area(1)
        self.assertEqual(res, 1)
    def test_square_single_digit_perimeter(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)
    def test_square_fraction_area(self):
        res = square.area(5.25)
        self.assertEqual(res, 27.5625)
    def test_square_fraction_perimeter(self):
        res = square.perimeter(1.1)
        self.assertEqual(res, 4.4)
    def test_square_negative_digit_area(self):
        res = square.area(-5)
        self.assertEqual(res, 0)
    def test_square_negative_digit_perimeter(self):
        res = square.perimeter(-520)
        self.assertEqual(res, 0)
    def test_square_string_area(self):
        res = square.area('5')
        self.assertEqual(res, 25)
    def test_square_string_perimeter(self):
        res = square.perimeter('250')
        self.assertEqual(res, 1000)

class CircleTestCase(unittest.TestCase):
    def test_circle_zero_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)
    def test_circle_zero_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)
    def test_circle_mul_digit_area(self):
        res = circle.area(23)
        self.assertEqual(res, 1661.9025137490005)
    def test_circle_mul_digit_perimeter(self):
        res = circle.perimeter(23)
        self.assertEqual(res, 144.51326206513048)
    def test_circle_single_digit_area(self):
        res = circle.area(2)
        self.assertEqual(res, 12.566370614359172)
    def test_circle_single_digit_perimeter(self):
        res = circle.perimeter(2)
        self.assertEqual(res, 12.566370614359172)
    def test_circle_fraction_area(self):
        res = circle.area(5.5)
        self.assertEqual(res, 95.03317777109123)
    def test_circle_fraction_perimeter(self):
        res = circle.perimeter(5.5)
        self.assertEqual(res, 34.55751918948772)
    def test_circle_negative_digit_area(self):
        res = circle.area(-5)
        self.assertEqual(res, 0)
    def test_circle_negative_digit_perimeter(self):
        res = circle.perimeter(-20)
        self.assertEqual(res, 0)
    def test_circle_string_area(self):
        res = circle.area('5')
        self.assertEqual(res, 78.53981633974483)
    def test_circle_string_perimeter(self):
        res = circle.perimeter('5')
        self.assertEqual(res, 31.41592653589793)

class TriangleTestCase(unittest.TestCase):
    def test_triangle_zero_area(self):
        res = triangle.area(0, 3)
        self.assertEqual(res, 0)
    def test_triangle_zero_perimeter(self):
        res = triangle.perimeter(5, 0, 6)
        self.assertEqual(res, 0)
    def test_triangle_mul_digit_area(self):
        res = triangle.area(23, 12)
        self.assertEqual(res, 138)
    def test_triangle_mul_digit_perimeter(self):
        res = triangle.perimeter(23, 71, 55)
        self.assertEqual(res, 149)
    def test_triangle_single_digit_area(self):
        res = triangle.area(2, 6)
        self.assertEqual(res, 6)
    def test_triangle_single_digit_perimeter(self):
        res = triangle.perimeter(2, 7, 5)
        self.assertEqual(res, 14)
    def test_triangle_fraction_area(self):
        res = triangle.area(5.25, 6)
        self.assertEqual(res, 15.75)
    def test_triangle_fraction_perimeter(self):
        res = triangle.perimeter(2.4, 7.5, 5)
        self.assertEqual(res, 14.9)
    def test_triangle_negative_digit_area(self):
        res = triangle.area(-5, 3)
        self.assertEqual(res, 0)
    def test_triangle_negative_digit_perimeter(self):
        res = triangle.perimeter(-2, 7, 6)
        self.assertEqual(res, 0)
    def test_triangle_string_area(self):
        res = triangle.area("5", "6")
        self.assertEqual(res, 15)
    def test_triangle_string_perimeter(self):
        res = triangle.perimeter("6", "3", "7")
        self.assertEqual(res, 16)


class TrapezeTestCase(unittest.TestCase):
    def test_trapeze_zero_area(self):
        res = trapeze.area(0, 3, 7)
        self.assertEqual(res, 0)

    def test_trapeze_zero_perimeter(self):
        res = trapeze.perimeter(5, 0, 6, 4)
        self.assertEqual(res, 0)

    def test_trapeze_mul_digit_area(self):
        res = trapeze.area(23, 12, 11)
        self.assertEqual(res, 192.5)

    def test_trapeze_mul_digit_perimeter(self):
        res = trapeze.perimeter(23, 71, 55, 62)
        self.assertEqual(res, 211)

    def test_trapeze_single_digit_area(self):
        res = trapeze.area(2, 6, 3)
        self.assertEqual(res, 12)

    def test_trapeze_single_digit_perimeter(self):
        res = trapeze.perimeter(2, 7, 5, 8)
        self.assertEqual(res, 22)

    def test_trapeze_fraction_area(self):
        res = trapeze.area(5.25, 6, 4.2)
        self.assertEqual(res, 23.625)

    def test_trapeze_fraction_perimeter(self):
        res = trapeze.perimeter(2.4, 7.5, 5, 8.4)
        self.assertEqual(res, 23.3)

    def test_trapeze_negative_digit_area(self):
        res = trapeze.area(-5, 3, 2)
        self.assertEqual(res, 0)

    def test_trapeze_negative_digit_perimeter(self):
        res = trapeze.perimeter(-2, 7, 6, 8)
        self.assertEqual(res, 0)

    def test_trapeze_string_area(self):
        res = trapeze.area("5", "6", "4")
        self.assertEqual(res, 22)

    def test_trapeze_string_perimeter(self):
        res = trapeze.perimeter("2", "7", "5", "8")
        self.assertEqual(res, 22)



