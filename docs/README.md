# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

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

+ area(1.5) = 7.068583

## Описание работы функции perimeter(r):

+ Возвращает длину окружности

### Параметры:
+ `r(int/float)`: радиус круга

### Возвращаемое значение:
+ `2 * math.pi * r (int/float)`: длина окружности

### Пример вызова функции:

+ perimeter(1.5) = 9.424778

# Описание работы файла rectangle.py:

## Описание работы функции area(a,b):

+ Возвращает площадь прямоугольника со сторонами a и b.

### Параметры:
+ `a` (int/float): ширина прямоугольника
+ `b` (int/float): длина прямоугольника

### Возвращаемое значение:
+ `a * b (int/float)`: площадь прямоугольника

### Пример вызова функции:

+ area(5,4) = 20

## Описание работы функции perimeter(a,b):

+ Возвращает периметр прямоугольника со сторонами a и b.

### Параметры:
+ `a` (int/float): ширина прямоугольника
+ `b` (int/float): длина прямоугольника

### Возвращаемое значение:
+ `2*(a + b) (int/float)`: периметр прямоугольника

### Пример вызова функции:

+ perimeter(5,4) = 18

# Описание работы файла square.py:

## Описание работы функции area(a):

+ Возвращает площадь квадрата со сторонами длины а.

### Параметры:
+ `a` (int/float): длина стороны квадрата

### Возвращаемое значение:
+ `a * a (int/float)`: площадь квадрата

### Пример вызова функции:

+ area(5) = 25

## Описание работы функции perimeter(a):

+ Возвращает периметр квадрата со сторонами длины а.

### Параметры:
+ `a` (int/float): длина стороны квадрата

### Возвращаемое значение:
+ `4*a (int/float)`: периметр квадрата

### Пример вызова функции:

+ perimeter(5) = 20

# Описание работы файла triangle.py:

## Описание работы функции area(a,h):

+ Возвращает площадь треугольника с основанием длины а и высотой длины h.

### Параметры:
+ `a` (int/float): длина основания треугольника
+ `h` (int/float): длина высоты треугольника

### Возвращаемое значение:
+ `a * h / 2` (int/float)`: площадь треугольника

### Пример вызова функции:

+ area(5,4) = 10

## Описание работы функции perimeter(a,h):

+ Возвращает периметр треугольника со сторонами длины a,b,c.

### Параметры:
+ `a` (int/float): длина стороны треугольника
+ `b` (int/float): длина стороны треугольника
+ `c` (int/float): длина стороны треугольника

### Возвращаемое значение:
+ `a + b + c` (int/float): периметр треугольника

### Пример вызова функции:
+ perimeter(5,4,3) = 12

# История изменений проекта
+ commit 361812da7f6280c5cdb956a67981b6fb7e83e5fa (HEAD -> main, origin/main, origin/HEAD)
  Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
  Date:   Wed Oct 4 23:08:44 2023 +0300

      Update triangle.py

+ commit 3537698097eebf4e0484f6f7ead5cbe03cb05f10
  Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
  Date:   Wed Oct 4 22:25:56 2023 +0300

      Добавил описание функций

+ commit 4a6dc54fa68fc522dcebff6621c997c07480c3d0
  Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
  Date:   Wed Oct 4 22:25:36 2023 +0300

      Добавил

+ commit 770b1cb346a6c9b750e844bd3d9a0592e978e33b
  Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
  Date:   Wed Oct 4 22:21:49 2023 +0300

  :...skipping...
+ commit 361812da7f6280c5cdb956a67981b6fb7e83e5fa (HEAD -> main, origin/main, origin/HEAD)
  Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
  Date:   Wed Oct 4 23:08:44 2023 +0300

      Update triangle.py

+ commit 3537698097eebf4e0484f6f7ead5cbe03cb05f10
  Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
  Date:   Wed Oct 4 22:25:56 2023 +0300

      Добавил описание функций

+ commit 4a6dc54fa68fc522dcebff6621c997c07480c3d0
  Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
  Date:   Wed Oct 4 22:25:36 2023 +0300

      Добавил

+ commit 770b1cb346a6c9b750e844bd3d9a0592e978e33b
  Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
  Date:   Wed Oct 4 22:21:49 2023 +0300

      Добавил описание функций

+ commit d6c08baaf69b4bc111099c56830c298393456186
  Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
  Date:   Wed Oct 4 22:19:09 2023 +0300

      Исправил ошибку в описании функций

+ commit 7a429281d2fd7baee06430a88db4a63bedf680f5
  Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
  Date:   Wed Oct 4 22:17:23 2023 +0300

      Добавил описание функций

+ commit 54da83bb9ecd820b91f5e09f7712181292596e68
  Author: Soltan Dydymov <144336474+Soltan-Dydymov@users.noreply.github.com>
  Date:   Wed Oct 4 22:10:00 2023 +0300

      Добавил описание функций

+ commit 398b940b26fc597fb7a02500cc497f6b752d6c43
  Author: Soltan Dydymov <sodidimov2005@gmail.com>
  Date:   Sat Sep 9 17:56:25 2023 +0300

      Исправил ошибку

+ commit d99d4c25a9fc35529b1c8eff22ea64c584441722
  Author: Soltan Dydymov <sodidimov2005@gmail.com>
  Date:   Sat Sep 9 17:54:10 2023 +0300

      Добавил файл

+ commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
  Author: smartiqa <info@smartiqa.ru>
  Date:   Thu Mar 4 14:55:29 2021 +0300

      L-03: Docs added

+ commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
  Author: smartiqa <info@smartiqa.ru>
  Date:   Thu Mar 4 14:54:08 2021 +0300

