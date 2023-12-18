import math
import unittest

def area(r):
    '''Возвращает площадь окружности

        Параметры:
            r (int) or (float):радиус окружности

        Возвращаемое значение:
            (float):Площадь данной окружности
    ''' 
    return math.pi * r * r


def perimeter(r):
    '''Возвращает периметр окружности
    
        Параметры:
            r (int) or (float):радиус окружности

        Возвращаемое значение:
            (float):Периметр данной окружности
    ''' 
    return 2 * math.pi * r
class Circle_TestCase(unittest.TestCase):
    #area test
    def test_area_int(self):
        res = area(425)
        self.assertEqual(res, 567450.1730546564)
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_circle_area_pi(self):
        res = area(math.pi)
        self.assertEqual(res, 31.006276680299816)
    def test_area_big_data(self):
        res = area(347889382374)
        self.assertEqual(res, 3.802176043589256e+23)

    def test_area_fraction(self):
        res = area(56.234)
        self.assertEqual(res, 9934.541442970212)

    # perimetr test
    def test_perimetr_int(self):
        res = perimeter(28)
        self.assertEqual(res, 175.92918860102841)
    def test_zero_perimetr(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_circle_perimetr_pi(self):
        res = perimeter(math.pi)
        self.assertEqual(res, 19.739208802178716)
    def test_perimetr_big_data(self):
        res = perimeter(57512357891)
        self.assertEqual(res, 361360802081.9851)

    def test_perimetr_fraction(self):
        res = perimeter(67.89732)
        self.assertEqual(res, 426.6114434208706)

