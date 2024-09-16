import math
import unittest

def area(r):
    """
     Расчет площади круга.
     
     Параметр r - Радиус круга
     
     Возвращает площадь круга
    """
    return math.pi * r * r


def perimeter(r):
    """
     Вычисляет периметр круга.
     
     Параметр r - Радиус круга
     
    Возвращает периметр круга
    """
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    """
    Класс для тестирования функций расчета площади и периметра круга.

    Методы класса тестируют функции area и perimeter на соответствие математическим
    расчетам для различных входных значений.
    """

    def test_area_zero(self):
        """
        Тестирование функции area с нулевым радиусом.

        Проверяет, что площадь круга с радиусом 0 равна 0.
        """
        self.assertEqual(area(0), 0)

    def test_area(self):
        """
        Тестирование функции area.

        Проверяет, что функция верно вычисляет площадь круга.
        В данном тесте используется радиус 10. 
        Ожидаемый результат - площадь круга, равная pi * 100.
        """
        self.assertAlmostEqual(area(10), math.pi * 100)

    def test_perimeter_zero(self):
        """
        Тестирование функции perimeter с нулевым радиусом.

        Проверяет, что периметр круга с радиусом 0 равен 0.
        """
        self.assertEqual(perimeter(0), 0)

    def test_perimeter(self):
        """
        Тестирование функции perimeter с положительным радиусом.

        Проверяет, что функция верно вычисляет периметр круга.
        В данном тесте используется радиус 10.
        Ожидаемый результат - периметр круга, равный 2 * pi * 10.
        """
        self.assertAlmostEqual(perimeter(10), 2 * math.pi * 10)


    def test_area_negative(self):
        """
        Тестирование функции area при отрицательном радиусе.
        Ожидаемый результат - ошибка.
        """
        with self.assertRaises(ValueError):
            area(-5)

    def test_perimeter_negative(self):
        """
        Тестирование функции perimeter при отрицательном радиусе.
        Ожидаемый результат - ошибка.
        """
        with self.assertRaises(ValueError):
            perimeter(-5)

    def test_area_string(self):
        """
        Тестирование функции area со строковым радиусом.
        Ожидаемый результат - ошибка.
        """
        with self.assertRaises(TypeError):
            area("10")

    def test_perimeter_string(self):
        """
        Тестирование функции perimeter со строковым радиусом.
        Ожидаемый результат - ошибка.
        """
        with self.assertRaises(TypeError):
            perimeter("10")

    def test_area_boolean(self):
        """
        Тестирование функции area с булевым радиусом.
        Ожидаемый результат - ошибка.
        """
        with self.assertRaises(TypeError):
            area(True)

    def test_perimeter_boolean(self):
        """
        Тестирование функции perimeter с булевым радиусом.
        Ожидаемый результат - ошибка.
        """
        with self.assertRaises(TypeError):
            perimeter(False)
