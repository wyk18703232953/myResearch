from collections import Counter
import math
l=list(input())
l1=list(input())
a=Counter(l)
b=Counter(l1)
if a['+']<b['+'] or a['-']<b['-']:
	print("0")
	exit()
else:
	a1=a['+']-b['+']
	b1=a['-']-b['-']
s=(math.factorial(a1+b1))//((math.factorial(a1))*(math.factorial(b1)))
s1=float(2**(a1+b1))
print(s/s1)