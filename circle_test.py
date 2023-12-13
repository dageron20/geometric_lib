import unittest
import math

def area(r):
    '''Принимает число r, возвращает квадрат числа r, умноженный на число пи'''
    return math.pi * r * r

def perimeter(r):
    '''Принимает число r, возвращает число r умноженное на два и на число п'''
    return 2 * math.pi * r


class Test_Circle_Calculations(unittest.TestCase):
        
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            area('r')
            perimeter('r')

if __name__ == '__main__':
    unittest.main()


