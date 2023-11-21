# Математические формулы
## Площадь
- Окружность: S = πR²
- Прямоугольник: S = ab
- Квадрат: S = a²
- Треугольник: S = ah / 2

## Периметр
- Окружность: P = 2πR
- Прямоугольник: P = 2a + 2b
- Квадрат: P = 4a
- Треугольник: P = a + b + c

# Функции
## circle.py
### Площадь
```python
def area(r):
```
> Принимает значение r, возвращает значение r в квадрате, умноженное на π

#### Пример вызова функции
```python
print(area(3))
# Вывод: 28.274333882308138
```
### Периметр
```python
def perimeter(r):
```
> Принимает значение r, возвращает r, умноженное на 2π

#### Пример вызова функции
```python
print(perimeter(3))
# Вывод: 18.84955592153876
```

## rectangle.py
### Площадь
```python
def area(a, b):
```
> Принимает значения a и b, возвращает их произведение

#### Пример вызова функции
```python
print(area(4, 2))
# Вывод: 8
```

### Периметр
```python
def perimeter(a, b):
```
> Принимает значения a и b, возвращает их сумму, умноженную на 2

#### Пример вызова функции
```python
print(perimeter(4, 2))
# Вывод: 12
```

## square.py
### Площадь
```python
def area(a):
```
> Принимает значение a, вовращает квадрат a

#### Пример вызова функции
```python
print(area(4))
# Вывод: 16
```

### Периметр
```python
def perimeter(a, b):
```
> Принимает значение a, возвращает 4a

#### Пример вызова функции
```python
print(perimeter(4))
# Вывод: 16
```

## triangle.py
### Площадь
```python
def area(a, h):
```
> Принимает значения a и h, вовращает их произведение, деленное на 2 (площадь)

#### Пример вызова функции
```python
print(area(1, 2))
# Вывод: 1.0
```

### Периметр
```python
def perimeter(a, b, c):
```
> Принимает значения a, b и c, возвращает их сумму (периметр)

#### Пример вызова функции
```python
print(perimeter(3, 4, 5))
# Вывод: 11
```

# Unit Тесты
```python
def test_zero_mul(self):
#####
def test_zero_sum(self):
# Проверяет, как функция работает с нулевым аргументом

def test_square_mul(self):
# Проверяет, как функция работает с одинаковыми входными данными

def test_negative_mul(self):
#####
def test_negative_sum(self):
# Проверяет, как функция работает с отрицательными числами

def test_float_mul(self):
#####
def test_float_sum(self):
# Проверяет, как функция работает с дробными числами

def test_char_mul(self):
#####
def test_char_sum(self):
# Проверяет, как функция работает с типом данных char/string (должно вывести ошибку)

def test_bool_mul(self):
#####
def test_bool_sum(self):
# Проверяет, как функция работает с типом данных bool

def test_overflow_mul(self):
#####
def test_overflow_sum(self):
# Проверяет, как функция работает с очень большими значениями

```

# История коммитов
| Коммит | Автор | Хэш |
| --- | --- | --- |
| L-03: Circle and square added | smartiqa | [8ba9aeb](https://github.com/hhhannahmmmontana/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460) |
| L-03: Docs added | smartiqa | [d078c8d](https://github.com/hhhannahmmmontana/geometric_lib/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2) |
| added rectangle.py | hhhannahmmmontana | [a8d7cb2](https://github.com/hhhannahmmmontana/geometric_lib/commit/a8d7cb25d5820c435447b411d96e4354e53fd8de) |
| added triangle.py + fixed rectangle.py | hhhannahmmmontana | [85beed4](https://github.com/hhhannahmmmontana/geometric_lib/commit/85beed4e687fcf35a76ea4f9678cab538cb5a330) |
| added unittests | hhhannahmmmontana | [c485ea8](https://github.com/hhhannahmmmontana/geometric_lib/commit/c485ea8aa9d4ee6acb9abd71948a9b3adbc52000) |
| made even more unit tests | hhhannahmmmontana | [9032cc5](https://github.com/hhhannahmmmontana/geometric_lib/commit/9032cc598a794f0c2e3d5da8875c13904c37f174) |
