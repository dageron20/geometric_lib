import unittest

def area(a, b):
    '''Принимает число a и число b, возвращает число a умноженное на число b'''
    return a * b

def perimeter(a, b):
    '''Принимает число a и число b, возвращает сумму чисел a и b, умноженную на 2'''
    return 2*(a + b)


class Test_Rectangle_Clculation(unittest.TestCase):
    
    def test_area_calculation(self):
        self.assertEqual(area(4, 5), 20)
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(-4, 5), -20)
    
    def test_perimeter_calculation(self):
        self.assertEqual(perimeter(4, 5), 18)
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(-4, 5), 2)
        
    def test_negative_values(self):
        self.assertEqual(area(-4, 5), -20)
        self.assertEqual(perimeter(-4, 5), 2)
    
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            area('a','b')
            perimeter('a','b')

if __name__ == '__main__':
    unittest.main()
