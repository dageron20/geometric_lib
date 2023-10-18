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
  