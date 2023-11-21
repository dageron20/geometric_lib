import unittest

def area(a):
    '''принимает число а (сторона квадрата), возвращает площадь данного квадрата'''
    if type(a) != int and type(a) != float:
        return "type error"
    if a <= 0:
        return "incorrect argument"
    return a * a


def perimeter(a):
    '''принимает число а (сторона квадрата), возвращает периметер данного квадрата'''
    if type(a) != int and type(a) != float:
        return "type error"
    if a <= 0:
        return "incorrect argument"
    return a * 4


def semiPerimiter(a):
    '''принимает число а (сторона квадрата), возвращает полупериметер данного квадрата'''
    if type(a) != int and type(a) != float:
        return "type error"
    if a <= 0:
        return "incorrect argument"
    return a * 2


class SquareTestCase(unittest.TestCase):
    def test_square_area(self):
        self.assertEqual(area(2), 4)
        self.assertEqual(area(1.5), 2.25)


    def test_square_perimeter(self):
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(2.5), 10)


    def test_square_semiPerimeter(self):
        self.assertEqual(perimeter(2), 4)
        self.assertEqual(perimeter(2.5), 5)


    def test_incorrect_arguments(self):
        self.assertEqual(area(-10), "incorrect argument")
        self.assertEqual(area(0), "incorrect argument")
        self.assertEqual(perimeter(-10), "incorrect argument")
        self.assertEqual(perimeter(0), "incorrect argument")
        self.assertEqual(semiPerimiter(-10), "incorrect argument")
        self.assertEqual(semiPerimiter(0), "incorrect argument")

    def test_incorrect_type(self):
        cases = [[1], '1', {1}]
        for case in cases:
            self.assertEqual(area(case), "type error")
            self.assertEqual(perimeter(case), "type error")
            self.assertEqual(semiPerimiter(case), "type error")