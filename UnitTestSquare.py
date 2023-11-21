import square
import unittest

class CircleTestCase(unittest.TestCase):

    '''
    test Area rectangle
    '''

    def test_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_positive_square_area(self):
        res = square.area(10)
        self.assertEqual(res, 100)

    def test_positive_float_area(self):
        res = square.area(29.5)
        self.assertEqual(res, 870.25)

    def test_negative_square_area(self):
        res = square.area(-10)
        self.assertEqual(res, "нельзя вычеслить для отрицательных входных значний")
    def test_negative_float_area(self):
        res = square.area(-29.5)
        self.assertEqual(res, "нельзя вычеслить для отрицательных входных значний")


    '''
    test Perimeter rectangle
    '''

    def test_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_positive_perimeter(self):
        res = square.perimeter(10)
        self.assertEqual(res, 40)

    def test_positive_float_perimeter(self):
        res = square.perimeter(29.5)
        self.assertEqual(res, 118.0)

    def test_negative_perimeter(self):
        res = square.perimeter(-10)
        self.assertEqual(res, "нельзя вычеслить для отрицательных входных значний")
    def test_negative_float_perimeter(self):
        res = square.perimeter(-29.5)
        self.assertEqual(res, "нельзя вычеслить для отрицательных входных значний")