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
