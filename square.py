import unittest

def area(a):
    '''принимает число а (сторона квадрата), возвращает площадь данного квадрата'''
    if a >= 0:
        return a * a
    return "error"


def perimeter(a):
    '''принимает число а (сторона квадрата), возвращает периметер данного квадрата'''
    if a >= 0:
        return a * 4
    return "error"

def semiPerimiter(a):
    '''принимает число а (сторона квадрата), возвращает полупериметер данного квадрата'''
    if a >= 0:
        return a * 2
    return "error"

class SquareTestCase(unittest.TestCase):
    def test_square_area(self):
        cases = [0, 1, 2, 50]
        answers = [0, 1, 4, 2500]
        for i in range(4):
            res = area(cases[i])
            self.assertEqual(res, answers[i])

    def test_incorrect_arguments_area(self):
        res = area(-10)
        self.assertEqual(res, "error")

    def test_incorrect_arguments_perimeter(self):
        res = perimeter(-10)
        self.assertEqual(res, "error")

    def test_incorrect_arguments_semiperimeter(self):
        res = semiPerimiter(-10)
        self.assertEqual(res, "error")

    def test_square_perimeter(self):
        cases = [0, 1, 2, 50]
        answers = [0, 4, 8, 200]
        for i in range(4):
            res = perimeter(cases[i])
            self.assertEqual(res, answers[i])

    def test_square_semiperimeter(self):
        cases = [0, 1, 2, 50]
        answers = [0, 2, 4, 100]
        for i in range(4):
            res = semiPerimiter(cases[i])
            self.assertEqual(res, answers[i])