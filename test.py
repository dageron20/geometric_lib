import rectangle
import circle
import triangle
import square
import unittest


class TestRectangle(unittest.TestCase):
    def test_rectangle_area(self):
        rect = rectangle.Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)
        rect = rectangle.Rectangle(6, 7)
        self.assertEqual(rect.area(), 42)

    def test_rectangle_perimeter(self):
        rect = rectangle.Rectangle(5, 10)
        self.assertEqual(rect.perimeter(), 30)
        rect = rectangle.Rectangle(3, 14)
        self.assertEqual(rect.perimeter(), 34)


class TestTriangle(unittest.TestCase):
    def test_triangle_area(self):
        tri = triangle.Triangle(6, 8, 5, 7, 9)
        self.assertEqual(tri.area(), 24.0)
        tri = triangle.Triangle(10, 6, 5, 7, 9)
        self.assertEqual(tri.area(), 30.0)

    def test_triangle_perimeter(self):
        tri = triangle.Triangle(5, 9, 6, 7, 8)
        self.assertEqual(tri.perimeter(), 21)
        tri = triangle.Triangle(10, 6, 10, 11, 12)
        self.assertEqual(tri.perimeter(), 33)


class TestCircle(unittest.TestCase):
    def test_circle_area(self):
        circ = circle.Circle(3)
        self.assertAlmostEqual(circ.area(), 28.274333882308138, places=5)
        circ = circle.Circle(5)
        self.assertAlmostEqual(circ.area(), 78.5398162, places=4)

    def test_circle_perimeter(self):
        circ = circle.Circle(3)
        self.assertAlmostEqual(circ.perimeter(), 18.84955592153876, places=5)
        circ = circle.Circle(5)
        self.assertAlmostEqual(circ.perimeter(), 31.4159265, places=4)


class TestSquare(unittest.TestCase):
    def test_square_area(self):
        sq = square.Square(4)
        self.assertEqual(sq.area(), 16)
        sq = square.Square(3)
        self.assertEqual(sq.area(), 9)

    def test_square_perimeter(self):
        sq = square.Square(4)
        self.assertEqual(sq.perimeter(), 16)
        sq = square.Square(3)
        self.assertEqual(sq.perimeter(), 12)


if __name__ == '__main__':
    unittest.main()
