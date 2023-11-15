import unittest
import math

class RectangleTestCase(unittest.TestCase):
    def test1_circle_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test2_circle_area(self):
        res = area(-1)
        self.assertEqual(res, 'error')

    def test3_circle_area(self):
        res = area(5)
        self.assertEqual(res, 78.5)

    def test1_circle_perimetr(self):
        res = perimeter(1)
        self.assertEqual(res, 6.28)

    def test2_circle_perimetr(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test3_circle_perimetr(self):
        res = perimeter(-1)
        self.assertEqual(res, 'error')
def area(r):
    if r > 0:
        return math.pi * r * r
    if r < 0:
        return 'error'
    if r == 0:
        return 0


    '''
    Данная функция вычисляет площадь круга.
        На вход поступает значение радиуса окружности.
        Функция возвращает значение равное произведению радиуса окружности на радиус окружности и на число пи, которое мы берём из библиотеки math.    
    '''


def perimeter(r):
    if r > 0:
        return 2 * math.pi * r
    if r < 0:
        return 'error'
    if r == 0:
        return 0
    '''
    Данная функция вычисляет периметр круга.
    На вход поступает значение радиуса окружности.
    Функция возвращает значение равное произведению 2 на радиус окружности и на число пи, которое взяли из библиотеки math.    
    '''
