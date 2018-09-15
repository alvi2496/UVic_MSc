import math

def calculate(info = []):
	a = 0;
	for i in info:
		a += i
	result = 0
	for x in info:
		if x != 0:
			b = x/a
			result -= b*math.log(b, 2)
	return result		
