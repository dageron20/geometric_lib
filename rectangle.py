import unittest


def area(a, b):
    '''
    Возвращает площадь прямоугольника со сторонами a и b.

	Параметры:
		a (int): первая сторона прямоугольника (ширина).
		b (int): вторая сторона прямоугольника (высота).

	Возвращаемое значение:
		area (int): площадь прямоугольника со сторонами a и b.
    '''
    if a < 0 or b < 0:
        raise ValueError('side cannot be negative')
    return a * b


def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника со сторонами a и b.

    Параметры:
        a (int): первая сторона прямоугольника (ширина).
        b (int): вторая сторона прямоугольника (высота).

    Возвращаемое значение:
        perimeter (int): периметр прямоугольника со сторонами a и b.
    '''
    if a < 0 or b < 0:
        raise ValueError('side cannot be negative')
    return 2 * (a + b)


class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0, 2)
        self.assertEqual(res, 0)

    def test_area_regular(self):
        res = area(2, 4)
        self.assertEqual(res, 8)

    def test_area_negative(self):
        with (self.assertRaises(ValueError) as context):
            area(8, -5)
        self.assertTrue('side cannot be negative' in str(context.exception))

    def test_perimeter_zero(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_regular(self):
        res = perimeter(3, 1)
        self.assertEqual(res, 8)

    def test_perimeter_negative(self):
        with (self.assertRaises(ValueError) as context):
            perimeter(-8, 3)
        self.assertTrue('side cannot be negative' in str(context.exception))
