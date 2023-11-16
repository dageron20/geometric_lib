import unittest
import triangle

class TriangleTestCase(unittest.TestCase):
    """тестирование функции area в случае, когда оба числа положительные"""
    def test_area_both_positive(self):
        a = 7
        h = 12
        expected_result = 42
        received_result = triangle.area(a, h)
        self.assertEqual(expected_result, received_result)
    """тестирование функции area в случае, когда оба числа отрицательные"""
    def test_area_both_negative(self):
        a = -4
        h = -32
        expected_result = 0
        received_result = triangle.area(a, h)
        self.assertEqual(expected_result, received_result)
    """тестирование функции area в случае, когда одно число положительное а другое отрицательное"""
    def test_area_negative_and_positive(self):
        a = -87
        h = 6
        expected_result = 0
        received_result = triangle.area(a, h)
        self.assertEqual(expected_result, received_result)
    """тестирование функции perimeter в случае, когда три числа положительные"""
    def test_perimeter_both_positive(self):
        a = 4
        b = 5
        c = 9
        expected_result = 18
        received_result = triangle.perimeter(a, b, c)
        self.assertEqual(expected_result, received_result)
    """тестирование функции perimeter в случае, когда три числа отрицательные"""
    def test_perimeter_both_negative(self):
        a = -3
        b = -7
        c = -9
        expected_result = 0
        received_result = triangle.perimeter(a, b, c)
        self.assertEqual(expected_result, received_result)
    """тестирование функции perimeter в случае, когда одно число положительное и два отрицательных"""
    def test_perimeter_negative_and_positive(self):
        a = -5
        b = 46
        c = -3
        expected_result = 0
        received_result = triangle.perimeter(a, b, c)
        self.assertEqual(expected_result, received_result)