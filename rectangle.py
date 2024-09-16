def area(a, b):
	'''
	### Calculating the area of the rectangle

	:param a: `int`/`float` - a side of the rectangle
	:param b: `int`/`float` - b side of the rectangle
	:return: `int`/`float` - area of the rectangle
 
	```
	>>> area(5, 4)
	>>> 20
	```
	'''
	return a * b

def perimeter(a, b):
	'''
	### Calculating the perimeter of the rectangle

	:param a: `int`/`float` - a side of the rectangle
	:param b: `int`/`float` - b side of the rectangle
	:return: `int`/`float` - perimeter of the rectangle
 
	```
	>>> perimeter(5, 4)
	>>> 18
	```
	'''
	return 2 * (a + b)
