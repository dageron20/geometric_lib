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
