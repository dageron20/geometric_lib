# Math formulas
- This project does some geometric calculations
- There are own files for each geometric shape, which contains funcs that return result by formulars

## Function's descriptions in files

### Square
#### Func area
- You can pass this function the value of the side of the square (a) and it will calculate the area of this square using the formula (a*a)
- you can call this function with argument 5:
```
print(area(5)) --> 25
```

#### Func perimeter
- You can pass this function the value of the side of the square (a) and it will calculate the perimeter of this square using the formula (a*4)
- you can call this function with argument 5:
```
print(perimeter(5)) --> 20
```

#### Func semiPerimeter
- You can pass this function the value of the side of the square (a) and it will calculate the half-meter of this square using the formula (a*4)
- you can call this function with argument 5:
```
print(semiPerimeter(5)) --> 10
```


### Triangle
#### Func area
- You can pass this function the values of the side and height of the triangle (a, h), and it will calculate the area of this triangle using the formula (a*h/2)
- you can call this function with arguments 3,2:
```
print(area(3,2)) --> 3
```

#### Func perimeter
- You can pass this function the values of the sides of the triangle (a, b, c) and it will calculate the perimeter of this triangle using the formula (a+b+c)
- you can call this function with arguments 3,4,5:
```
print(perimeter(3,4,5)) --> 12
```

#### Func semiPerimeter
- You can pass this function the values of the sides of the triangle (a, b, c) and it will calculate the half-meter of this triangle using the formula ((a+b+c)/2)
- you can call this function with arguments 3,4,5:
```
print(semiPerimeter(3,4,5)) --> 6
```


### Rectangle
#### Func area
- You can pass this function the values of the sides of the rectangle (a, b) and it will calculate the area of this rectangle using the formula (a*b)
- you can call this function with arguments 5,3:
```
print(area(5,3)) --> 15
```

#### Func perimeter
- You can pass this function the values of the sides of the rectangle (a, b) and it will calculate the perimeter of this square using the formula ((a+b)*2)
- you can call this function with arguments 5,3:
```
print(perimeter(5,3)) --> 16
```


### Circle
#### Func area
- You can pass this function the value of the radius of the circle (r), and it will calculate the area of this circle using the formula (𝝿 * r * r)
- you can call this function with argument 1:
```
print(area(1)) --> 3,14
```

#### Func perimeter
- You can pass this function the value of the radius of the circle (r), and it will calculate the circumference of this circle using the formula (2 * 𝝿 * r)
- you can call this function with argument 1:
```
print(perimeter(1)) --> 6,28
```


## A set of formulas for geometric shapes

### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a


## commit history
- [The first commit](https://github.com/dageron20/geometric_lib/pull/19/commits/2d93ce1e05456ae9ef7d9637588df28092c395dc) was made with errors in some formulas
- The half-meter function was added in [the second commit](https://github.com/dageron20/geometric_lib/commit/6431fe50093f40b6ff7ec2c2ec8d7a9028b0c1e4)
- Function descriptions have been added in [the third commit](https://github.com/dageron20/geometric_lib/commit/7221095add246cd080ff45ad40b69db5d37aaff2)
