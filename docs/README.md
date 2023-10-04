# Математические формулы
## Площадь
- Круг: S = πR²
- Прямоугольник: S = ab
- Площадь: S = a²

## Периметр
- Круг: P = 2πR
- Прямоугольник: P = 2a + 2b
- Площадь: P = 4a

# Описание решения:
## Созданы функции для поиска области и периметра форм: круг, прямоугольник, квадрат, треугольник

# Описание функций:
## Круг:
```питон
импорт математики

def площадь (r):
вернуть math.pi * r * r

def perimetr (r):
возврат 2 * math.pi * r
```
- Код файла crup.py

```питон
def площадь (r):
вернуть math.pi * r * r
```
- Функция для расчета области принимает число **r** - радиус круга для дальнейшего расчета площади круга

```питон
def perimetr (r):
возврат 2 * math.pi * r
```

- Функция для расчета периметра круга принимает число **r** - радиус круга для расчета периметра круга

### Пример вызова:
```питон
импорт математики

def площадь (r):
 вернуть math.pi * r * r

def perimetr (r):
 возврат 2 * math.pi * r

печать (область (5))
print (периметр (5))
```

- Result area function = 78.53981633974483
- Result perimeter function = 31.41592653589793

## Rectangle
```python
def area(a, b):
    return a * b

def perimetr(a, b):
    return 2 * (a + b)
```

- File code rectangle.py

```python
def area(a, b):
	return a * b
```
- Takes two numbers: a and b - the length and width of the rectangle to calculate its area

```python
def perimetr(a, b):
	return 2 * (a + b)
```
- The function for calculating the perimeter takes two numbers: a and b - the length and width of the rectangle to calculate its perimeter
### Example call:
```python
def area(a, b):
    return a * b

def perimetr(a, b):
    return 2 * (a + b)

print(area(2, 4))
print(perimetr(2, 4))
```

- Result area function = 8
- Result perimetr function = 12

## Square
```python
def area(a):
    return a * a

def perimetr(a):
    return 4 * a
```
- File code square.py

```python
def area(a):
	return a * a
```
- The function for calculating the area takes the number a - the side of the square to calculate its area


```питон
def perimetr (a):
возвод 4 * а
```
- Функция расчета периметра принимаэт число а - сторону квадрата для расчета его периметра
### Пример Вызова :
```питон
def plopchadь (а):
 вернуть * а

def perimetr (a):
 возвод 4 * а

pechatj (облат (6))
печать (периметр (6))
```
- Фунция области резултата = 36
- Регламент фонкти и периметра 24
## Тройгольник
```питон
def plopchadь (а, ч):
 вернуть * ч / 2

def perimetr (a, b, c):
 вернуть + б + в
```
- Код Файла Тиангла.пи

```питон
def plopchadь (а, ч):
 вернуть * ч / 2
```
- Фунция даль расчета плащади принимает сва числа: а и ч - стона и вюголничка для расчета
```питон

def perimetr (a, b, c):
 вернуть + б + в
```
- Функция расчета периметра принимает три числа: а, б, в - стороны троиника

### Пример Вызова :
```питон
def plopchadь (а, ч):
 вернуть * ч / 2

def perimetr (a, b, c):
 вернуть + б + в


pechatj (облат (2, 4))
печать (периметр (2, 3, 4))
```
- Фунция области резултата = 4
- Фунция периметра результата = 9
## История эмиссии проэкта с поместю коммитов
> коммит 54029aef4b78f8468b63d7ed1cdc136a86b03afa (HEAD -> main, proishozdenié / main, proyshozdenié / HEAD)
- | Автор: Максим <karimovmaksim121@gmail.com>
- | Дата: ср 13 сентьября 19: 34:15 2023 +0500
- |
- | FIX: ancellogne.py


> коммит d93c047818ab0a08f8978e1700e0f884e1ee7dc8
- | Автор: Максим <karimovmaksim121@gmail.com>
- | Дата: ср 13 сентьября 19: 29:51 2023 +0500
- |
- | FIX: ancellogne.py; ДОБАВИТ: trangle.py


> commit e802e55f4c24cbfce3026419972cb13f0e6c14fb
- | Автор: Максим <karimovmaksim121@gmail.com>
- | Ср 13 сентибрия 19: 22:28 2023 +0500
-  |
- | ДОБАВИТЬ: ancellogne.py

> commit e802e55f4c24cbfce3026419972cb13f0e6c14fb
- | Автор: Максим <karimovmaksim121@gmail.com>
- | Ср 13 сентибря 19: 22:28 2023 +0500
-  |
- | ИЗМЕНЕНИЕ: README.md
