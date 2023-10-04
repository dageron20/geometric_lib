# A set of functions for calculating the area and perimeter of some shapes
___
# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
--- 
# Содержание проекта
#### Проект состоит из файлов:
- circle.py
- rectangle.py
- triangle.py
- square.py

Ниже приведены способы работы с данными файлам и функциями, которые они содержут

## Файл circle.py
Содержит две функции:

1. area(r) - принимает число r - радиус окружности, возвращает площадь окружности
- Пример вызова:  

```python
from circle import area
circleArea = area(2)
print(circleArea) # 4pi
```
2. perimiter(r) - принимает число r - радиус окружности, возвращает периметр (длину) окружности
- Пример вызова:
```python
from circle import perimeter
circlePerimeter = perimeter(2)
print(circlePerimeter) # 4pi
```

## Файл rectangle.py
Содержит две функции:

1. area(a, b) - принимает числа a, b - стороны прямоугольника, возвращает площадь прямоугольника
- Пример вызова:

```python
from rectangle import area
rectangleArea = area(2, 3)
print(rectangleArea) # 6
```
2. perimiter(a, b) - принимает числа a, b - стороны прямоугольника, возвращает периметр прямоугольника
- Пример вызова:
```python
from rectangle import perimeter
circlePerimeter = perimeter(4, 9)
print(circlePerimeter) # 26
```

## Файл square.py
Содержит две функции:

1. area(a) - принимает число a - сторона квадрата, возвращает площадь квадрата  
- Пример вызова:

```python
from square import area
squareArea = area(50)
print(squareArea) # 2500
```
2. perimiter(a) - принимает число a - сторона квадрата, возвращает периметр квадрата
- Пример вызова:
```python
from square import perimeter
squarePerimeter = perimeter(4)
print(squarePerimeter) # 16
```

## Файл triangle.py
Содержит две функции:

1. area(a, h) - принимает два числа: a - сторона треугольника, число h - высота, опущенная на сторону а. Возвращает площадь треугольника
- Пример вызова:

```python
from triangle import area
triangleArea = area(50, 10)
print(triangleArea) # 500
```
2. perimiter(a, b, c) - Принимает числа a, b и c - стороны треугольника, возвращает периметр треугольника
- Пример вызова:
```python
from triangle import perimeter
trianglePerimeter = perimeter(3, 4, 5)
print(trianglePerimeter) # 12
```

___
# История изменения комитов
3bd17ce: Add new file and fix issue in rectangle.py  
a4b396c: Add new file rectangle.py  
d078c8d: L-03: Docs added  
8ba9aeb: L-03: Circle and square added  
