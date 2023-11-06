import unittest

from math import inf


def area(data):
    '''
    Принимает на вход число массив data (data[0]: число с плавающей точкой в десятичной системе счисления), возвращает квадрат числа data[0].

        Пример вызова функции:
            area([196]) = 38416.0
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
        a = data[0]

    # обработка и выдача результатов
    if is_digit(str(a)):
        a = float(a)
        if a < 0:
            return 'Значение элемента геометрической фигуры не может быть отрицательным, введите корректные данные.'
        elif a == 1.7976931348623157e+308:
            return 'Ошибка: Переполнение в результате выполнения арифметической операции.'
        else:
            return a * a
    else:
        return 'Входные данные являются строковыми значениями, а не численными. Попробуйте еще раз и введите корректные данные.'


def perimeter(data):
    '''
        Возвращает произведение десятичной константы и числа с плавающей точкой в десятичной системе счисления.

            Параметры:
                a (float) : число с плавающей точкой в десятичной системе счисления

                Возвращаемое значение:
                (4 * a) (float) : число с плавающей точкой в десятичной системе счисления

                Пример вызова функции:
                    perimeter(196) = 784.0
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
        a = data[0]

    # обработка и выдача результатов
    if is_digit(str(a)):
        a = float(a)
        if a < 0:
            return 'Значение элемента геометрической фигуры не может быть отрицательным, введите корректные данные.'
        elif a == 1.7976931348623157e+308:
            return 'Ошибка: Переполнение в результате выполнения арифметической операции.'
        else:
            return 4 * a
    else:
        return 'Входные данные являются строковыми значениями, а не численными. Попробуйте еще раз и введите корректные данные.'

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area([0])
        self.assertEqual(res, 0)

    def test_area_mul(self):
        res = area([542])
        self.assertEqual(res, 293764)

    def test_perimeter_mul(self):
        res = perimeter([78358252])
        self.assertEqual(res, 313433008)

    def test_perimeter_negative(self):
        res = perimeter([-8329])
        self.assertEqual(res, 'Значение элемента геометрической фигуры не может быть отрицательным, введите корректные данные.')

    def test_area_negative(self):
        res = area([-18.301])
        self.assertEqual(res, 'Значение элемента геометрической фигуры не может быть отрицательным, введите корректные данные.')

    def test_perimeter_inf(self):
        res = perimeter([1.7976931348623157e+308])
        self.assertEqual(res, 'Ошибка: Переполнение в результате выполнения арифметической операции.')

    def test_area_inf(self):
        res = area([1.7976931348623157e+308])
        self.assertEqual(res, 'Ошибка: Переполнение в результате выполнения арифметической операции.')

    def test_perimeter_str(self):
        res = perimeter(['bibaboba'])
        self.assertEqual(res, 'Входные данные являются строковыми значениями, а не численными. Попробуйте еще раз и введите корректные данные.')

    def test_area_str(self):
        res = area(['bambam'])
        self.assertEqual(res, 'Входные данные являются строковыми значениями, а не численными. Попробуйте еще раз и введите корректные данные.')

    def test_perimeter_value(self):
        res = perimeter([10, 62819])
        self.assertEqual(res, 'Перечитайте условие и введите необходимое количество входных данных.')

    def test_area_value(self):
        res = area([5932, 3, 1, 6, 9])
        self.assertEqual(res, 'Перечитайте условие и введите необходимое количество входных данных.')