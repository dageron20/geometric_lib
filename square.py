import unittest

def area(a):
    """
     Вычисляет площадь квадрата
     
     Параметр a - Сторона квадрата
     
     Возвращает площадь 
    """
    return a * a


def perimeter(a):
    """
     Вычисляет периметр квадрата
     
     Параметр a - Сторона квадрата
     
     Возвращает периметр квадрата
    """
    return 4 * a

class SquareCalculationsTestCase(unittest.TestCase):
    """
    Класс для тестирования функций расчета площади и периметра квадрата.

    Методы класса тестируют функции area и perimeter на соответствие математическим
    расчетам для различных входных значений.
    """

    def test_area(self):
        """
        Тестирование функции area.

        Проверяет, что функция верно вычисляет площадь прямоугольника.
        В данном тесте используется сторона 10. 
        Ожидаемый результат - площадь квадрата, равная 100.
        """

        self.assertEqual(area(10), 100)

    def test_area_zero(self):
        """
        Тестирование функции area с нулевой стороной.

        Проверяет, что площадь квадрата со сторонами 0 равна 0.
        """
        self.assertEqual(area(0), 0)

    def test_perimeter(self):
        """
        Тестирование функции perimeter.

        Проверяет, что функция верно вычисляет периметр квадрата.
        В данном тесте используются стороны 10. 
        Ожидаемый результат - периметр квадрата, равный 40.
        """
        self.assertEqual(perimeter(10), 40)

    def test_perimeter_zero(self):
        """
        Тестирование функции perimeter с нулевыми сторонами.

        Проверяет, что результат периметра при нулевых значениях сторон равен 0.
        """
        self.assertEqual(perimeter(0), 0)
    
    def test_area_negative(self):
        """
        Тестирование функции area с отрицательной стороной.
        Ожидаемый результат - ошибка.
        """
        with self.assertRaises(ValueError):
            area(-10)

    def test_perimeter_negative(self):
        """
        Тестирование функции perimeter с отрицательной стороной.
        Ожидаемый результат - ошибка.
        """
        with self.assertRaises(ValueError):
            perimeter(-10)

    def test_area_string(self):
        """
        Тестирование функции area со строковой стороной.
        Ожидаемый результат - ошибка.
        """
        with self.assertRaises(TypeError):
            area("10")

    def test_perimeter_string(self):
        """
        Тестирование функции perimeter со строковой стороной.
        Ожидаемый результат - ошибка.
        """
        with self.assertRaises(TypeError):
            perimeter("10")

    def test_area_boolean(self):
        """
        Тестирование функции area с булевой стороной.
        Ожидаемый результат - ошибка.
        """
        with self.assertRaises(TypeError):
            area(True)

    def test_perimeter_boolean(self):
        """
        Тестирование функции perimeter с булевой стороной.
        Ожидаемый результат - ошибка.
        """
        with self.assertRaises(TypeError):
            perimeter(False)
