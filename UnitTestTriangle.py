import triangle
import unittest

class CircleTestCase(unittest.TestCase):

    '''
    test Area triangle
    '''

    def test_zero_area(self):
        res = triangle.area(0, 0)
        self.assertEqual(res, 0)

    def test_positive_square_area(self):
        res = triangle.area(10, 10)
        self.assertEqual(res, 50)

    def test_positive_float_area(self):
        res = triangle.area(29.5, 20.3)
        self.assertEqual(res, 299.425)

    def test_negative_square_area(self):
        res = triangle.area(-10, -10)
        self.assertEqual(res, "нельзя вычеслить для отрицательных входных значний")
    def test_negative_float_area(self):
        res = triangle.area(-29.5, -20.3)
        self.assertEqual(res, "нельзя вычеслить для отрицательных входных значний")


    '''
    test Perimeter triangle
    '''

    def test_zero_perimeter(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_positive_perimeter(self):
        res = triangle.perimeter(10, 10, 10)
        self.assertEqual(res, 30)

    def test_positive_float_perimeter(self):
        res = triangle.perimeter(29.5, 20.3, 10.4)
        self.assertEqual(res, 60.199999999999996)

    def test_negative_perimeter(self):
        res = triangle.perimeter(-10, -10, -10)
        self.assertEqual(res, "нельзя вычеслить для отрицательных входных значний")
    def test_negative_float_perimeter(self):
        res = triangle.perimeter(-29.5, - 20.3, -10.4)
        self.assertEqual(res, "нельзя вычеслить для отрицательных входных значний")