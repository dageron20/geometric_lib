# Function for calculation math formulas

## Math formulas
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = a(h / 2)

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## Functions
### Circle
- **area**: takes a number r, returns the area of a circle with radius r
```
Syntax: area(r) 
e.g. area(5) = 78.5398
```

- **perimeter**: takes a number r, returns the perimeter (length) of a circle with radius r
```
Syntax: perimteter(r) 
e.g. perimeter(2) = 12.5664
```

### Rectangle
- **area**: takes numbers a and b, returns the area of a rectangle with width a and length b
```
Syntax: area(a, b) 
e.g. area(10, 2) = 20
```

- **perimeter**: takes numbers a and b, returns the perimeter of a rectangle with width a and length b
```
Syntax: perimeter(a, b) 
e.g. perimeter(3, 4) = 14
```

### Square
- **area**: takes a number a, returns the area of a square with side length a
```
Syntax: area(a) 
e.g. area(5) = 25
```

- **perimeter**: takes a number a, returns the perimeter of a square with side length a
```
Syntax: perimeter(a) 
e.g. perimeter(40) = 160
```

### Triangle
- **area**: takes numbers a and h, returns the area of a triangle with side length a and height h
```
Syntax: area(a, h) 
e.g. area(5, 4) = 10
```

- **perimeter**: takes numbers a, b and c, returns the perimeter of a triangle with side lengths a, b and c
```
Syntax: perimeter(a, b, c) 
e.g. perimeter(1, 2, 3) = 6
```

## History of project changes

### cc9bb00
- Added new file rectangle.py

### 749353b
- Fixed error in file rectangle.py
- Added new file triangle.py