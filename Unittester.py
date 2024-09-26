import unittest

import rectangle
import square
import triangle
import circle


class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area1(self):
        '''Тест на корректность работы функции area в файле rectangle.py'''
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_rectangle_area2(self):
        res = rectangle.area(1123441, 5643234)
        self.assertEqual(res, 6339840448194)

    def test_rectangle_area3(self):
        res = rectangle.area("1123441", "5643234")
        self.assertEqual(res, 6339840448194)

    def test_rectangle_perimeter1(self):
        '''Тест на корректность работы функции perimeter в файле rectangle.py'''
        res = rectangle.perimeter(15, 0)
        self.assertEqual(res, 30)

    def test_rectangle_perimeter2(self):
        res = rectangle.perimeter(354, 321)
        self.assertEqual(res, 1350)

    def test_rectangle_perimeter3(self):
        res = rectangle.perimeter("354", "321")
        self.assertEqual(res, 1350)

    def test_square_area1(self):
        '''Тест на корректность работы функции area в файле square.py'''
        res = square.area(11324)
        self.assertEqual(res, 128232976)

    def test_square_area2(self):
        res = square.area(-11)
        self.assertEqual(res, 121)

    def test_square_area3(self):
        res = square.area("-11")
        self.assertEqual(res, 121)

    def test_square_perimeter1(self):
        '''Тест на корректность работы функции perimeter в файле square.py'''
        res = square.perimeter(153)
        self.assertEqual(res, 612)

    def test_square_perimeter2(self):
        res = square.perimeter(312)
        self.assertEqual(res, 1248)

    def test_square_perimeter3(self):
        res = square.perimeter("312")
        self.assertEqual(res, 1248)

    def test_circle_area1(self):
        '''Тест на корректность работы функции area в файле circle.py'''
        res = circle.area(14)
        self.assertEqual(res, 615.7521601035994)

    def test_circle_area2(self):
        res = circle.area(164)
        self.assertEqual(res, 84496.27601095107)

    def test_circle_area3(self):
        res = circle.area("164")
        self.assertEqual(res, 84496.27601095107)

    def test_circle_perimeter1(self):
        '''Тест на корректность работы функции perimeter в файле circle.py'''
        res = circle.perimeter(15)
        self.assertEqual(res, 94.24777960769379)

    def test_circle_perimeter2(self):
        res = circle.perimeter(3)
        self.assertEqual(res, 18.84955592153876)

    def test_circle_perimeter3(self):
        res = circle.perimeter("3")
        self.assertEqual(res, 18.84955592153876)

    def test_triangle_area1(self):
        '''Тест на корректность работы функции area в файле triangle.py'''
        res = triangle.area(15, 48)
        self.assertEqual(res, 360)

    def test_triangle_area2(self):
        res = triangle.area(15, 43)
        self.assertEqual(res, 322.5)

    def test_triangle_area3(self):
        res = triangle.area("15", "43")
        self.assertEqual(res, 322.5)

    def test_triangle_perimeter1(self):
        '''Тест на корректность работы функции perimeter в файле triangle.py'''
        res = triangle.perimeter(13, 323, 32)
        self.assertEqual(res, 368)

    def test_triangle_perimeter2(self):
        res = triangle.perimeter(13, 33, 32)
        self.assertEqual(res, 78)

    def test_triangle_perimeter3(self):
        res = triangle.perimeter("13", "33", "32")
        self.assertEqual(res, 78)

    def test_triangle_perimeter4(self):
        res = triangle.perimeter(100000, 1000000, 1)
        self.assertEqual(res, -1)


if __name__ == '__main__':
    unittest.main()
