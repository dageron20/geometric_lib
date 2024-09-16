import math
import unittest


def area(r):
    '''
    Возвращает площадь круга радиусом r.

	Параметры:
		r (int): радиус круга.
	
	Возвращаемое значение:
		area (float): площадь круга радиусом r.
    '''
    if r < 0:
        raise ValueError('radius cannot be negative')
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга радиусом r.

	Параметры:
		r (int): радиус круга.

	Возвращаемое значение:
		perimeter (float): периметр круга радиусом r.
    '''
    if r < 0:
        raise ValueError('radius cannot be negative')
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_regular(self):
        res = area(4)
        self.assertEqual(res, 50.26548245743669)

    def test_area_negative(self):
        with (self.assertRaises(ValueError) as context):
            area(-3)
        self.assertTrue('radius cannot be negative' in str(context.exception))

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_regular(self):
        res = perimeter(5)
        self.assertEqual(res, 31.41592653589793)

    def test_perimeter_negative(self):
        with (self.assertRaises(ValueError) as context):
            perimeter(-8)
        self.assertTrue('radius cannot be negative' in str(context.exception))
