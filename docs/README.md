# Общее описание решения
**В данном проекте представлены математические формулы для нахождения площади и периметра круга, прямоугольника, квадрата, треугольника**

# Описание работы файла circle.py:

## Описание работы функции area(r):

+ Возвращает площадь круга.

### Параметры:
+ `r(int/float)`: радиус круга

### Возвращаемое значение:
+ `math.pi * r * r (int/float)`: площадь круга

### Пример вызова функции:

+ area(1.5)  
  Output: 7.068583

## Описание работы функции perimeter(r):

+ Возвращает длину окружности

### Параметры:
+ `r(int/float)`: радиус круга

### Возвращаемое значение:
+ `2 * math.pi * r (int/float)`: длина окружности

### Пример вызова функции:

+ perimeter(1.5)  
  Output: 9.424778

# Описание работы файла rectangle.py:

## Описание работы функции area(a,b):

+ Возвращает площадь прямоугольника со сторонами a и b.

### Параметры:
+ `a (int/float)`: ширина прямоугольника
+ `b (int/float)`: длина прямоугольника

### Возвращаемое значение:
+ `a * b (int/float)`: площадь прямоугольника

### Пример вызова функции:

+ area(5,4)  
  Output: 20

## Описание работы функции perimeter(a,b):

+ Возвращает периметр прямоугольника со сторонами a и b.

### Параметры:
+ `a (int/float)`: ширина прямоугольника
+ `b (int/float)`: длина прямоугольника

### Возвращаемое значение:
+ `2*(a + b) (int/float)`: периметр прямоугольника

### Пример вызова функции:

+ perimeter(5,4)  
  Output: 18

# Описание работы файла square.py:

## Описание работы функции area(a):

+ Возвращает площадь квадрата со сторонами длины а.

### Параметры:
+ `a (int/float)`: длина стороны квадрата

### Возвращаемое значение:
+ `a * a (int/float)`: площадь квадрата

### Пример вызова функции:

+ area(5)  
  Output: 25

## Описание работы функции perimeter(a):

+ Возвращает периметр квадрата со сторонами длины а.

### Параметры:
+ `a (int/float)`: длина стороны квадрата

### Возвращаемое значение:
+ `4*a (int/float)`: периметр квадрата

### Пример вызова функции:

+ perimeter(5)  
  Output: 20

# Описание работы файла triangle.py:

## Описание работы функции area(a,h):

+ Возвращает площадь треугольника с основанием длины а и высотой длины h.

### Параметры:
+ `a (int/float)`: длина основания треугольника
+ `h (int/float)`: длина высоты треугольника

### Возвращаемое значение:
+ `a * h / 2 (int/float)`: площадь треугольника

### Пример вызова функции:

+ area(5,4)  
  Output: 10

## Описание работы функции perimeter(a,h):

+ Возвращает периметр треугольника со сторонами длины a,b,c.

### Параметры:
+ `a (int/float)`: длина стороны треугольника
+ `b (int/float)`: длина стороны треугольника
+ `c (int/float)`: длина стороны треугольника

### Возвращаемое значение:
+ `a + b + c (int/float)`: периметр треугольника

### Пример вызова функции:
+ perimeter(5,4,3)  
  Output: 12

# История изменений проекта
```
commit 64254a8e0f26aa674972eab0bceeeff62a3440a0 (HEAD -> main, origin/main, origin/HEAD)
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Fri Oct 6 10:02:51 2023 +0300

    Исправил пример вызова функции в triangle.py
```
```
commit a9f7c51695c99a28c49a611c7c4df17626297f68
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Fri Oct 6 10:02:02 2023 +0300

    Исправил пример вызова функции в square.py
```
```
commit 0429ff4404ee719abdb9762e1b02527b6fd7e136
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Fri Oct 6 10:01:05 2023 +0300

    Исправил пример вызова функции в rectangle.py
```
```
commit e0750027f6783549b73a89f0ebac24e9619b8973
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Fri Oct 6 09:59:00 2023 +0300

    Исправил пример вызова функции в circle,py
```
```
commit f02dc81be599ccfaa6c566e215e7e42a037cad14
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Fri Oct 6 09:57:59 2023 +0300

    Update README.md
```
```
commit 84fb42f6545e760236fbfd9e99eae8c03c95b6d7
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Fri Oct 6 09:55:41 2023 +0300

    Исправил пример вызова функции
```
```
commit 920f6a484b5721198dedd1db2ea4e3056c5acc83
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Fri Oct 6 09:53:58 2023 +0300

    Исправил пример вызова функций
```
```
commit 84fb42f6545e760236fbfd9e99eae8c03c95b6d7 (HEAD -> main, origin/main, origin/HEAD)
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Fri Oct 6 09:55:41 2023 +0300

    Исправил пример вызова функции
```
```
commit 920f6a484b5721198dedd1db2ea4e3056c5acc83
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Fri Oct 6 09:53:58 2023 +0300

    Исправил пример вызова функций
```
```
commit 2924e932e4b7d7ce48e15695892b51d6a2e46266
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Thu Oct 5 23:44:04 2023 +0300

    Update README.md
```
```
commit 87d6a36eba1be2e12a5996d7127440705a81c869
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Thu Oct 5 23:41:37 2023 +0300

:...skipping...
```
```
commit 84fb42f6545e760236fbfd9e99eae8c03c95b6d7 (HEAD -> main, origin/main, origin/HEAD)
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Fri Oct 6 09:55:41 2023 +0300

    Исправил пример вызова функции
```
```
commit 920f6a484b5721198dedd1db2ea4e3056c5acc83
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Fri Oct 6 09:53:58 2023 +0300

    Исправил пример вызова функций
```
```
commit 2924e932e4b7d7ce48e15695892b51d6a2e46266
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Thu Oct 5 23:44:04 2023 +0300

    Update README.md
```
```
commit 87d6a36eba1be2e12a5996d7127440705a81c869
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Thu Oct 5 23:41:37 2023 +0300

    Update README.md
```
```
commit 15bbaa73a961db855b296a52f710f539ab50866a
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Thu Oct 5 23:38:38 2023 +0300

    Update README.md
```
```
commit f22075c0fee24e7ea2a41beca3a0aaef3382da38
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Wed Oct 4 23:42:14 2023 +0300

    Update README.md
```
```
commit 65541b00cc288f43051980acf7ae8d7cb76a6d62
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Wed Oct 4 23:36:21 2023 +0300

    Update README.md
```
```
commit 1a615fd69049a7ef410cc8a50e1f368a11a41232
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Wed Oct 4 23:31:58 2023 +0300

    Update README.md
```
```
commit f0d0ec883d5724cc21c81d59880835d890d014ee
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Wed Oct 4 23:31:27 2023 +0300

    Update README.md
```
```
commit 178575aa58e8269ef032f245eb1d7f5bc09237e6
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Wed Oct 4 23:25:40 2023 +0300

    Update README.md
```
```
commit 361812da7f6280c5cdb956a67981b6fb7e83e5fa
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Wed Oct 4 23:08:44 2023 +0300

    Update triangle.py
```
```
commit 3537698097eebf4e0484f6f7ead5cbe03cb05f10
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Wed Oct 4 22:25:56 2023 +0300

    Добавил описание функций
```
```
commit 4a6dc54fa68fc522dcebff6621c997c07480c3d0
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Wed Oct 4 22:25:36 2023 +0300

    Добавил
```
```
commit 770b1cb346a6c9b750e844bd3d9a0592e978e33b
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Wed Oct 4 22:21:49 2023 +0300

    Добавил описание функций
```
```
commit d6c08baaf69b4bc111099c56830c298393456186
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Wed Oct 4 22:19:09 2023 +0300

    Исправил ошибку в описании функций
```
```
commit 7a429281d2fd7baee06430a88db4a63bedf680f5
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Wed Oct 4 22:17:23 2023 +0300

    Добавил описание функций
```
```
commit 54da83bb9ecd820b91f5e09f7712181292596e68
Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
Date:   Wed Oct 4 22:10:00 2023 +0300

    Добавил описание функций
```
```
commit 398b940b26fc597fb7a02500cc497f6b752d6c43
Author: Soltan Dydymov <sodidimov2005@gmail.com>
Date:   Sat Sep 9 17:56:25 2023 +0300

    Исправил ошибку
```
```
commit d99d4c25a9fc35529b1c8eff22ea64c584441722
Author: Soltan Dydymov <sodidimov2005@gmail.com>
Date:   Sat Sep 9 17:54:10 2023 +0300

    Добавил файл
```
```
commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added
```
```
commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added
```
