import unittest
from rectangle import area, perimeter
class RectangleTestCase(unittest.TestCase):

    def test_area(self):
        # Проверка площади прямоугольника
        a = 5
        b = 10
        expected_area = a * b
        actual_area = area(a, b)
        self.assertEqual(actual_area, expected_area)

    def test_perimeter(self):
        # Проверка периметра прямоугольника
        a = 5
        b = 10
        expected_perimeter = (a + b) * 2
        actual_perimeter = perimeter(a, b)
        self.assertEqual(actual_perimeter, expected_perimeter)

if __name__ == '__main__':
    unittest.main()