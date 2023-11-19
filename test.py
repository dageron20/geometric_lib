import unittest
import circle
import rectangle
import square
import triangle
import math


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_positive(self):
        self.assertEqual(circle.area(5), math.pi * 25)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            res = circle.area(-3)

    def test_area_text(self):
        with self.assertRaises(TypeError):
            res = circle.area("text")

    def test_area_none(self):
        with self.assertRaises(TypeError):
            res = circle.area(None)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_positive(self):
        self.assertEqual(circle.perimeter(5), math.pi * 2 * 5)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            res = circle.perimeter(-3)

    def test_perimeter_text(self):
        with self.assertRaises(TypeError):
            res = circle.perimeter("text")

    def test_perimeter_none(self):
        with self.assertRaises(TypeError):
            res = circle.perimeter(None)


class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_area_positive(self):
        self.assertEqual(rectangle.area(5, 5), 25)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            res = rectangle.area(-3, 4)

    def test_area_text(self):
        with self.assertRaises(TypeError):
            res = rectangle.area(10, "text")

    def test_area_none(self):
        with self.assertRaises(TypeError):
            res = rectangle.area(10, None)

    def test_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def test_perimeter_positive(self):
        self.assertEqual(rectangle.perimeter(5, 5), 20)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            res = rectangle.perimeter(-1, 2)

    def test_perimeter_text(self):
        with self.assertRaises(TypeError):
            res = rectangle.perimeter("text", 2)

    def test_perimeter_none(self):
        with self.assertRaises(TypeError):
            res = rectangle.perimeter(None, 2)


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_area_positive(self):
        self.assertEqual(square.area(5), 25)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            res = square.area(-3)

    def test_area_text(self):
        with self.assertRaises(TypeError):
            res = square.area("text")

    def test_area_none(self):
        with self.assertRaises(TypeError):
            res = square.area(None)

    def test_perimeter_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_perimeter_positive(self):
        self.assertEqual(square.area(5), 25)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            res = square.area(-3)

    def test_perimeter_text(self):
        with self.assertRaises(TypeError):
            res = square.area("text")

    def test_perimeter_none(self):
        with self.assertRaises(TypeError):
            res = square.area(None)


class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(triangle.area(0, 2), 0)

    def test_area_positive(self):
        self.assertEqual(triangle.area(5, 4), 10)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            res = triangle.area(-3, 2)

    def test_area_text(self):
        with self.assertRaises(TypeError):
            res = triangle.area("text", 2)

    def test_area_none(self):
        with self.assertRaises(TypeError):
            res = triangle.area(None, 2)

    def test_perimeter_zero(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    def test_perimeter_positive(self):
        self.assertEqual(triangle.perimeter(5, 5, 5), 15)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            res = triangle.perimeter(-3, 2, 1)

    def test_perimeter_text(self):
        with self.assertRaises(TypeError):
            res = triangle.perimeter("text", 2, 1)

    def test_perimeter_none(self):
        with self.assertRaises(TypeError):
            res = triangle.perimeter(None, 2, 1)


if __name__ == '__main__':
    unittest.main()
