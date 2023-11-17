import unittest
from triangle import area, perimeter 
class TriangleTestCase(unittest.TestCase):

    def test_area(self):
        # Проверка площади треугольника
        a = 5
        h = 10
        expected_area = a * h / 2
        actual_area = area(a, h)
        self.assertEqual(actual_area, expected_area)

    def test_perimeter(self):
        # Проверка периметра треугольника
        a = 3
        b = 4
        c = 5
        expected_perimeter = a + b + c
        actual_perimeter = perimeter(a, b, c)
        self.assertEqual(actual_perimeter, expected_perimeter)

if __name__ == '__main__':
    unittest.main()