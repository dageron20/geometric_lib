# Описание библиотеки

### В данной библиотеке собраны формулы для определения площади и периметра таких фигур как:

- Окружность
- Прямоугольник
- Квадрат
- Треугольник

> Формулы площадей и периметров описаны в разделе [Математический формулы](#математические-формулы)


# Результаты Unit-Тестов

## RectangleTestCase

| Test name           | Function  | Input      | Expected | Status (before) | Status (after) |
| ------------------- | --------- | ---------- | -------- | --------------- | -------------- |
| test_area           | area      | 174, 452   | 78648    | Ok              | Ok             |
| test_area           | area      | -174, -452 | None     | Error           | Ok             |
| test_perimeter      | perimeter | 43, 27     | 140      | Ok              | Ok             |
| test_perimeter      | perimeter | -510, 21   | None     | Error           | Ok             |
| test_area_zero      | area      | 123, 0     | 0        | Ok              | Ok             |
| test_area_zero      | area      | 0, 0       | 0        | Ok              | Ok             |
| test_perimeter_zero | perimeter | -124, -124 | 0        | Ok              | Ok             |
| test_perimeter_zero | perimeter | 0, 0       | 0        | Ok              | Ok             |

## SquareTestCase

| Test name       | Function       | Input | Expected | Status (before) | Status (after) |
| --------------- | -------------- | ----- | -------- | --------------- | -------------- |
| test_area       | square_area    | 241   | 58081    | Ok              | Ok             |
| test_area       | square_area    | -32   | None     | Error           | Ok             |
| test_perimeter  | square_perimeter| 452   | 1808     | Ok              | Ok             |
| test_perimeter  | square_perimeter| -510  | None     | Error           | Ok             |
| test_area_zero  | square_area    | 0     | 0        | Ok              | Ok             |
| test_perimeter_zero | square_perimeter | 0 | 0       | Ok              | Ok             |

## TriangleTestCase

| Test name            | Function          | Input             | Expected    | Status (before) | Status (after) |
| -------------------- | ----------------- | ----------------- | ----------- | --------------- | -------------- |
| test_area            | triangle_area     | 723, 5439         | 1966198.5   | Ok              | Ok             |
| test_area            | triangle_area     | 723, 5438         | float       | Ok              | Ok             |
| test_area            | triangle_area     | -76, 12           | None        | Error           | Ok             |
| test_perimeter       | triangle_perimeter| 34, 85, 56         | 175         | Ok              | Ok             |
| test_perimeter       | triangle_perimeter| -831, -7790, -3215 | None        | Error           | Ok             |
| test_area_zero       | triangle_area     | 432, 0            | 0           | Ok              | Ok             |
| test_area_zero       | triangle_area     | 0, 0              | 0           | Ok              | Ok             |
| test_perimeter_zero  | triangle_perimeter| -51, 50, 0         | None        | Error           | Ok             |
| test_perimeter_zero  | triangle_perimeter| 0, 0, 0           | 0           | Ok              | Ok             |


## CircleTestCase

| Test name       | Function       | Input | Expected               | Status (before) | Status (after) |
| --------------- | -------------- | ----- | ---------------------- | --------------- | -------------- |
| test_area       | circle_area    | 75    | float                  | Ok              | Ok             |
| test_area       | circle_area    | 691   | 1500050.801828708     | Ok              | Ok             |
| test_area       | circle_area    | -76   | None                   | Error           | Ok             |
| test_perimeter  | circle_perimeter| 64    | float                  | Ok              | Ok             |
| test_perimeter  | circle_perimeter| 74    | 464.9557127312894     | Ok              | Ok             |
| test_perimeter  | circle_perimeter| -42   | None                   | Error           | Ok             |
| test_area_zero  | circle_area    | 0     | 0                      | Ok              | Ok             |
| test_perimeter_zero | circle_perimeter | 0 | 0                      | Ok              | Ok             |




# Примеры работы библиотеки

## Треугольник

### Определение площади

```python

from src import triangle

a = 2
h = 4
area = triangle.area(a=a, h=h)
print(area)
```

> Вывод: 4.0

### Определение периметра

```python

from src import triangle

a = 2
b = 4
c = 5
perimeter = triangle.perimeter(a=a, b=b, c=c)
print(perimeter)
```

> Вывод: 11

## Прямоугольник

### Определение площади

```python

from src import rectangle

a = 7
b = 6
area = rectangle.area(a=a, b=b)
print(area)
```

> Вывод: 42


### Определение периметра

```python

from src import rectangle

a = 7
b = 6
perimeter = rectangle.perimeter(a=a, b=b)
print(perimeter)
```

> Вывод: 26


## Окружность

### Определение площади

```python

from src import circle

r = 7
area = circle.area(r=r)
print(area)
```

> Вывод: 153.93804002589985


### Определение периметра

```python

from src import circle

r = 7
area = circle.perimeter(r=r)
print(area)
```

> Вывод: 43.982297150257104


## Квадрат

### Определение площади

```python

from src import square

a = 8
area = square.area(a=a)
print(area)
```

> Вывод: 64


### Определение периметра

```python

from src import square

a = 8
area = square.perimeter(a=a)
print(area)
```

> Вывод: 32



# История изменений проекта

## Обновление 2.0

### Список изменений

- Добавлены формулы площади и периметра треугольника (`triangle.py`)
- Исправлена ошибка в формуле расчёта периметра прямоугольника (`rectangle.py`) 

Хеш коммита: `c0f02cddb517c8011cf48892a618363ff2903541`


## Обновление 1.2

### Список изменений

- Добавлены формулы площади и периметра прямоугольника (`rectangle.py`)

Хеш коммита: `3af04a2643e2f19755d745ad4b700bf29266b17e`

## Обновление 1.1

### Список изменений

- Добавлен файл `README.md` с описанием математических формул (`docs/README.md`)

Хеш коммита: `d078c8d9ee6155f3cb0e577d28d337b791de28e2`

## Обновление 1.0

### Список изменений

- Добавлены формулы площади и периметра круга (`circle.py`)
- Добавлены формулы площади и периметра квадрата (`square.py`)

Хеш коммита: `8ba9aeb3cea847b63a91ac378a2a6db758682460`



# Математические формулы
## Площади
- Окружность: S = πR²
- Прямоугольник: S = ab
- Квадрат: S = a²
- Треугольник: S = a * h / 2

## Периметры
- Окружность: P = 2πR
- Прямоугольник: P = 2a + 2b
- Квадрат: P = 4a
- Треугольник: S = a + b + c
