import unittest
import square
import rectangle
import circle
import triangle

class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area(self):
        res = rectangle.area(23, 0)  # zero
        self.assertEqual(res, "Invalid input")
        res = rectangle.area(1, 4)  # integers
        self.assertEqual(res, 4)
        res = rectangle.area(5, 5)  # same integers
        self.assertEqual(res, 25)
        res = rectangle.area(5, "w")  # string
        self.assertEqual(res, "Invalid input")
        res = rectangle.area(1.1, 3)  # float
        self.assertEqual(res, 3.3)
        res = rectangle.area(3, True)  # boolean
        self.assertEqual(res, "Invalid input")
        res = rectangle.area(False, 3)  # boolean
        self.assertEqual(res, "Invalid input")
        res = rectangle.area(-1, 2)  # negative integer
        self.assertEqual(res, "Invalid input")
        res = rectangle.area('\n', 23)  # enter :)
        self.assertEqual(res, "Invalid input")
        res = rectangle.area([10, "gutenTag", 232.223], 23)  # list
        self.assertEqual(res, "Invalid input")
        res = rectangle.area({"mama": "papa", "lala": "rara"}, 23)  # dictionaries
        self.assertEqual(res, "Invalid input")
        res = rectangle.area((10, "hello", 1286.92873), 23)  # tuples
        self.assertEqual(res, "Invalid input")
        res = rectangle.area({"a", "b"}, 23)  # sets
        self.assertEqual(res, "Invalid input")
        res = rectangle.area(' ', 1)  # spase
        self.assertEqual(res, "Invalid input")
        res = rectangle.area(12, 13, 14)  # overflow
        self.assertEqual(res, "Invalid input")
        res = rectangle.area()  # nothing
        self.assertEqual(res, "Invalid input")


    def test_rectangle_perimeter(self):
        res = rectangle.perimeter(2, 3)  # integer
        self.assertEqual(res, 10)
        res = rectangle.perimeter(3, 3)  # same integer
        self.assertEqual(res, 12)
        res = rectangle.perimeter(10, 0)  # zero
        self.assertEqual(res, "Invalid input")
        res = rectangle.perimeter(1.2, 3)  # float
        self.assertEqual(res, 8.4)
        res = rectangle.perimeter(3, "A")  # string
        self.assertEqual(res, "Invalid input")
        res = rectangle.perimeter(3, True)  # boolean
        self.assertEqual(res, "Invalid input")
        res = rectangle.perimeter(False, 3)  # boolean
        self.assertEqual(res, "Invalid input")
        res = rectangle.perimeter(-1, 2)  # negative integer
        self.assertEqual(res, "Invalid input")
        res = rectangle.perimeter('\n', 23)  # enter :)
        self.assertEqual(res, "Invalid input")
        res = rectangle.perimeter([10, "gutenTag", 232.223], 23)  # list
        self.assertEqual(res, "Invalid input")
        res = rectangle.perimeter({"mama": "papa", "lala": "rara"}, 23)  # dictionaries
        self.assertEqual(res, "Invalid input")
        res = rectangle.perimeter((10, "hello", 1286.92873), 23)  # tuples
        self.assertEqual(res, "Invalid input")
        res = rectangle.perimeter({"a", "b"}, 23)  # sets
        self.assertEqual(res, "Invalid input")
        res = rectangle.area(' ', 1)  # spase
        self.assertEqual(res, "Invalid input")
        res = rectangle.area(12, 13, 14)  # overflow
        self.assertEqual(res, "Invalid input")
        res = rectangle.area()  # nothing
        self.assertEqual(res, "Invalid input")


class CircleTestCase(unittest.TestCase):
    def test_circle_area(self):
        res = circle.area(0)  # zero
        self.assertEqual(res, "Invalid input")
        res = circle.area(2)  # integer
        self.assertEqual(res, 12.56)
        res = circle.area("A")  # string
        self.assertEqual(res, "Invalid input")
        res = circle.area(1.2)  # float
        self.assertEqual(res, 4.5216)
        res = circle.area(True)  # boolean
        self.assertEqual(res, "Invalid input")
        res = circle.area(False)  # boolean
        self.assertEqual(res, "Invalid input")
        res = circle.area(-1)  # negative integer
        self.assertEqual(res, "Invalid input")
        res = circle.area('\n')  # enter :)
        self.assertEqual(res, "Invalid input")
        res = circle.area([10, "gutenTag", 232.223])  # list
        self.assertEqual(res, "Invalid input")
        res = circle.area({"mama": "papa", "lala": "rara"})  # dictionaries
        self.assertEqual(res, "Invalid input")
        res = circle.area((10, "hello", 1286.92873))  # tuples
        self.assertEqual(res, "Invalid input")
        res = circle.area({"a", "b"})  # sets
        self.assertEqual(res, "Invalid input")
        res = circle.area(' ')  # spase
        self.assertEqual(res, "Invalid input")
        res = circle.area(12, 13)  # overflow
        self.assertEqual(res, "Invalid input")
        res = circle.area()  # nothing
        self.assertEqual(res, "Invalid input")

    def test_circle_perimeter(self):
        res = circle.perimeter(0)  # zero
        self.assertEqual(res, "Invalid input")
        res = circle.perimeter(2)  # integer
        self.assertEqual(res, 12.56)
        res = circle.perimeter(2.9)  # float
        self.assertEqual(res, 18.212)
        res = circle.perimeter("A")  # string
        self.assertEqual(res, "Invalid input")
        res = circle.perimeter(True)  # booleng
        self.assertEqual(res, "Invalid input")
        res = circle.perimeter(False)  # boolean
        self.assertEqual(res, "Invalid input")
        res = circle.perimeter(-1)  # negative integer
        self.assertEqual(res, "Invalid input")
        res = circle.perimeter('\n')  # enter :)
        self.assertEqual(res, "Invalid input")
        res = circle.perimeter([10, "gutenTag", 232.223])  # list
        self.assertEqual(res, "Invalid input")
        res = circle.perimeter({"mama": "papa", "lala": "rara"})  # dictionaries
        self.assertEqual(res, "Invalid input")
        res = circle.perimeter((10, "hello", 1286.92873))  # tuples
        self.assertEqual(res, "Invalid input")
        res = circle.perimeter({"a", "b"})  # sets
        self.assertEqual(res, "Invalid input")
        res = circle.area(' ')  # spase
        self.assertEqual(res, "Invalid input")
        res = circle.area(12, 13)  # overflow
        self.assertEqual(res, "Invalid input")
        res = circle.area()  # nothing
        self.assertEqual(res, "Invalid input")


class SquareTestCase(unittest.TestCase):
    def test_square_area(self):
        res = square.area(0)  # zero
        self.assertEqual(res, "Invalid input")
        res = square.area(5)  # integer
        self.assertEqual(res, 25)
        res = square.area("A")  # string
        self.assertEqual(res, "Invalid input")
        res = square.area(3.5)  # float
        self.assertEqual(res, 12.25)
        res = square.area(True)  # boolean
        self.assertEqual(res, "Invalid input")
        res = square.area(False)  # boolean
        self.assertEqual(res, "Invalid input")
        res = square.area(-1)  # negative integer
        self.assertEqual(res, "Invalid input")
        res = square.area('\n')  # enter :)
        self.assertEqual(res, "Invalid input")
        res = square.area([10, "gutenTag", 232.223])  # list
        self.assertEqual(res, "Invalid input")
        res = square.area({"mama": "papa", "lala": "rara"})  # dictionaries
        self.assertEqual(res, "Invalid input")
        res = square.area((10, "hello", 1286.92873))  # tuples
        self.assertEqual(res, "Invalid input")
        res = square.area({"a", "b"})  # sets
        self.assertEqual(res, "Invalid input")
        res = square.area(' ')  # spase
        self.assertEqual(res, "Invalid input")
        res = square.area(12, 13)  # overflow
        self.assertEqual(res, "Invalid input")
        res = square.area()  # nothing
        self.assertEqual(res, "Invalid input")

    def test_square_perimeter(self):
        res = square.perimeter(0)  # zero
        self.assertEqual(res, 0)
        res = square.perimeter(4)  # integer
        self.assertEqual(res, 16)
        res = square.perimeter("A")  # string
        self.assertEqual(res, "Invalid input")
        res = square.perimeter(4.6)  # float
        self.assertEqual(res, 18.4)
        res = square.perimeter(True)  # boolean
        self.assertEqual(res, "Invalid input")
        res = square.perimeter(False)  # boolean
        self.assertEqual(res, "Invalid input")
        res = square.perimeter(-1)  # negative integer
        self.assertEqual(res, "Invalid input")
        res = square.perimeter('\n')  # enter :)
        self.assertEqual(res, "Invalid input")
        res = square.perimeter([10, "gutenTag", 232.223])  # list
        self.assertEqual(res, "Invalid input")
        res = square.perimeter({"mama": "papa", "lala": "rara"})  # dictionaries
        self.assertEqual(res, "Invalid input")
        res = square.perimeter((10, "hello", 1286.92873))  # tuples
        self.assertEqual(res, "Invalid input")
        res = square.perimeter({"a", "b"})  # sets
        self.assertEqual(res, "Invalid input")
        res = square.area(' ')  # spase
        self.assertEqual(res, "Invalid input")
        res = square.area(12, 13)  # overflow
        self.assertEqual(res, "Invalid input")
        res = square.area()  # nothing
        self.assertEqual(res, "Invalid input")


class TriangeTestCase(unittest.TestCase):
    def test_triangle_area(self):
        res = triangle.area(0, 10)  # zero
        self.assertEqual(res, "Invalid input")
        res = triangle.area(2, 3)  # integer
        self.assertEqual(res, 3)
        res = triangle.area(2, 2)  # same integers
        self.assertEqual(res, 2)
        res = triangle.area("A", 3)  # string
        self.assertEqual(res, "Invalid input")
        res = triangle.area(2.3, 1)  # float
        self.assertEqual(res, 1.15)
        res = triangle.area(True, 1)  # boolean
        self.assertEqual(res, "Invalid input")
        res = triangle.area(False, 3)  # boolean
        self.assertEqual(res, "Invalid input")
        res = triangle.area(-1, 2)  # negative integer
        self.assertEqual(res, "Invalid input")
        res = triangle.area('\n', 23)  # enter :)
        self.assertEqual(res, "Invalid input")
        res = triangle.area([10, "gutenTag", 232.223], 23)  # list
        self.assertEqual(res, "Invalid input")
        res = triangle.area({"mama": "papa", "lala": "rara"}, 23)  # dictionaries
        self.assertEqual(res, "Invalid input")
        res = triangle.area((10, "hello", 1286.92873), 23)  # tuples
        self.assertEqual(res, "Invalid input")
        res = triangle.area({"a", "b"}, 23)  # sets
        self.assertEqual(res, "Invalid input")
        res = triangle.area(' ', 1)  # spase
        self.assertEqual(res, "Invalid input")
        res = triangle.area(12, 13, 14)  # overflow
        self.assertEqual(res, "Invalid input")
        res = triangle.area()  # nothing
        self.assertEqual(res, "Invalid input")

    def test_triangle_perimeter(self):
        res = triangle.perimeter(0, 1, 2)  # zero
        self.assertEqual(res, "Invalid input")
        res = triangle.perimeter(3, 4, 5)  # integer
        self.assertEqual(res, 12)
        res = triangle.perimeter("A", 2, 3)  # string
        self.assertEqual(res, "Invalid input")
        res = triangle.perimeter(2.99, 2, 3)  # float
        self.assertEqual(res, 7.99)
        res = triangle.perimeter(True, 2, 3)  # boolean
        self.assertEqual(res, "Invalid input")
        res = triangle.perimeter(1, 1, 1)  # same integers
        self.assertEqual(res, 3)
        res = triangle.perimeter(False, 3, 1)  # boolean
        self.assertEqual(res, "Invalid input")
        res = triangle.perimeter(-1, 2, 1)  # negative integer
        self.assertEqual(res, "Invalid input")
        res = triangle.perimeter('\n', 23, 1)  # enter :)
        self.assertEqual(res, "Invalid input")
        res = triangle.perimeter([10, "gutenTag", 232.223], 23, 1)  # list
        self.assertEqual(res, "Invalid input")
        res = triangle.perimeter({"mama": "papa", "lala": "rara"}, 23, 1)  # dictionaries
        self.assertEqual(res, "Invalid input")
        res = triangle.perimeter((10, "hello", 1286.92873), 23, 1)  # tuples
        self.assertEqual(res, "Invalid input")
        res = triangle.perimeter({"a", "b"}, 23, 1)  # sets
        self.assertEqual(res, "Invalid input")
        res = triangle.area(' ', 1, 1)  # spase
        self.assertEqual(res, "Invalid input")
        res = triangle.area(12, 13, 1, 14)  # overflow
        self.assertEqual(res, "Invalid input")
        res = triangle.area()  # nothing
        self.assertEqual(res, "Invalid input")


if __name__ == '__main__':
    unittest.main()
