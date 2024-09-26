import unittest
import circle
import rectangle
import square
import triangle

class unitTests(unittest.TestCase):
    
    '''ТЕСТЫ ДЛЯ КРУГА'''
        '''периметр'''
    def test_perimeter_right_circle(self):
        self.assertEqual(circle.perimeter(1), 6.283185307179586)

    def test_perimeter_wrong_circle(self):
        self.assertEqual(circle.perimeter(0), "figure not exist")
        self.assertEqual(circle.perimeter(-1), "figure not exist")

        self.assertEqual(circle.perimeter("a"), "wrong argument type")
        self.assertEqual(circle.perimeter("7"), "wrong argument type")

        '''площадь'''
    def test_area_right_circle(self):
        self.assertEqual(circle.area(1), 3.141592653589793)
        self.assertEqual(circle.area(2), 12.566370614359172)

    def test_area_wrong_circle(self):
        self.assertEqual(circle.area(0), "figure not exist")
        self.assertEqual(circle.area(-1), "figure not exist")

        self.assertEqual(circle.area("a"), "wrong argument type")
        self.assertEqual(circle.area("7"), "wrong argument type")


     '''ТЕСТЫ ДЛЯ ПРЯМОУГОЛЬНИКА'''
        '''периметр'''
    def test_perimeter_right_rectangle(self):
        self.assertEqual(rectangle.perimeter(2, 5), 14)
        self.assertEqual(rectangle.perimeter(4, 10), 28)

    def test_perimeter_wrong_rectangle(self):
        self.assertEqual(rectangle.perimeter(0, 0), "figure not exist")
        self.assertEqual(rectangle.perimeter(0, 5), "figure not exist")
        self.assertEqual(rectangle.perimeter(4, 0), "figure not exist")

        self.assertEqual(rectangle.perimeter("a", "7"), "wrong argument type")
        self.assertEqual(rectangle.perimeter("a", 1), "wrong argument type")
        self.assertEqual(rectangle.perimeter(1, "7"), "wrong argument type")

        '''площадь'''
    def test_area_right_rectangle(self):
        self.assertEqual(rectangle.area(2, 3), 6)
        self.assertEqual(rectangle.area(10, 10), 100)

    def test_area_wrong_rectangle(self):
        self.assertEqual(rectangle.area(0, 0), "figure not exist")
        self.assertEqual(rectangle.area(0, 1), "figure not exist")
        self.assertEqual(rectangle.area(1, 0), "figure not exist")
        
        self.assertEqual(rectangle.area("a", "7"), "wrong argument type")
        self.assertEqual(rectangle.area("a", 1), "wrong argument type")
        self.assertEqual(rectangle.area(1, "7"), "wrong argument type")


 '''ТЕСТЫ ДЛЯ КВАДРАТА'''
        '''периметр'''
    def test_perimeter_right_square(self):
        self.assertEqual(square.perimeter(2), 8)
        self.assertEqual(square.perimeter(6), 24)

    def test_perimeter_wrong_square(self):
        self.assertEqual(square.perimeter(0), "figure not exist")

        self.assertEqual(square.perimeter("a"), "wrong argument type")
        self.assertEqual(square.perimeter("7"), "wrong argument type")


        '''площадь'''
    def test_area_right_square(self):
        self.assertEqual(square.area(2), 4)
        self.assertEqual(square.area(10), 100)

    def test_area_wrong_square(self):
        self.assertEqual(square.area(0), "figure not exist")
        
        self.assertEqual(square.area("a"), "wrong argument type")
        self.assertEqual(square.area("7"), "wrong argument type")



'''ТЕСТЫ ДЛЯ ТРЕУГОЛЬНИКА'''
        '''периметр'''
    def test_perimeter_right_triangle(self):
        self.assertEqual(triangle.perimeter(2, 3, 4), 9)
        self.assertEqual(triangle.perimeter(6, 7, 8), 21)

    def test_perimeter_wrong_triangle(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), "figure not exist")
        self.assertEqual(triangle.perimeter(1, 0, 0), "figure not exist")
        self.assertEqual(triangle.perimeter(0, 1, 0), "figure not exist")
        self.assertEqual(triangle.perimeter(0, 0, 1), "figure not exist")

        self.assertEqual(triangle.perimeter("a", "7", "q"), "wrong argument type")
        self.assertEqual(triangle.perimeter(1, "7", "q"), "wrong argument type")
        self.assertEqual(triangle.perimeter("a", 1, "q"), "wrong argument type")
        self.assertEqual(triangle.perimeter("a", "7", 1), "wrong argument type")


        '''площадь'''
    def test_area_right_triangle(self):
        self.assertEqual(triangle.area(3, 4), 6)
        self.assertEqual(triangle.area(10, 10), 50)

    def test_area_wrong_triangle(self):
        self.assertEqual(triangle.area(0, 0), "figure not exist")
        self.assertEqual(triangle.area(1, 0), "figure not exist")
        self.assertEqual(triangle.area(0, 1), "figure not exist")
        
        self.assertEqual(triangle.area("a", "7"), "wrong argument type")
        self.assertEqual(triangle.area(1, "7"), "wrong argument type")
        self.assertEqual(triangle.area("a", 1), "wrong argument type")

if __name__ == '__main__':
    unittest.main()

