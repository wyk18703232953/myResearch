import math
from sys import stdin

#stdin=open('input.txt','r')
I=stdin.readline

s=I()
t=I()

p=0
for c in s:
	if(c=='+'): p+=1

pt,qt=0,0

for c in t:
	if(c=='+'):pt+=1
	elif(c=='?'): qt+=1

req=p-pt
if(req>qt or req<0): ans=0

else:
	ans=(math.factorial(qt)/math.factorial(req))
	ans/=math.factorial(qt-req)
	ans/=pow(2,qt)

print(ans)