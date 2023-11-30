# Solution:

# Description of function:
## Circle:
    import math

    - Импортирую библиотеку math для того чтобы использовать число пи

    def area(r):
    - Принимает число r, возвращает квадрат числа r, умноженный на число пи
        return math.pi * r * r

    def perimeter(r):
    - Принимает число r, возвращает число r умноженное на два и на число пи
        return 2 * math.pi * r
```
a = 2
print(area(a))
print(perimeter(a))
```       
## Rectangle:
    def area(a, b):
    - Принимает число a и число b, возвращает число a умноженное на число b
        return a * b

    def perimeter(a, b):
    - Принимает число a и число b, возвращает сумму чисел a и b, умноженную на 2
        return 2*(a + b)
## Square:
    def area(a):
    - Принимает число a, возвращает квадрат числа а
        return a * a

    def perimeter(a):
    - Принимает число a, возвращает число a умноженное на 4
        return 4 * a
## Tringle:
    def area(a, h):
    - Принимает число a и число h, возвращает среднее геометрическое чисел а и b
        return a * h / 2

    def perimeter(a, b, c):
    - Принимает число a, число b и число с, возвращает сумму чисел a,b,c
        return a + b + с

#History of project:
commit 0af89386f54bbb8cc6c67752bdc371216fc2958c (HEAD -> main, origin/main, origin/HEAD)
Author: viktoriagalakhova <viktoria.galakhova@gmail.com>
Date:   Thu Sep 21 19:55:37 2023 +0300

    fixed bug

commit cd51f4cb013930b09dcf7ab023be7b56b919f4ea
Author: viktoriagalakhova <viktoria.galakhova@gmail.com>
Date:   Thu Sep 21 19:52:17 2023 +0300

    add new file

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added

# Write Unit tests:
## Circle:
    import unittest
    import math
    
    -Импортирую библиотеку unittest для того чтобы использовать юниттесты 
    -Импортирую библиотеку math для того чтобы использовать число пи

    def area(r):
        '''Принимает число r, возвращает квадрат числа r, умноженный на число пи'''
        return math.pi * r * r

    def perimeter(r):
        '''Принимает число r, возвращает число r умноженное на два и на число п'''
        return 2 * math.pi * r


    class Test_Circle_Calculations(unittest.TestCase):
    
        def test_area_calculation(self):
            -В данной функции проверяется правильность работы функции area для различных входных значений
            self.assertEqual(area(4), math.pi * 16)
            self.assertEqual(area(0), 0)
            self.assertEqual(area(5), math.pi * 25)
            -сравниваем значение, которое выдает функция area и правильный ответ 
    
        def test_perimeter_calculation(self):
            -В данной функции проверяется правильность работы функции perimeter для различных входных значений
            self.assertEqual(perimeter(4), 2 * math.pi * 4)
            self.assertEqual(perimeter(0), 0)
            self.assertEqual(perimeter(5), 2 * math.pi * 5)
            -сравниваем значение, которое выдает функция perimeter и правильный ответ
        
        def test_negative_values(self):
            self.assertEqual(area(-4), math.pi * 16)
            self.assertEqual(perimeter(-4), 2 * math.pi * (-4))
            -сравниваем значение, которое выдает функция area  и perimeter при отрицательных значениях и правильный ответ
        
        def test_invalid_input(self):
            with self.assertRaises(TypeError):
                area('r')
                perimeter('r')

    if __name__ == '__main__':
        unittest.main()
    -вызов юниттеста
        
## Rectangle:
    import unittest
    -Импортирую библиотеку unittest для того чтобы использовать юниттесты 
        
    def area(a, b):
        '''Принимает число a и число b, возвращает число a умноженное на число b'''
        return a * b

    def perimeter(a, b):
        '''Принимает число a и число b, возвращает сумму чисел a и b, умноженную на 2'''
        return 2*(a + b)


    class Test_Rectangle_Clculation(unittest.TestCase):
    
        def test_area_calculation(self):
            -В данной функции проверяется правильность работы функции area для различных входных значений
            self.assertEqual(area(4, 5), 20)
            self.assertEqual(area(0, 5), 0)
            self.assertEqual(area(-4, 5), -20)
            -сравниваем значение, которое выдает функция area и правильный ответ
    
        def test_perimeter_calculation(self):
            -В данной функции проверяется правильность работы функции perimeter для различных входных значений
            self.assertEqual(perimeter(4, 5), 18)
            self.assertEqual(perimeter(0, 5), 10)
            self.assertEqual(perimeter(-4, 5), 2)
            -сравниваем значение, которое выдает функция perimeter и правильный ответ
        
        def test_negative_values(self):
            self.assertEqual(area(-4, 5), -20)
            self.assertEqual(perimeter(-4, 5), 2)
            -сравниваем значение, которое выдает функция area  и perimeter при отрицательных значениях и правильный ответ
        
        def test_invalid_input(self):
            with self.assertRaises(TypeError):
                area('a','b')
                perimeter('a','b')

    if __name__ == '__main__':
        unittest.main()
    -вызов юниттеста

## Square:
    import unittest
    -Импортирую библиотеку unittest для того чтобы использовать юниттесты 

    def area(a):
        '''Принимает число a, возвращает квадрат числа а'''
        return a * a

    def perimeter(a):
        '''Принимает число a, возвращает число a умноженное на 4'''
        return 4 * a

    class Test_Square_Calculations(unittest.TestCase):
    
        def test_area_calculation(self):
            -В данной функции проверяется правильность работы функции area для различных входных значений
            self.assertEqual(area(4), 16)
            self.assertEqual(area(0), 0)
            self.assertEqual(area(-4), 16)
            -сравниваем значение, которое выдает функция area и правильный ответ
    
        def test_perimeter_calculation(self):
            -В данной функции проверяется правильность работы функции perimeter для различных входных значений
            self.assertEqual(perimeter(4), 16)
            self.assertEqual(perimeter(0), 0)
            self.assertEqual(perimeter(-4), -16)
            -сравниваем значение, которое выдает функция perimeter и правильный ответ
        
        def test_negative_values(self):
            self.assertEqual(area(-4), 16)
            self.assertEqual(perimeter(-4), -16)
            -сравниваем значение, которое выдает функция area  и perimeter при отрицательных значениях и правильный ответ
        
        def test_invalid_input(self):
            with self.assertRaises(TypeError):
                area('a')
                perimeter('a')

    if __name__ == '__main__':
        unittest.main()
    -вызов юниттеста

## Tringle:
    import unittest
    -Импортирую библиотеку unittest для того чтобы использовать юниттесты 

    def area(a, h):
        '''Принимает число a и число h, возвращает среднее геометрическое чисел а и b'''
        return a * h / 2

    def perimeter(a, b, c):
        '''Принимает число a, число b и число c, возвращает сумму чисел a, b, c'''
        return a + b + c

    class Test_Tringle_Calculations(unittest.TestCase):
        
        def test_area_calculation(self):
            -В данной функции проверяется правильность работы функции area для различных входных значений
            self.assertEqual(area(4, 6), 12)
            self.assertEqual(area(0, 5), 0)
            self.assertEqual(area(-4, 5), -10)
            -сравниваем значение, которое выдает функция area и правильный ответ
        
        def test_perimeter_calculation(self):
            -В данной функции проверяется правильность работы функции perimeter для различных входных значений
            self.assertEqual(perimeter(4, 5, 6), 15)
            self.assertEqual(perimeter(0, 5, 10), 15)
            self.assertEqual(perimeter(-4, 5, 3), 4)
            -сравниваем значение, которое выдает функция perimeter и правильный ответ
            
        def test_negative_values(self):
            self.assertEqual(area(-4, 5), -10)
            self.assertEqual(perimeter(-4, 5, 3), 4)
            -сравниваем значение, которое выдает функция area  и perimeter при отрицательных значениях и правильный ответ
        
        def test_invalid_input(self):
            with self.assertRaises(TypeError):
                area('s','h')
                perimeter('p1','p2','p3')

    if __name__ == '__main__':
        unittest.main()
    -вызов юниттеста
