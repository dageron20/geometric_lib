def area(a, h):
	'''
	### Calculating the area of the triangle

	:param a: `int`/`float` - side of the triangle
	:param h: `int`/`float` - height of the triangle
	:return: `int`/`float` - area of the triangle

	```
	>>> area(5, 3)
	>>> 7.5
	```
	'''
	return a * h / 2

def perimeter(a, b, c):
	'''
	### Calculating the perimeter of the triangle

	:param a: `int`/`float` - a side of the triangle
	:param b: `int`/`float` - b side of the triangle
	:param c: `int`/`float` - c side of the triangle
	:return: `int`/`float` - perimeter of the triangle

	```
	>>> perimeter(5, 3, 2)
	>>> 10
	```
	'''
	return a + b + c
