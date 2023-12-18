import unittest
from ../bin import circle
from ../bin import rectangle
from ../bin import square
from ../bin import triangle


class CircleTestCase(unittest.TestCase):
    def test_zero_multiply(self):
        area_result = circle.area(0)
        perimeter_result = circle.perimeter(0)
        self.assertEqual(area_result, 0)
        self.assertEqual(perimeter_result, 0)

    def test_integer_multiply(self):
        area_result = circle.area(10)
        perimeter_result = circle.perimeter(5)
        self.assertEqual(area_result, 314.15927)
        self.assertEqual(perimeter_result, 31.41593)

    def test_negative_multiply(self):
        area_result = circle.area(-10)
        perimeter_result = circle.perimeter(-5)
        self.assertEqual(area_result, "Error: radius cannot be negative")
        self.assertEqual(perimeter_result, "Error: radius cannot be negative")

    def test_boolean_type(self):
        area_result = circle.area(True)
        perimeter_result = circle.perimeter(True)
        self.assertEqual(area_result, "Error: function cannot work with not integer or float values")
        self.assertEqual(perimeter_result, "Error: function cannot work with not integer or float values")

    def test_string_type(self):
        area_result = circle.area("10")
        perimeter_result = circle.perimeter("5")
        self.assertEqual(area_result, "Error: function cannot work with not integer or float values")
        self.assertEqual(perimeter_result, "Error: function cannot work with not integer or float values")


class RectangleTestCase(unittest.TestCase):
    def test_zero_multiply(self):
        area_result = rectangle.area(0, 10)
        perimeter_result = rectangle.perimeter(0, 0)
        self.assertEqual(area_result, 0)
        self.assertEqual(perimeter_result, 0)

    def test_integer_multiply(self):
        area_result = rectangle.area(10, 5)
        perimeter_result = rectangle.perimeter(5, 7)
        self.assertEqual(area_result, 50)
        self.assertEqual(perimeter_result, 24)

    def test_negative_multiply(self):
        area_result = rectangle.area(-10, -5)
        perimeter_result = rectangle.perimeter(-5, -7)
        self.assertEqual(area_result, "Error: sides cannot be negative")
        self.assertEqual(perimeter_result, "Error: sides cannot be negative")

    def test_float_number(self):
        area_result = rectangle.area(5.2, 3.6)
        perimeter_result = rectangle.perimeter(5.2, 3.6)
        self.assertEqual(area_result, 18.72)
        self.assertEqual(perimeter_result, 17.6)

    def test_boolean_type(self):
        area_result = rectangle.area(True, False)
        perimeter_result = rectangle.perimeter(True, False)
        self.assertEqual(area_result, "Error: function cannot work with not integer or float values")
        self.assertEqual(perimeter_result, "Error: function cannot work with not integer or float values")

    def test_string_type(self):
        area_result = rectangle.area("1", "2")
        perimeter_result = rectangle.perimeter("2", "3")
        self.assertEqual(area_result, "Error: function cannot work with not integer or float values")
        self.assertEqual(perimeter_result, "Error: function cannot work with not integer or float values")


class SquareTestCase(unittest.TestCase):
    def test_zero_multiply(self):
        area_result = square.area(0)
        perimeter_result = square.perimeter(0)
        self.assertEqual(area_result, 0)
        self.assertEqual(perimeter_result, 0)

    def test_integer_multiply(self):
        area_result = square.area(4)
        perimeter_result = square.perimeter(9)
        self.assertEqual(area_result, 16)
        self.assertEqual(perimeter_result, 36)

    def test_negative_multiply(self):
        area_result = square.area(-4)
        perimeter_result = square.perimeter(-9)
        self.assertEqual(area_result, "Error: side cannot be negative")
        self.assertEqual(perimeter_result, "Error: side cannot be negative")

    def test_float_number(self):
        area_result = square.area(7.7)
        perimeter_result = square.perimeter(7.7)
        self.assertEqual(area_result, 59.29)
        self.assertEqual(perimeter_result, 30.8)

    def test_boolean_type(self):
        area_result = square.area(True)
        perimeter_result = square.perimeter(True)
        self.assertEqual(area_result, "Error: function cannot work with not integer or float values")
        self.assertEqual(perimeter_result, "Error: function cannot work with not integer or float values")

    def test_string_type(self):
        area_result = square.area("123")
        perimeter_result = square.perimeter("123")
        self.assertEqual(area_result, "Error: function cannot work with not integer or float values")
        self.assertEqual(perimeter_result, "Error: function cannot work with not integer or float values")


class TriangleTestCase(unittest.TestCase):
    def test_zero_multiply(self):
        area_result = triangle.area(0, 3)
        self.assertEqual(area_result, 0)

    def test_integer_multiply(self):
        area_result = triangle.area(3, 9)
        perimeter_result = triangle.perimeter(17, 23, 16)
        self.assertEqual(area_result, 13.5)
        self.assertEqual(perimeter_result, 56)

    def test_negative_multiply(self):
        area_result = triangle.area(-3, -9)
        perimeter_result = triangle.perimeter(-17, -23, -16)
        self.assertEqual(area_result, "Error: sides cannot be negative")
        self.assertEqual(perimeter_result, "Error: sides cannot be negative")

    def test_triangle_exist(self):
        perimeter_result = triangle.perimeter(7, 1, 2)
        self.assertEqual(perimeter_result, "Error: triangle doesn't exist")

    def test_float_number(self):
        area_result = triangle.area(2.22, 3.33)
        perimeter_result = triangle.perimeter(2.22, 3.33, 4.44)
        self.assertEqual(area_result, 3.6963)
        self.assertEqual(perimeter_result, 9.99)

    def test_boolean_type(self):
        area_result = triangle.area(True, False)
        perimeter_result = triangle.perimeter(True, False, True)
        self.assertEqual(area_result, "Error: function cannot work with not integer or float values")
        self.assertEqual(perimeter_result, "Error: function cannot work with not integer or float values")

    def test_string_type(self):
        area_result = triangle.area("1", "2")
        perimeter_result = triangle.perimeter("2", "3", "4")
        self.assertEqual(area_result, "Error: function cannot work with not integer or float values")
        self.assertEqual(perimeter_result, "Error: function cannot work with not integer or float values")


if __name__ == '__main__':
    unittest.main()
