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





