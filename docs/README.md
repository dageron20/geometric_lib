# Geometric Library
## Общее описание решения
Данный репозиторий включает в себя файлы для работы с простыми геометрическими фигурами, используя язык Python. В каждом файле 
хранятся функции нахождения площади и периметра одной из фигур.
## Описание каждой функции с примерами вызова
### circle.py
- area(r) - принимает число r, возвращает площадь круга с радиусом r

*Пример:*
```Python
area(3) #input: 3 ; output: ~28.26
```
- perimeter(r) - принимает число r, возвращает длину окружности с радиусом r

*Пример:*
```Python
perimeter(5) #input: 5 ; output: ~31.4
```
### rectangle.py
- area(a,b) - принимает значение сторон a и b прямоугольника, возвращает площадь прямоугольника

*Пример:*
```Python
area(3,2) #input: 3 , 2 ; output: 6
```
- perimeter(r) - принимает значение сторон a и b прямоугольника, возвращает периметр прямоугольника

*Пример:*
```Python
perimeter(5,9) #input: 5 , 9 ; output: 90
```
### square.py
- area(a) - принимает значение стороны a квадрата, возвращает площадь квадрата

*Пример:*
```Python
area(7) #input: 7 ; output: 49 
```
- perimeter(a) - принимает значение стороны a квадрата, возвращает периметр квадрата

*Пример:*
```Python
perimeter(3) #input: 3 ; output: 12
```
### triangle.py
- area(a,h) - принимает значение стороны a треугольника и прилежащей к ней высоте h, возвращает площадь треугольника

*Пример:*
```Python
area(7,4) #input: 7 , 4 ; output: 14 
```
- perimeter(a,b,c) - принимает значения сторон a,b и c треугольника, возвращает периметр треугольника

*Пример:*
```Python
perimeter(3,4,5) #input: 3 , 4 , 5 ; output: 12 
```

1.	Цели и задачи тестирования:

Цели:

-  Обнаружение недочетов в программме;
-  “Полировка” кода в случае найденных ошибок.
	
Задача заключается в проверке правильного вычисления функций в данных программных файлах. При проверке надо учесть все возможные частные случаи, которые могут повлиять на подсчет и вывести неожидаемый ответ.

2.	Описание тестируемого продукта:

Продуктом тестирования являются программые файлы, вычисляющие площадь и периметр фигур: круги, прямоугольники, треугольники и квадраты. Продукт должен корректно находить площадь или периметр фигуры, используя аргументы, введенные в функцию.

3.	Область тестрирования:

Функции perimeter и area в каждом программном файле. Количество аргументов функций зависит от расмматриваемой фигуры.

4.	Стратегия тестирования:

Для эффективности применяем функциональный тип тестированния, заключающийся в написании юниттестов, однако также можем тестировать продукт вручную. В основном будем пользоваться методом .assertEqual, который проверяет, соответствует ли результат подсчета функции ожидаемому результату.


5.	Критерии приемки:

-  Все частные случаи, которые могут быть обработаны функцией, учтены;
-  Ошибки найдены тестами и программы подкорректированны, чтобы они удовлетворяли все тесты.

6.	Ожидаемые результаты

Функции должны правильно считать периметр и площадь по правильным формулам. Тажке функции должны учесть частные случаи - такие как: использование строк, логических типов данных и неположительных чисел в качестве аргументов функций, в случае чего функции должны вывести “Invalid input”. Также надо учесть несуществуемые фигуры, например, треугольники с некорректными сторонами.

## Описание работы юнит-тестов tests.py

### Тесты для rectangle.py
- Тесты, проверяющие корректность вычисления площади и периметра прямоугольника.
#### test_positive_rec_area
- тест на корректность вычисления площади с вводом положительных чисел
#### test_non_positive_rec_area
- тест на корректность вычисления площади с вводом неположительных чисел
#### test_string_rec_area
- тест на корректность вычисления площади с вводом строк
#### test_bool_rec_area
- тест на корректность вычисления площади с вводом логических типов данных
#### test_positive_rec_perimeter
- тест на корректность вычисления периметра с вводом положительных чисел
#### test_non_positive_rec_perimeter
- тест на корректность вычисления периметра с вводом неположительных чисел
#### test_string_rec_perimeter
- тест на корректность вычисления периметра с вводом строк
#### test_bool_rec_perimeter
- тест на корректность вычисления периметра с вводом логических типов данных

| Номер кейса         |   Входные данные    |    Ожидаемый результат     |   Фактический результат    | Статус  |
|---------------------|:-------------------:|:--------------------------:|:--------------------------:|---------|   
| 1) area(a, b)         |    a = 5, b = 5     | 25 | 25 | Успешно | 
| 2) area(a, b)         |   a = 20, b = 4     |            80            |            80           | Успешно |
| 3) area(a, b)         |   a = 4, b = 20     |     80       |      80       | Успешно |
| 4) area(a, b)         |  a = 0, b = 0   |      Invalid input       |    Invalid input      | Успешно |
| 5) area(a, b)         | a = -1, b = 4 |      Invalid input      |    Invalid input      | Успешно |
| 6) area(a, b)        |    a = 4, b = -1    | Invalid input |Invalid input| Успешно | 
| 7) area(a, b)        |   a = -2, b = 0   |    Invalid input        |        Invalid input  | Успешно |
| 8) area(a, b)        |   a = 0, b = -2    |      Invalid input      |   Invalid input     | Успешно |
| 9) area(a, b)        |  a = -1, b = -10   |   Invalid input    |     Invalid input     | Успешно |
| 10) area(a, b)       | a = "A", b = 20 |    Invalid input      |   Invalid input       | Успешно |
| 11) area(a, b)       | a = 20, b = "A" |    Invalid input      |   Invalid input       | Успешно |
| 12) area(a, b)       | a = True, b = 4 |    Invalid input      |   Invalid input       | Успешно |
| 13) area(a, b)       | a = 4, b = True |    Invalid input      |   Invalid input       | Успешно |
| 14) area(a, b)       | a = False, b = 4 |    Invalid input      |   Invalid input       | Успешно |
| 15) area(a, b)        | a = 4, b = False |    Invalid input      |   Invalid input       | Успешно |
| 16) perimeter(a, b)  |    a = 5, b = 5     | 20 | 20 | Успешно | 
| 17) perimeter(a, b)       |   a = 2, b = 5     |          14      |            14         | Успешно |
| 18) perimeter(a, b)       |   a = 5, b = 2     |    14      |     14      | Успешно |
| 19) perimeter(a, b)       |  a = 0, b = 10   |      Invalid input       |    Invalid input      | Успешно |
| 20) perimeter(a, b)       | a = 0, b = 0 |      Invalid input      |    Invalid input      | Успешно |
| 21) perimeter(a, b)  |    a = -1, b = -2    | Invalid input |Invalid input| Успешно | 
| 22) perimeter(a, b)  |   a = -1, b = 0   |    Invalid input        |        Invalid input  | Успешно |
| 23) perimeter(a, b)  |   a = 10, b = 0    |      Invalid input      |   Invalid input     | Успешно |
| 24) perimeter(a, b)  |  a = 0, b = -1   |   Invalid input    |     Invalid input     | Успешно |
| 25) perimeter(a, b) | a = "b", b = 1 |    Invalid input      |   Invalid input       | Успешно |
| 26) perimeter(a, b) | a = 3, b = "A" |    Invalid input      |   Invalid input       | Успешно |
| 27) perimeter(a, b) | a = True, b = 7 |    Invalid input      |   Invalid input       | Успешно |
| 28) perimeter(a, b) | a = 9, b = True |    Invalid input      |   Invalid input       | Успешно |
| 29) perimeter(a, b) | a = False, b = 1 |    Invalid input      |   Invalid input       | Успешно |
| 30) perimeter(a, b) | a = 2, b = False |    Invalid input      |   Invalid input       | Успешно |

### Тесты для triangle.py
- Тесты, проверяющие корректность вычисления площади и периметра треугольника.
#### test_positive_triangle_area
- тест на корректность вычисления площади с вводом положительных чисел
#### test_non_positive_triangle_area
- тест на корректность вычисления площади с вводом неположительных чисел
#### test_string_triangle_area
- тест на корректность вычисления площади с вводом строк
#### test_bool_triangle_area
- тест на корректность вычисления площади с вводом логических типов данных
#### test_positive_triangle_perimeter
- тест на корректность вычисления периметра с вводом положительных чисел
#### test_non_positive_triangle_perimeter
- тест на корректность вычисления периметра с вводом неположительных чисел
#### test_string_triangle_perimeter
- тест на корректность вычисления периметра с вводом строк
#### test_bool_triangle_perimeter
- тест на корректность вычисления периметра с вводом логических типов данных
#### test_nonexistent_triangles
- тест, проверяющий существование данного треугольника

| Номер кейса         |   Входные данные    |    Ожидаемый результат     |   Фактический результат    | Статус  |
|---------------------|:-------------------:|:--------------------------:|:--------------------------:|---------|   
| 1) area(a, h)         |    a = 20, h = 4     | 40 | 40 | Успешно | 
| 2) area(a, h)         |   a = 4, h = 20     |            40            |            40           | Успешно |
| 3) area(a, h)         |   a = 0, h = 0     |     80       |      80       | Успешно |
| 4) area(a, h)         |  a = -1, h = 0   |      Invalid input       |    Invalid input      | Успешно |
| 5) area(a, h)         | a = 0, h = -1 |      Invalid input      |    Invalid input      | Успешно |
| 6) area(a, h)        |    a = -1, h = -1    | Invalid input |Invalid input| Успешно | 
| 7) area(a, h)        |   a = 1, h = 0   |    Invalid input        |        Invalid input  | Успешно |
| 8) area(a, h)        |   a = 0, h = 1    |      Invalid input      |   Invalid input     | Успешно |
| 9) area(a, h)        |  a = -1, h = -10   |   Invalid input    |     Invalid input     | Успешно |
| 10) area(a, h)       | a = "c", h = 9 |    Invalid input      |   Invalid input       | Успешно |
| 11) area(a, h)       | a = 10, h = "E" |    Invalid input      |   Invalid input       | Успешно |
| 12) area(a, h)       | a = True, h = 107 |    Invalid input      |   Invalid input       | Успешно |
| 13) area(a, h)       | a = 9, h = True |    Invalid input      |   Invalid input       | Успешно |
| 14) area(a, h)       | a = False, h = 5 |    Invalid input      |   Invalid input       | Успешно |
| 15) area(a, h)        | a = 3, h = False |    Invalid input      |   Invalid input       | Успешно |
| 16) perimeter(a, b, c)  |    a = 7, b = 7, c = 7     | 21 | 21 | Успешно | 
| 17) perimeter(a, b, c)      |   a = 3, b = 5, c = 7     |          15      |           15        | Успешно |
| 18) perimeter(a, b, c)      |    a = -1, b = -1, c = -1     |   Invalid input   |  Invalid input | Успешно |
| 19) perimeter(a, b, c) |    a = 5, b = 5, c = -1     |   Invalid input   |  Invalid input | Успешно |
| 20) perimeter(a, b, c) |    a = 5, b = -1, c = 5     |   Invalid input   |  Invalid input | Успешно |
| 21) perimeter(a, b, c) |    a = -1, b = 5, c = 5     |   Invalid input   |  Invalid input | Успешно |
| 22) perimeter(a, b, c) |    a = 0, b = 7, c = 7     |   Invalid input   |  Invalid input | Успешно |
| 23) perimeter(a, b, c)|    a = 0, b = 7, c = 7     |   Invalid input   |  Invalid input | Успешно |
| 24) perimeter(a, b, c) |    a = 7, b = 7, c = 0     |   Invalid input   |  Invalid input | Успешно |
| 25) perimeter(a, b, c) |    a = 7, b = 7, c = "C"     |   Invalid input   |  Invalid input | Успешно |
| 26) perimeter(a, b, c) |    a = "ABCDEF", b = 7, c = 3     |   Invalid input   |  Invalid input | Успешно |
| 27) perimeter(a, b, c) |    a = 7, b = 'm', c = "C"     |   Invalid input   |  Invalid input | Успешно |
| 28) perimeter(a, b, c) |    a = True, b = 7, c = 7     |   Invalid input   |  Invalid input | Успешно |
| 29) perimeter(a, b, c) |    a = 7, b = False, c = 7     |   Invalid input   |  Invalid input | Успешно |
| 30) perimeter(a, b, c)|    a = 7, b = False, c = True   |   Invalid input   |  Invalid input | Успешно |
| 31) perimeter(a, b, c) |    a = 1, b = 1, c = 5     |   Nonexistent figure   |  Nonexistent figure | Успешно |
| 32) pperimeter(a, b, c) |    a = 2, b = 20, c = 10     |   Nonexistent figure   |  Nonexistent figure | Успешно |
| 33) perimeter(a, b, c) |    a = 15, b = 3, c = 7   |   Nonexistent figure   |  Nonexistent figure | Успешно |

### Тесты для circle.py
- Тесты, проверяющие корректность вычисления площади и длины окружности.
#### test_positive_circle_area
- тест на корректность вычисления площади с вводом положительных чисел
#### test_non_positive_circle_area
- тест на корректность вычисления площади с вводом неположительных чисел
#### test_string_circle_area
- тест на корректность вычисления площади с вводом строк
#### test_bool_circle_area
- тест на корректность вычисления площади с вводом логических типов данных
#### test_positive_circle_circumference
- тест на корректность вычисления длины окружности с вводом положительных чисел
#### test_non_positive_circle_circumference
- тест на корректность вычисления длины окружности с вводом неположительных чисел
#### test_string_circle_circumference
- тест на корректность вычисления длины окружности с вводом строк
#### test_bool_circle_circumference
- тест на корректность вычисления длины окружности с вводом логических типов данных

| Номер кейса         |   Входные данные    |    Ожидаемый результат     |   Фактический результат    | Статус  |
|---------------------|:-------------------:|:--------------------------:|:--------------------------:|---------|   
| 1) area(r)         |   r = 3     | 9π | 9π | Успешно | 
| 2) area(r)       |  r = 1   |            π           |          π         | Успешно |
| 3) area(r)         |  r = -1    |    Invalid input   |   Invalid input    | Успешно |
| 4) area(r)        | r = 0  |      Invalid input       |    Invalid input      | Успешно |
| 5) area(r)        | r = True  |      Invalid input      |    Invalid input      | Успешно |
| 6) area(r)        |  r = False    | Invalid input |Invalid input| Успешно | 
| 7) area(r)        |  r = "No"   |    Invalid input        |        Invalid input  | Успешно |
| 8) perimeter(r)        |   r = 7    |     14π    |  14π  | Успешно |
| 9) perimeter(r)    |   r = 1  |   2π    |     2π   | Успешно |
| 10) perimeter(r)       |  r = 0  |    Invalid input      |   Invalid input       | Успешно |
| 11) perimeter(r)     |  r = -1 |    Invalid input      |   Invalid input       | Успешно |
| 12) perimeter(r)      |  r = True |    Invalid input      |   Invalid input       | Успешно |
| 13) perimeter(r)       |  r = False |    Invalid input      |   Invalid input       | Успешно |
| 14) perimeter(r)     |  r = "abcdefgh"  |    Invalid input      |   Invalid input       | Успешно |

### Тесты для square.py
- Тесты, проверяющие корректность вычисления площади и периметра квадрата.
#### test_positive_square_area
- тест на корректность вычисления площади с вводом положительных чисел
#### test_non_positive_square_area
- тест на корректность вычисления площади с вводом неположительных чисел
#### test_string_square_area
- тест на корректность вычисления площади с вводом строк
#### test_bool_square_area
- тест на корректность вычисления площади с вводом логических типов данных
#### test_positive_square_perimeter
- тест на корректность вычисления периметра с вводом положительных чисел
#### test_non_positive_square_perimeter
- тест на корректность вычисления периметра с вводом неположительных чисел
#### test_string_square_perimeter
- тест на корректность вычисления периметра с вводом строк
#### test_bool_square_perimeter
- тест на корректность вычисления периметра с вводом логических типов данных

| Номер кейса         |   Входные данные    |    Ожидаемый результат     |   Фактический результат    | Статус  |
|---------------------|:-------------------:|:--------------------------:|:--------------------------:|---------|   
| 1) area(a)         |   a = 7     | 49 | 49 | Успешно | 
| 2) area(a)       |  a = 1   |            1           |          1         | Успешно |
| 3) area(a)         |  a = 0    |    Invalid input   |   Invalid input    | Успешно |
| 4) area(a)      | a = -1 |      Invalid input       |    Invalid input      | Успешно |
| 5) area(a)        | r = True  |      Invalid input      |    Invalid input      | Успешно |
| 6) area(a)       |  r = False    | Invalid input |Invalid input| Успешно | 
| 7) area(a)        |  r = "unittests are not fun"   |    Invalid input        |        Invalid input  | Успешно |
| 8) perimeter(a)        |   a = 7     |     28    |  28  | Успешно |
| 9) perimeter(a)     |   a = 1   |   4    |     4  | Успешно |
| 10) perimeter(a)       |   a = 0  |    Invalid input      |   Invalid input       | Успешно |
| 11) perimeter(a)     | a = -1 |    Invalid input      |   Invalid input       | Успешно |
| 12) perimeter(a)      |  a = True |    Invalid input      |   Invalid input       | Успешно |
| 13) perimeter(a)      |  a = False |    Invalid input      |   Invalid input       | Успешно |
| 14) perimeter(a)      |  a = "AAAAAAA"  |    Invalid input      |   Invalid input       | Успешно |

# История изменения проекта с хешами коммитов
- 84d511e263ec62dfae79ee378e957a4fbe17d2b5 (HEAD -> main, origin/main, origin/HEAD) Unit test added, corrected figure libraries
- 04ef3404ec57c051b7ca755b9249e9e520e32e35 Update README.md 2
- bfa2687dcedd31d42f64291b5770cdd69b097161 Update README.md
- 0e290c692494f587dbc558bc107db8ee13c39fef added annotations to each function
- 974d71972c3069d3185d060009252f6fd44ced0d fix:rectangle.py add:triangle.py
- ca3c0f085363d778984fd660733bc2ce2cd28c44 add:rectangle.py
- d078c8d9ee6155f3cb0e577d28d337b791de28e2 L-03: Docs added
- 8ba9aeb3cea847b63a91ac378a2a6db758682460 L-03: Circle and square added
  
# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
