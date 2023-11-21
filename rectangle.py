import unittest

def area(a, b):
    '''принимает числа а, b (стороны прямоугольника), возвращает площадь данного прямоугольника'''
    if not ((type(a) == int or type(a) == float) and (type(b) == int or type(b) == float)):
        return "type error"
    if a <= 0 or b <= 0:
        return "incorrect arguments"
    return a * b


def perimeter(a, b):
    '''принимает числа а, b (стороны прямоугольника), возвращает периметер данного прямоугольника'''
    if not ((type(a) == int or type(a) == float) and (type(b) == int or type(b) == float)):
        return "type error"
    if a <= 0 or b <= 0:
        return "incorrect arguments"
    return (a + b) * 2


class RectangleTestCase(unittest.TestCase):
    def test_incorrect_type(self):
        cases = [('5', 5), (5, [5]), ({5}, 0)]
        for case in cases:
            self.assertEqual(area(case[0], case[1]), "type error")
            self.assertEqual(perimeter(case[0], case[1]), "type error")


    def test_incorrect_arguments(self):
        cases = [(-5, -5), (-5, 1), (1, -5), (0, 10), (10, 0), (0, 0)]
        for case in cases:
            self.assertEqual(area(case[0], case[1]), "incorrect arguments")
            self.assertEqual(perimeter(case[0], case[1]), "incorrect arguments")

    def test_rectangle_area(self):
        self.assertEqual(area(10, 2.5), 25)
        self.assertEqual(area(10, 2), 20)

    def test_rectangle_perimeter(self):
        self.assertEqual(perimeter(10, 5), 30)
        self.assertEqual(perimeter(10, 2.5), 25)