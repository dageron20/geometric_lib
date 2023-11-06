import unittest

from math import inf


def area(data):
    '''
    Возвращает произведение двух чисел с плавающей точкой в десятичной системе счисления.

        Параметры:
            data (str) : массив входных данных (числа с плавающей точкой в десятичной системе счисления)

            Возвращаемое значение:
            (data[0] * data[1]) (float) : число с плавающей точкой в десятичной системе счисления

                Пример вызова функции:
                    area([27.1, 18.9]) = 512.1899999999999
    '''
    def is_digit(a):
        length = len(str(a))
        for i in range(0, length):
            if (not (a[i].isdigit())) and (a[i] != "e") and (a[i] != ".") and (a[i] != "+") and (a[i] != "-"):
                return False
        return True

    if len(data) != 2:
        return 'Перечитайте условие и введите необходимое количество входных данных.'
    else:
        a, b = data

    # обработка и выдача результатов
    if is_digit(str(a)) and is_digit(str(b)):
        a = float(a)
        b = float(b)
        if a < 0 or b < 0:
            return 'Значение элемента геометрической фигуры не может быть отрицательным, введите корректные данные.'
        elif a == 1.7976931348623157e+308 or b == 1.7976931348623157e+308:
            return 'Ошибка: Переполнение в результате выполнения арифметической операции.'
        else:
            return a * b
    else:
        return 'Входные данные являются строковыми значениями, а не численными. Попробуйте еще раз и введите корректные данные.'



def perimeter(data):
    '''
        Возвращает произведение десятичной константы и суммы двух чисел с плавающей точкой в десятичной системе счисления.

            Параметры:
                data (str) : массив входных данных (числа с плавающей точкой в десятичной системе счисления)

                Возвращаемое значение:
                (2 * (data[0] + data[1])) (float) : число с плавающей точкой в десятичной системе счисления

                    Пример вызова функции:
                        perimeter([27.1, 18.9]) = 92.0
    '''
    def is_digit(a):
        length = len(str(a))
        for i in range(0, length):
            if (not (a[i].isdigit())) and (a[i] != "e") and (a[i] != ".") and (a[i] != "+") and (a[i] != "-"):
                return False
        return True

    if len(data) != 2:
        return 'Перечитайте условие и введите необходимое количество входных данных.'
    else:
        a, b = data

    # обработка и выдача результатов
    if is_digit(str(a)) and is_digit(str(b)):
        a = float(a)
        b = float(b)
        if a < 0 or b < 0:
            return 'Значение элемента геометрической фигуры не может быть отрицательным, введите корректные данные.'
        elif a == 1.7976931348623157e+308 or b == 1.7976931348623157e+308:
            return 'Ошибка: Переполнение в результате выполнения арифметической операции.'
        else:
            return 2 * (a + b)
    else:
        return 'Входные данные являются строковыми значениями, а не численными. Попробуйте еще раз и введите корректные данные.'


class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area([0, 9])
        self.assertEqual(res, 0)

    def test_area_mul(self):
        res = area([613, 463])
        self.assertEqual(res, 283819)

    def test_perimeter_mul(self):
        res = perimeter([1983, 8348292])
        self.assertEqual(res, 16700550)

    def test_perimeter_negative(self):
        res = perimeter([-8329, 7929])
        self.assertEqual(res, 'Значение элемента геометрической фигуры не может быть отрицательным, введите корректные данные.')

    def test_area_negative(self):
        res = area([-18.301, 0])
        self.assertEqual(res, 'Значение элемента геометрической фигуры не может быть отрицательным, введите корректные данные.')

    def test_perimeter_inf(self):
        res = perimeter([1.7976931348623157e+308, 1])
        self.assertEqual(res, 'Ошибка: Переполнение в результате выполнения арифметической операции.')

    def test_area_inf(self):
        res = area([9, 1.7976931348623157e+308])
        self.assertEqual(res, 'Ошибка: Переполнение в результате выполнения арифметической операции.')

    def test_perimeter_str(self):
        res = perimeter(['bibaboba', 'www'])
        self.assertEqual(res, 'Входные данные являются строковыми значениями, а не численными. Попробуйте еще раз и введите корректные данные.')

    def test_area_str(self):
        res = area(['bambam', 373021])
        self.assertEqual(res, 'Входные данные являются строковыми значениями, а не численными. Попробуйте еще раз и введите корректные данные.')

    def test_perimeter_value(self):
        res = perimeter([10, 62819, 1])
        self.assertEqual(res, 'Перечитайте условие и введите необходимое количество входных данных.')

    def test_area_value(self):
        res = area([5932])
        self.assertEqual(res, 'Перечитайте условие и введите необходимое количество входных данных.')