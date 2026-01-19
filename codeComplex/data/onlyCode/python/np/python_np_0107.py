import math
a=input()
b=input()
i=a.count('+')
j=a.count('-')
k=b.count('+')
l=b.count('-')
m=b.count('?')
c1=(i-j)
c2=(k-l)
c=abs(c1-c2)
w=m-c
x=w//2
y=w//2+c
if(c==0 and m==0):
    print(1)
elif((c)>m):
    print(0)
else:
    x=math.factorial(m)//(math.factorial(x)*math.factorial(y))
    print(x/pow(2,m))
    
    

