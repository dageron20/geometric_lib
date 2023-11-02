import unittest

class RectangleTestCase(unittest.TestCase):
    def test_circle_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_circle_perimetr(self):
        res = area(1)
        self.assertEqual(res, 6.28)

import math

def area(r):
    return math.pi * r * r
    '''
    Данная функция вычисляет площадь круга.
        На вход поступает значение радиуса окружности.
        Функция возвращает значение равное произведению радиуса окружности на радиус окружности и на число пи, которое мы берём из библиотеки math.    
    '''


def perimeter(r):
    return 2 * math.pi * r
    '''
    Данная функция вычисляет периметр круга.
    На вход поступает значение радиуса окружности.
    Функция возвращает значение равное произведению 2 на радиус окружности и на число пи, которое взяли из библиотеки math.    
    '''
