import unittest
import circle
import rectangle
import square
import triangle

class unitTests(unittest.TestCase):
    def test_circle_right(self):
        self.assertEqual(circle.area(
