import unittest
import square

class SquareTestCase(unittest.TestCase):
    """тестирование функции area в случае, когда сторона квадрата является положительным числом"""
    def test_area_positive_side(self):
        a = 6
        expected_result = 36
        received_result = square.area(a)
        self.assertEqual(expected_result, received_result)
    """тестирование функции area в случае, когда сторона квадрата равна нулю"""
    def test_area_zero_side(self):
        a = 0
        expected_result = 0
        received_result = square.area(a)
        self.assertEqual(expected_result, received_result)
    """тестирование функции area в случае, когда сторона квадрата является отрицательным числом"""
    def test_area_negative_side(self):
        a = -5
        expected_result = 0
        received_result = square.area(a)
        self.assertEqual(expected_result, received_result)
    """тестирование функции perimeter в случае, когда сторона квадрата является положительным числом"""
    def test_perimeter_positive_side(self):
        a = 6
        expected_result = 24
        received_result = square.perimeter(a)
        self.assertEqual(expected_result, received_result)
    """тестирование функции perimeter в случае, когда сторона квадрата равна нулю"""
    def test_perimeter_zero_side(self):
        a = 0
        expected_result = 0
        received_result = square.perimeter(a)
        self.assertEqual(expected_result, received_result)
    """тестирование функции perimeter в случае, когда сторона квадрата является отрицательным числом"""
    def test_perimeter_negative_side(self):
        a = -5
        expected_result = 0
        received_result = square.perimeter(a)
        self.assertEqual(expected_result, received_result)
        