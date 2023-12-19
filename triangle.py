
def area(a, h):
    if a < 0 or h < 0:
        return "Negative number"
    return a * h / 2


def perimeter(a, h, c):
    if a < 0 or h < 0 or c < 0:
        return "Negative number"
    return a + h + c

def exists(a, h, c):
    if a + h > c or a + c > h or h + c > a:
        return True
    return False
