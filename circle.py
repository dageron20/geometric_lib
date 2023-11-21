import unittest


def area(r):
    '''принимает число r (радиус круга), возвращает площадь данного круга'''
    if type(r) != int and type(r) != float:
        return "type error"
    if r <= 0:
        return "incorrect argument"
    return 3.14 * r * r

def perimeter(r):
    '''принимает число r (радиус круга), возвращает длину окружности данного круга'''
    if type(r) != int and type(r) != float:
        return "type error"
    if r <= 0:
        return "incorrect argument"
    return 2 * 3.14 * r


class CicrcleTestCase(unittest.TestCase):
    def test_circle_area(self):
        self.assertEqual(area(1), 3.14)
        self.assertEqual(area(2.5), 19.625)


    def test_circle_perimeter(self):
        self.assertEqual(perimeter(1), 6.28)
        self.assertEqual(perimeter(0.5), 3.14)


    def test_incorrect_type(self):
        cases = [[1], '1', {1}]
        for case in cases:
            self.assertEqual(area(case), "type error")
            self.assertEqual(perimeter(case), "type error")


    def test_incorrect_arguments(self):
        self.assertEqual(area(-5), "incorrect argument")
        self.assertEqual(area(0), "incorrect argument")
        self.assertEqual(perimeter(-5), "incorrect argument")
        self.assertEqual(perimeter(0), "incorrect argument")