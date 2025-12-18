from math import factorial as fc
def per(a,b):
    return fc(a+b)/(fc(a)*fc(b))
import sys
s=input()
s1=input()
x=s.count("+")
y=s.count("-")
x1=s1.count("+")
y1=s1.count("-")
p=x-y
p1=x1-y1
q=s1.count("?")
dif=p-p1
if q<abs(p1-p) or dif>q:
    print(0.0)
    sys.exit()
m=abs(y-y1)
pl=abs(x-x1)
print(per(m,pl)/(2**(m+pl)))
    
