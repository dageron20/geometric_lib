import unittest

def area(a, b):
    '''принимает числа а, b (стороны прямоугольника), возвращает площадь данного прямоугольника'''
    if a >= 0 and b >= 0:
        return a * b
    return "error"

def perimeter(a, b):
    '''принимает числа а, b (стороны прямоугольника), возвращает периметер данного прямоугольника'''
    if a >= 0 and b >= 0:
        return (a + b) * 2
    return "error"


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_incorrect_arguments_area(self):
        cases = [(-5, -5), (-1, 2), (1, -8)]
        for case in cases:
            res = area(case[0], case[1])
            self.assertEqual(res, "error")

    def test_incorrect_arguments_perimeter(self):
        cases = [(-5, -5), (-1, 2), (1, -8)]
        for case in cases:
            res = area(case[0], case[1])
            self.assertEqual(res, "error")

    def test_rectangle_area(self):
        cases = [(10, 10), (2, 2), (7, 1), (24, 38)]
        answers = [100, 4, 7, 912]
        for i in range(4):
            res = area(cases[i][0], cases[i][1])
            self.assertEqual(res, answers[i])

    def test_rectangle_perimeter(self):
        cases = [(10, 10), (2, 2), (7, 1), (24, 38)]
        answers = [40, 8, 16, 124]
        for i in range(4):
            res = perimeter(cases[i][0], cases[i][1])
            self.assertEqual(res, answers[i])
