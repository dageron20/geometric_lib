import circle
import unittest
import math
import rectangle
import square
import triangle

class CircleTest(unittest.TestCase):
    def test_area(self):
        area = circle.area(25)
        self.assertEqual(area, 1963.4954084936207)
    def test_perimeter(self):
        per = circle.perimeter(10)
        self.assertEqual(per, (2 * math.pi * 10))
    def test_negative_number(self):
        area = circle.area(-25)
        self.assertEqual(area, "Negative number")

    def test_negative_number(self):
        per = circle.perimeter(-10)
        self.assertEqual(per, "Negative number")
class RectangleTest(unittest.TestCase):
    def test_area(self):
        area = rectangle.area(10, 5)
        self.assertEqual(area, 50)
    def test_perimeter(self):
        per = rectangle.perimeter(12, 87)
        self.assertEqual(per, 198)
    def test_negative_number(self):
        area = rectangle.area(12, -9)
        self.assertEqual(area, "Negative number")

    def test_negative_number(self):
        per = rectangle.perimeter(-8, 54)
        self.assertEqual(per, "Negative number")
class SquareTest(unittest.TestCase):
    def test_area(self):
        area = square.area(8)
        self.assertEqual(area, 64)
    def test_perimeter(self):
        per = square.perimeter(1)
        self.assertEqual(per, 4)
    def test_negative_number(self):
        area = square.area(-8)
        self.assertEqual(area, "Negative number")

    def test_negative_number(self):
        per = square.perimeter(-123)
        self.assertEqual(per, "Negative number")
class TriangleTest(unittest.TestCase):
    def test_area(self):
        area = triangle.area(12, 3)
        self.assertEqual(area, 18)
    def test_perimeter(self):
        per = triangle.perimeter(8, 9, 10)
        self.assertEqual(per,27)
    def test_negative_number(self):
        area = triangle.area(-12, 5)
        self.assertEqual(area, "Negative number")
    def test_negative_number(self):
        per = triangle.perimeter(-89, 8, 7)
        self.assertEqual(per, "Negative number")

if __name__ == '__main__':
    unittest.main()
