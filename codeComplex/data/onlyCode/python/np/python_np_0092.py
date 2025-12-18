import math
def C(a, b):
	return math.factorial(a)//(math.factorial(b)*math.factorial(a-b))

a = list(input())
b = list(input())
x, y, d, ans, power = 0, 0, 0, 0, 0
for i in range(len(a)):
	if a[i] == '+':
		x += 1
	if a[i] == '-':
		x -= 1
	if b[i] == '?':
		d += 1
	if b[i] == '+':
		y += 1
	if b[i] == '-':
		y -= 1
plus, minus = d, 0
for i in range(0, d+1):
	k = C(d, plus)
	if y+(plus-minus) == x:
		ans += k
	power += k
	plus -= 1
	minus += 1
print("{0:.12f}".format(ans/power))