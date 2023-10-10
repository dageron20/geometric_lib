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

# История изменений (от новых к старым)
* commit dc93a50ee44fe4f438df3ce30b26ba02a1174221
	add docs

* commit 17e680216126c9d07c55ba0f75cbe466b3f57dc1

	file triangle.py added, bug in rectrangle.py fixed
* commit 94ef0e2fff3d06e637b58eb7dff3b44b4fe350a1

	file rectrangle.py added
