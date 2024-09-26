# Math formulas

## Area

- Circle: S = πR²
  - Функция area принимает параметр r &#40;int/float&#41; - длину радиуса этой окружности, и возвращает значение площади этого квадрата.
    ```python
    print(area(2))
    # Output: 12.566370614359172
- Rectangle: S = ab
  - Функция area принимает на вход параметр a &#40;int/float&#41; - длину стороны прямоугольника. Возвращает значение площади этого прямоугольника.
  ```python
  print(area(8, 2))
  # Output: 16
- Square: S = a²
  - Функция area принимает на вход параметр a &#40;int/float&#41; - длину стороны квадрата. Возвращает значение площади этого квадрата.
    ```python
    print(area(4))
    # Output: 16
- Triangle: S = ab
  - Функция area принимает на вход два параметра a и h (int/float) - длины стороны и высоты треугольника соответственно. Возвращает площадь этого треугольника (float).
    ```python
    print(area(4, 12))
    # Output: 24.0

## Perimeter

- Circle: P = 2πR 
  - Функция perimeter принимает параметр r &#40;int/float&#41; - длину радиуса этой окружности. Возвращает значение периметра этой окружности.
    ```python
    print(perimeter(3))
    # Output: 25.132741228718345

- Rectangle: P = 2a + 2b
  - Функция perimeter принимает на вход два параметра a и b (int/float) - длины смежных сторон квадрата. Возвращает периметр этого прямоугольника (int/float (в зависимости от типа входных данных)).
    ```python
    print(perimeter(7, 8))
    # Output: 30
    
- Square: P = 4a
  - Функция perimeter принимает на вход параметр a (int/float) - длину стороны квадрата. Возвращает периметр этого квадрата (int/float (в зависимости от типа входных данных)).
    ```python
    print(perimeter(5))
    # Output: 20
    
- Triangle: P = a + b + c
  - Функция perimeter принимает на вход три параметра: a, b и c (int/float) - длины сторон треугольника. Возвращает периметр этого треугольника (int/float (в зависимости от типа входных данных)).
    ```python
    print(perimeter(8, 3, 1))
    # Output: 12

## Unit tests
В файле test.py содержатся Unit-тесты, которые помогают проверить функционал программы.

| Тестируемый файл | Функция   | Входные данные | Результат           |
|------------------|-----------|----------------|---------------------|
| circle.py        | area      | 0              | passed              |
| circle.py        | area      | 5              | passed              |
| circle.py        | area      | -3             | failed (ValueError) |
| circle.py        | area      | "text"         | failed (TypeError)  |
| circle.py        | area      | None           | failed (TypeError)  |
| circle.py        | perimeter | 0              | passed              |
| circle.py        | perimeter | 5              | passed              |
| circle.py        | perimeter | -3             | failed (ValueError) |
| circle.py        | perimeter | "text"         | failed (TypeError)  |
| circle.py        | perimeter | None           | failed (TypeError)  |
| rectangle.py     | area      | 10, 0          | passed              |
| rectangle.py     | area      | 5, 5           | passed              |
| rectangle.py     | area      | -3, 4          | failed (ValueError) |
| rectangle.py     | area      | 10, "text"     | failed (TypeError)  |
| rectangle.py     | area      | 10, None       | failed (TypeError)  |
| rectangle.py     | perimeter | 0, 0           | passed              |
| rectangle.py     | perimeter | 5, 5           | passed              |
| rectangle.py     | perimeter | -1, 2          | failed (ValueError) |
| rectangle.py     | perimeter | "text", 2      | failed (TypeError)  |
| rectangle.py     | perimeter | None, 2        | failed (TypeError)  |
| square.py        | area      | 0              | passed              |
| square.py        | area      | 5              | passed              |
| square.py        | area      | -3             | failed (ValueError) |
| square.py        | area      | "text"         | failed (TypeError)  |
| square.py        | area      | None           | failed (TypeError)  |
| square.py        | perimeter | 0              | passed              |
| square.py        | perimeter | 5              | passed              |
| square.py        | perimeter | -3             | failed (ValueError) |
| square.py        | perimeter | "text"         | failed (TypeError)  |
| square.py        | perimeter | None           | failed (TypeError)  |
| triangle.py      | area      | 0, 2           | passed              |
| triangle.py      | area      | 5, 4           | passed              |
| triangle.py      | area      | -3, 2          | failed (ValueError) |
| triangle.py      | area      | "text", 2      | failed (TypeError)  |
| triangle.py      | area      | None, 2        | failed (TypeError)  |
| triangle.py      | perimeter | 0, 0, 0        | passed              |
| triangle.py      | perimeter | 5, 5, 5        | passed              |
| triangle.py      | perimeter | -3, 2, 1       | failed (ValueError) |
| triangle.py      | perimeter | "text", 2, 1   | failed (TypeError)  |
| triangle.py      | perimeter | None, 2, 1     | failed (TypeError)  |

## История изменения проекта
* *6d003c1a37d9accff61da2dc5c0e505fc0bedffa* - now files are up to date
* *a8dfd20c36de5dd8ec4c31c746c30eb0a854f4d9* - added documentation