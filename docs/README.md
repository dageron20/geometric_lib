# **Labwork 3**
## Unit tests
Данный проект содержит файл tests.py в директории tests, который проверяет на валидность площадь и периметр фигур, расположенных в директории bin.

### Test functions
#### Circle Test Case
- ```test_zero_multiply```: Проверяет ```area()``` и ```perimeter()```  __circle.py__. Подставляет радиус равный 0 и 0 и проверяет, что результатом работы программы являются числа 0 и 0 соответственно.
- ```test_integer_multiply```: Проверяет ```area()``` и ```perimeter()```  __circle.py__. Подставляет радиус равный 10 и 5 и проверяет, что результатом работы программы являются числа 314.1592653589793 и 31.41592653589793 соответственно.

#### Rectangle Test Case
- ```test_zero_multiply```: Проверяет ```area()``` и ```perimeter()```  __rectangle.py__. Подставляет стороны (0, 10) и (0, 0) и проверяет, что результатом работы программы являются числа 0 и 0 соответственно.
- ```test_integer_multiply```: Проверяет ```area()``` и ```perimeter()```  __rectangle.py__. Подставляет стороны (10, 5) и (5, 7) и проверяет, что результатом работы программы являются числа 50 и 24 соответственно.

#### Square Test Case
- ```test_zero_multiply```: Проверяет ```area()``` и ```perimeter()```  __square.py__. Подставляет стороны 0 и 0 и проверяет, что результатом работы программы являются числа 0 и 0 соответственно.
- ```test_integer_multiply```: Проверяет ```area()``` и ```perimeter()```  __square.py__. Подставляет стороны 4 и 9 и проверяет, что результатом работы программы являются числа 16 и 36 соответственно.

#### Triangle Test Case
- ```test_zero_multiply```: Проверяет ```area()``` и ```perimeter()```  __triangle.py__. Подставляет стороны равные (0, 3) и (0, 0, 0) и проверяет, что результатом работы программы являются числа 0 и 0 соответственно.
- ```test_integer_multiply```: Проверяет ```area()``` и ```perimeter()```  __triangle.py__. Подставляет стороны равные (3, 9) и (17, 23, 56) и проверяет, что работы результатом программы являются числа 13.5 и 56 соответственно.
  
### Test cases

| Название теста                     | Входные данные                                 | Ожидаемый результат                                          | Результат                                                    | Статус |
|------------------------------------|------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|--------|
| Circle - test_zero_multiply        | r = 0, 0                                       | 0, 0                                                         | 0, 0                                                         | True   |
| Circle - test_integer_multiply     | r = 10, r = 5                                  | 314.15927, 31.41593                                          | 314.15927, 31.41593                                          | True   |
| Circle - test_negative_multiply    | r = -10, -5                                    | Error: radius cannot be negative                             | Error: radius cannot be negative                             | True   |
| Circle - test_boolean_type         | r = True, r = True                             | Error: function cannot work with not integer or float values | Error: function cannot work with not integer or float values | True   |
| Circle - test_string_type          | r = "10", r = "5"                              | Error: function cannot work with not integer or float values | Error: function cannot work with not integer or float values | True   |
| Rectangle - test_zero_multiply     | a, b = (0, 10), (0, 0)                         | 0, 0                                                         | 0, 0                                                         | True   |
| Rectangle - test_integer_multiply  | a, b = (10, 5), (5, 7)                         | 50, 24                                                       | 0, 24                                                        | True   |
| Rectangle - test_negative_multiply | a, b = (-10, -5), (-5, -7)                     | Error: sides cannot be negative                              | Error: sides cannot be negative                              | True   |
| Rectangle - test_float_number      | a, b = (5.2, 5.2), (3.6, 3.6)                  | 18.72, 17.6                                                  | 18.72, 17.6                                                  | True   |
| Rectangle - test_boolean_type      | a, b = (True, True), (False, False)            | Error: function cannot work with not integer or float values | Error: function cannot work with not integer or float values | True   |
| Rectangle - test_string_type       | a, b = ("1", "2"), ("2", "3")                  | Error: function cannot work with not integer or float values | Error: function cannot work with not integer or float values | True   |
| Square - test_zero_multiply        | a = 0, 0                                       | 0, 0                                                         | 0, 0                                                         | True   |
| Square - test_integer_multiply     | a = 4, 9                                       | 16, 36                                                       | 16, 36                                                       | True   |
| Square - test_negative_multiply    | a = -4, -9                                     | Error: side cannot be negative                               | Error: side cannot be negative                               | True   |
| Square - test_float_number         | a = 7.7, 7.7                                   | 59.29, 30.8                                                  | 59.29, 30.8                                                  | True   |
| Square - test_boolean_type         | a = True, True                                 | Error: function cannot work with not integer or float values | Error: function cannot work with not integer or float values | True   |
| Square - test_string_type          | a = "123", "123"                               | Error: function cannot work with not integer or float values | Error: function cannot work with not integer or float values | True   |
| Triangle - test_zero_multiply      | a = 3, h = 0                                   | 0                                                            | 0                                                            | True   |
| Triangle - test_integer_multiply   | a = 3, 17, b = 23, c = 16, h = 9               | 13.5, 56                                                     | 13.5, 56                                                     | True   |
| Triangle - test_negative_multiply  | a = -3, -17, b = -23, c = -16, h = -9          | Error: sides cannot be negative                              | Error: sides cannot be negative                              | True   |
| Triangle - test_triangle_exist     | a = 7, b = 1, c = 2                            | Error: triangle doesn't exist                                | Error: sides cannot be negative                              | True   |
| Triangle - test_float_number       | a = 2.22, 2.22, b = 3.33, c = 4.44, h = 3.33   | 3.6963, 9.99                                                 | 3.6963, 9.99                                                 | True   |
| Triangle - test_boolean_type       | a = True, True, b = False, c = True, h = False | Error: function cannot work with not integer or float values | Error: function cannot work with not integer or float values | True   |
| Triangle - test_string_type        | a = "1", "2", b = "3", c = "4", h = "2"        | Error: function cannot work with not integer or float values | Error: function cannot work with not integer or float values | True   |

### Как запустить тесты

Для запуска тестов введите в консоль данную команду:
```
python.exe -m unittest tests/tests.py
```
____
# **Labwork 2**
# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Cirlce.py
## Описание функции

Программа содержит две функции и одну библиотеку:
1. def area(r):
    return (math.pi * r * r)
   
    >Возвращает площадь окружности.
    
    >Параметры:   
            r(int): Радиус окружности.
    
    >Возвращаемое значение:   
            int(math.pi * r * r): Площадь окружности.
    
    >Пример:  
        Входные данные: 10  
        Возвращаемое значение: 314,15926...и так далее.

2. def perimeter(r):  
    return 2 * math.pi * r
    >Возвращает периметр окружности.
    
    >Параметры:   
            r(int): Радиус окружности.
    
    >Возвращаемое значение:   
            int(2 * math.pi * r): Периметр окружности.
    
    >Пример:  
        Входные данные: 5 
        Возвращаемое значение: 31,415926...и так далее.

3. import math
    > Добавление библиотеки math. В контексте кода добавляет число Пи. (3.1415926...)


# Rectangle.py
## Описание функции

Программа содержит две функции:
1. def area(a, b):  
    return a * b
    >Возвращает площадь прямоугольника.  

    >Параметры: 
                a, b (int): Две стороны прямоугольника.  

    >Возвращаемое значение: 
                (a * b): Площадь прямоугольника. 

    >Пример:  
              Входные данные: 2, 5
              Возвращаемое значение: 10
    
2. def perimeter(a, b):  
       return (a + b) * 2
    >Возвращает периметр прямоугольника.

    >Параметры: 
                a, b (int): Две стороны прямоугольника.

    >Возвращаемое значение: 
                   ((a + b) * 2): Периметр прямоугольника.
    
    >Пример:  
              Входные данные: 2, 5
              Возвращаемое значение: 14



# Square.py
## Описание функции

Программа содержит две функции:
1. def area(a):  
    return a * a
    >Возвращает площадь квадрата. 

    >Параметры: 
                a(int): Сторона квадрата.

    >Возвращаемое значение: 
                (a * a): Площадь квадрата. 

    >Пример:  
              Входные данные: 5
              Возвращаемое значение: 25
    
2. def perimeter(a):  
    return 4 * a
    >Возвращает периметр квадрата.

    >Параметры: 
                a (int): Сторона квадрата.

    >Возвращаемое значение: 
                   (a * 4): Периметр квадрата.
    
    >Пример:  
              Входные данные: 5
              Возвращаемое значение: 20



# Triangle.py
## Описание функции

Программа содержит две функции:
1. def area(a, h):   
    return a * h / 2
    >Возвращает площадь треугольника. 

    >Параметры: 
                a, h(int): Сторона и высота треугольника.

    >Возвращаемое значение: 
                (a * h / 2): Площадь треугольника. 

    >Пример:  
              Входные данные: 10, 6
              Возвращаемое значение: 30
    
2. def perimeter(a, b, c):   
    return a + b + c
    >Возвращает периметр треугольника.

    >Параметры: 
                a, b, c (int): Стороны треугольника.

    >Возвращаемое значение: 
                   (a + b + c): Периметр треугольника.
    
    >Пример:  
              Входные данные: 3, 4, 5
              Возвращаемое значение: 9


## Хеши коммитов
1. **8ba9aeb3cea847b63a91ac378a2a6db758682460**  
Author: smartiqa <info@smartiqa.ru>  
Date:   Thu Mar 4 14:54:08 2021 +0300  
    L-03: Circle and square added


2. **d078c8d9ee6155f3cb0e577d28d337b791de28e2**  
Author: smartiqa <info@smartiqa.ru>  
Date:   Thu Mar 4 14:55:29 2021 +0300  
    L-03: Docs added


3. **4eebc7997c1c0b1b49580728bceced193f20b13b**  
Author: HirakiriShogun <hirakirishogun@gmail.com>  
Date:   Sat Sep 23 17:31:07 2023 +0300  
    add: add new rectangle.py file


4. **ae28fb7395d4f9c5f636a20ace26cc596b551aea (origin/main, origin/HEAD, main)**  
Author: HirakiriShogun <hirakirishogun@gmail.com>  
Date:   Sat Sep 23 17:44:45 2023 +0300  
    fix: fixed rectangle.py file


5. **9e732fe48a9b06029cb18c4b791e1bdc711462cf**
Author: HirakiriShogun <hirakirishogun@gmail.com>  
Date:   Thu Oct 5 18:25:18 2023 +0300  
    add: add documentation in rectangle.py


6. **a64e984707d91db82e53021d0b010435236f9c58**  
Author: HirakiriShogun <hirakirishogun@gmail.com>  
Date:   Thu Oct 5 18:31:53 2023 +0300  
    add: add documentation in triangle.py


7. **9df86dcf29f4f19e3c64d3cb8b9c20d620e67b5f**  
Author: HirakiriShogun <hirakirishogun@gmail.com>  
Date:   Thu Oct 5 18:51:27 2023 +0300  
    add: add documentation in square.py
