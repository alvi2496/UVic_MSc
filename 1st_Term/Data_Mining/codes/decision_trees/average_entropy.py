import entropy

def calculate(info = [[]]):
	a = 0
	result = 0
	for i in info:
		for j in i:
			a += j
	for i in info:
		x = 0
		for j in i:
			x += j	
		result += entropy.calculate(i) * (x/a)	
	return result
		