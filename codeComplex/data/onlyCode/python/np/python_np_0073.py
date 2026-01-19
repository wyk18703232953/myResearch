import math

a=input()
b=input()
x1=a.count('+')
y1=a.count('-')
x2=b.count('+')
y2=b.count('-')
l=b.count('?')
if l==0 and(x1==x2 and y1==y2):
	print(float(1))
elif x1>(x2+l) or y1>(y2+l):
	print(float(0))
else:
	w=math.factorial(l)
	m=math.factorial(x1-x2)
	n=math.factorial(l-(x1-x2))
	print((w/(m*n)) /2**(x1+y1-x2-y2))
