import unittest

def area(a):
    return a * a


def perimeter(a):
    return 4 * a

class SquareTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(5), 25)
        self.assertEqual(area(10), 100)
        self.assertEqual(area(0), 0)
        
    def test_perimeter(self):
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(10), 40)
        self.assertEqual(perimeter(0), 0)
