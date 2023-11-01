import unittest
import square


class SquareTest(unittest.TestCase):
    """unit test, который проверяет правильность работы функции для вычисления площади квадрата на диапазоне
        сторон от 0 до 100"""
    def test_area_mul(self):
        for i in range(0, 100):
            res = square.area(i)
            self.assertEqual(res, i * i)

    """unit test, который проверяет правильность работы функции для вычисления периметра квадрата на диапазоне
            сторон от 0 до 100"""
    def test_perimeter_mul(self):
        for i in range(0, 100):
            res = square.perimeter(i)
            self.assertEqual(res, 4 * i)


if __name__ == '__main__':
    unittest.main()