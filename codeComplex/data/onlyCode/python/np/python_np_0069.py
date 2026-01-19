from math import factorial
s = input().strip()
new = input().strip()
questions = 0
plus = s.count('+')
minus = s.count('-')
for i in new:
	if i == '+':
		plus -= 1
	elif i == '-':
		minus -= 1
	else:
		questions += 1
if plus < 0 or minus < 0:
	print(0)
else:
	num = factorial(questions)/(factorial(plus)*factorial(minus))
	den = 2**questions
	print("{0:.10f}".format(num/den))