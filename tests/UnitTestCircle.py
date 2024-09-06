import circle
import unittest

class CircleTestCase(unittest.TestCase):

    '''
    test circle Area
    '''

    def test_zero_radius_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_positive_radius_area(self):
        res = circle.area(100)
        self.assertEqual(res, 31415.926535897932)

    def test_positive_radius_float_area(self):
        res = circle.area(29.5)
        self.assertEqual(res, 2733.9710067865176)

    def test_negative_radius_area(self):
        res = circle.area(-100)
        self.assertEqual(res, "нельзя вычеслить для отрицательных входных значний")
    def test_negative_radius_float_area(self):
        res = circle.area(-29.5)
        self.assertEqual(res, "нельзя вычеслить для отрицательных входных значний")
    def test_str_area(self):
        res = circle.area("9")
        self.assertEqual(res, "тип дынных передонных в функцию не подлежит вычеслениям")

    '''
    test circle Perimeter
    '''

    def test_zero_radius_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_positive_radius_perimeter(self):
        res = circle.perimeter(100)
        self.assertEqual(res, 628.3185307179587)

    def test_positive_radius_float_perimeter(self):
        res = circle.perimeter(29.5)
        self.assertEqual(res, 185.3539665617978)

    def test_negative_radius_perimeter(self):
        res = circle.perimeter(-100)
        self.assertEqual(res, "нельзя вычеслить для отрицательных входных значний")
    def test_negative_radius_float_perimeter(self):
        res = circle.perimeter(-29.5)
        self.assertEqual(res, "нельзя вычеслить для отрицательных входных значний")
    def test_str_perimeter(self):
        res = circle.perimeter("9")
        self.assertEqual(res, "тип дынных передонных в функцию не подлежит вычеслениям")


