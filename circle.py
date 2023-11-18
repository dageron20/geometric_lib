import unittest


def area(r):
    '''принимает число r (радиус круга), возвращает площадь данного круга'''
    if r >= 0:
        return 3.14 * r * r
    return "error"

def perimeter(r):
    '''принимает число r (радиус круга), возвращает длину окружности данного круга'''
    if r >= 0:
        return 2 * 3.14 * r
    return "error"

class CicrcleTestCase(unittest.TestCase):
    def test_circle_area(self):
        cases = [0, 1, 2, 10]
        answers = [0, 3.14, 12.56, 314.0]
        for i in range(4):
            res = area(cases[i])
            self.assertEqual(res, answers[i])

    def test_incorrect_arguments_area(self):
        res = area(-1)
        self.assertEqual(res, "error")

    def test_incorrect_arguments_perimeter(self):
        res = perimeter(-10)
        self.assertEqual(res, "error")

    def test_circle_perimeter(self):
        cases = [0, 1, 2, 50]
        answers = [0, 6.28, 12.56, 314.0]
        for i in range(4):
            res = perimeter(cases[i])
            self.assertEqual(res, answers[i])