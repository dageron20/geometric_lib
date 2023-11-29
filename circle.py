import math

def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r

import unittest

class Test_Functions_Circle(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(-1), math.pi)
        self.assertEqual(area(0), 0)
        self.assertAlmostEqual(area(2.5), 5 * math.pi)

    def test_perimeter(self):
        self.assertEqual(perimeter(1), 2 *  math.pi)
        self.assertEqual(perimeter(0), 0)
        self.assertAlmostEqual(perimeter(-2), -4 * math.pi)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            area('a')
            perimeter('b')

if __name__ == '__main__':
    unittest.main()