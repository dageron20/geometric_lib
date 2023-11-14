import unittest
import square


class SquareTest(unittest.TestCase):
    ''' модуль UNITTEST, проверяющий корректность вычислений функцией площади квадрата'''
    def test_area_1(self):
        res = square.area(2)
        self.assertEqual(res, 4)

    def test_area_2(self):
        res = square.area(0)
        self.assertEqual(res, "The figure doesn't exist")

    def test_area_3(self):
        res = square.area(-1)
        self.assertEqual(res, 'Invalid input')

    def test_area_4(self):
        res = square.area('a')
        self.assertEqual(res, 'Invalid input')

    def test_area_5(self):
        res = square.area(True)
        self.assertEqual(res, 'Invalid input')

   ''' модуль UNITTEST, проверяющий корректность вычислений функцией периметр2 квадрата'''

    def test_perimeter_1(self):
        res = square.perimeter(4)
        self.assertEqual(res, 16)

    def test_perimeter_2(self):
        res = square.perimeter(0)
        self.assertEqual(res, "The figure doesn't exist")

    def test_perimeter_3(self):
        res = square.perimeter(-1)
        self.assertEqual(res, 'Invalid input')

    def test_perimeter_4(self):
        res = square.perimeter('a')
        self.assertEqual(res, 'Invalid input')

    def test_perimeter_5(self):
        res = square.perimeter(True)
        self.assertEqual(res, 'Invalid input')


if __name__ == '__main__':
    unittest.main()
