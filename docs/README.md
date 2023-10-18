# Description of function:
## Circle:
    import math

    - Импортирую библиотеку math для того чтобы использовать число пи

    def area(r):
    - Принимет значение r, параметры:r - это радиус
    пример вызова:area(4)

    def perimeter(r):
    - Принимет значение r, где r - это радиус, возвращает периметр круга
        return 2 * math.pi * r
```
b = 4
print(area(b))
print(perimeter(b))
```
## Rectangle:
    def area(a, b):
    - Принимает значение a и b, возвращает площадь прямоугольника.
   параметры:a - это сторона прямоугольника, b - это сторона прямоугольникa
   пример вызова:area(3,9)
        return a * b

    def perimeter(a, b):
    - Принимает значение a и b, где a и b - это стороны прямоугольника, возвращает периметр прямоугольника
        return 2*(a + b)
```
a = 3
b = 9
print(area(a,b))
print(perimeter(a,b))
```
## Square:
    def area(a):
    - Принимает значение a, возвращает площадь квадрата.
  параметры:a - это сторона квадрата
  пример вызова:area(7)
        return a * a

    def perimeter(a):
    - Принимает значение a, где а - это сторона квадрата, возвращает периметр квадрата
        return 4 * a
```
a = 7
print(area(a))
print(perimeter(a))
```
## Tringle:
    def area(a, h):
    - Принимает значение a и h, возвращает площадь треугольника.
  параметры:a - это сторона треугольника, h - это высота треугольника
  пример вызова:area(6,8)
        return a * h / 2

    def perimeter(a, b, c):
    - Принимет значение a,b,c, где a,b,c - это стороны треугольника, возвращает периметр треугольника
        return a + b + с
```
a = 6
h = 8
b = 1
c = 2
print(area(a,h))
print(perimeter(a,b,c))
```

#History of commit:
commit 90fed5769fc50363651f9f63b18d5e101d31dba0 (origin/main, origin/HEAD)
Author: Дарья Войтович <dashavoitovich2006@gmail.com>
Date:   Thu Sep 21 19:38:40 2023 +0300

    fixed a bug
commit caf350acd135f38846272adff44b1e46b000c5aa
Author: Дарья Войтович <dashavoitovich2006@gmail.com>
Date:   Thu Sep 21 18:12:44 2023 +0300

    add new file

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added
