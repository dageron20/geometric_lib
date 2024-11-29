def area(a, h): 
    if a>0 and h>0: return a * h / 2 
    return 0

def perimeter(a, b, c): 
    if a>(b+c) or b>(a+c) or c>(a+b): return 0
    if a>0 and b>0 and c>0: return a + b + c 
    return 0