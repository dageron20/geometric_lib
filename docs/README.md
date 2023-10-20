# Figures
## Circle

    def area(r):
 
    '''
    Takes r - the radius of a circle, outputs the area of ​​the circle
    
    area (5)
    
    Output:78.5
    '''
    
    return math.pi * r * r

    def perimeter(r):

    '''
    Takes r - the radius of the circle, outputs the perimeter of the circle
    
    area (5)
    
    Output:31.4
    '''
    
    return 2 * math.pi * r
### Commit 

The function calculates the area and perimeter of a circle using one input number


 1)Takes r - the radius of a circle, outputs the area of ​​the circle
 
 
 2)Takes r - the radius of the circle, outputs the perimeter of the circle

## Rectangle


    def area(a, b):

    '''
    Takes a and b - sides of a rectangle, outputs the area of ​​the rectangle
    
    area(2, 3)
    
    Output:6
    '''
    
    return a * b 

    def perimeter(a, b): 

    '''
    Takes a and b - sides of a rectangle, outputs the perimeter of ​​the rectangle
    
    perimeter(2,3)
    
    Output:10
    '''
    
    return 2a + 2b 

### Commits
Has been fixed

    def area(a, b):

    return a * b

    def perimeter(a, b):

    return a + b

Takes a and b - sides of a rectangle, outputs the area of ​​the rectangle

Takes a and b - sides of a rectangle, outputs the perimeter of ​​the rectangle

The function calculated the perimeter incorrectly, I replaced it with this:

    def area(a, b):

    return a * b

    def perimeter(a, b):

    return 2a + 2b

Now the formula for the perimeter of a rectangle is written correctly

The function calculates the area and perimeter of a rectangle using two input numbers

1) Takes a and b - sides of a rectangle, outputs the area of ​​the rectangle
2) Takes a and b - sides of a rectangle, outputs the perimeter of ​​the rectangle

## Square

    def area(a):

    '''
    Takes a and b - sides of a square, outputs the area of ​​the square
    
    area(3)
    
    Output:9
    '''
    
    return a * a


    def perimeter(a):

    '''
    Takes a and b - sides of a square, outputs the perimeter of ​​the square
    
    perimeter(3)
    
    Output:12
    '''
    
    return 4 * a

### Commit

The function calculates the area and perimeter of a circle using one input number

1)Takes a and b - sides of a square, outputs the area of ​​the square

2)Takes a and b - sides of a square, outputs the perimeter of ​​the square

## Triangle

    def area(a, h): 

    '''
    Takes a - the side of the triangle and h - the height of the triangle, outputs the area of ​​the triangle
    
    area(2, 3)
    
    Output:3
    '''
    
    return a* h / 2 

    def perimeter(a, b, c): 

    '''
    Takes a, b and c - sides of a triangle, outputs the perimeter of ​​the triangle
    
    perimeter(3, 4, 5)
    
    Output:12
    '''
    
    return a + b + c 

### Commit

The function calculates the area of ​​a triangle using two input numbers and the perimeter of a triangle using three input numbers

1)Takes a - the side of the triangle and h - the height of the triangle, outputs the area of ​​the triangle

2)Takes a, b and c - sides of a triangle, outputs the perimeter of ​​the triangle

## project change history

* 554b014 (HEAD -> main, origin/main, origin/HEAD) Исправлена ошибка с периметром
  
* bf68d22 Добавлен файл rectangle
 
* 620d8e4 Готово
  
* 9821b20 Исправлена ошибка
 
* 3888066 Добавлен файл треугольник
 
* 8a13da8 Добавлен новый файл
 
* 22a6f12 Update workspace.xml
 
* 2aa0f7c Create workspace.xml
 
* d078c8d (upstream/main, upstream/HEAD) L-03: Docs added
 
* 8ba9aeb L-03: Circle and square added



