import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):

    def test_area(self):
        # Проверка площади круга
        r = 5
        expected_area = math.pi * r * r
        actual_area = area(r)
        self.assertEqual(actual_area, expected_area)

    def test_perimeter(self):
        # Проверка периметра круга
        r = 5
        expected_perimeter = 2 * math.pi * r
        actual_perimeter = perimeter(r)
        self.assertEqual(actual_perimeter, expected_perimeter)


if __name__ == '__main__':
    unittest.main()
