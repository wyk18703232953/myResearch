import math
s1=list(input())
s2=list(input())
p1,m1,p2,m2,c=0,0,0,0,0
for i in range(len(s1)):
	if(s1[i]=='+'):
		p1+=1
	if(s1[i]=='-'):
		m1+=1
	if(s2[i]=='+'):
		p2+=1
	if(s2[i]=='-'):
		m2+=1
	if(s2[i]=='?'):
		c+=1
p=abs(p1-p2)
m=abs(m1-m2)
if((p+m)==c):
	print(math.factorial(c)/(math.factorial(p)*math.factorial(m)*pow(2,c)))
else:
	print(0/1)