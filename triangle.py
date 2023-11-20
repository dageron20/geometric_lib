import unittest


def area(a, h):
    '''
    Возвращает площадь треугольника по стороне и опущенной к ней высоте.

    Параметры:
        a (int): сторона треугольника.
        h (int): высота треугольника.

    Возвращаемое значение:
        area (float): площадь треугольника.
    '''
    if a < 0 or h < 0:
        raise ValueError('side or height cannot be negative')
    return a * h / 2


def perimeter(a, b, c):
    '''
    Возвращает периметр треугольника со сторонами a, b и c.

    Параметры:
        a (int): первая сторона треугольника.
        b (int): вторая сторона треугольника.
        c (int): третья сторона треугольника.

    Возвращаемое значение:
        perimeter (int): периметр треугольника со сторонами a, b и c.
    '''
    if a < 0 or b < 0 or c < 0:
        raise ValueError('side cannot be negative')
    return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_area_regular(self):
        res = area(1, 3)
        self.assertEqual(res, 1.5)

    def test_area_negative(self):
        with (self.assertRaises(ValueError) as context):
            area(-1, 8)
        self.assertTrue('side or height cannot be negative' in str(context.exception))

    def test_perimeter_zero(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_regular(self):
        res = perimeter(8, 1, 9)
        self.assertEqual(res, 18)

    def test_perimeter_negative(self):
        with (self.assertRaises(ValueError) as context):
            perimeter(-8, 3, -5)
        self.assertTrue('side cannot be negative' in str(context.exception))
