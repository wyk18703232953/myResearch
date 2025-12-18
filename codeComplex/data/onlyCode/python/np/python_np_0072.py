# import sys
# sys.stdin = open("#input.txt", "r")

from math import factorial

s1 = input()
s2 = input()

finPos=0
for c in s1:
	if c=='+': finPos+=1
	else: finPos-=1

stPos=0
for c in s2:
	if c=='+': stPos+=1
	elif c=='-': stPos-=1

n=s2.count('?')
diff=abs(finPos-stPos)
if diff > n:
	print(0)
elif n&1 != diff&1:
	print(0)
else:
	i=0
	for i in range(n//2,n):
		if i*2-n == diff: break
	if i*2-n != diff: i+=1

	print((factorial(n)/(factorial(n-i)*factorial(i)))/(1<<n))