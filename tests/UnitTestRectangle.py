import rectangle
import unittest

class CircleTestCase(unittest.TestCase):

    '''
    test Area rectangle
    '''

    def test_zero_area(self):
        res = rectangle.area(0, 0)
        self.assertEqual(res, 0)

    def test_positive_square_area(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_positive_float_area(self):
        res = rectangle.area(29.5, 20.3)
        self.assertEqual(res, 598.85)

    def test_negative_square_area(self):
        res = rectangle.area(-10, -10)
        self.assertEqual(res, "нельзя вычеслить для отрицательных входных значний")
    def test_negative_float_area(self):
        res = rectangle.area(-29.5, -20.3)
        self.assertEqual(res, "нельзя вычеслить для отрицательных входных значний")
    def test_str_float_area(self):
        res = rectangle.area("9", "2")
        self.assertEqual(res, "тип дынных передонных в функцию не подлежит вычеслениям")


    '''
    test Perimeter rectangle
    '''

    def test_zero_perimeter(self):
        res = rectangle.area(0, 0)
        self.assertEqual(res, 0)

    def test_positive_perimeter(self):
        res = rectangle.perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_positive_float_perimeter(self):
        res = rectangle.perimeter(29.5, 20.3)
        self.assertEqual(res, 99.6)

    def test_negative_perimeter(self):
        res = rectangle.perimeter(-10, -10)
        self.assertEqual(res, "нельзя вычеслить для отрицательных входных значний")
    def test_negative_float_perimeter(self):
        res = rectangle.perimeter(-29.5, - 20.3)
        self.assertEqual(res, "нельзя вычеслить для отрицательных входных значний")
    def test_str_perimeter(self):
        res = rectangle.perimeter("9", "2")
        self.assertEqual(res, "тип дынных передонных в функцию не подлежит вычеслениям")