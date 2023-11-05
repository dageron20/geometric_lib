import unittest

import rectangle
import square
import triangle
import circle


class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area(self):
        '''Тест на корректность работы функции area в файле rectangle.py'''
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)
        res = rectangle.area(1123441, 5643234)
        self.assertEqual(res, 6339840448194)

    def test_rectangle_perimeter(self):
        '''Тест на корректность работы функции perimeter в файле rectangle.py'''
        res = rectangle.perimeter(15, 0)
        self.assertEqual(res, 30)
        res = rectangle.perimeter(354, 321)
        self.assertEqual(res, 1350)

    def test_square_area(self):
        '''Тест на корректность работы функции area в файле square.py'''
        res = square.area(11324)
        self.assertEqual(res, 128232976)
        res = square.area(-11)
        self.assertEqual(res, 121)

    def test_square_perimeter(self):
        '''Тест на корректность работы функции perimeter в файле square.py'''
        res = square.perimeter(153)
        self.assertEqual(res, 612)
        res = square.perimeter(312)
        self.assertEqual(res, 1248)

    def test_circle_area(self):
        '''Тест на корректность работы функции area в файле circle.py'''
        res = circle.area(14)
        self.assertEqual(res, 615.7521601035994)
        res = circle.area(164)
        self.assertEqual(res, 84496.27601095107)

    def test_circle_perimeter(self):
        '''Тест на корректность работы функции perimeter в файле circle.py'''
        res = circle.perimeter(15)
        self.assertEqual(res, 94.24777960769379)
        res = circle.perimeter(3)
        self.assertEqual(res, 18.84955592153876)

    def test_triangle_area(self):
        '''Тест на корректность работы функции area в файле triangle.py'''
        res = triangle.area(15, 48)
        self.assertEqual(res, 360)
        res = triangle.area(15, 48)
        self.assertEqual(res, 360)

    def test_triangle_perimeter(self):
        '''Тест на корректность работы функции perimeter в файле triangle.py'''
        res = triangle.perimeter(13, 323, 32)
        self.assertEqual(res, 368)
        res = triangle.perimeter(13, 33, 32)
        self.assertEqual(res, 78)
