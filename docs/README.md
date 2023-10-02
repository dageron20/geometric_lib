# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a * h

# Functions
## circle.py
* def area(r)
  - returns area of circle with radius r.
* def perimeter(r)
  - returns perimeter of circle with radius r.
```
print(area(3)) # 28.274
print(perimeter(4)) # 25.132
```

## rectangle.py
* def area(a)
  - returns area of rectangle with sides a and b.
* def perimeter(a)
  - returns perimeter of rectangle with sides a and b.
```
print(area(3, 5)) # 15
print(perimeter(4, 2)) # 12
```
  
## square.py
* def area(a)
  - returns area of square with side a.
* def perimeter(a)
  - returns perimeter of square with side a.
```
print(area(3)) # 9
print(perimeter(4)) # 16
```

## triangle.py
* def area(a, h)
  - returns area of triangle with side a and height h.
    > :warning: The entered height h must fall to the side a!
* def perimeter(a, b, c)
  - returns perimeter of triangle with sides a, b, c
```
print(area(4, 7)) # 14
print(perimeter(4, 3, 6)) # 13
```
