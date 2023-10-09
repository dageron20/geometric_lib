# Математические формулы
## Нахождение площади
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Нахождение периметра
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Функции
## Круг
- area(r) Вычисление площади (r - радиус)
> Пример вызова: area(5) -> 78.53981633974483
- perimeter(r) Вычисление периметра (r - радиус)
> Пример вызова: perimeter(5) -> 31.41592653589793

## Прямоугольник
### Вычиселине площади
**(a,b - стороны прямоугольника)**
```python
def area(a, b)
```
> Пример вызова: area(3, 4) -> 12
- perimeter(a, b) Вычисление периметра (a,b - стороны прямоугольника)
> Пример вызова: perimeter(3, 4) -> 14

## Квадрат
- area(a) Вычиселине площади (a - сторона квадрата)
> Пример вызова: area(3) -> 9
- perimeter(a) Вычисление периметра (a - сторона квадрата)
> Пример вызова: perimeter(3) -> 12

## Треугольник
- area(a, h) Вычиселине площади (a - основание, h - высота)
> Пример вызова: area(3, 4) -> 6
- perimeter(a, b, c) Вычисление периметра (a,b,c - стороны треугольника)
> Пример вызова: perimeter(3, 4, 5) -> 12

# Changelog
- [Fixed rectangle.py](https://github.com/soilow/geometric_lib/commit/68eb5b9fa84158b73667fd18002cd3c1c36a62bf)
- [Added triangle.py](https://github.com/soilow/geometric_lib/commit/0737645eb11b576050358c21c90d048ab8ff9a61)
- [Added rectangle.py](https://github.com/soilow/geometric_lib/commit/176e0720cda60b0d434ee8ba5a3a934610403548)
- [L-03: Docs added](https://github.com/soilow/geometric_lib/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2)
- [L-03: Circle and square added](https://github.com/soilow/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460)

