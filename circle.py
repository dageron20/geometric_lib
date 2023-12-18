import unittest

import math
from math import inf


def area(data):
    '''
        Возвращает произведение математической константы и двух чисел с плавающей точкой в десятичной системе счисления.

            Параметры:
                data (str) : массив входных данных (числа с плавающей точкой в десятичной системе счисления)

            Возвращаемое значение:
                (math.pi * r * r) (float) : число с плавающей точкой в десятичной системе счисления

                Пример вызова функции:
                    area([10.5]) = 346.36059005827474
        
                    Пример вызова функции:
                        perimeter(10.5) = 65.97344572538566
    '''

    def is_digit(a):
        length = len(str(a))
        for i in range(0, length):
            if (not (a[i].isdigit())) and (a[i] != "e") and (a[i] != ".") and (a[i] != "+") and (a[i] != "-"):
                return False
        return True

    if len(data) != 1:
        return 'Перечитайте условие и введите необходимое количество входных данных.'
    else:
        r = data[0]

    # обработка и выдача результатов
    if is_digit(str(r)):
        r = float(r)
        if r < 0:
            return 'Значение элемента геометрической фигуры не может быть отрицательным, введите корректные данные.'
        elif r == 1.7976931348623157e+308:
            return 'Ошибка: Переполнение в результате выполнения арифметической операции.'
        else:
            return math.pi * r * r
    else:
        return (
            'Входные данные являются строковыми значениями, а не численными. Попробуйте еще раз и введите корректные данные.')


def perimeter(data):
    '''
            Возвращает произведение десятичной константы, математической константы и числа с плавающей точкой в десятичной системе счисления.

                Параметры:
                    data (str) : массив входных данных (числа с плавающей точкой в десятичной системе счисления)

                Возвращаемое значение:
                    (2 * math.pi * r) (float) : число с плавающей точкой в десятичной системе счисления

                        Пример вызова функции:
                            perimeter(10.5) = 65.97344572538566

        '''

    def is_digit(a):
        length = len(str(a))
        for i in range(0, length):
            if (not (a[i].isdigit())) and (a[i] != "e") and (a[i] != ".") and (a[i] != "+") and (a[i] != "-"):
                return False
        return True

    if len(data) != 1:
        return 'Перечитайте условие и введите необходимое количество входных данных.'
    else:
        r = data[0]

    # обработка и выдача результатов
    if is_digit(str(r)):
        r = float(r)
        if r < 0:
            return 'Значение элемента геометрической фигуры не может быть отрицательным, введите корректные данные.'
        elif r == 1.7976931348623157e+308:
            return 'Ошибка: Переполнение в результате выполнения арифметической операции.'
        else:
            return 2 * math.pi * r
    else:
        return (
            'Входные данные являются строковыми значениями, а не численными. Попробуйте еще раз и введите корректные данные.')


class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area([0])
        self.assertEqual(res, 0)

    def test_area_mul(self):
        res = area([254])
        self.assertEqual(res, 202682.99163899910057265590051566)

    def test_perimeter_mul(self):
        res = perimeter([198])
        self.assertEqual(res, 1244.0706908215581224312067797787)

    def test_perimeter_negative(self):
        res = perimeter([-8329])
        self.assertEqual(res,
                         'Значение элемента геометрической фигуры не может быть отрицательным, введите корректные данные.')

    def test_area_negative(self):
        res = area([-18.301])
        self.assertEqual(res,
                         'Значение элемента геометрической фигуры не может быть отрицательным, введите корректные данные.')

    def test_perimeter_inf(self):
        res = perimeter([1.7976931348623157e+308])
        self.assertEqual(res, 'Ошибка: Переполнение в результате выполнения арифметической операции.')

    def test_area_inf(self):
        res = area([1.7976931348623157e+308])
        self.assertEqual(res, 'Ошибка: Переполнение в результате выполнения арифметической операции.')

    def test_perimeter_str(self):
        res = perimeter(['bibaboba'])
        self.assertEqual(res,
                         'Входные данные являются строковыми значениями, а не численными. Попробуйте еще раз и введите корректные данные.')

    def test_area_str(self):
        res = area(['bambam'])
        self.assertEqual(res,
                         'Входные данные являются строковыми значениями, а не численными. Попробуйте еще раз и введите корректные данные.')

    def test_perimeter_value(self):
        res = perimeter([10, 62819])
        self.assertEqual(res, 'Перечитайте условие и введите необходимое количество входных данных.')

    def test_area_value(self):
        res = area([5932, 3, 1, 6, 9])
        self.assertEqual(res, 'Перечитайте условие и введите необходимое количество входных данных.')
