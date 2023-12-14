import unittest


def area(a, h):
    '''принимает числа а, h (сторона и высота треугольника), возвращает площадь данного треугольника'''
    if not ((type(a) == int or type(a) == float) and (type(h) == int or type(h) == float)):
        return "type error"
    if a <= 0 or h <= 0:
        return "incorrect arguments"
    return a * h / 2


def perimeter(a, b, c):
    '''принимает числа а, b, c (стороны треугольника), возвращает периметер данного треугольника'''
    for i in [a, b, c]:
        if not (type(i) == int or type(i) == float):
            return "type error"
        if i <= 0:
            return "incorrect arguments"
    return a + b + c


def semiPerimiter(a, b, c):
    '''принимает числа а, b, c (стороны треугольника), возвращает полупериметер данного треугольника'''
    for i in [a, b, c]:
        if not (type(i) == int or type(i) == float):
            return "type error"
        if i <= 0:
            return "incorrect arguments"
    return (a + b + c) / 2


class TriangleTestCase(unittest.TestCase):
    def test_triangle_area(self):
        self.assertEqual(area(5, 2), 5)
        self.assertEqual(area(10, 2.6), 13)

    def test_triangle_perimeter(self):
        self.assertEqual(perimeter(10, 6, 8), 24)
        self.assertEqual(perimeter(10.5, 6.5, 8.5), 25.5)

    def test_incorrect_arguments(self):
        self.assertEqual(area(-10, 3), "incorrect arguments")
        self.assertEqual(area(10, -3), "incorrect arguments")
        self.assertEqual(area(0, 0), "incorrect arguments")
        self.assertEqual(perimeter(0, 0, 0), "incorrect arguments")
        self.assertEqual(semiPerimiter(0, 0, 0), "incorrect arguments")

    def test_incorrect_type(self):
        self.assertEqual(area([7], '0'), "type error")
        self.assertEqual(perimeter('0', {0}, [0]), "type error")
        self.assertEqual(semiPerimiter('0', {0}, [0]), "type error")