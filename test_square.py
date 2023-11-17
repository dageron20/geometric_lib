import unittest
from square import area, perimeter 
class SquareTestCase(unittest.TestCase):

    def test_area(self):
        # Проверка площади квадрата
        a = 5
        expected_area = a * a
        actual_area = area(a)
        self.assertEqual(actual_area, expected_area)

    def test_perimeter(self):
        # Проверка периметра квадрата
        a = 5
        expected_perimeter = 4 * a
        actual_perimeter = perimeter(a)
        self.assertEqual(actual_perimeter, expected_perimeter)

if __name__ == '__main__':
    unittest.main()