import unittest
import circle
import rectangle
import square
import triangle

class CircleTestCase(unittest.TestCase):
    
    def test_positive_1(self):
        area_res = circle.area(10)
        perimeter_res = circle.perimeter(10)
        self.assertAlmostEqual(area_res, 314.1592, places=0)
        self.assertAlmostEqual(perimeter_res, 62.8318, places=0)
    
    def test_positive_2(self):
        area_res = circle.area(111)
        perimeter_res = circle.perimeter(111)
        self.assertAlmostEqual(area_res, 38707.5630, places=0)
        self.assertAlmostEqual(perimeter_res, 697.4335, places=0)
        
    def test_positive_3(self):
        area_res = circle.area(1000000)
        perimeter_res = circle.perimeter(1000000)
        self.assertAlmostEqual(area_res, 3141592653589.793, places=0)
        self.assertAlmostEqual(perimeter_res, 6283185.3071, places=0)
    
    def test_zero(self):
        area_res = circle.area(0)
        perimeter_res = circle.perimeter(0)
        self.assertEqual(area_res, 0)
        self.assertEqual(perimeter_res, 0)
    
    def test_negative_1(self):
        area_res = circle.area(-10)
        perimeter_res = circle.perimeter(-10)
        self.assertAlmostEqual(area_res, 314.1592, places=0)
        self.assertAlmostEqual(perimeter_res, -62.8318, places=0)
    
    def test_negative_2(self):
        area_res = circle.area(-1000000)
        perimeter_res = circle.perimeter(-1000000)
        self.assertAlmostEqual(area_res, 3141592653589.793, places=0)
        self.assertAlmostEqual(perimeter_res, -6283185.3071, places=0)
    
    def test_float_1(self):
        area_res = circle.area(1.5)
        perimeter_res = circle.perimeter(1.5)
        self.assertAlmostEqual(area_res, 7.0685, places=0)
        self.assertAlmostEqual(perimeter_res, 9.4247, places=0)
    
    def test_float_2(self):
        area_res = circle.area(1.55555555555)
        perimeter_res = circle.perimeter(1.55555555555)
        self.assertAlmostEqual(area_res, 7.6018, places=0)
        self.assertAlmostEqual(perimeter_res, 9.7738, places=0)
    
    def test_float_3(self):
        area_res = circle.area(1000000.55555555555)
        perimeter_res = circle.perimeter(1000000.55555555555)
        self.assertAlmostEqual(area_res, 3141596144249.2666, places=0)
        self.assertAlmostEqual(perimeter_res, 6283188.7978, places=0)

class RectangleTestCase(unittest.TestCase):
    
    def test_positive_1(self):
        area_res = rectangle.area(10, 10)
        perimeter_res = rectangle.perimeter(10, 10)
        self.assertEqual(area_res, 100)
        self.assertEqual(perimeter_res, 40)
    
    def test_positive_2(self):
        area_res = rectangle.area(349, 256)
        perimeter_res = rectangle.perimeter(349, 256)
        self.assertEqual(area_res, 89344)
        self.assertEqual(perimeter_res, 1210)
    
    def test_positive_3(self):
        area_res = rectangle.area(1000000, 256)
        perimeter_res = rectangle.perimeter(1000000, 256)
        self.assertEqual(area_res, 256000000)
        self.assertEqual(perimeter_res, 2000512)
    
    def test_zero_1(self):
        area_res = rectangle.area(0, 256)
        perimeter_res = rectangle.perimeter(0, 256)
        self.assertEqual(area_res, 0)
        self.assertEqual(perimeter_res, 512)
    
    def test_zero_2(self):
        area_res = rectangle.area(256, 0)
        perimeter_res = rectangle.perimeter(256, 0)
        self.assertEqual(area_res, 0)
        self.assertEqual(perimeter_res, 512)
    
    def test_zero_3(self):
        area_res = rectangle.area(0, 0)
        perimeter_res = rectangle.perimeter(0, 0)
        self.assertEqual(area_res, 0)
        self.assertEqual(perimeter_res, 0)
    
    def test_float_1(self):
        area_res = rectangle.area(1.5, 2.25)
        perimeter_res = rectangle.perimeter(1.5, 2.25)
        self.assertEqual(area_res, 3.375)
        self.assertEqual(perimeter_res, 7.5)
    
    def test_float_2(self):
        area_res = rectangle.area(1.55555555, 1.1111111)
        perimeter_res = rectangle.perimeter(1.55555555, 1.1111111)
        self.assertAlmostEqual(area_res, 1.7283, places=0)
        self.assertAlmostEqual(perimeter_res, 5.3, places=0)
    
    def test_float_3(self):
        area_res = rectangle.area(1000000.5555555, 1000000.111111)
        perimeter_res = rectangle.perimeter(1000000.55555555555, 1000000.1111111111)
        self.assertAlmostEqual(area_res, 1000000666666.7284, places=0)
        self.assertAlmostEqual(perimeter_res, 4000001.33, places=0)

    def test_negative_1(self):
        area_res = rectangle.area(-10, 10)
        perimeter_res = rectangle.perimeter(-10, 10)
        self.assertEqual(area_res, -100)
        self.assertEqual(perimeter_res, 0)
    
    def test_negative_2(self):
        area_res = rectangle.area(10, -10)
        perimeter_res = rectangle.perimeter(10, -10)
        self.assertEqual(area_res, -100)
        self.assertEqual(perimeter_res, 0)
    
    def test_negative_3(self):
        area_res = rectangle.area(-10, -10)
        perimeter_res = rectangle.perimeter(-10, -10)
        self.assertEqual(area_res, 100)
        self.assertEqual(perimeter_res, -40)
    
    def test_negative_4(self):
        area_res = rectangle.area(-1.5, 2.55)
        perimeter_res = rectangle.perimeter(-1.5, 2.55)
        self.assertAlmostEqual(area_res, -3.825, places=0)
        self.assertAlmostEqual(perimeter_res, 2.1, places=0)

class SquareTestCase(unittest.TestCase):
    
    def test_positive_1(self):
        area_res = square.area(10)
        perimeter_res = square.perimeter(10)
        self.assertEqual(area_res, 100)
        self.assertEqual(perimeter_res, 40)
    
    def test_positive_2(self):
        area_res = square.area(256)
        perimeter_res = square.perimeter(256)
        self.assertEqual(area_res, 65536)
        self.assertEqual(perimeter_res, 1024)
    
    def test_positive_3(self):
        area_res = square.area(1000000)
        perimeter_res = square.perimeter(1000000)
        self.assertEqual(area_res, 1000000000000)
        self.assertEqual(perimeter_res, 4000000)
    
    def test_zero(self):
        area_res = square.area(0)
        perimeter_res = square.perimeter(0)
        self.assertEqual(area_res, 0)
        self.assertEqual(perimeter_res, 0)
    
    def test_float_1(self):
        area_res = square.area(1.5)
        perimeter_res = square.perimeter(1.5)
        self.assertEqual(area_res, 2.25)
        self.assertEqual(perimeter_res, 6.0)
    
    def test_float_2(self):
        area_res = square.area(1.5555555)
        perimeter_res = square.perimeter(1.5555555)
        self.assertAlmostEqual(area_res, 2.4197, places=0)
        self.assertAlmostEqual(perimeter_res, 6.2, places=0)
    
    def test_float_3(self):
        area_res = square.area(1000000.5555555)
        perimeter_res = square.perimeter(1000000.5555555)
        self.assertAlmostEqual(area_res, 1000001111111.3086, places=0)
        self.assertAlmostEqual(perimeter_res, 4000002.2222, places=0)

    def test_negative_1(self):
        area_res = square.area(-10)
        perimeter_res = square.perimeter(-10)
        self.assertEqual(area_res, 100)
        self.assertEqual(perimeter_res, -40)
    
    def test_negative_2(self):
        area_res = square.area(-1.5)
        perimeter_res = square.perimeter(-1.5)
        self.assertEqual(area_res, 2.25)
        self.assertEqual(perimeter_res, -6.0)

class TriangleTestCase(unittest.TestCase):
    
    def test_positive_1(self):
        area_res = triangle.area(3, 10)
        perimeter_res = triangle.perimeter(3, 4, 5)
        self.assertEqual(area_res, 15.0)
        self.assertEqual(perimeter_res, 12)
    
    def test_positive_2(self):
        area_res = triangle.area(256, 349)
        perimeter_res = triangle.perimeter(256, 349, 415)
        self.assertEqual(area_res, 44672.0)
        self.assertEqual(perimeter_res, 1020)
    
    def test_positive_3(self):
        area_res = triangle.area(3000000, 4000000)
        perimeter_res = triangle.perimeter(3000000, 4000000, 5000000)
        self.assertEqual(area_res, 6000000000000.0)
        self.assertEqual(perimeter_res, 12000000)
    
    def test_zero_1(self):
        area_res = triangle.area(0, 10)
        perimeter_res = triangle.perimeter(0, 10, 0)
        self.assertEqual(area_res, 0)
        self.assertEqual(perimeter_res, 10)
    
    def test_zero_2(self):
        area_res = triangle.area(10, 0)
        perimeter_res = triangle.perimeter(10, 0, 0)
        self.assertEqual(area_res, 0)
        self.assertEqual(perimeter_res, 10)
    
    def test_zero_3(self):
        area_res = triangle.area(0, 0)
        perimeter_res = triangle.perimeter(0, 0, 0)
        self.assertEqual(area_res, 0)
        self.assertEqual(perimeter_res, 0)
    
    def test_float_1(self):
        area_res = triangle.area(1.5, 2.25)
        perimeter_res = triangle.perimeter(1.5, 2.25, 3.75)
        self.assertEqual(area_res, 1.6875)
        self.assertEqual(perimeter_res, 7.5)
    
    def test_float_2(self):
        area_res = triangle.area(1.555555, 1.11111)
        perimeter_res = triangle.perimeter(1.555555, 1.33333, 1.11111)
        self.assertAlmostEqual(area_res, 1.037, places=0)
        self.assertAlmostEqual(perimeter_res, 3.99, places=0)

    def test_negative_1(self):
        area_res = triangle.area(-10, 20)
        perimeter_res = triangle.perimeter(-10, 20, 30)
        self.assertEqual(area_res, -100.0)
        self.assertEqual(perimeter_res, 40)
    
    def test_negative_2(self):
        area_res = triangle.area(10, -20)
        perimeter_res = triangle.perimeter(10, -20, -30)
        self.assertEqual(area_res, -100.0)
        self.assertEqual(perimeter_res, -40)
    
    def test_negative_3(self):
        area_res = triangle.area(-10, -20)
        perimeter_res = triangle.perimeter(-10, -20, -30)
        self.assertEqual(area_res, 100.0)
        self.assertEqual(perimeter_res, -60)
    
    def test_negative_4(self):
        area_res = triangle.area(-1.5, 2.55)
        perimeter_res = triangle.perimeter(-1.5, 2.55, 3.75)
        self.assertAlmostEqual(area_res, -1.9125, places=0)
        self.assertAlmostEqual(perimeter_res, 4.8, places=0)
    
    def test_negative_5(self):
        area_res = triangle.area(-1.5, -2.55)
        perimeter_res = triangle.perimeter(-1.5, -2.55, -3.75)
        self.assertAlmostEqual(area_res, 1.9125, places=0)
        self.assertAlmostEqual(perimeter_res, -7.8, places=0)

if __name__ == '__main__':
    unittest.main()
