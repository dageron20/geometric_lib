import unittest
import rectangle


class RectangleTest(unittest.TestCase):
    """unit test, который проверяет правильность работы функции для вычисления площади прямоугольника на диапазоне
    сторон от 0 до 100"""

    def test_area_mul(self):
        for i in range(0, 100):
            for j in range(0, 100):
                res = rectangle.area(i, j)
                self.assertEqual(res, i * j)

    """unit test, который проверяет правильность работы функции для вычисления периметра прямоугольника на диапазоне 
    сторон от 0 до 100"""

    def test_perimeter_mul(self):

        for i in range(0, 100):
            for j in range(0, 100):
                res = rectangle.perimeter(i, j)
                """Предсумотрен случай, когда одна из сторон равна 0, значит, фигура в принципе не существует и ответом
                будет 0"""
                if i == 0 or j == 0:
                    self.assertEqual(res, 0)
                else:
                    self.assertEqual(res, 2 * (i + j))


if __name__ == '__main__':
    unittest.main()
