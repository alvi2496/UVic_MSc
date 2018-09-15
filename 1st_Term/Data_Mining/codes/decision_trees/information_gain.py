import entropy
import average_entropy

def calculate(info = [[]]):
	a = 0
	b = 0
	sum = 0
	for i in info:
		a += i[0]
		b += i[1] 
	result = entropy.calculate([a, b]) - average_entropy.calculate(info)
	return result
	