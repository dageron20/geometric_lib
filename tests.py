import math
import triangle
import rectangle
import circle
import square
import unittest

class TestCases(unittest.TestCase):

    # Тесты, проверяющие корректность вычисления площади прямоугольника.

    def test_positive_rec_area(self):
        self.assertEqual(rectangle.area(5, 5), 25)
        self.assertEqual(rectangle.area(20, 4), 80)
        self.assertEqual(rectangle.area(4, 20), 80)


    def test_non_positive_rec_area(self):
        self.assertEqual(rectangle.area(0, 0), "Invalid input")
        self.assertEqual(rectangle.area(-1, 4), "Invalid input")
        self.assertEqual(rectangle.area(4, -1), "Invalid input")
        self.assertEqual(rectangle.area(-2, 0), "Invalid input")
        self.assertEqual(rectangle.area(0, -2), "Invalid input")
        self.assertEqual(rectangle.area(-1, -10), "Invalid input")

    def test_string_rec_area(self):
        self.assertEqual(rectangle.area("A", 20), "Invalid input")
        self.assertEqual(rectangle.area(20, "A"), "Invalid input")

    def test_bool_rec_area(self):
        self.assertEqual(rectangle.area(True, 4), "Invalid input")
        self.assertEqual(rectangle.area(4, True), "Invalid input")
        self.assertEqual(rectangle.area(False, 4), "Invalid input")
        self.assertEqual(rectangle.area(4, False), "Invalid input")

    # Тесты, проверяющие корректность вычисления периметра прямоугольника.

    def test_positive_rec_perimeter(self):
        self.assertEqual(rectangle.perimeter(5,5), 20)
        self.assertEqual(rectangle.perimeter(2, 5), 14)
        self.assertEqual(rectangle.perimeter(5, 2), 14)

    def test_non_positive_rec_perimeter(self):
        self.assertEqual(rectangle.perimeter(0, 10), "Invalid input")
        self.assertEqual(rectangle.perimeter(0, 0), "Invalid input")
        self.assertEqual(rectangle.perimeter(-1, -2), "Invalid input")
        self.assertEqual(rectangle.perimeter(-1, 0), "Invalid input")
        self.assertEqual(rectangle.perimeter(10, 0), "Invalid input")
        self.assertEqual(rectangle.perimeter(0, -1), "Invalid input")

    def test_string_rec_perimeter(self):
        self.assertEqual(rectangle.perimeter("b", 1), "Invalid input")
        self.assertEqual(rectangle.perimeter(3, "A"), "Invalid input")

    def test_bool_rec_perimeter(self):
        self.assertEqual(rectangle.perimeter(True, 7), "Invalid input")
        self.assertEqual(rectangle.perimeter(9, True), "Invalid input")
        self.assertEqual(rectangle.perimeter(False, 1), "Invalid input")
        self.assertEqual(rectangle.perimeter(2, False), "Invalid input")

    # Тесты, проверяющие корректность вычисления площади треугольника.

    def test_positive_triangle_area(self):
        self.assertEqual(triangle.area(20, 4), 40)
        self.assertEqual(triangle.area(4, 20), 40)

    def test_non_positive_triangle_area(self):
        self.assertEqual(triangle.area(0, 0), "Invalid input")
        self.assertEqual(triangle.area(-1, 0), "Invalid input")
        self.assertEqual(triangle.area(0, -1), "Invalid input")
        self.assertEqual(triangle.area(-1, -1), "Invalid input")
        self.assertEqual(triangle.area(1, 0), "Invalid input")
        self.assertEqual(triangle.area(0, 1), "Invalid input")

    def test_string_triangle_area(self):
        self.assertEqual(triangle.area("c", 9), "Invalid input")
        self.assertEqual(triangle.area(10, "E"), "Invalid input")

    def test_bool_triangle_area(self):
        self.assertEqual(triangle.area(True, 107), "Invalid input")
        self.assertEqual(triangle.area(9, True), "Invalid input")
        self.assertEqual(triangle.area(False, 5), "Invalid input")
        self.assertEqual(triangle.area(3, False), "Invalid input")

    # Тесты, проверяющие корректность вычисления периметра треугольника.

    def test_positive_triangle_perimeter(self):
        self.assertEqual(triangle.perimeter(7, 7, 7), 21)
        self.assertEqual(triangle.perimeter(3, 5, 7), 15)

    def test_non_positive_triangle_perimeter(self):
        self.assertEqual(triangle.perimeter(-1, -1, -1), "Invalid input")
        self.assertEqual(triangle.perimeter(5, 5, -1), "Invalid input")
        self.assertEqual(triangle.perimeter(5, -1, 5), "Invalid input")
        self.assertEqual(triangle.perimeter(-1, 5, 5), "Invalid input")
        self.assertEqual(triangle.perimeter(0, 7, 7), "Invalid input")
        self.assertEqual(triangle.perimeter(7, 7, 0), "Invalid input")
        self.assertEqual(triangle.perimeter(7, 0, 7), "Invalid input")

    def test_string_triangle_perimeter(self):
        self.assertEqual(triangle.perimeter(7, 7, "C"), "Invalid input")
        self.assertEqual(triangle.perimeter("ABCDEF", 7, 3), "Invalid input")
        self.assertEqual(triangle.perimeter(7, 'm', "C"), "Invalid input")

    def test_bool_triangle_perimter(self):
        self.assertEqual(triangle.perimeter(True, 7, 7), "Invalid input")
        self.assertEqual(triangle.perimeter(7, False, 7), "Invalid input")
        self.assertEqual(triangle.perimeter(7, False, True), "Invalid input")

    # Тесты, проверяющие существование данного треугольника

    def test_nonexistent_triangles(self):
        self.assertEqual(triangle.perimeter(1, 1, 5), "Nonexistent figure")
        self.assertEqual(triangle.perimeter(2, 20, 10), "Nonexistent figure")
        self.assertEqual(triangle.perimeter(15, 3, 7), "Nonexistent figure")

    # Тесты, проверяющие корректность вычисления площади окружности.

    def test_positive_circle_area(self):
        self.assertEqual(circle.area(3), math.pi * 9)
        self.assertEqual(circle.area(1), math.pi)

    def test_non_positive_circle_area(self):
        self.assertEqual(circle.area(-1), "Invalid input")
        self.assertEqual(circle.area(0), "Invalid input")

    def test_bool_circle_area(self):
        self.assertEqual(circle.area(True), "Invalid input")
        self.assertEqual(circle.area(False), "Invalid input")

    def test_string_circle_area(self):
        self.assertEqual(circle.area("No"), "Invalid input")

    # Тесты, проверяющие корректность вычисления длины окружности.

    def test_positive_circle_circumference(self):
        self.assertEqual(circle.perimeter(7), math.pi * 14)
        self.assertEqual(circle.perimeter(1), math.pi * 2)

    def test_non_positive_circle_circumference(self):
        self.assertEqual(circle.perimeter(0), "Invalid input")
        self.assertEqual(circle.perimeter(-1), "Invalid input")

    def test_bool_circle_circumference(self):
        self.assertEqual(circle.perimeter(True), "Invalid input")
        self.assertEqual(circle.perimeter(False), "Invalid input")

    def test_string_circle_circumference(self):
        self.assertEqual(circle.perimeter("abcdefgh"), "Invalid input")

    # Тесты, проверяющие корректность вычисления площади квадрата.

    def test_positive_square_area(self):
        self.assertEqual(square.area(7),49)
        self.assertEqual(square.area(1), 1)

    def test_non_positive_square_area(self):
        self.assertEqual(square.area(0),"Invalid input")
        self.assertEqual(square.area(-1), "Invalid input")

    def test_bool_square_area(self):
        self.assertEqual(square.area(True), "Invalid input")
        self.assertEqual(square.area(False), "Invalid input")

    def test_string_square_area(self):
        self.assertEqual(square.area("unittests are not fun"), "Invalid input")

    # Тесты, проверяющие корректность вычисления периметра квадрата.

    def test_positive_square_perimeter(self):
        self.assertEqual(square.perimeter(7), 28)
        self.assertEqual(square.perimeter(1), 4)

    def test_non_positive_square_perimeter(self):
        self.assertEqual(square.perimeter(0), "Invalid input")
        self.assertEqual(square.perimeter(-1), "Invalid input")

    def test_bool_square_perimeter(self):
        self.assertEqual(square.perimeter(True), "Invalid input")
        self.assertEqual(square.perimeter(False), "Invalid input")

    def test_string_square_perimeter(self):
        self.assertEqual(square.perimeter("AAAAAAA"), "Invalid input")


if __name__ == '__main__':
    unittest.main()
