import math
s=input()
p=input()
c=1
ss=0
ps=0
k=0
for i in range(len(s)):
	if(p[i]=='?'):
		c*=2
		k+=1
	if(s[i]=='+'):
		ss+=1
	else:
		ss-=1
	if(p[i]=='+'):
		ps+=1
	elif p[i]=='-':
		ps-=1
y=math.fabs(ss-ps)
x=k-y
a=y+x/2
b=k-a
if k<y:
	ans=0.000000000
else:
	ans=math.factorial(a+b)/(math.factorial(a)*math.factorial(b))
	ans/=c
print("%.12f"%ans)
# print(a,b)