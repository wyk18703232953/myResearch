import math
a=input()
b=input()
x=a.count('+')-b.count('+')
y=a.count('-')-b.count('-')
c=a.count('+')-a.count('-')
d=b.count('+')-b.count('-')
e=c-d
f=b.count('?')
if x==0 and y==0:
    print(1)
elif f==0 and (x!=0 or y!=0):
    print(0)
elif x!=0 and y==0:
    print(1/2**f)
elif y!=0 and x==0:
    print(1/2**f)
elif abs(e)>f:
    print(0)
else:
    print(math.factorial(f)/(math.factorial(y)*math.factorial(x)*2**f))