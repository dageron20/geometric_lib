import unittest

def area(a, h):
    '''принимает числа а, h (сторона и высота треугольника), возвращает площадь данного треугольника'''
    if a >= 0 and h >= 0:
        return a * h / 2
    return "error"


def perimeter(a, b, c):
    '''принимает числа а, b, c (стороны треугольника), возвращает периметер данного треугольника'''
    if a >= 0 and b >= 0 and c >= 0:
        return a + b + c
    return "error"

def semiPerimiter(a, b, c):
    '''принимает числа а, b, c (стороны треугольника), возвращает полупериметер данного треугольника'''
    if a >= 0 and b >= 0 and c >= 0:
        return (a + b + c) / 2
    return "error"

class TriangleTestCase(unittest.TestCase):
    def test_triangle_area(self):
        cases = [(10, 6), (8, 2), (4, 1), (15, 2)]
        answers = [30, 8, 2, 15]
        for i in range(4):
            res = area(cases[i][0], cases[i][1])
            self.assertEqual(res, answers[i])

    def test_incorrect_arguments_area(self):
        cases = [(-5, -2), (-1, 2), (10, -8)]
        for case in cases:
            res = area(case[0], case[1])
            self.assertEqual(res, "error")

    def test_incorrect_arguments_perimeter(self):
        cases = [(5, 2, -3), (5, -2, 3), (-5, 2, 3), (-5, -2, -3), (-5, -2, 3), (5, -2, -3), (-5, 2, -3)]
        for case in cases:
            res = perimeter(case[0], case[1], case[2])
            self.assertEqual(res, "error")

    def test_incorrect_arguments_semiperimeter(self):
        cases = [(5, 2, -3), (5, -2, 3), (-5, 2, 3), (-5, -2, -3), (-5, -2, 3), (5, -2, -3), (-5, 2, -3)]
        for case in cases:
            res = semiPerimiter(case[0], case[1], case[2])
            self.assertEqual(res, "error")

    def test_triangle_perimeter(self):
        cases = [(10, 6, 8), (8, 2, 7), (4, 1, 4), (15, 11, 20)]
        answers = [24, 17, 9, 46]
        for i in range(4):
            res = perimeter(cases[i][0], cases[i][1], cases[i][2])
            self.assertEqual(res, answers[i])

    def test_triangle_semiperimeter(self):
        cases = [(10, 6, 8), (8, 2, 7), (4, 1, 4), (15, 11, 20)]
        answers = [12, 8.5, 4.5, 23]
        for i in range(4):
            res = semiPerimiter(cases[i][0], cases[i][1], cases[i][2])
            self.assertEqual(res, answers[i])
