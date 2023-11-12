import unittest
import rectangle


class RectangleTest(unittest.TestCase):
    ''' модуль UNITTEST, проверяющий корректность вычислений функцией площади прямоугольника'''

    def test_area_1(self):
        res = rectangle.area(2, 0)
        self.assertEqual(res, "The figure doesn't exist")

    def test_area_2(self):
        res = rectangle.area(2, 3)
        self.assertEqual(res, 6)

    def test_area_3(self):
        res = rectangle.area(5, -1)
        self.assertEqual(res, 'Invalid input')

    def test_area_4(self):
        res = rectangle.area('a', 10)
        self.assertEqual(res, 'Invalid input')

    def test_area_5(self):
        res = rectangle.area(True, False)
        self.assertEqual(res, 'Invalid input')

    ''' модуль UNITTEST, проверяющий корректность вычислений функцией периметра прямоугольника'''

    def test_perimeter_1(self):
        res = rectangle.perimeter(2, 0)
        self.assertEqual(res, "The figure doesn't exist")

    def test_perimeter_2(self):
        res = rectangle.perimeter(2, 3)
        self.assertEqual(res, 10)

    def test_perimeter_3(self):
        res = rectangle.perimeter(5, -1)
        self.assertEqual(res, 'Invalid input')

    def test_perimeter_4(self):
        res = rectangle.perimeter('a', 10)
        self.assertEqual(res, 'Invalid input')

    def test_perimeter_5(self):
        res = rectangle.perimeter(True, False)
        self.assertEqual(res, 'Invalid input')


if __name__ == '__main__':
    unittest.main()
