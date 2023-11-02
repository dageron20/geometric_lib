import unittest
from triangle import area, perimeter


class TestTriangle(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(5, 2), (5 * 2) / 2)
        self.assertEqual(area(10 ** 6, 876589), ((10 ** 6) * 876589) / 2)
        self.assertEqual(area(97537437, 4), (97537437 * 4) / 2)
        self.assertEqual(area(99 ** 3, 10 ** 6), (((99 ** 3) * (10 ** 6)) / 2))
        self.assertEqual(area(99999, 10 ** 5), (99999 * (10 ** 5)) / 2)
        self.assertEqual(area(0.111111, 0.480238847539), (0.111111 * 0.480238847539) / 2)
        self.assertEqual(area(0.1245387537, 1035678.1029473756), (0.1245387537 * 1035678.1029473756) / 2)
        self.assertEqual(area(10 ** 6, 0.12874832558746378), (0.12874832558746378 * (10 ** 6)) / 2)
        self.assertEqual(area(184.01, 0.99), (184.01 * 0.99) / 2)
        self.assertEqual(area(0.0000000000000015457846, 10 ** 6), (0.0000000000000015457846 * (10 ** 6)) / 2)
        self.assertEqual(area('a', 2), 'Не корректные входные данные')
        self.assertEqual(area(0, 2), 'Не корректные входные данные')
        self.assertEqual(area(-100, 2), 'Не корректные входные данные')
        self.assertEqual(area(0.0, 2), 'Не корректные входные данные')
        self.assertEqual(area(-0.0, 2), 'Не корректные входные данные')

    def test_perimetr(self):
        self.assertEqual(perimeter(5, 2, 3), 5 + 2 + 3)
        self.assertEqual(perimeter(10 ** 6, 106, 3 * (10 ** 6)), 106 + (10 ** 6) + (3 * (10 ** 6)))
        self.assertEqual(perimeter(95674, 10 ** 6, 25688), 25688 + (10 ** 6) + 95674)
        self.assertEqual(perimeter(10 ** 6, 10 ** 3, 10 ** 5), (10 ** 3) + (10 ** 6) + (10 ** 5))
        self.assertEqual(perimeter(9999999999, 9999999999, 9999999999), 9999999999 + 9999999999 + 9999999999)
        self.assertEqual(perimeter(0.7456478254974, 0.197464836452, 0.03), 0.7456478254974 + 0.197464836452 + 0.03)
        self.assertEqual(perimeter(0.0000000000000001, 0.0000000000013245, 0.12345),
                         0.0000000000000001 + 0.0000000000013245 + 0.12345)
        self.assertEqual(perimeter(0.9, 0.13, 1.325), 0.9 + 0.13 + 1.325)
        self.assertEqual(perimeter(126356.000001, 1000000.35624, 0.2145673568),
                         126356.000001 + 1000000.35624 + 0.2145673568)
        self.assertEqual(perimeter(99999999.99999999, 0.111111111111, 9314521),
                         99999999.99999999 + 0.111111111111 + 9314521)
        self.assertEqual(perimeter(0, 5, 5), 'Не корректные входные данные')
        self.assertEqual(perimeter(1, 'a', 5), 'Не корректные входные данные')
        self.assertEqual(perimeter(0.000, 'ab', 5), 'Не корректные входные данные')
        self.assertEqual(perimeter(-0, 5, 5), 'Не корректные входные данные')
        self.assertEqual(perimeter(-10000, 5, 5), 'Не корректные входные данные')
