# Подсчет площадей и периметров разных фигур
Этот проект создан для того, чтобы считать площади и периметры кругов, квадратов, прямоугольников и треугольников
## Файл circle.py
### Функция area
- Считает площадь круга по его радиусу
- Circle: S = πR²
```python
circle_area = area(3)
print (circle_area)
```
### Функция perimeter
- Считает периметр круга по его радиусу
- Circle: P = 2πR
```python 
circle_perimeter = perimeter(3)
print (circle_area)
```
## Файл rectangle.py
### Функция area
- Считает площадь прямоугольника по его сторонам
- Rectangle: S = ab
```python
rectangle_area = area(3, 4)
print (rectangle_area)
```
### Функция perimeter
- Считает периметр прямоугольника в зависимости от его сторон 
- Rectangle: P = 2a + 2b
```python
rectangle_perimeter = perimeter(3, 4)
print (rectangle_perimeter)
```
## Файл square.py
### Функция area
- Считает площадь квадрата в зависимости от его стороны
- Square: S = a²
```python
square_area = area(3)
print (square_area)
```
### Функция perimeter
- Считает периметр квадрата в зависимости от его стороны
- Square: P = 4a
```python
square_perimeter = perimeter(3)
print (square_perimeter)
```
## Файл triangle.py
### Функция area
- Считает площадь треугольника по его стороне и высоте, проведенной к ней
- Triangle: S = ah/2
```python
triangle_area = area(3, 4)
print (triangle_area)
```
### Функция perimeter
- Считает периметр треугольника в зависимости от его сторон
- Triangle: P = a+b+c
```python
triangle_perimeter = perimeter(3, 4, 5)
print (triangle_perimeter)
```
## История коммитов
- 7673f6658d7bb61cfc1c20af2a9ac2bef29dc6a9 added unittest
- 20b1d2b925d45c07b83d9544468c5287a89c1ceb Update triangle.py
- dc69550500ce85b183acdc0584dce55832d51278 Update square.py
- ad66bc5d813cf9c9ee3a933854d049747b64ac4c Update rectangle.py
- d5a39d76546895cfe66dc3c74e9214e145bc7585 Update circle.py
- 7415e8b50d082af6da240cfb8a6498005c2b12bb Исправлена ошибка в файле rectangle
- 2da68a849da67dfd594e2d597ed7881513021093 добавлен новый файл triangle
- cb8f1efa26b3b55b4cf8e81f0d2fff14e4ed228d добавлен новый файл
- d078c8d9ee6155f3cb0e577d28d337b791de28e2 L-03: Docs added
- 8ba9aeb3cea847b63a91ac378a2a6db758682460 L-03: Circle and square added
## Unit tests
- Добавлены тесты, которые проверяют корректность работы функций в файлах rectangle.py, circle.py, square.py и triangle.py. Эти тесты не возвращают информацию об ошибке, а просто возвращают информацию о тесте, в котором произошла эта ошибка. Программа имеет несколько недачетов: функции по нахождения площади и периметра не могут работать с данными в строковом типе, а так же выводят 0 если один из переданных в них аргументов был равен 0. 
### Результаты ручного тестирования
| Тестируемая функция         | Входные данные    | Ожидаемый результат         | Результат |
|-----------------------------|-------------------|-----------------------------|-----------|
| circle.area(a)              | a = 0             | "There is no such figure"   | false     |
| circle.area(a)              | a = -12           | "args should be > 0"        | false      |
| circle.perimeter(a)         | a = 0             | "There is no such figure"   | false      |
| circle.perimeter(a)         | a = -1            | "args should be > 0"        | false      |
| rectangle.area(a)           | a = 0             | "There is no such figure"   | false      |
| rectangle.area(a)           | a = -12           | "args should be > 0"        | false      |
| rectangle.perimeter(a)      | a = 0             | "There is no such figure"   | false      |
| rectangle.perimeter(a)      | a = -1            | "args should be > 0"        | false      |
| square.area(a)              | a = 0             | "There is no such figure"   | false      |
| square.area(a)              | a = -12           | "args should be > 0"        | false      |
| square.perimeter(a)         | a = 0             | "There is no such figure"   | false      |
| square.perimeter(a)         | a = -1            | "args should be > 0"        | false      |
| triangle.area(a)            | a = 0             | "There is no such figure"   | false      |
| triangle.area(a)            | a = -12           | "args should be > 0"        | false      |
| triangle.perimeter(a)       | a = 0             | "There is no such figure"   | false      |
| triangle.perimeter(a)       | a = -1            | "args should be > 0"        | false      |
| triangle.perimeter(a, b, c) | a = 1 b = 3 c = 6 | "There is no such triangle" | false      |
### Результаты unittest-ов
| Название теста              | Входные данные          | Ожидаемый результат | Результат |
|-----------------------------|-------------------------|---------------------|-----------|
| Circle area int test        | a = 3                   | 28.274333882308138  | true      |
| Circle area zero test       | a = 0                   | 0                   | true      |
| Circle area float test      | a = 5.442               | 93.03940997578762   | true      |
| Circle perimeter int test   | a = 3                   | 18.84955592153876   | true      |
| Circle perimeter zero test  | a = 0                   | 0                   | true      |
| Circle perimeter float test | a = 5.442               | 34.193094441671306  | true      |
| Rectangle area int test        | a = 3 b = 4             | 12                  | true      |
| Rectangle area zero test       | a = 0 b = 0             | 0                   | true      |
| Rectangle area float test      | a = 5.4 b = 4.8         | 25.92               | true      |
| Rectangle perimeter int test   | a = 3 b = 4             | 14                  | true      |
| Rectangle perimeter zero test  | a = 0 b = 0             | 0                   | true      |
| Rectangle perimeter float test | a = 5.4 b = 4.8         | 20.4                | true      |
| Square area int test        | a = 3                   | 9                   | true      |
| Square area zero test       | a = 0                   | 0                   | true      |
| Square area float test      | a = 5.4                 | 29.160000000000004  | true      |
| Square perimeter int test   | a = 3                   | 12                  | true      |
| Square perimeter zero test  | a = 0                   | 0                   | true      |
| Square perimeter float test | a = 5.4                 | 21.6                | true      |
| Triangle area int test        | a = 3 b = 4             | 6                   | true      |
| Triangle area zero test       | a = 0 b = 0             | 0                   | true      |
| Triangle area float test      | a = 5.4 b = 4.8         | 12.96               | true      |
| Triangle perimeter int test   | a = 3 b = 4 c = 5       | 12                  | true      |
| Triangle perimeter zero test  | a = 0 b = 0 c = 0       | 0                   | true      |
| Triangle perimeter float test | a = 5.4 b = 4.8 c = 6.7 | 16.9                | true      |




