import unittest

def area(a, h):
    '''Принимает число a и число h, возвращает среднее геометрическое чисел а и b'''
    return a * h / 2

def perimeter(a, b, c):
    '''Принимает число a, число b и число c, возвращает сумму чисел a, b, c'''
    return a + b + c

class Test_Tringle_Calculations(unittest.TestCase):
    
    def test_area_calculation(self):
        self.assertEqual(area(4, 6), 12)
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(-4, 5), -10)
    
    def test_perimeter_calculation(self):
        self.assertEqual(perimeter(4, 5, 6), 15)
        self.assertEqual(perimeter(0, 5, 10), 15)
        self.assertEqual(perimeter(-4, 5, 3), 4)
        
    def test_negative_values(self):
        self.assertEqual(area(-4, 5), -10)
        self.assertEqual(perimeter(-4, 5, 3), 4)
    
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            area('s','h')
            perimeter('p1','p2','p3')

if __name__ == '__main__':
    unittest.main()



