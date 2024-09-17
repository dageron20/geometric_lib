import unittest
from circle import area, perimeter
from math import pi


class TestCircle(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(3), pi * (3 * 3))
        self.assertEqual(area(100), pi * (100 * 100))
        self.assertEqual(area(10 ** 5), pi * (10 ** 5) * (10 ** 5))
        self.assertEqual(area(10 ** 6), pi * (10 ** 6) * (10 ** 6))
        self.assertEqual(area(9999999), pi * (9999999 * 9999999))
        self.assertEqual(area(1.2), pi * (1.2 * 1.2))
        self.assertEqual(area(100.0), pi * (100.0 * 100.0))
        self.assertEqual(area(250.9999999), pi * (250.9999999 * 250.9999999))
        self.assertEqual(area(1000000.666666), pi * (1000000.666666 * 1000000.666666))
        self.assertEqual(area(0.98765), pi * (0.98765 * 0.98765))
        self.assertEqual(area(-10), 'Не корректные входные данные')
        self.assertEqual(area('a'), 'Не корректные входные данные')
        self.assertEqual(area(0.), 'Не корректные входные данные')
        self.assertEqual(area(0), 'Не корректные входные данные')

    def test_perimetr(self):
        self.assertEqual(perimeter(1), pi * 1 * 2)
        self.assertEqual(perimeter(100), pi * 100 * 2)
        self.assertEqual(perimeter(99 ** 4), pi * (99 ** 4) * 2)
        self.assertEqual(perimeter(10 ** 6), pi * (10 ** 6) * 2)
        self.assertEqual(perimeter(9876543), pi * 9876543 * 2)
        self.assertEqual(perimeter(0.9299399), pi * 0.9299399 * 2)
        self.assertEqual(perimeter(186746.9299399), pi * 186746.9299399 * 2)
        self.assertEqual(perimeter(100.01), pi * 100.01 * 2)
        self.assertEqual(perimeter(10000000.986), pi * 10000000.986 * 2)
        self.assertEqual(area(-10), 'Не корректные входные данные')
        self.assertEqual(area('a'), 'Не корректные входные данные')
        self.assertEqual(area(0.), 'Не корректные входные данные')
        self.assertEqual(area(0), 'Не корректные входные данные')
