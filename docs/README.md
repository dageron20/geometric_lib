# В проекте представлены функции для подсчета периметра и площади у некоторых фигур

# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle:S = a * h / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: a + b + c
### содержание проекта
##### в проекте есть файлы:
* *rectangle.py*
* *triangle.py*
* *circle.py*
* *square.py*




### *описание каждой функции с примерами вызова*
* #### файл rectangle.py
    * функция area(a, b) - принимает две стороны прямоугольника и возвращает его площадь
    ``` python
    def area(a, b): 
        return a * b  
    print(perimetr(2, 3))  #6  
    ```
    * функция perimetr(a, b) - принимает две стороны прямоугольника и возвращает его периметр
    ``` python
    def perimeter(a, b): 
        return (a + b) * 2
    print(perimetr(2, 3)) #10
    ```
* #### файл triangle.py
    * функция area(a, h) - принимает сторону треугольника и высоту, опущенную на эту сторону, а возвращает площадь
    ``` python
    def area(a, h): 
        return a * h / 2  
    print(area(6, 4))   #12
    ```
    * функция perimetr(a, b, c) - принимает три стороны треугольника и возвращает его периметр
     ``` python
    def perimeter(a, b, c): 
        return a + b + c 
    print(perimetr(6, 4, 5))    #15
    ```
* #### файл circle.py
    * функция area(r) - принимает радиус окружности , а возвращает площадь
    ``` python
    def area(r): 
        return p*(r**2)
    print(area(8)) #64pi
    ```
    * функция perimetr(r) - принимает радиус окружност, а возвращает периметр
     ``` python
    def perimeter(r): 
        return 2*p*r
    print(perimetr(8)) #16pi
    ```
* #### файл square.py
   * функция area(a) - принимает сторону квадрата и возвращает площадь
    ``` python
    def area(a): 
        return a*a
    print(area(5)) #25
    ```
    * функция perimetr(r) - принимает радиус окружности и возвращает периметр
     ``` python
    def perimeter(a): 
        return a*4 
    print(perimetr(5)) #20
    ```

### *История изменения прокта*

* 9016de2: Добавил файл triangle.py и исправил файл rectangle.py
* 17668d1: добавил новый файл rectangle.py  
* d078c8d: L-03: Docs added
* 8ba9aeb: L-03: Circle and square added
## функции класса Rectangle

```
def area(self):
    return self.length * self.width

def perimeter(self):
    return 2 * (self.length + self.width)
```


## функции класса Square

```
    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side
```


## функции класса Circle

```
    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
```

## функции 

# тесты

## для rectangle.py
| тестирующая функция     | значения параметров | что ожидаем | что получаем |
|-------------------------|---------------------|-------------|--------------|
| test_rectangle_area     | a = 5 , b = 10      | 50          | 50           |
| test_perimeter_positive | a = 3, b = 14       | 34          | 34           |

## для square.py
| тестирующая функция | значения параметров | что ожидаем | что получаем |
|----|----------------|---------------------|--------------|
| test_square_area | a = 4          | 16                  | 16           |
| test_square_perimeter | a = 3          | 12                  | 12           |

## для circle.py
| тестирующая функция | значения параметров | что ожидаем | что получаем |
|----|----------------|---------------|----------------------|
| test_circle_area | a = 3          | 28.274333              |        28.274333              |
| test_circle_perimeter | a = 5          | 31.4159265              |        31.4159265               |

## для triangle.py
| тестирующая функция | значения параметров               | что ожидаем | что получаем |
|----|-----------------------------------|---------------------|-----------------------|
| test_triangle_area | base = 6, height = 8, a = 5, b = 7, c = 9 | 24                  | 24                    |
| test_triangle_perimeter | base = 5, height = 9, a = 6, b = 7, c = 8 | 21                  | 21                    |
