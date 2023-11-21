import unittest
import math

import circle
class CircleTestCases(unittest.TestCase):

    """ Тестиривание вычисления площади круга """
    def test_area(self):
        self.assertEqual(circle.area(4), 50.26548245743669)
        self.assertEqual(circle.area(0), 0)

    """ Тестиривание вычисления периметра круга """
    def test_perimeter(self):
        self.assertEqual(circle.perimeter(5), 31.41592653589793)
        self.assertEqual(circle.perimeter(0), 0)

    """ Тестирование невалидных значений """
    def test_assert(self):
        self.assertFalse(circle.area("some string"))
        self.assertFalse(circle.area("0"))


import rectangle
class RectangleTestCases(unittest.TestCase):

    """ Тестиривание вычисления площади прямоугольника """
    def test_area(self):
        self.assertEqual(rectangle.area(4, 9), 36)
        self.assertEqual(rectangle.area(0, 0), 0)

    """ Тестиривание вычисления периметра """
    def test_perimeter(self):
        self.assertEqual(rectangle.perimeter(5, 6), 22)
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    """ Тестирование невалидных значений """
    def test_assert(self):
        self.assertFalse(rectangle.area("4", 9))
        self.assertFalse(rectangle.perimeter("4", "1qq"))


import square
class SquareTestCases(unittest.TestCase):

    """ Тестиривание вычисления площади квадрата """
    def test_area(self):
        self.assertEqual(square.area(9), 81)
        self.assertEqual(square.area(0), 0)

    """ Тестиривание вычисления периметра квадрата """
    def test_perimeter(self):
        self.assertEqual(square.perimeter(3), 12)
        self.assertEqual(square.perimeter(0), 0)
        
    """ Тестирование невалидных значений """
    def test_assert(self):
        self.assertFalse(square.area("-"))
        self.assertFalse(square.perimeter("10"))


import triangle
class TriangleTestCases(unittest.TestCase):

    """ Тестиривание вычисление площади треугольника """
    def test_area(self):
        self.assertEqual(triangle.area(9, 2), 9)
        self.assertEqual(triangle.area(0, 0), 0)

    """ Тестиривание вычисления периметра треугольника """
    def test_perimeter(self):
        self.assertEqual(triangle.perimeter(5, 9, 7), 21)
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    """ Тестирование невалидных значений """
    def test_assert(self):
        self.assertFalse(triangle.area("-", 0))
        self.assertFalse(triangle.perimeter("10", 3, 9))


if __name__ == '__main__':
    unittest.main()
