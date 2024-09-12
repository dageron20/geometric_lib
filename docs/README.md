# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Документация
## Общее описание решения
-Цель:
  - Создание программ вычисляющих площади и периметры различных фигур.
-Назначение:
  -Вычисление площадей и периметрова
- В каждом файле мы задаем функцию, чтобы найти либо площадь, либо периметр данной фигуры. Эти функции используют стандартные математические операции.

## Описание каждой функции с примерами вызова
- circle.py :
  - def area(r) : Рассчитывает площадь круга; Пример вызова: area(2)  # Возвращает площадь круга с радиусом 2.
  - def perimeter(r): Рассчитывает периметр круга; Пример вызова: perimeter(2) # Возвращает периметр круга с радиусом 2.
    
- rectangle.py:
  - def area(a, b): Рассчитывает площадь прямоугольника; Пример вызова: area(2, 3)  # Возвращает площадь прямоугольника с длиной 2 и шириной 3.
  - def perimeter(a, b): Рассчитывает площадь прямоугольника; Пример вызова: area(2, 3)  # Возвращает периметр прямоугольника с длиной 2 и шириной 3.
- square.py:
  - def area(a): Рассчитывает площадь квадрата; Пример вызова: area(2)  # Возвращает площадь квадрата со стороной 2.
  - def perimeter(a): Рассчитывает периметр квадрата; Пример вызова: area(2)  # Возвращает периметр квадрата со стороной 2.
- triangle.py:
  - def area(a, h): Рассчитывает площадь треугольника; Пример вызова: area(2, 3)  # Возвращает площадь треугольника с длинами основания 2 и высоты 3.
  - def perimeter(a, b, c): Рассчитывает периметр треугольника; Пример вызова: area(2, 3, 4)  # Возвращает периметр треугольника со сторонами 2, 3, 4.

## История изменений
- Коммит 8ba9aeb3cea847b63a91ac378a2a6db758682460
  - Автор: smartiqa <info@smartiqa.ru>
  - Дата: Thu Mar 4 14:54:08 2021 +0300
  - Сообшение: L-03: Circle and square added
- Коммит d078c8d9ee6155f3cb0e577d28d337b791de28e2
  - Автор: smartiqa <info@smartiqa.ru>
  - Дата: Thu Mar 4 14:55:29 2021 +0300
  - Сообшение: L-03: Docs added
- Коммит ee0ec56cc61a124c76b0797753ed4942ec0dd569
  - Автор: isosh <tuturu5012@gmail.com>
  - Дата: Mon Sep 25 00:43:01 2023 +0300
  - Сообшение: Добавлен файл rectangle.py
- Коммит 587ed3d322f4064da51cd595c841d5d3e2e75aee
  - Автор: isosh <tuturu5012@gmail.com>
  - Дата: Mon Sep 25 01:03:02 2023 +0300
  - Сообшение: Исправлена ошибка в файле rectangle.py
- Коммит 8cd2f928ed243bc34b886a14151ca6c7867289ff
  - Автор: isosh <tuturu5012@gmail.com>
  - Дата: Tue Oct 10 03:33:10 2023 +0300
  - Сообшение: Добавлены комментарии к функциям.
# Unit-tests
## Описание тестов

### Юнит-тесты для rectangle.py
| Название теста                     | Входные данные                                 | Ожидаемый результат                                          | Результат                                                    | Статус |
|------------------------------------|------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|--------|
| test_zero_area                     | a = 0, b = 8                                   | 0                                                            | 0                                                            | True   |
| test_zero_perimeter                | a = 0, b = 2                                   | 4                                                            | 4                                                            | True   |
| test_str_area                      | a = '2', b = '4'                               | "Error: can't work with not integer or not float types"      | "Error: can't work with not integer or not float types"      | True   |
| test_str_perimeter                 | a = '2', b = '8'                               | "Error: can't work with not integer or not float types"      | "Error: can't work with not integer or not float types"      | True   |
| test_negative_area                 | a = 2, b = -3                                  | "Error: values can't be negative"                            | "Error: values can't be negative"                            | True   |
| test_negative_perimeter            | a = 3, b = -12                                 | "Error: values can't be negative"                            | "Error: values can't be negative"                            | True   |
| test_right_area                    | a = 3, b = 2                                   | 6                                                            | 6                                                            | True   |
| test_right_perimeter               | a = 1, b = 2                                   | 6                                                            | 6                                                            | True   |

### Юнит-тесты для сircle.py
| Название теста                     | Входные данные                                 | Ожидаемый результат                                          | Результат                                                    | Статус |
|------------------------------------|------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|--------|
| test_zero_area                     | r = 0                                          | 0                                                            | 0                                                            | True   |
| test_zero_perimeter                | r = 0                                          | 0                                                            | 0                                                            | True   |
| test_str_area                      | r = '2'                                        | "Error: can't work with not integer or not float types"      | "Error: can't work with not integer or not float types"      | True   |
| test_str_perimeter                 | r = '2'                                        | "Error: can't work with not integer or not float types"      | "Error: can't work with not integer or not float types"      | True   |
| test_negative_area                 | r = -2                                         | "Error: values can't be negative"                            | "Error: values can't be negative"                            | True   |
| test_negative_perimeter            | r = -12                                        | "Error: values can't be negative"                            | "Error: values can't be negative"                            | True   |
| test_right_area                    | r = 3                                          | 28.274333882308138                                           | 28.274333882308138                                           | True   |
| test_right_perimeter               | r = 3                                          | 18.84955592153876                                            | 18.84955592153876                                            | True   |

### Юнит-тесты для square.py
| Название теста                     | Входные данные                                 | Ожидаемый результат                                          | Результат                                                    | Статус |
|------------------------------------|------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|--------|
| test_zero_area                     | a = 0                                          | 0                                                            | 0                                                            | True   |
| test_zero_perimeter                | a = 0                                          | 0                                                            | 0                                                            | True   |
| test_str_area                      | a = '2'                                        | "Error: can't work with not integer or not float types"      | "Error: can't work with not integer or not float types"      | True   |
| test_str_perimeter                 | a = '2'                                        | "Error: can't work with not integer or not float types"      | "Error: can't work with not integer or not float types"      | True   |
| test_negative_area                 | a = -7                                         | "Error: values can't be negative"                            | "Error: values can't be negative"                            | True   |
| test_negative_perimeter            | a = -14                                        | "Error: values can't be negative"                            | "Error: values can't be negative"                            | True   |
| test_right_area                    | a = 7                                          | 49                                                           | 49                                                           | True   |
| test_right_perimeter               | a = 2                                          | 8                                                            | 8                                                            | True   |

### Юнит-тесты для triangle.py
| Название теста                     | Входные данные                                 | Ожидаемый результат                                          | Результат                                                    | Статус |
|------------------------------------|------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|--------|
| test_zero_area                     | a = 0, h = 8                                   | 0                                                            | 0                                                            | True   |
| test_zero_perimeter                | a = 0, b = 2, c = 0                            | 2                                                            | 2                                                            | True   |
| test_str_area                      | a = '2', h = '4'                               | "Error: can't work with not integer or not float types"      | "Error: can't work with not integer or not float types"      | True   |
| test_str_perimeter                 | a = '2', b = '8', c = '5'                      | "Error: can't work with not integer or not float types"      | "Error: can't work with not integer or not float types"      | True   |
| test_negative_area                 | a = 2, h = -3                                  | "Error: values can't be negative"                            | "Error: values can't be negative"                            | True   |
| test_negative_perimeter            | a = 3, b = -12, c = -2                         | "Error: values can't be negative"                            | "Error: values can't be negative"                            | True   |
| test_right_area                    | a = 3, h = 8                                   | 12                                                           | 12                                                            | True   |
| test_right_perimeter               | a = 1, b = 2, c = 3                            | 6                                                            | 6                                                            | True   |
