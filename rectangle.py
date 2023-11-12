import unittest

def area(a, b): 
    """
     Вычисляет площадь прямоугольник
     
     Параметр a - Сторона прямоугольника 1
     Параметр b - Сторона прямоугольника 1
     
     Возвращает площадь прямоугольника
    """
    return a * b 

def perimeter(a, b): 
    """
     Вычисляет периметр прямоугольник
     
     Параметр a - Сторона прямоугольника 1
     Параметр b - Сторона прямоугольника 1
     
     Возвращает периметр прямоугольника
    """
    return (a + b )*2


class RectangleTestCase(unittest.TestCase):
   """
    Класс для тестирования функций расчета площади и периметра прямоугольника.

    Методы класса тестируют функции area и perimeter на соответствие математическим
    расчетам для различных входных значений.
    """
   
   def test_zero_mul(self):
       """
        Тестирование функции area с нулевой стороной.

        Проверяет, что площадь прямоугольника с одной стороной 0 равна 0.
        """
       res = area(10, 0)
       self.assertEqual(res, 0)
       
   def test_square_mul(self):
        """
        Тестирование функции area.

        Проверяет, что функция верно вычисляет площадь прямоугольника.
        В данном тесте используется радиус 10. 
        Ожидаемый результат - площадь прямоугольника, равная 100.
        """
        res = area(10, 10)
        self.assertEqual(res, 100)

   def test_zero_perimeter(self):
       """
        Тестирование функции perimeter с нулевыми сторонами.

        Проверяет результат при периметра при нулевых значениях сторон.
        """
       res = perimeter(0, 0)
       self.assertEqual(res, 0)
       
   def test_square_perimeter(self):
        """
        Тестирование функции perimeter.

        Проверяет, что функция верно вычисляет периметр прямоугольника.
        В данном тесте используются стороны 10 и 20. 
        Ожидаемый результат - периметр прямоугольника, равный 60.
        """
        res = perimeter(10, 20)
        self.assertEqual(res, 60)
