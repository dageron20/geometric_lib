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
a = 3
print(area(a))
print(perimeter(a))
       
## Rectangle:
    def area(a, b):
    - Принимает число a и число b, возвращает число a умноженное на число b
        return a * b

    def perimeter(a, b):
    - Принимает число a и число b, возвращает сумму чисел a и b, умноженную на 2
        return 2*(a + b)
a = 3
b = 4
print(area(a, b))
print(perimeter(a, b))

## Square:
    def area(a):
    - Принимает число a, возвращает квадрат числа а
        return a * a

    def perimeter(a):
    - Принимает число a, возвращает число a умноженное на 4
        return 4 * a
a = 3
print(area(a))
print(perimeter(a))

## Tringle:
    def area(a, h):
    - Принимает число a и число h, возвращает среднее геометрическое чисел а и b
        return a * h / 2

    def perimeter(a, b, c):
    - Принимает число a, число b и число с, возвращает сумму чисел a,b,c
        return a + b + с
a = 3
b = 4
c = 5
print(area(a, b))
print(perimeter(a, b, c))

#History of project:
* e28e290aeab265494eb9646c04f9f5417446afc5 (HEAD -> main) added unittests
* ffdbf7a1ad11f6345e1b74ecb61662d6a8e325b0 (origin/main, origin/HEAD) better readme 2.0
* c0395a259d9e3eac635664eb59d7beb6282c99b3 better readme
* 06e63a62a3bf1c62013a98223ddc0151a0f275ae updated readme file
* c3836e8072757e797debdff723b077a6f8777358 Added comments to function
* 059bcc3ca4cff3652ca783d641f35b7e239eb56e corrected mistake in recyangle.py
* 05131862823049ac3d46fe698eb92122937b2d4a new fail added
* d078c8d9ee6155f3cb0e577d28d337b791de28e2 L-03: Docs added
* 8ba9aeb3cea847b63a91ac378a2a6db758682460 L-03: Circle and square added

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

class Test_Functions_Circle(unittest.TestCase):
    -Проверяет корректность выполнения функции area для различных числовых значений
    def test_area(self):
        self.assertEqual(area(-1), math.pi)
        self.assertEqual(area(0), 0)
        self.assertAlmostEqual(area(2.5), 5 * math.pi)

    def test_perimeter(self):
     -Проверяет корректность выполнения функции area для различных числовых значений
        self.assertEqual(perimeter(1), 2 *  math.pi)
        self.assertEqual(perimeter(0), 0)
        self.assertAlmostEqual(perimeter(-2), -4 * math.pi)

    def test_invalid_input(self):
     -Проверяет результат выполнения функций для ввода нечисловых значений
        with self.assertRaises(TypeError):
            area('a')
            perimeter('b')

    if name == 'main':
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

class Test_Functions_Rectangle(unittest.TestCase):

    def test_area(self):
 -Проверяет корректность выполнения функции area для различных числовых значений
        self.assertEqual(area(3, -4), -12)
        self.assertEqual(area(0, 4), 0)
        self.assertAlmostEqual(area(2.5, 3.5), 8.75)

    def test_perimeter(self):
 -Проверяет корректность выполнения функции perimeter для различных числовых значений
        self.assertEqual(perimeter(-3, 4), 2)
        self.assertEqual(perimeter(0, 4), 8)
        self.assertAlmostEqual(perimeter(2.5, 3.5), 12.0)

    def test_invalid_input(self):
-Проверяет результат выполнения функций для ввода нечисловых значений
        with self.assertRaises(TypeError):
            area('a', 'b')
            perimeter('a', 'b')    

    if name == 'main':
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

    class Test_Functions_Square(unittest.TestCase):

    def test_area(self):
     -Проверяет корректность выполнения функции area для различных числовых значений
        self.assertEqual(area(-3), 9)
        self.assertEqual(area(0), 0)
        self.assertAlmostEqual(area(2.5), 6.25)

    def test_perimeter(self):
      -Проверяет корректность выполнения функции perimeter для различных числовых значений
        self.assertEqual(perimeter(-3), -12)
        self.assertEqual(perimeter(0), 0)
        self.assertAlmostEqual(perimeter(2.5), 10.0)

    def test_invalid_input(self):
-Проверяет результат выполнения функций для ввода нечисловых значений
        with self.assertRaises(TypeError):
            area('a')
            perimeter('b')

    if name == 'main':
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

    class Test_Functions_Triangle(unittest.TestCase):

    def test_area(self):
    -Проверяет корректность выполнения функции area для различных числовых значений
        self.assertAlmostEqual(area(-3, 4), -6)
        self.assertEqual(area(0, 4), 0)
        self.assertAlmostEqual(area(5, 6.5), 16.25)

    def test_perimeter(self):
     -Проверяет корректность выполнения функции perimeter для различных числовых значений
        self.assertEqual(perimeter(3.5, 4.5, 5), 13)
        self.assertEqual(perimeter(0, 4, 5), 9)
        self.assertEqual(perimeter(-5, 6, 7), 8)

    def test_invalid_input(self):
-Проверяет результат выполнения функций для ввода нечисловых значений
        with self.assertRaises(TypeError):
            area('a', 'b')
            perimeter('a', 'b', 'c')

 if name == 'main':
        unittest.main()
    -вызов юниттеста



   