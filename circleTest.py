import unittest
import circle
import math

class CircleTestCase(unittest.TestCase):
    """тестирование функции area в случае, когда радиус является положительным числом"""
    def test_area_positive_radius(self):
        r = 5
        expected_result = math.pi * 25
        received_result = circle.area(r)
        self.assertEqual(expected_result, received_result)
    """тестирование функции area в случае, когда радиус равен нулю"""
    def test_area_zero_radius(self):
        r = 0
        expected_result = 0
        received_result = circle.area(r)
        self.assertEqual(expected_result, received_result)
    """тестирование функции area в случае, когда радиус является отрицательным числом"""
    def test_area_negative_radius(self):
        r = -5
        expected_result = 0
        received_result = circle.area(r)
        self.assertEqual(expected_result, received_result)
    """тестирование функции perimeter в случае, когда радиус является положительным числом"""
    def test_perimeter_positive_radius(self):
        r = 5
        expected_result = 2 * math.pi * 5
        received_result = circle.perimeter(r)
        self.assertEqual(expected_result, received_result)
    """тестирование функции perimeter в случае, когда радиус равен нулю"""
    def test_perimeter_zero_radius(self):
        r = 0
        expected_result = 0
        received_result = circle.perimeter(r)
        self.assertEqual(expected_result, received_result)
    """тестирование функции perimeter в случае, когда радиус является отрицательным числом"""
    def test_perimeter_negative_radius(self):
        r = -5
        expected_result = 0
        received_result = circle.perimeter(r)
        self.assertEqual(expected_result, received_result)