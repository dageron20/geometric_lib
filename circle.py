import unittest
import math

def area(r):
    '''Принимает число r, возвращает квадрат числа r, умноженный на число пи'''
    return math.pi * r * r

def perimeter(r):
    '''Принимает число r, возвращает число r умноженное на два и на число п'''
    return 2 * math.pi * r


class Test_Circle_Calculations(unittest.TestCase):
    
    def test_area_calculation(self):
        self.assertEqual(area(4), math.pi * 16)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(5), math.pi * 25)
    
    def test_perimeter_calculation(self):
        self.assertEqual(perimeter(4), 2 * math.pi * 4)
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(5), 2 * math.pi * 5)
        
    def test_negative_values(self):
        self.assertEqual(area(-4), math.pi * 16)
        self.assertEqual(perimeter(-4), 2 * math.pi * (-4))
        
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            area('r')
            perimeter('r')

if __name__ == '__main__':
    unittest.main()


