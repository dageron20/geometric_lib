import math

def area(r):
	'''
	### Calculating the area of the circle

	:param r: `int`/`float` - radius of the circle
	:return: `int`/`float` - area of the circle
	'''
	return math.pi * r * r


def perimeter(r):
	'''
	### Calculating the perimeter of the circle

	:param r: `int`/`float` - radius of the circle
	:return: `int`/`float` - perimeter of the circle
	'''
	return 2 * math.pi * r
