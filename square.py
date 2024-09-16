import unittest


def area(a):
    '''
    Возвращает площадь квадрата со стороной a.

    Параметры:
        a (int): сторона квадрата.

    Возвращаемое значение:
        area (int): площадь квадрата со стороной a.
    '''
    if a < 0:
        raise ValueError('side cannot be negative')
    return a * a


def perimeter(a):
    '''
    Возвращает периметр квадрата со стороной a.

    Параметры:
        a (int): сторона квадрата.

    Возвращаемое значение:
        perimeter (int): периметр квадрата со стороной a.
    '''
    if a < 0:
        raise ValueError('side cannot be negative')
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_regular(self):
        res = area(2)
        self.assertEqual(res, 4)

    def test_area_negative(self):
        with (self.assertRaises(ValueError) as context):
            area(-1)
        self.assertTrue('side cannot be negative' in str(context.exception))

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_regular(self):
        res = perimeter(3)
        self.assertEqual(res, 12)

    def test_perimeter_negative(self):
        with (self.assertRaises(ValueError) as context):
            perimeter(-8)
        self.assertTrue('side cannot be negative' in str(context.exception))
