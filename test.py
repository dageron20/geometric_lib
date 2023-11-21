import unittest
import rectangle
import circle
import square
import triangle

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        area_res_1 = rectangle.area(0, 0)
        area_res_2 = rectangle.area(10, 0)
        area_res_3 = rectangle.area(0, 10)
        perimeter_res_1 = rectangle.perimeter(0, 0)
        perimeter_res_2 = rectangle.perimeter(10, 0)
        perimeter_res_3 = rectangle.perimeter(0, 10)
        self.assertEqual(area_res_1, 0)
        self.assertEqual(area_res_2, 0)
        self.assertEqual(area_res_3, 0)
        self.assertEqual(perimeter_res_1, 0)
        self.assertEqual(perimeter_res_2, 20)
        self.assertEqual(perimeter_res_3, 20)

    def test_square_mul(self):
        area_res = rectangle.area(10, 10)
        perimeter_res = rectangle.perimeter(10, 10)
        self.assertEqual(area_res, 100)
        self.assertEqual(perimeter_res, 40)

    def test_negative_mul(self):
        area_res_1 = rectangle.area(-10, -5)
        area_res_2 = rectangle.area(-10, 5)
        area_res_3 = rectangle.area(10, -5)
        perimeter_res_1 = rectangle.perimeter(-10, -5)
        perimeter_res_2 = rectangle.perimeter(-10, 5)
        perimeter_res_3 = rectangle.perimeter(10, -5)
        self.assertEqual(area_res_1, 'Сторона прямоугольника не может быть отрицательной')
        self.assertEqual(area_res_2, 'Сторона прямоугольника не может быть отрицательной')
        self.assertEqual(area_res_3, 'Сторона прямоугольника не может быть отрицательной')
        self.assertEqual(perimeter_res_1, 'Сторона прямоугольника не может быть отрицательной')
        self.assertEqual(perimeter_res_2, 'Сторона прямоугольника не может быть отрицательной')
        self.assertEqual(perimeter_res_3, 'Сторона прямоугольника не может быть отрицательной')

    def test_str_mul(self):
        area_res = rectangle.area('str', 10)
        perimeter_res = rectangle.perimeter(10, 'str')
        self.assertEqual(area_res, 'Вы ввели строку')
        self.assertEqual(perimeter_res, 'Вы ввели строку')

    def test_float_mul(self):
        area_res = rectangle.area(4.5, 10)
        perimeter_res = rectangle.perimeter(10, 2.3)
        self.assertEqual(area_res, 45)
        self.assertEqual(perimeter_res, 24.6)

    if __name__ == '__main__':
        unittest.main()

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        area_res = circle.area(0)
        perimeter_res = circle.perimeter(0)
        self.assertEqual(area_res, 0)
        self.assertEqual(perimeter_res, 0)

    def test_number_mul(self):
        area_res = circle.area(5)
        perimeter_res = circle.perimeter(5)
        self.assertEqual(area_res, 78.53981633974483)
        self.assertEqual(perimeter_res, 31.41592653589793)

    def test_negative_mul(self):
        area_res = circle.area(-5)
        perimeter_res = circle.perimeter(-5)
        self.assertEqual(area_res, 'Радиус не может быть отрицательным числом')
        self.assertEqual(perimeter_res, 'Радиус не может быть отрицательным числом')

    def test_str_mul(self):
        area_res = circle.area('str')
        perimeter_res = circle.perimeter('str')
        self.assertEqual(area_res, 'Вы ввели строку')
        self.assertEqual(perimeter_res, 'Вы ввели строку')

    def test_float_mul(self):
        area_res = circle.area(5.5)
        perimeter_res = circle.perimeter(5.5)
        self.assertEqual(area_res, 95.03317777109123)
        self.assertEqual(perimeter_res, 34.55751918948772)

    if __name__ == '__main__':
        unittest.main()

class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        area_res = square.area(0)
        perimeter_res = square.perimeter(0)
        self.assertEqual(area_res, 0)
        self.assertEqual(perimeter_res, 0)

    def test_number_mul(self):
        area_res = square.area(5)
        perimeter_res = square.perimeter(5)
        self.assertEqual(area_res, 25)
        self.assertEqual(perimeter_res, 20)

    def test_negative_mul(self):
        area_res = square.area(-5)
        perimeter_res = square.perimeter(-5)
        self.assertEqual(area_res, 'Сторона квадрата не может быть отрицательным числом')
        self.assertEqual(perimeter_res, 'Сторона квадрата не может быть отрицательным числом')

    def test_str_mul(self):
        area_res = square.area('str')
        perimeter_res = square.perimeter('str')
        self.assertEqual(area_res, 'Вы ввели строку')
        self.assertEqual(perimeter_res, 'Вы ввели строку')

    def test_float_mul(self):
        area_res = square.area(5.5)
        perimeter_res = square.perimeter(5.5)
        self.assertEqual(area_res, 30.25)
        self.assertEqual(perimeter_res, 22)

    if __name__ == '__main__':
        unittest.main()

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        area_res_1 = triangle.area(0, 0)
        area_res_2 = triangle.area(10, 0)
        area_res_3 = triangle.area(0, 10)
        perimeter_res_1 = triangle.perimeter(0, 0, 0)
        perimeter_res_2 = triangle.perimeter(0, 10, 10)
        perimeter_res_3 = triangle.perimeter(10, 0, 10)
        perimeter_res_4 = triangle.perimeter(10, 10, 0)
        self.assertEqual(area_res_1, 0)
        self.assertEqual(area_res_2, 0)
        self.assertEqual(area_res_3, 0)
        self.assertEqual(perimeter_res_1, 'Сторона треугольника не может быть отрицательным числом или нулем')
        self.assertEqual(perimeter_res_2, 'Сторона треугольника не может быть отрицательным числом или нулем')
        self.assertEqual(perimeter_res_3, 'Сторона треугольника не может быть отрицательным числом или нулем')
        self.assertEqual(perimeter_res_4, 'Сторона треугольника не может быть отрицательным числом или нулем')

    def test_number_mul(self):
        area_res = triangle.area(5, 10)
        perimeter_res = triangle.perimeter(5, 10, 15)
        self.assertEqual(area_res, 25)
        self.assertEqual(perimeter_res, 30)

    def test_negative_mul(self):
        area_res_1 = triangle.area(-5, -10)
        area_res_2 = triangle.area(-5, 10)
        area_res_3 = triangle.area(5, -10)
        perimeter_res_1 = triangle.perimeter(-5, -10, -15)
        perimeter_res_2 = triangle.perimeter(-5, 10, 15)
        perimeter_res_3 = triangle.perimeter(5, -10, 15)
        perimeter_res_4 = triangle.perimeter(5, 10, -15)
        self.assertEqual(area_res_1, 'Сторона или высота треугольника не может быть отрицательным числом')
        self.assertEqual(area_res_2, 'Сторона или высота треугольника не может быть отрицательным числом')
        self.assertEqual(area_res_3, 'Сторона или высота треугольника не может быть отрицательным числом')
        self.assertEqual(perimeter_res_1, 'Сторона треугольника не может быть отрицательным числом или нулем')
        self.assertEqual(perimeter_res_2, 'Сторона треугольника не может быть отрицательным числом или нулем')
        self.assertEqual(perimeter_res_3, 'Сторона треугольника не может быть отрицательным числом или нулем')
        self.assertEqual(perimeter_res_4, 'Сторона треугольника не может быть отрицательным числом или нулем')

    def test_str_mul(self):
        area_res = triangle.area('str', 10)
        perimeter_res = triangle.perimeter(10, 'str', 2)
        self.assertEqual(area_res, 'Вы ввели строку')
        self.assertEqual(perimeter_res, 'Вы ввели строку')

    def test_float_mul(self):
        area_res = triangle.area(5.5, 2)
        perimeter_res = triangle.perimeter(5.5, 2, 10)
        self.assertEqual(area_res, 5.5)
        self.assertEqual(perimeter_res, 17.5)

    if __name__ == '__main__':
        unittest.main()
