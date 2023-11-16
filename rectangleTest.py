import unittest
import rectangle

class RectangleTestCase(unittest.TestCase):
    """тестирование функции area в случае, когда оба числа положительные"""
    def test_area_both_positive(self):
        a = 4
        b = 5
        expected_result = 20
        received_result = rectangle.area(a, b)
        self.assertEqual(expected_result, received_result)
    """тестирование функции area в случае, когда оба числа отрицательные"""
    def test_area_both_negative(self):
        a = -3
        b = -7
        expected_result = 0
        received_result = rectangle.area(a, b)
        self.assertEqual(expected_result, received_result)
    """тестирование функции area в случае, когда одно число положительное а другое отрицательное"""
    def test_area_negative_and_positive(self):
        a = -5
        b = 6
        expected_result = 0
        received_result = rectangle.area(a, b)
        self.assertEqual(expected_result, received_result)
    """тестирование функции perimeter в случае, когда оба числа положительные"""
    def test_perimeter_both_positive(self):
        a = 4
        b = 5
        expected_result = 18
        received_result = rectangle.perimeter(a, b)
        self.assertEqual(expected_result, received_result)
    """тестирование функции perimeter в случае, когда оба числа отрицательные"""
    def test_perimeter_both_negative(self):
        a = -3
        b = -7
        expected_result = 0
        received_result = rectangle.perimeter(a, b)
        self.assertEqual(expected_result, received_result)
    """тестирование функции perimeter в случае, когда одно число положительное а другое отрицательное"""
    def test_perimeter_negative_and_positive(self):
        a = -5
        b = 6
        expected_result = 0
        received_result = rectangle.perimeter(a, b)
        self.assertEqual(expected_result, received_result)