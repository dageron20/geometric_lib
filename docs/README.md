# Общее описание
Эта библиотека включает в себя функции для расчета площади и периметра круга, прямоугольника, квадрата и треугольника

# Функции
* **circle.py**
    * area(r)

        Расчитывает площадь круга с заданным радиусом r.

    * perimeter(r)

        Расчитывает периметр круга с заданным радиусом r.

    * Примеры использования:
    ```python
    import circle
    r=5
    print(circle.area(r))
    print(circle.perimeter(r))
    ```
    ожидаемый вывод: 78.53981633974483 - площадь круга и 31.41592653589793 - периметр круга.

    **Результаты тестирования:**
 
| Тестируемый кейс                  | Входные данные | Ожидаемый результат        | Итоговый результат         |
|-----------------------------------|----------------|----------------------------|----------------------------|
| с нулевыми входными данными       | area test: 0        | area test: 0                    | area test: 0                    |
|                                   | perimeter test: 0   | perimeter test: 0                    | perimeter test: 0               |
| с успешными входными              |                |                            |                            |
| для площади                       | Test 1: 5      | Test 1: 78.53981633974483  | Test 1: 78.53981633974483  |
|                                   | Test 2: 17     | Test 2: 907.9202768874503  | Test 2: 907.9202768874503  |
| для периметра                     | Test 1: 7      | Test 1: 43.982297150257104 | Test 1: 43.982297150257104 |
|                                   | Test 2: 10     | Test 2: 62.83185307179586  | Test 2: 62.83185307179586  |
| с отрицательными входными данными | area test: -1       | area test: 0                    | area test: 0                    |
|                                   | perimeter test: -1  | perimeter test: 0                    | perimeter test: 0               |

    

* **rectangle.py**
    * area(a,b)

    Расчитывает площадь прямоугольника с заданными сторонами a и b.

    * perimeter(a,b)

    Расчитывает периметр прямоугольника с заданными сторонами a и b.

    * Примеры использования:
    ```python
    import rectangle
    a=5
    b=10
    print(rectangle.area(a,b))
    print(rectangle.perimeter(a,b))
    ```
    Ожидаемый вывод: 50 - площадь прямоугольника и 30 - периметр прямоугольника.

     **Результаты тестирования:**
   
| Тестируемый кейс                  | Входные данные          | Ожидаемый результат | Итоговый результат  |
|-----------------------------------|-------------------------|---------------------|---------------------|
| с нулевыми входными данными       | area test 1: 5, 0       | area test 1: 0      | area test 1: 0      |
|                                   | area test 2: 0, 5       | area test 2: 0      | area test 2: 0      |
|                                   | perimeter test 1: 7, 0  | perimeter test 1: 0 | perimeter test 1: 0 |
|                                   | perimeter test 2: 0, 6  | perimeter test 2: 0 | perimeter test 2: 0 |
| с успешными входными данными      |                         |                     |                     |
| для площади                       | test 1: 5, 14           | test 1: 70          | test 1: 70          |
|                                   | test 2: 13, 25          | test 2: 325         | test 2: 325         |
| для периметра                     | test 1: 5, 14           | test 1: 38          | test 1: 38          |
|                                   | test 2: 13, 25          | test 2: 76          | test 2: 76          |
| с отрицательными входными данными | area test 1: 5, -1      | area test 1: 0      | area test 1: 0      |
|                                   | area test 2: -1, 5      | area test 2: 0      | area test 2: 0      |
|                                   | perimeter test 1: 7, -1 | perimeter test 1: 0 | perimeter test 1: 0 |
|                                   | perimeter test 2: -1, 7 | perimeter test 2: 0 | perimeter test 2: 0 |
|                                   |                         |                     |                     |



* **square.py**
    * area(a)

            Расчитывает площадь квадрата с заданной стороной a.

    * perimeter(a)

            Расчитывает периметр квадрата с заданной стороной a.

    * Примеры использования:
    ```python
    import square
    a=5
    print(square.area(a))
    print(square.perimeter(a))
    ```
    Ожидаемый вывод: 25 - площадь квадрата и 20 - периметр квадрата.
**Результаты тестирования:**

|          Тестируемый кейс         |   Входные данные   | Ожидаемый результат | Итоговый результат |
|:---------------------------------:|:------------------:|:-------------------:|:------------------:|
| с нулевыми входными данными       | area test: 0       | area test: 0        | area test: 0       |
|                                   | perimeter test: 0  | perimeter test: 0   | perimeter test: 0  |
| с успешными входными              |                    |                     |                    |
| для площади                       | Test 1: 5          | Test 1: 25          | Test 1: 25         |
|                                   | Test 2: 13         | Test 2: 169         | Test 2: 169        |
| для периметра                     | Test 1: 14         | Test 1: 56          | Test 1: 56         |
|                                   | Test 2: 25         | Test 2: 100         | Test 2: 100        |
| с отрицательными входными данными | area test: -1      | area test: 0        | area test: 0       |
|                                   | perimeter test: -1 | perimeter test: 0   | perimeter test: 0  |
    
* **triangle.py**
    * area(a,h)

    Расчитывает площадь треугольника по заданным стороне a и высоте h.

    * perimeter(a,b,c)

    Расчитывает периметр треугольника по заданным сторонам a,b и c.

    * Примеры использования:
    ```python
    import triangle
    a=8
    h=4
    b=10
    c=12
    print(triangle.area(a,h))
    print(triangle.perimeter(a,b,c))
    ```
    Ожидаемый вывод: 16 - площадь треугольника и 30 - периметр треугольника.
    
     **Результаты тестирования:**
    
| Тестируемый кейс                                 | Входные данные              | Ожидаемый результат | Итоговый результат  |
|--------------------------------------------------|-----------------------------|---------------------|---------------------|
| с нулевыми входными данными                      | area test 1: 0, 5           | area test 1: 0      | area test 1: 0      |
|                                                  | area test 2: 5, 0           | area test 2: 0      | area test 2: 0      |
|                                                  | perimeter test 1: 0, 5, 6   | perimeter test 1: 0 | perimeter test 1: 0 |
|                                                  | perimeter test 2: 5, 0, 6   | perimeter test 2: 0 | perimeter test 2: 0 |
|                                                  | perimeter test 3: 5, 6, 0   | perimeter test 3: 0 | perimeter test 3: 0 |
| с успешными входными данными                     |                             |                     |                     |
| для площади                                      | test 1: 5, 3                | test 1: 7.5         | test 1: 7.5         |
|                                                  | test 2: 8, 5                | test 2: 20          | test 2: 20          |
| для периметра                                    | test 1: 4, 7, 9             | test 1: 20          | test 1: 20          |
|                                                  | test 2: 3, 4, 5             | test 2: 12          | test 2: 12          |
| с отрицательными входными данными                | area test 1: -1, 5          | area test 1: 0      | area test 1: 0      |
|                                                  | area test 2: 5, -1          | area test 2: 0      | area test 2: 0      |
|                                                  | perimeter test 1: -1, 5, 6  | perimeter test 1: 0 | perimeter test 1: 0 |
|                                                  | perimeter test 2: 5, -1, 6  | perimeter test 2: 0 | perimeter test 2: 0 |
|                                                  | perimeter test 3: 5, 6, -1  | perimeter test 3: 0 | perimeter test 3: 0 |
| с невозможным треугольником по входным параметрам |                             |                     |                     |
| для периметра                                    | perimeter test 1: 1, 10, 15 | perimeter test 1: 0 | perimeter test 1: 0 |
|                                                  | perimeter test 2: 10, 15, 1 | perimeter test 2: 0 | perimeter test 2: 0 |
|                                                  | perimeter test 3: 15, 10, 1 | perimeter test 3: 0 | perimeter test 3: 0 |

# История изменений (от новых к старым)

* commit 17e680216126c9d07c55ba0f75cbe466b3f57dc1

    file triangle.py added, bug in rectrangle.py fixed
* commit 94ef0e2fff3d06e637b58eb7dff3b44b4fe350a1

    file rectrangle.py added