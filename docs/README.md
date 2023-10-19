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
 
 ## Добавлены функции для вычисления площади и периметра для следующих фигур: Круг, Прямоугольник, Квадрат и Треугольник

 # Описание функции
 
 ## Вычисление площади и периметра для фигуры: Круг
```python
import math

def area(r):
return math.pi * r * r

def perimeter(r):
return 2 * math.pi * r
```

Библиотека **math** предоставляет набор функций для выполнения математических, тригонометрических и логарифмических операций.
В нашем случае используется для добавления работы с числом **pi**.
```python
import math
```
Функция для вычисления площади берет число **r**. Число **r** - радиус круга.
```python
import math

def area(r):
```
Инструкция **return** говорит, что нужно вернуть значение. В нашем случае функция возвращает площадь круга.
```python
import math

def area(r):
return math.pi * r * r
```
Функция для вычисления периметра берет число **r**. Число **r** - радиус круга.
```python
import math

def area(r):
return math.pi * r * r

def perimeter(r):
```
Инструкция **return** говорит, что нужно вернуть значение. В нашем случае функция возвращает периметр круга.
```python
import math

def area(r):
return math.pi * r * r

def perimeter(r):
return 2 * math.pi * r
```
## Примеры выводов
```python
import math

def area(r):
return math.pi * r * r

def perimeter(r):
return 2 * math.pi * r

int r = 3
print(area(r))
print(perimeter(r))
```

 ## Вычисление площади и периметра для фигуры: Прямоугольник 
```python
def area(a, b): 
return a * b 

def perimeter(a, b): 
return (a + b)*2
```

Функция для вычисления площади берет числа **a** и **b**. Числа **a** и **b** - стороны прямоугольника.
```python
def area(a, b): 
```
Инструкция **return** говорит, что нужно вернуть значение. В нашем случае функция возвращает площадь прямоугольника.
```python
import math

def area(a, b): 
return a * b 
```
Функция для вычисления периметра берет числа **a** и **b**. Числа **a** и **b** - стороны прямоугольника.
```python
def area(a, b): 
return a * b 

def perimeter(a, b): 
```
Инструкция **return** говорит, что нужно вернуть значение. В нашем случае функция возвращает периметр прямогульника.
```python
def area(a, b): 
return a * b 

def perimeter(a, b): 
return (a + b)*2
```

## Примеры выводов
```python
def area(a, b): 
return a * b 

def perimeter(a, b): 
return (a + b)*2

int a = 3
int b = 4
print(area(a,b))
print(perimeter(a,b))
```

 ## Вычисление площади и периметра для фигуры: Квадрат
```python
def area(a):
return a * a

def perimeter(a):
return 4 * a
```

Функция для вычисления площади берет число **a**. Число **a** - сторона квадрата.
```python
def area(a):
```
Инструкция **return** говорит, что нужно вернуть значение. В нашем случае функция возвращает площадь квадрата.
```python
def area(a):
return a * a
```
Функция для вычисления площади берет число **a** и умножает. Число **a** - сторона квадрата.
```python
def area(a):
return a * a

def perimeter(a):
```
Инструкция **return** говорит, что нужно вернуть значение. В нашем случае функция возвращает периметр квадрата.
```python
def area(a):
return a * a

def perimeter(a):
return 4 * a
```

## Примеры выводов
```python
def area(a):
return a * a

def perimeter(a):
return 4 * a

int a=3
print(area(a))
print(perimeter(a))
```

 ## Вычисление площади и периметра для фигуры: Треугольник
```python
def area(a, h): 
return a * h / 2 

def perimeter(a, b, c)
return a + b + c 
```

Функция для вычисления площади берет число **a** и число **h**. Число **a** - сторона треугольника, число **h** - высота треугольника.
```python
def area(a, h): 
```
Инструкция **return** говорит, что нужно вернуть значение. В нашем случае функция возвращает площадь треугольника.
```python
def area(a, h): 
return a * h / 2 
```
Функция для вычисления периметра берет числа **a**, **b** и **c**. Числа **a**, **b** и **c** - стороны треугольника.
```python
def area(a, h): 
return a * h / 2 

def perimeter(a, b, c)
```
Инструкция **return** говорит, что нужно вернуть значение. В нашем случае функция возвращает периметр треугольника.
```python
def area(a, h): 
return a * h / 2 

def perimeter(a, b, c)
return a + b + c 
```

## Примеры выводов
```python
def area(a, h): 
return a * h / 2 

def perimeter(a, b, c)
return a + b + c

int a=5
int b=6
int c=7
int h=3
print(area(a, h))
print(perimeter(a,b,c))
```

## История изменения проекта с хешами комитов
> commit f27a2693297b2ef472f537d96c46094b5329db52
- Автор: Danik <danikitmo.gmail.com>
- Дата: Thu Sep 21 21:03:51 2023 +0300
- Added rectangle

> commit 4dd6020b2f7c5a56e4f68960751c8ecb7746af75 (HEAD => new_features_408869)
- Автор: Danik <danikitmo.gmail.com>
- Дата: Thu Sep 21 21:22:41 2023 +0300
- Исправление ошибки

> commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, main)
- Автор: smartiqa <info@smartiqa.ru>
- Дата: Thu Mar 4 14:55:29 +0300
- Docs added


