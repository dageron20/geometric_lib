import unittest
from src import rectangle_area, rectangle_perimeter
from src import square_area, square_perimeter
from src import triangle_area, triangle_perimeter
from src import circle_area, circle_perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(rectangle_area(174, 452), 78648)
        self.assertIsNone(rectangle_area(-174, -452))

    def test_perimeter(self):
        self.assertEqual(rectangle_perimeter(43, 27), 140)
        self.assertIsNone(rectangle_perimeter(-510, 21))

    def test_area_zero(self):
        self.assertEqual(rectangle_area(123, 0), 0)
        self.assertEqual(rectangle_area(0, 0), 0)

    def test_perimeter_zero(self):
        self.assertEqual(rectangle_perimeter(-124, 124), 0)
        self.assertEqual(rectangle_perimeter(0, 0), 0)


class SquareTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(square_area(241), 58081)
        self.assertIsNone(square_area(-32))

    def test_perimeter(self):
        self.assertEqual(square_perimeter(452), 1808)
        self.assertIsNone(square_perimeter(-510))

    def test_area_zero(self):
        self.assertEqual(square_area(0), 0)

    def test_perimeter_zero(self):
        self.assertEqual(square_perimeter(0), 0)


class TriangleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(triangle_area(723, 5439), 1966198.5)
        self.assertIsInstance(triangle_area(723, 5438), float)
        self.assertIsNone(triangle_area(-76, 12), float)

    def test_perimeter(self):
        self.assertEqual(triangle_perimeter(34, 85, 56), 175)
        self.assertIsNone(triangle_perimeter(-831, -7790, -3215))

    def test_area_zero(self):
        self.assertEqual(triangle_area(432, 0), 0)
        self.assertEqual(triangle_area(0, 0), 0)

    def test_perimeter_zero(self):
        self.assertIsNone(triangle_perimeter(-51, 50, 0))
        self.assertEqual(triangle_perimeter(0, 0, 0), 0)


class CircleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertIsInstance(circle_area(75), float)
        self.assertEqual(circle_area(691), 1500050.801828708)
        self.assertIsNone(circle_area(-76))

    def test_perimeter(self):
        self.assertIsInstance(circle_perimeter(64), float)
        self.assertEqual(circle_perimeter(74), 464.9557127312894)
        self.assertIsNone(circle_perimeter(-42))

    def test_area_zero(self):
        self.assertEqual(circle_area(0), 0)

    def test_perimeter_zero(self):
        self.assertEqual(circle_perimeter(0), 0)


if __name__ == '__main__':
    unittest.main()
